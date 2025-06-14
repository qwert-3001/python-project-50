install:
	uv sync
build:
	uv build
lint:
	uv run ruff check gendiff
lint-fix:
	uv run ruff check gendiff --fix
test:
	uv run pytest
activate:
	source .venv/bin/activate
