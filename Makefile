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
test-coverage:
	uv run pytest --cov=gendiff/
