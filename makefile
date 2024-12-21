# Remove old venv and cached files
# create new venv and install dependencies
# run tests so you know that they pass before you start working
install: clean setup_venv test

setup_venv:
	uv venv
	. .venv/bin/activate
	uv sync
	. .venv/bin/activate; pre-commit install
	@echo "** Installation complete **"

clean:
	@echo "** Deleting venv and cached files **"
	rm -rf .venv/
	rm -rf __pycache__/
	rm -rf .pytest_cache

test:  
	. .venv/bin/activate; pytest -v -s --cov . tests

lint:
	. .venv/bin/activate; ruff check

format:
	. .venv/bin/activate; ruff format

commit:
	. .venv/bin/activate; pre-commit run --all

