dev:
	docker compose -f docker-compose.dev.yml up --build --abort-on-container-exit
prod:
	docker compose -f docker-compose.prod.yml up --build --abort-on-container-exit