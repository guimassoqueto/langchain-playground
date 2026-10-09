# langchain-playground

Scratch repo for working through a LangChain course, using Claude as the model provider.

## Requirements

- Python 3.14.7 (see `.tool-versions`)
- An Anthropic API key

## Setup

```bash
make venv       # create .venv
make env        # copy devtools/.env.sample to .env (won't overwrite an existing one)
make install    # install dependencies and the git hooks
```

Then put your key in `.env`:

```
ANTHROPIC_API_KEY="sk-ant-..."
```

## Usage

| Command              | Does                                                        |
| -------------------- | ----------------------------------------------------------- |
| `make main`          | Run `main.py`                                               |
| `make lint`          | Lint and format, applying fixes                             |
| `make lint-check`    | Lint and format checks only, no writes                      |
| `make commit`        | Commit through commitizen (conventional commit messages)    |
| `make hooks`         | (Re)install the pre-commit and commit-msg hooks             |
| `make update-hooks`  | Bump the pinned hook revisions in `.pre-commit-config.yaml` |
| `make check-updates` | List outdated dependencies                                  |
| `make reinstall`     | Force a clean reinstall of all dependencies                 |

## Layout

```
app/config/envs.py   # env loading and API key access
main.py              # entry point
devtools/            # requirements, tool config (ruff, commitizen), .env.sample
```

Tool configuration lives in `devtools/pyproject.toml`; every command that needs it
passes `--config devtools/pyproject.toml`.
