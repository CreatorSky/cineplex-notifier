.PHONY: help build run stop purge

help:
	@echo Available targets:
	@echo build       Build the Docker image
	@echo run         Run the application
	@echo stop        Stop the application
	@echo purge       Stop and remove all containers

build:
	docker-compose build

run:
	docker-compose up -d

stop:
	docker-compose down

purge:
	docker-compose kill
	docker-compose rm
