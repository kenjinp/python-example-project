install:
	@echo "Installing project's dependencies... 🚀"
	@docker-compose run --rm animalsounds which python

say_hello:
	@echo "Running tests... 🧪"
	@docker-compose run --rm animalsounds python hello

test:
	@echo "Running tests... 🧪"
	@docker-compose run --rm animalsounds pytest tests