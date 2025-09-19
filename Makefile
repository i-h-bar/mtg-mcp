test:
	@uv run coverage run
	@uv run coverage report

lint:
	@uv run ruff check --fix
	@uv run ty check src

setup:
	@uv sync
	@uv run pre-commit install
	@uv run pre-commit install --hook-type pre-push
