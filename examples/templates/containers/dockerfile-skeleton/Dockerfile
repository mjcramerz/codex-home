# syntax=docker/dockerfile:1.7
ARG BASE_IMAGE=debian:bookworm-slim
FROM ${BASE_IMAGE} AS runtime

ARG APP_UID=10001
ARG APP_GID=10001
ARG APP_HOME=/app

WORKDIR ${APP_HOME}

# Create the app directory with non-root ownership.
RUN mkdir -p ${APP_HOME} \
    && chown -R ${APP_UID}:${APP_GID} ${APP_HOME}

# Copy the application into the image (adjust paths as needed).
COPY --chown=${APP_UID}:${APP_GID} . ${APP_HOME}

# Drop privileges for runtime.
USER ${APP_UID}:${APP_GID}

# Optional: document the service port.
EXPOSE 8080

# Replace with your app's entrypoint.
CMD ["./app"]
