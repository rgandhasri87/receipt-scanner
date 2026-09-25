# 0001. Use uv for Python tooling

- Status: accepted
- Date: 2026-09-24

## Context

The user prefers to use uv over Anaconda or basic pip. The project needs reproducible dependency management for Flask and pytest.

## Decision

Use [uv](https://docs.astral.sh/uv/) to manage the virtual environment and
dependencies. Dependencies are declared in `pyproject.toml` and locked in
`uv.lock`. Add packages with `uv add` (`uv add --dev` for dev-only) and run
commands with `uv run` (e.g. `uv run pytest`). Do not use the global Python or
bare `pip`.

## Consequences

- Reproducible environments via the committed lockfile; the `.venv` is
  git-ignored.
- Contributors and agents need uv installed.
- Alternative considered: `python -m venv` + `pip`. Rejected in favour of uv's
  speed and built-in lockfile.
