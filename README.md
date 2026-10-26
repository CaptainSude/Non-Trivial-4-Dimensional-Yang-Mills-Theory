# YM4: proof status and research record

**Updated 26 October 2026. The continuum Yang–Mills existence proof remains unfinished.**

The target is a nontrivial, interacting, local four-dimensional **SU(2) Yang–Mills theory on R⁴ at positive renormalized coupling**. Mass gap, uniqueness, universality and extension to all compact gauge groups are not additional requirements of this program.

The latest research reaches a bounded checkpoint: a regulator-uniform comparison of **four separated reflected energy covariances under the complete original Wilson law**, retaining the history normalization, posterior marks, mixed contacts and outer-R operations. The argument has scoped internal audits and uses explicitly listed native analytic estimates. This is not external peer review or certification of every inherited dependency.

## Start here

1. [New proof draft — PDF](research/2026-10-26-full-history-checkpoint/Proof-draft.pdf) · [editable LaTeX](research/2026-10-26-full-history-checkpoint/proof-draft/main.tex).
2. [Current proof-status ledger](docs/PROOF-STATUS.md) and [remaining work](docs/OPEN-PROBLEMS.md).
3. [Dated result, dependencies and audits](research/2026-10-26-full-history-checkpoint/README.md).
4. [Reading routes](docs/READING-GUIDE.md), [notation](docs/NOTATION.md) and [source catalogue](docs/SOURCES.md).

## The new checkpoint

The observable remains

`O_a(f) = (x_n / e_n^old) Σ_(original positive plaquettes p) f(x_p) [1 − ½ Tr(U_p)]`.

There is **no additional a⁴ factor**. The same real calibration is held fixed for all four probes and during source differentiation. For the two unit-mass bumps and their reflections specified in the [contract](research/2026-10-26-full-history-checkpoint/work/full-history-four-entry-checkpoint-contract-20261025.txt), the comparison gives

`|C_orig,ij − C_old,ij| ≤ 9 / (6400 π⁴ τ⁸)`, for `i,j ∈ {0,1}`,

after the stated finite weak-floor and scale choices and control of the named regulator errors. Together with the registered homogeneous comparison, this leaves the original-law reflected witness

`E_mu[(θF)F] ≥ 9 / (800 π⁴ τ⁸)`, with `F = O_a(f₀−f₁) − E_mu O_a(f₀−f₁)`.

Read the [assembly](research/2026-10-26-full-history-checkpoint/work/full-history-four-entry-assembly-20261026.txt) together with its [main application audit](research/2026-10-26-full-history-checkpoint/work/consolidated-main-application-independent-readback-20261026.txt). The conclusion concerns these separated probes on the declared admissible regulator sequence; it is not a general theorem for arbitrary sources, collisions or normalized complex private posteriors.

## What is established, and what remains?

| Ingredient | Current status | Scope that must remain explicit |
| --- | --- | --- |
| Exact finite source transport and mixed-contact identities | Exact finite identities | All original weights and final covariance remain. |
| Canonical weak windows, calibration and homogeneous signed comparison | Internally reviewed research modules | Named domain, native estimate and finite-period premises apply. |
| From-bare source construction, dated private-block costs and common-vacuum stability | Internally reviewed for the declared construction | Old and new coefficient conventions are compared; complex private masses are not divided out. |
| Full original-law four-entry energy checkpoint | Internally reviewed under the listed native inputs | Four separated reflected probes, with all error allowances and the same calibration. |
| Observable algebra, collisions and a common continuum/infinite-volume state | **Open** | The four-entry estimate is insufficient for these limits and joint bounds. |
| Reconstruction, Yang–Mills identification and interaction | **Open** | A positive energy two-point witness does not exclude a free-field composite. |

The [ledger](docs/PROOF-STATUS.md) separates exact statements, published inputs, internal deductions, conditional consumers and open obligations. No percentage of a completed existence proof is assigned.

## Next work

The immediate construction task is to specify the common observable algebra and contact topology, then prove the joint estimates and compatibility needed for one continuum and infinite-volume state. The positive witness must survive that same limiting procedure. Reconstruction, dynamical identification and a valid interaction criterion remain necessary.

The former cavity-prefix route is preserved as a specific historical/alternative problem. The new construction addresses the source interface needed for this checkpoint; it does not declare every version of the older G1/G2 tasks solved. See [the work packages](docs/OPEN-PROBLEMS.md).

## Evidence and collaboration

The [26 October research addition](research/2026-10-26-full-history-checkpoint/README.md) contains the draft, mathematical producer notes, scoped audits and a publication manifest. The [24 October manuscript](paper/YM4-incomplete-proof.pdf), guides and imported evidence remain unchanged as historical snapshots. The [archive guide](docs/ARCHIVE.md) distinguishes the two editions and maps their paths.

Use the [contribution guide](CONTRIBUTING.md): state the precise claim, its original law and domains, dependencies, bounds and limitations, and supply a scoped audit. [Corrections](docs/CORRECTIONS.md) records failed shortcuts. Raw conversation exports, operational logs and third-party article caches are not republished here.
