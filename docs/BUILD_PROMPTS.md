# Phased build prompts

1. **Discovery:** Build a metadata-only local scanner for `.pub` files with path aliases, checksums, page/font/link probes, CSV/JSON export, and Windows tests. Never upload content.
2. **Pilot conversion:** Add an isolated queue worker, version-pinned converters, malware scanning, timeouts, idempotency, encrypted artifacts, and representative fixtures with golden render comparisons.
3. **QA:** Build side-by-side page review, missing-font/link detection, reviewer decisions, exception routing, keyboard navigation, and WCAG checks.
4. **Operations:** Add tenant isolation, retention controls, audit events, OpenTelemetry, job SLOs, cost attribution, support runbooks, and disaster recovery exercises.
5. **Commercial:** Add paid audit intake, volume discovery, quotes with assumptions, partner referrals, outcome analytics, and opt-in archive assurance. Do not automate pricing until labor variance is measured.
