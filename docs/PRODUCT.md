# Product plan

## ICP and JTBD
Primary ICP: US schools and churches with 100+ Publisher files, no dedicated migration team, and recurring documents. Buyer: operations/IT lead; user: office administrator. JTBD: preserve access and visual fidelity before the October 2026 sunset while producing a defensible audit trail.

## MVP
1. Local/on-prem inventory collector emits metadata only. 2. Risk classifier flags pages, fonts, linked images, size, and corruption. 3. Human-approved pilot conversion. 4. Batch queue with checksums and retries. 5. Side-by-side visual QA and exception log. 6. Exportable completion runbook. This prototype proves risk selection, estimates, validation, and runbook interaction—not conversion.

## Data model
Organization → MigrationJob → SourceFile → ConversionAttempt → OutputArtifact → QAReview → Exception. Store source checksum, source path alias, selected format, converter version, timestamps, reviewer and retention state. Separate customer content from telemetry.

## Architecture
Next.js dashboard; FastAPI orchestration; Postgres metadata; encrypted object storage; isolated conversion workers; queue with idempotency keys; LibreOffice/controlled Windows worker where format support requires it; screenshot/diff service; OpenTelemetry and immutable audit events. Customer-managed storage is the preferred high-trust option.

## AI/model strategy
No model is required for conversion. Later, an opt-in vision model can rank visual differences and summarize exceptions; deterministic render comparison and human approval remain authoritative. Never train on customer documents by default.

## Economics and offer ladder
- Free: inventory template/checklist.
- $299 audit: up to 100 files and five-file pilot.
- $1,500–$7,500 migration: volume, complexity, and manual remediation dependent.
- $199/month archive assurance: quarterly access checks and retention report.
Target 70% gross margin after discovery, but model labor per page and exception rate before promising fixed pricing.

## GTM and validation
Partner with Microsoft 365 MSPs, dioceses, school associations, print shops, and records consultants. Deadline content should drive to a paid audit, not free unlimited conversion. Validate with 20 observed interviews, three paid pilots, ≥60% pilot-to-migration conversion, <8% unplanned exception rate, and <20 minutes operator labor per 100 simple pages.

## Moat, risks, roadmap
Moat comes from conversion failure corpus, vertical retention maps, partner distribution, and a trustworthy chain of custody—not the converter. Risks: inaccurate source claims, malware, sensitive records, fidelity loss, inaccessible outputs, conversion licensing, deadline-only demand, and scope-heavy services.

**30 days:** paid manual audits, failure taxonomy, chain-of-custody SOP. **60 days:** inventory agent, isolated worker, diff viewer, first MSP channel. **90 days:** repeatable batches, accessibility checks, retention export, evidence-based pricing. Kill or narrow if paid demand is absent after 20 qualified conversations.
