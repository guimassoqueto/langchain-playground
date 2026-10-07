VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

PYTEST=$(VENV)/bin/pytest
RUFF=$(VENV)/bin/ruff
PRE_COMMIT=$(VENV)/bin/pre-commit
PIP_REVIEW=$(VENV)/bin/pip-review

venv:
	@python -m venv .venv

install:
	@$(PIP) install --upgrade pip && $(PIP) install --force-reinstall --no-cache-dir -r devtools/requirements.txt
	@$(PRE_COMMIT) install && $(PRE_COMMIT) install --hook-type commit-msg && $(PRE_COMMIT) autoupdate

lint:
	@$(RUFF) check --fix --config devtools/pyproject.toml .
	@$(RUFF) format --config devtools/pyproject.toml .

check-updates:
	@$(PIP_REVIEW)