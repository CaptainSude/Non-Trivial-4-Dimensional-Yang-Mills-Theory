# Contributing to YM4

Start with the [proof-status ledger](docs/PROOF-STATUS.md) and choose a bounded claim from [open problems](docs/OPEN-PROBLEMS.md). This is an incomplete research program. A proof, a counterexample, a corrected primary-source reading, or a precise missing hypothesis is a useful contribution.

## A contribution that can be checked

Please provide:

1. **Claim and status.** State the result to be proved and whether the submission is a proposal, conditional lemma, proof, or obstruction.
2. **Objects and domain.** Specify the finite law, source, field/current slots, scale range, gauge representatives, cuts, normalizers, complete reads, and all smallness assumptions actually used.
3. **Dependencies.** Link exact producer notes and their audits. For published imports, give the theorem/equation and printed page, not just the paper title.
4. **Argument and accounting.** Track calibration, scale constants, radius prices, root counts, source dates, carrier size, contacts, and complements where relevant. Identify which bounds are uniform.
5. **Scope and failure tests.** Say what the result does not cover and check the relevant obstructions in [corrections](docs/CORRECTIONS.md).
6. **Review.** Include or request a separate scoped audit. A review should say what it checked and which dependencies it took as premises. Record disagreements and corrections explicitly.

## Keep evidence and status synchronized

Keep the imported snapshot files unchanged. Add new dated research notes under `research/` and audits beside them. A filename such as `2026-10-25-G1a-endpoint-return.md` makes the claim and date easy to find. Update the corresponding ledger row and open-problem entry in the same pull request, with links to the new evidence and any superseded claim.

Do not close a gate merely because a numerical consumer or one-step estimate is proved: match the actual native hypotheses. An obstruction should identify the precise route it rules out; failure of one sufficient estimate is not a no-go theorem for the whole program.

## Status vocabulary

| Label | Meaning |
| --- | --- |
| Exact finite identity | Algebra/disintegration under the specified finite law and domain. |
| Published input | An external theorem imported at its original hypotheses. |
| Internally reviewed | A local deduction with a scoped internal audit; inherited premises still apply. |
| Conditional | A proved implication whose application requires premises not all established here. |
| Open / proposal | Unavailable as a theorem input. |
| Historical / superseded | Retained for provenance; use the linked correction to determine current scope. |

The archive's “PASS,” “ACTIVE,” and paused-goal messages are historical records. They are not mathematical certification or authorization to change project scope. Hash checks establish byte identity only.

## Submitting a correction

Use a pull request for mathematical files or an issue for a focused claim, question, or counterexample. Give the work-package ID and the smallest relevant source excerpt. Avoid bulk conversation dumps. Do not introduce a license for material whose reuse terms have not been established; cite external papers through their official records.
