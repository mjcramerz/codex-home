# syntax=docker/dockerfile:1.7
ARG BASE_IMAGE=debian:bookworm-slim
FROM ${BASE_IMAGE} AS runtime

ARG APP_UID=10001
ARG APP_GID=10001
ARG APP_HOME=/app

WORKDIR ${APP_HOME}
RUN mkdir -p ${APP_HOME} \
    && chown -R ${APP_UID}:${APP_GID} ${APP_HOME}

COPY --chown=${APP_UID}:${APP_GID} . ${APP_HOME}
USER ${APP_UID}:${APP_GID}

EXPOSE 8080
CMD ["./app"]
