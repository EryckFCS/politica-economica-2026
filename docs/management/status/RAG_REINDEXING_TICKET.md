# TICKET: RAG Re-indexing & Sanitization Required

## Status: PENDING
## Priority: HIGH
## Assigned to: Antigravity AI

## Description
Following the migration to **Federated Architecture v8.0.0**, the existing RAG chunks for the `economic_policy` collection are considered "Dirty" or "Legacy". The current indexing (performed on 2026-04-21) uses paths that no longer exist and lacks the high-density sanitization required for Level 5 intelligence.

## Technical Tasks
1. [ ] **Flush Collection**: Clear all existing chunks for `politica_economica` in the central vector store.
2. [ ] **USP Pipeline Activation**:
    - [ ] Run OCR on `bibliography/raw/` (if density < 60%).
    - [ ] Convert to Markdown in `bibliography/markdown/`.
    - [ ] Sanitize and chunk into `bibliography/sanitized/`.
3. [ ] **Re-indexing**: Ingest the sanitized chunks using the `ecs_quantitative.intelligence` tools.
4. [ ] **Validation**: Verify retrieval quality against the `unit-01-policy-formulation` query set.

## Links
- [bibliography_index.json](../../../bibliography/bibliography_index.json)
- [rag_status.json](../../../bibliography/rag_status.json)

---
*Created during Federation Intervention Phase.*
