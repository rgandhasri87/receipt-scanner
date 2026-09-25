# Grocery Receipt Processor — Roadmap

Last updated: 2026-09-24

## Vision / approach

Backend-first learning project. Core is a FastAPI app (see ADR 0002) wrapping the receipt-processing
logic, with a barebones intake endpoint (`POST /receipts` accepting an image) so
testing is just POSTing an image. UI is intentionally deferred to a later, separate
learning arc.

Primary learning goals: OCR / image processing, data analysis & visualization, and
eventually classification/model comparison for categorizing line items. Comfortable
starting rough (mock output or a VLM reading the receipt) to get the skeleton running
before solving image → accurate structured data "for real."

## Phases

**Phase 0 — Skeleton app**
FastAPI app with one route, `POST /receipts`, accepting an image and returning JSON.
Starts with a hardcoded mock line-item response — no real OCR yet. Goal: get the
full request-in/structured-data-out shape working end to end, and have something
to write first tests against immediately.

**Phase 1 — Extraction pipeline**
The core interesting problem. Two sub-decisions:
- How to get text off the image: classic OCR (Tesseract/pytesseract — free, local,
  rougher on receipt layouts), a cloud OCR API (Google Vision / AWS Textract —
  better accuracy, costs money/API key), or a VLM prompted to read the receipt
  directly (fastest to get working, interesting to compare later).
- Parsing raw extracted text into structured data (item name, quantity, price,
  store, date, total) — regex/heuristics first since real receipts are messy.
Doing OCR-then-parse and a VLM-does-it-all approach both, eventually, gives a
natural comparison to write up (ties into the model-comparison interest).

**Phase 2 — Storage**
Schema design: receipts, line_items, maybe categories. SQLite to start. Good spot
to practice raw SQL or SQLAlchemy.

**Phase 3 — Categorization**
Start rule-based (keyword → category). Later, treat as its own small ML project:
baseline (rules) vs. trained classifier (Naive Bayes/logistic regression on item
text) vs. maybe embeddings. Self-contained enough to be its own mini learning arc
once real data is flowing.

**Phase 4 — Analysis / visualization**
Once receipts are actually in the database: spending by category, trends over
time, price-per-item history. Can live behind another FastAPI endpoint returning
JSON — no UI needed yet.

**Phase 5 — UI**
Deliberately separate and later; treated as its own learning project.

## Testing strategy

Everything hangs off `POST /receipts`, so build a small set of sample receipt
images (or mocked payloads) as fixtures early and reuse them across phases.

## Open decisions before writing code

- Which OCR/VLM approach to start with (Phase 1).
- ~~A loose JSON schema for a "line item"~~ — done: Pydantic models in `models.py`.

## Status

Phase 0 complete: FastAPI skeleton with mock `POST /receipts` and basic tests.
Next: Phase 1 — decide on OCR/VLM approach.
