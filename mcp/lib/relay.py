"""Bounded, binary-transparent, full-duplex stdio relay with half-close support."""
from __future__ import annotations
import os
import selectors
import socket
import time
from typing import Callable

class RelayError(RuntimeError):
    pass


def bridge(read_a: int, write_a: int, read_b: int, write_b: int, *,
           close_write_a: Callable[[], None], close_write_b: Callable[[], None],
           limit: int = 1048576, idle: float = 1800, lifetime: float = 28800,
           stopped: Callable[[], bool] = lambda: False,
           stderr_fd: int | None = None, stderr_limit: int = 32768,
           stderr_sink: Callable[[bytes], None] | None = None,
           eof_grace: float = 15, startup_timeout: float | None = None) -> dict[str, int]:
    """read_a -> write_b and read_b -> write_a; never decode MCP messages.

    The same fd may be both readable and writable (a connected Unix socket).
    Writes close once their input reaches EOF and queued bytes have drained.
    The remaining direction gets a bounded grace period to return final replies.
    """
    inputs = [read_a, read_b]
    outputs = [write_b, write_a]
    closers = [close_write_b, close_write_a]
    pending = [bytearray(), bytearray()]
    eof = [False, False]
    output_closed = [False, False]
    counts = [0, 0]
    stderr_count = 0
    stderr_open = stderr_fd is not None
    descriptors = set(inputs+outputs+([] if stderr_fd is None else [stderr_fd]))
    for fd in descriptors:
        os.set_blocking(fd, False)
    start = last = time.monotonic()
    eof_at: float | None = None
    with selectors.PollSelector() as selector:
        while True:
            now = time.monotonic()
            if stopped():
                raise RelayError('session interrupted')
            if startup_timeout is not None and counts[1] == 0 and now-start >= startup_timeout:
                raise RelayError('server startup timed out')
            if now-start >= lifetime:
                raise RelayError('maximum session lifetime reached')
            if now-last >= idle:
                raise RelayError('idle session timed out')
            for i in range(2):
                if eof[i] and not pending[i] and not output_closed[i]:
                    try:
                        closers[i]()
                    except (OSError, ValueError):
                        pass
                    output_closed[i] = True
            if all(eof) and not any(pending):
                break
            if eof_at is not None and now-eof_at >= eof_grace:
                if any(pending):
                    raise RelayError('peer failed to drain during EOF grace period')
                break
            desired: dict[int, int] = {}
            for i in range(2):
                if not eof[i] and len(pending[i]) < limit:
                    desired[inputs[i]] = desired.get(inputs[i],0) | selectors.EVENT_READ
                if pending[i] and not output_closed[i]:
                    desired[outputs[i]] = desired.get(outputs[i],0) | selectors.EVENT_WRITE
            if stderr_open and stderr_fd is not None:
                desired[stderr_fd] = desired.get(stderr_fd,0) | selectors.EVENT_READ
            for fd in list(selector.get_map()):
                if fd not in desired:
                    selector.unregister(fd)
            for fd, mask in desired.items():
                if fd in selector.get_map():
                    selector.modify(fd, mask)
                else:
                    selector.register(fd, mask)
            for key, mask in selector.select(timeout=0.2):
                fd = key.fd
                if stderr_open and fd == stderr_fd and mask & selectors.EVENT_READ:
                    try:
                        block = os.read(fd,65536)
                    except BlockingIOError:
                        block = None
                    if block == b'':
                        stderr_open = False
                    elif block:
                        available = max(0,stderr_limit-stderr_count)
                        if stderr_sink is not None and available:
                            stderr_sink(block[:available])
                        stderr_count += len(block)
                for i in range(2):
                    if fd == inputs[i] and mask & selectors.EVENT_READ and not eof[i]:
                        try:
                            block = os.read(fd,min(65536,limit-len(pending[i])))
                        except BlockingIOError:
                            continue
                        except (ConnectionResetError, BrokenPipeError):
                            block = b''
                        if block:
                            pending[i].extend(block); counts[i] += len(block); last = now
                        else:
                            eof[i] = True
                            if eof_at is None:
                                eof_at = now
                    if fd == outputs[i] and mask & selectors.EVENT_WRITE and pending[i]:
                        try:
                            count = os.write(fd,pending[i])
                        except BlockingIOError:
                            continue
                        except (BrokenPipeError, ConnectionResetError):
                            raise RelayError('peer disconnected') from None
                        del pending[i][:count]; last = now
    return {'to_server_bytes':counts[0], 'from_server_bytes':counts[1],
            'suppressed_stderr_bytes':stderr_count}


def shutdown_write(sock: socket.socket) -> None:
    try:
        sock.shutdown(socket.SHUT_WR)
    except OSError:
        pass
