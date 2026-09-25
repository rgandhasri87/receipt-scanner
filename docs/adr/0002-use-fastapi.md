# 0002. Use FastAPI instead of Flask

- Status: accepted
- Date: 2026-09-24

## Context

Phase 0 was first built on Flask. The roadmap calls for a shared line-item schema
that Phases 1–4 (extraction, storage, categorization, analysis) all target, but
Flask has no built-in way to define or enforce one. The project is one route and
two tests, so switching now is nearly free.

## Decision

Use FastAPI with Pydantic models (`models.py`: `LineItem`, `Receipt`) as the API
framework. `POST /receipts` takes an `UploadFile` and declares `Receipt` as its
return type. Run with uvicorn (`uv run uvicorn app:app --reload`); tests use
`fastapi.testclient.TestClient`.

## Consequences

- The line-item schema is explicit, validated and shared across phases.
- Request validation is automatic (a missing image is a 422, not a hand-written 400).
- Interactive docs at `/docs` give a file-upload UI for manual testing.
- Async support suits Phase 1's network-bound VLM / cloud OCR calls.
- Extra dependencies: `uvicorn`, `python-multipart` (file uploads), and `httpx`
  (dev, for `TestClient`).
- Alternative considered: staying on Flask. Rejected for the lack of typed models.
