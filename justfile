# show this help message and exit
help:
	just --list

# start server
run:
	tox run -e run

# start server in auto-reload mode
listen:
	tox run -e run -- --reload

# start server in docker
up:
	docker compose up --build --remove-orphans
