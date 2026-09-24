# PubRescue

A runnable concept for auditing Microsoft Publisher inventories and producing a migration runbook. The demo uses shared fictional fixtures and deterministic estimates.

## What works
- Select Publisher files and compare risk signals.
- Choose PDF, DOCX, or PNG output and optional visual QA.
- Calculate pages, effort, price, warnings, and a three-step runbook.
- Copy the demo runbook; run the equivalent validated FastAPI operation locally.

GitHub Pages serves only the static Next.js frontend. The Python backend is tested, runnable source and is **not deployed**. No real files, conversions, customers, payment, paid APIs, or AI are involved.

## Verify
`npm ci && npm run typecheck && npm run test:e2e && npm run build && npm run audit:prod`

`cd api && uv sync --frozen && uv run pytest`

Frontend: `npm run dev` · API: `cd api && uv run uvicorn main:app --reload`

See `docs/` for product, architecture, Office Hours, CEO review, and phased build prompts. Source inspiration: [Ideabrowser](https://www.ideabrowser.com/hub/ideas/a-microsoft-publisher-migration-service-for-schools-and-churches-93282e04).
