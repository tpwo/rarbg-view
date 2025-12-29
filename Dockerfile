FROM golang:1.25 AS build

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY --parents app static /app/

RUN go build -v -ldflags="-s -w" --tags fts5 -o rarbg-view ./app

FROM ubuntu:24.04
COPY --from=build /app/rarbg-view /app/rarbg-view
COPY --from=build /app/static /app/static
WORKDIR /app
CMD ["./rarbg-view"]
