# receipt-scanner

## On session start

Review the ADRs in `docs/adr/` before doing any work. They record the project's
roadmap and architectural decisions. If a change you make introduces or alters a
decision, add or update an ADR in the same folder.

## Commands

- Run tests: `uv run pytest`
- Run the app: `uv run uvicorn app:app --reload` (interactive docs at `/docs`)
- Use `uv` for all Python tooling (see `docs/adr/0001-use-uv-for-python-tooling.md`): add dependencies with `uv add` (`uv add --dev` for dev-only) and run things with `uv run`. Don't use the global Python or bare `pip`.
