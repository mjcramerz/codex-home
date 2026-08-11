FROM rust:1.82-slim AS build
WORKDIR /src
COPY . .
RUN if [ -f Cargo.lock ]; then cargo build --release --locked; else cargo build --release; fi

FROM debian:stable-slim
RUN useradd -m app
USER app
WORKDIR /home/app
ENV RUST_LOG=info
COPY --from=build /src/target/release/axum_api_template ./axum_api_template
EXPOSE 3000
CMD ["./axum_api_template"]
