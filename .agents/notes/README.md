# Decision records

This directory is the authority for durable Daily Source Intelligence decisions that are not already owned by a more specific ADR, RFC, or repository document.

## Lifecycle

- `proposed/`: an active proposal that is not yet shipped or accepted.
- `implemented/`: the present-tense decision after implementation and verification.
- `rejected/`: a considered proposal that was explicitly rejected.
- `archived/`: frozen history that has been superseded or is no longer active.

## Classes

Use one of: `feature`, `bug-fix`, `simplification`, `architecture`, `process`, or `testing`. Create a class directory only when it contains a record.

## Record contract

A proposed record states its status, class, owner, problem, proposal, actually considered alternatives, consequences or risks, durable boundaries or non-goals, related `REQ-*` semantics, and required verification. An implemented record rewrites those sections in present tense and contains only verification actually obtained.

The owner updates the same proposed record while the decision is still active. Before creating another record, search active records by decision semantics. Full or partial supersession must cross-link the new and old records, state the replaced scope, and leave unaffected decisions current. Archived records are not rewritten.
