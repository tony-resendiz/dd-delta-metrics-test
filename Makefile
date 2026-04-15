.PHONY: check-env test-same-tags test-unique-tags up-all down-all

check-env:
	@if [ ! -f .env ]; then \
		echo "❌ .env file not found."; \
		echo "👉 Copy .example.env to .env and add your DD_API_KEY first:"; \
		echo "   cp .example.env .env"; \
		exit 1; \
	fi

test-same-tags: check-env
	@echo "🚀 Running test-same-tags..."
	@cd test-same-tags && docker compose --env-file ../.env up --build

test-unique-tags: check-env
	@echo "🚀 Running test-unique-tags..."
	@cd test-unique-tags && docker compose --env-file ../.env up --build

up-all: test-same-tags test-unique-tags

down-all:
	@echo "🛑 Stopping all environments..."
	@cd test-same-tags && docker compose down || true
	@cd test-unique-tags && docker compose down || true