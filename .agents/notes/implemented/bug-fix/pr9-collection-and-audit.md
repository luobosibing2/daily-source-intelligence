# PR9 collection and audit closure fixes

- Status: implemented on the isolated fix branch; pending review and main merge
- Class: bug-fix
- Owner: Daily Source Intelligence maintainers
- Baseline: production main `376f5982160134d588f76daf3599e9272cc3eea6`
- Scope: PR9 [missing-key P1](https://github.com/luobosibing2/daily-source-intelligence/pull/9#discussion_r4214238343) and [stale disposition P1](https://github.com/luobosibing2/daily-source-intelligence/pull/9#discussion_r4214238358)

## Decision

[The X collector](../../../../scripts/collect-twitterapi-io.py) returns a nonzero code when credentials are unavailable. It writes skipped account records with empty tweets. A targeted run replaces only selected accounts and preserves unselected account records. [The unified runner](../../../../scripts/dsi.py) records failed collection attempts and stops automatic preparation after a nonzero collector exit. Collection resume requires real output files with matching hashes. The X fingerprint contract changes once to invalidate pre-fix success records that could contain stale or missing output.

[Candidate audit](../../../../scripts/candidate-audit.py) restores manual dispositions and notes, while recomputing the generated `covered_in_report` value from current coverage. [Report validation](../../../../scripts/validate-daily-report.py) rejects any missed row claiming `covered_in_report`, including artifacts written before this correction.

## Alternatives and consequences

Keeping exit code zero with only a skipped artifact was rejected because the unified runner would still record collection success. Returning failure alone was insufficient because direct preparation could still read the old selected-account tweets. Output hashes alone cannot identify a legacy stale success; the X contract version invalidates those cached records.

The next resume of a pre-fix run containing X performs collection again. With available credentials it can make normal paid read requests. Other channel-only fingerprints stay compatible. A failed unified run requires a collection retry or deliberate preparation of reviewed skipped/failed evidence, as described in the [runbook](../../../../runbook.md).

Manual dispositions remain free-form under the existing contract; this fix excludes the generated coverage value rather than introducing a new disposition enum.

## Verification and boundaries

- The new regressions reproduced missing-key false success, stale/empty-output resume, stale generated dispositions, and acceptance of contradictory audit rows before the production fixes.
- `python3 -m unittest tests.test_collect_twitterapi_io tests.test_dsi_cli tests.test_candidate_audit tests.test_validate_daily_report`: 33 tests passed.
- `python3 -m unittest discover -s tests -v`: 116 tests passed.
- Regression fixtures cover targeted and full no-key runs, existing and absent output, preservation of unselected accounts, legacy cached success, repeated failed resume, successful resume, report removal and re-audit for official links/Engineering/podcasts, manual disposition preservation, and independent validator rejection.
- Python bytecode compilation and `git diff --check` passed.
- No repository lint or type-check configuration or GitHub Actions workflow is present on this baseline. Real paid collection, model execution, daily publication, credential changes, scheduling, merge and deployment were not performed.
