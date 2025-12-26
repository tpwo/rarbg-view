# RareTide

Web-based interface for P2P file sharing.

Very initial state, now only ready to use locally from localhost.

Schema was inspired by rarbg (RIP).

## Running

Requirements:

* docker
* just command runner

App is dockerized with compose, and can be started with `just`:

    just up

To run without docker:

    just run

To run with auto-reload mode enabled:

    just listen

To list all available recipes run `just --list`.
