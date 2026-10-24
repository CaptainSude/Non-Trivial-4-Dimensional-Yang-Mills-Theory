# Archive coverage and reproducibility

The research snapshot is the user-supplied **YM4-collaborator-handoff-20261024.zip**, dated 24 October 2026. The GitHub repository was empty when this research edition was prepared.

Original ZIP SHA-256:

```text
30a58901d3fc7b000de6c810997fc00fb928aeacc479086edf79faa031a80f0e
```

The ZIP has **6,000 files**: 5,999 payload entries listed in its manifest plus the manifest itself. Its 250 current delivered TXT files consist of a frozen checkpoint and 249 referenced files. Ten later files form five additional producer/audit pairs. These are document counts, not theorem counts.

## What this edition contains

The [evidence catalogue](../catalog/README.md) is the exact public selection. It includes all 250 current delivered TXT notes, substantive current working notes not byte-identical to deliveries, the latest five producer/audit pairs, selected inherited dependencies, the status/frontier records, and the existing incomplete manuscript and PDF. A search through explicit scientific TXT/TeX references added 570 older dependency files to the initial 288-note core. These older files retain their historical scopes and corrections. Historical current-checkpoint fragments, duplicate copies, operational scripts, conversation exports, and third-party paper caches stay in the original archive.

This is a curated research edition. It is **not a complete reproduction of the ZIP, a transitive certification of all imported modules, or a new proof audit**. The [full archive index](../catalog/archive-index.tsv) records every manifested payload path, original size and hash, and whether it is included, represented by a byte-identical published copy, or available only in the original archive. The original ZIP is not hosted by this repository; archive-only entries require access to that supplied handoff. Official literature references are in [sources](SOURCES.md).

The [published-evidence manifest](../catalog/published-evidence.json) records original and published hashes. Local workstation roots in inherited notes are replaced by archive-relative or supplied-PDF locators; mathematical text, paper filenames, and DOI identifiers are retained. Each changed file records that publication edit. Other selected source bytes are preserved. Newly written Markdown files are navigation and editorial summaries, not frozen original evidence.

## Resolving historical paths

Current source notes often use these historical forms:

| Reference in a current note | Location in the supplied ZIP / repository selection |
| --- | --- |
| `outputs/YM4-….txt` | `evidence/current/outputs/YM4-….txt` |
| `work/<current-note>.txt` | `evidence/current/work/<current-note>.txt`, or its byte-identical delivered copy in the catalogue |
| `work/handoff/…` | `evidence/inherited/…` |
| `P = work/handoff/original-workspace/work/package` | `evidence/inherited/original-workspace/work/package` |
| `A = P/work` | `evidence/inherited/original-workspace/work/package/work` |
| `C = work/handoff/continuation-workspace` | `evidence/inherited/continuation-workspace` |

Apply the specific inherited mapping before the general current `work/` mapping. Within older inherited notes, `work/` may refer to their own earlier workspace: resolve it against the archive index and surrounding dependency chain, not automatically against today's working directory. A basename match alone is not sufficient when several versions differ.

Current working/delivered aliases and inherited duplicate aliases are explicitly recorded in the published manifest. Alias identity refers to the original archive bytes; any public path normalization is recorded separately. A different scientific source version must not be substituted merely because names look similar.

## Status and review boundaries

Use [PROOF-STATUS](PROOF-STATUS.md), the preserved [current status](../guide/CURRENT-STATUS.txt), and the newest claim-specific producer/audit pair together. The manuscript summarizes their scopes; it cannot enlarge their hypotheses. [Latest addenda](../guide/latest-reviewed-addenda.json) identifies the five post-checkpoint pairs, while [frontier](../guide/frontier.txt) records the unproved complex-prefix investigation.

The manuscript's source audit records the hash of its reviewed source before the final appendix path-formatting change. The archived `guide/reviewed-manuscript-source.tex` matches that audit hash; the published `paper/manuscript_core.tex` is the final handoff source. The source inventory comparison found the difference to be appendix path formatting, not a newly reviewed theorem. Both archive versions are identified by the full catalogue.

The organization work checked selected-source hashes, checkpoint/addendum coverage, and the navigation links. Those checks establish preservation and usability. They do not certify the mathematical validity of all dependencies. Historical task instructions, goals, chat state, and “ACTIVE” labels in preserved notes do not govern this repository's current work.
