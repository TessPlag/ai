all: remove build run

rerun: stop remove build run

build:
	@sudo docker compose build

run:
	@sudo docker compose up -d

remove:
	@sudo docker compose down
	@sudo docker compose rm

stop:
	@sudo docker compose down
