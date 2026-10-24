# Proof status

**Snapshot: 24 October 2026. The existence theorem is not proved.**

The target is one nontrivial, interacting, local four-dimensional **SU(2) Yang–Mills theory on R⁴ at positive renormalized coupling**. Mass gap, universality, uniqueness and a construction for every compact gauge group are not claims of this program.

This ledger reports what the supplied research records establish **at their declared scopes**. It does not independently certify the mathematics. Each producer and its latest scoped audit control the precise statement; an overview cannot enlarge its hypotheses. Read the [incomplete manuscript](../paper/YM4-incomplete-proof.pdf) for the argument connecting these modules, and the [current handoff status](../guide/CURRENT-STATUS.txt) for the snapshot authority.

## How to read the labels

| Label | Meaning |
|---|---|
| **Exact** | A finite algebraic or disintegration identity, with its stated integrability and domain assumptions. It is not a uniform estimate. |
| **Published input** | A result imported from primary literature at its original hypotheses. This repository does not re-prove the entire input. |
| **Internally reviewed** | A local producer has a recorded scoped internal audit. This is not peer review or certification of all inherited dependencies. |
| **Conditional** | An implication or consumer is proved under listed premises; the required premises have not all been established for the new source family. |
| **Open** | The result is unavailable as a theorem input. A candidate argument or numerical budget does not change this status. |

“Available” below means available under these qualifications. File counts, manuscript length, internal PASS labels and preservation hashes do not count proved theorems.

## Available finite and homogeneous results

### R01 — Exact finite law, sources and contacts

**Status: Exact.** Actual normalized backward kernels give a covariance telescope, an exact evolution of mixed logarithmic contacts, and a raw-transfer identity cancelling intermediate normalizers. The terminal covariance remains in the identity. Replacing actual compiled means by static sources also introduces three outer covariance correction terms.

**Limit:** these identities do not bound the emitted terms or the terminal covariance. They do not erase original cuts, coarea factors, scalar weights or retained variables.

Evidence: [producer](../evidence/inherited/continuation-workspace/work/connected_covariance_actual_kernel_consumer_20261023.txt), [independent audit](../evidence/inherited/continuation-workspace/work/connected_covariance_actual_kernel_consumer_independent_audit_20261023.txt). Readable statement: manuscript §2, Proposition 2.1, “Exact connected-source identity”; equations `covariance-tower`, `contact` and `raw-telescope` in the [source](../paper/manuscript_core.tex#L39).

### R02 — Original-law energy and P0 rarity

**Status: Internally reviewed deductions using an inherited finite-law theorem.** The original Wilson energy exponential-moment input yields simultaneous P0 bad-cube tails, a local exponential moment and a rooted bad-cluster tail with the original partition normalizer.

**Limit:** these are original-law/annealed statements. Uniform rarity under arbitrary exterior conditioning is false. P1 failures and the full outside-chart defect catalogue remain separate tasks.

Evidence: [producer, §§1–3, equations (1)–(5)](../evidence/current/outputs/YM4-original-P0-defect-mass-20261024.txt), [audit](../evidence/current/outputs/YM4-original-P0-defect-mass-audit-20261024.txt). The producer explicitly identifies its inherited energy theorem and assumptions.

### R03 — Original four-edge cavity and analytic rare source

**Status: Exact disintegration plus internally reviewed finite estimates.** Integrating the four physical edges of a plaquette gives an exact boundary source under the original exterior law. The fixed cavity has a pinned saddle, a zero-free **unmarked** denominator on a fixed tube, and raw rare marked moments and fixed-order derivatives on a cutoff-sized tube. The recorded bound is of the form `C A β⁶ exp(−c β τ²)`.

**Limit:** the interior Borel mark is fixed independently of the continued exterior parameter. Zero-freeness of the unmarked denominator does not establish zero-freeness of the event probability, so division by that probability is not justified on this tube. The original exterior weight and its complement remain.

Evidence: [original projection](../evidence/current/outputs/YM4-original-rare-cavity-source-projection-20261024.txt) / [audit](../evidence/current/outputs/YM4-original-rare-cavity-source-projection-audit-20261024.txt); [pinned tube, §§1–4 and §6](../evidence/current/outputs/YM4-pinned-plaquette-cavity-enlarged-tube-20261024.txt) / [audit](../evidence/current/outputs/YM4-pinned-plaquette-cavity-enlarged-tube-audit-20261024.txt). Manuscript §3, Theorem 3.1 and Remark 3.2 ([source](../paper/manuscript_core.tex#L93)).

### R04 — First native independent-pair cavity column

**Status: Internally reviewed finite domain match, importing the native marked-expansion module.** A gauge-invariant cavity mark has a first ordinary connected source column on a declared shrinking domain. The certificate keeps independent field/current arguments, complete reconstructed pair tests, protected occupied real noise, source localization and an explicit seed cost. Its quantum difference has the running-radius factor `(g₀/ε₀)²`.

**Limit:** this is not a fixed-core `g₀²` bound or an induction for all later generated sources. The action-only response circle is not automatically a source contour. After this step, generated coefficients have new current, operator and carrier reads; they are no longer just the original boundary function.

Evidence: [producer, §§2–5; limitations §7](../evidence/current/outputs/YM4-pinned-cavity-native-pair-first-column-20261024.txt), [audit](../evidence/current/outputs/YM4-pinned-cavity-native-pair-first-column-audit-20261024.txt). Manuscript §4, Proposition 4.1, “First shrinking-domain column” ([source](../paper/manuscript_core.tex#L221)).

### R05 — Restricted second-step pair-image certificate

**Status: Internally reviewed conditional image lemma.** On a smaller complete old/current domain intersection, the image certificate includes both direct and reconstructed old-pair tests and the literal selected current.

**Limit: the actual second source column remains open.** The standard next domain, all response norms on source contours, complete determining data and quantitative radius evolution still need registration. Repeated fixed radius contraction does not automatically provide the required logarithmic delay. The variational constant `B₃` depends on the block factor `L`.

Evidence: [producer](../evidence/current/work/pinned_cavity_second_ordinary_pair_image_20261024.txt), [root audit, §§1–4](../evidence/current/work/pinned_cavity_second_ordinary_pair_image_root_audit_20261024.txt).

### R06 — Exact real minimum tower and additive curvature bound

**Status: Internally reviewed on admitted real homogeneous prefixes.** Literal recursive ordinary constraints and regular critical-orbit uniqueness give an exact tower of original-Wilson minima up to permitted real gauge equivalence. Admitted real comparison segments yield curvature increments `C L^(−2j) δⱼ`, with coefficient one on the preceding curvature norm. This avoids an artificial loss multiplied at every scale.

**Limit:** the theorem uses complete regularity and comparison-segment hypotheses. Gauge equivalence of real minima does not prove equality of ordinary averages after a complex return, or admission of an independent-current source catalogue. Original history predicates and normalized weights remain.

Evidence: [producer, §§2 and 4–7; complex gate §8](../evidence/current/work/original_cavity_real_prefix_minimum_tower_20261024.txt), [independent audit](../evidence/current/work/original_cavity_real_prefix_minimum_tower_audit_20261024.txt). Manuscript §5, Lemma 5.1 and Theorem 5.2 ([source](../paper/manuscript_core.tex#L295)).

### R07 — Separate real whole-product continuation

**Status: Internally reviewed auxiliary source-zero real result.** A separate full-matrix current estimate, with increments `C L^(−3j) δⱼ`, closes a descending construction of the real maps on the whole product of original noise balls under fixed smallness conditions. On an admitted weak prefix with the stated coupling comparability and cutoff hierarchy, a logarithmic delay gives a rare real cavity-value bound.

**Limit:** original masks may vanish on this auxiliary domain. Whole-product map reconstruction does not make all physical histories successful, prove a selected-history mass bound, or provide a normalized complex/source-column norm. This is separate from R06 and has its own audit.

Evidence: [producer, §9](../evidence/current/work/original_cavity_real_prefix_whole_product_20261024.txt), [independent audit](../evidence/current/work/original_cavity_real_prefix_whole_product_audit_20261024.txt). Manuscript §6, equations `current-step`, `bootstrap-KJ` and `real-prefix-value` ([source](../paper/manuscript_core.tex#L406)).

### R08 — Homogeneous signed drift and finite endpoint tuning

**Status: Internally reviewed homogeneous assembly with explicit imported modules.** Complete native Gaussian factor allocation, heat/Schur estimates and Maxwell extraction give a signed whole-stretch drift with a uniform `O(1)` error. Causal continuous finite shooting supplies a homogeneous trajectory ending at any sufficiently weak terminal inverse coupling, with two-sided linear bounds in remaining depth.

**Limit:** this is a finite homogeneous result. It assumes neither positive individual increments nor a memoryless flow. Separately tuned horizons need not select compatible or unique roots, and no common continuum state follows. The recorded coefficient is tied to the producer’s action/trace convention. The result does not extend to arbitrary mixed large-field histories.

Evidence: [producer, input ledger §1, drift §§2–5, tuning §6, scope §7](../evidence/current/outputs/YM4-native-signed-drift-and-homogeneous-tuning-20261024.txt), [independent audit](../evidence/current/outputs/YM4-native-signed-drift-and-tuning-audit-20261024.txt). Manuscript §7, Proposition 7.1 ([source](../paper/manuscript_core.tex#L470)).

### R09 — Coherent regular source core on tuned trajectories

**Status: Internally reviewed registration of an inherited typed source theorem.** The actual tuned trajectory and Gaussian-window sums close the dated recurrence for the already admitted complete coherent Wilson family. Its special marginal cancellation gives a `g⁴` reference term and controls coefficient drift. Each birth retains its domain, date, scalar, full marginal tensor and original root census.

**Limit:** the special coherent cancellation does not transfer to arbitrary masks, cavity marks or neighborhood projections. A nonzero reference coefficient is not a nonzero reflection norm or interaction witness. The finite-period option remains conditional on matching the complete construction or controlling the wrapping/image remainder.

Evidence: [registration, §§1–5; scope §6](../evidence/current/outputs/YM4-tuned-regular-core-Volterra-registration-20261024.txt), [root audit](../evidence/current/outputs/YM4-tuned-regular-core-Volterra-audit-20261024.txt). Inherited inputs: [TURN77 typing](../evidence/inherited/original-workspace/work/package/work/turn77_homogeneous_typing_gauge.txt), [neutral preparation](../evidence/inherited/original-workspace/work/package/work/turn77_neutral_native_preparation_history.txt), [dated Volterra theorem](../evidence/inherited/original-workspace/work/package/work/turn77_dated_volterra_root.txt). Manuscript §8.1 ([source](../paper/manuscript_core.tex#L525)).

### R10 — Finite original-source/complement decompositions

**Status: Internally reviewed exact local identities and scoped first completions.** The first full-Omega source difference has an exact decomposition into rare one-cut covariance increments, with the connected-contact change expressed by third cumulants. Summing specified atoms on a common fiber before normalization cancels their internal moving boundaries in the recorded finite analytic completions.

**Limit:** outer complements, prior-record failures, held exterior data and later source/contact transport remain. This is not uniform-depth closure of all original histories. Rare or Lipschitz response at a hard mask does not itself prove analytic source jets.

Evidence: [producer and scoped attachment addenda](../evidence/current/outputs/YM4-original-source-rare-complement-20261024.txt), [audit and scoped addenda](../evidence/current/outputs/YM4-original-source-rare-complement-audit-20261024.txt); [completed-sector defect gate](../evidence/current/outputs/YM4-original-P0-defect-mass-20261024.txt). Manuscript §9.3 ([source](../paper/manuscript_core.tex#L624)).

## Conditional consumers and finite estimates

These results are useful, but none establishes its own missing native source hypotheses.

| ID / status | Available statement | Required input or limitation | Evidence |
|---|---|---|---|
| **C01 — Conditional** | Rare-source Volterra stability permits generic `g²` feedback and once-born rare forcing with exponential age memory. | Actual admitted recursion, uniform feedback constants and completed original source census must already hold. Smallness does not admit a new source. | [Producer §§1–5](../evidence/current/outputs/YM4-rare-source-Volterra-stability-20261024.txt), [audit](../evidence/current/outputs/YM4-rare-source-Volterra-stability-audit-20261024.txt); manuscript §8.2. |
| **C02 — Conditional** | A finite admission delay `t ≤ C log x₀` has a cost budget of order `exp[C(log x₀)²]` under the stated localization/reblocking assumptions. | Every actual complex substituted image, complete current read, baseline map, inverse margin and spatial reserve must be registered. The seed exponential does not disappear because an insertion is linear. | [Producer §§1, 3–6](../evidence/current/outputs/YM4-analytic-mark-finite-admission-transport-20261024.txt), [audit](../evidence/current/outputs/YM4-analytic-mark-finite-admission-transport-audit-20261024.txt). |
| **C03 — Exact finite criterion; native application conditional** | The normalized complex functional norm on all bounded tests is the inverse normalized phase average. Phase/Poincare and score hypotheses can yield polynomial read costs on a smaller read-dependent tube. | Native real-part coercivity, score, contour and image hypotheses are unregistered. Real positivity/convexity alone permits exponential read cost; bounded tests and holomorphic tests on a specified tube are distinct classes. | [Producer, §1 and RESULT](../evidence/current/work/normalized_complex_conditional_read_cost_20261024.txt), [root audit](../evidence/current/work/normalized_complex_conditional_read_cost_root_audit_20261024.txt). |
| **C04 — Internally reviewed finite-box result** | Quantitative rectangular-cavity pinning, saddle and raw rare-tube estimates retain explicit box-size losses. | The conservative marked tube includes a `τ R⁻⁶` restriction. It does not admit unbounded box growth with one fixed native noise hierarchy. This limits the estimate; it is not an impossibility theorem. | [Producer](../evidence/current/work/rectangular_cavity_quantitative_pinning_20261024.txt), [audit](../evidence/current/work/rectangular_cavity_quantitative_pinning_audit_20261024.txt). |

## Published inputs and their boundaries

The [source catalogue](SOURCES.md) gives the primary bibliography; the [archive guide](ARCHIVE.md#resolving-historical-paths) explains historical file paths. The table records these inputs' use in this program, not a new independent audit of each published argument.

| Input | Role here | Boundary to retain |
|---|---|---|
| [Balaban, Averaging Operations (CMP 98)](https://doi.org/10.1007/BF01211042) | Recursive averaging and relative gauge returns; printed p.33, (104)–(108), and Proposition 4, (130)–(135). | Ordinary averaging and background-relative `Q` must be explicitly matched. |
| [Balaban, Gauge Fixing Conditions (CMP 99)](https://doi.org/10.1007/BF01466594) | Regular gauge charts and full matrix curvature/current comparison, including (1.54). | This is distinct from the propagator paper; projected and full matrix currents are different claims. |
| [Balaban, Propagators in a Background Field (CMP 99)](https://doi.org/10.1007/BF01240355) | Native precision, Green kernels, localized operators and complete current insertions. | Preserve its background/domain assumptions and actual operator definitions. |
| [Balaban, Variational Problem (CMP 102)](https://doi.org/10.1007/BF01229381) | Regular critical-orbit uniqueness and response: Theorem 1, Section G, Proposition 9/(190). | Not uniqueness for rough fields; `B₃` depends on dimension and block factor. |
| [Balaban, RG Approach I (CMP 109)](https://doi.org/10.1007/BF01215223) | Averaging, constraints, independent-pair domains (1.10)–(1.17), ordinary center (2.3), selected current (3.13). | Printed Theorem 2 announces a coupling result with proof deferred. That label is not used as a proof; R08 is a separate local assembly. |
| [Balaban, RG Approach II (CMP 116)](https://doi.org/10.1007/BF01239022) and [Convergent Expansions (CMP 119)](https://doi.org/10.1007/BF01217741) | Native cluster/marked expansions, occupied real noise and connected cancellation, including B119(3.44)–(3.47). | A source must be admitted on its actual source contours and complete reads, with original normalizers. |
| [Large Field Renormalization I](https://doi.org/10.1007/BF01257412) and [II](https://doi.org/10.1007/BF01238433) | Actual R operations, eligibility, localization and bounds. | Not an automatic theorem for every new source or complete mixed-history closure. |
| [Balaban–O’Carroll, Correlation Functions (1997)](https://doi.org/10.1006/aphy.1997.5690) | Effective-action correlation method at its stated model scope. | The supplied `balaban3.pdf` is this paper, not “Large Field Renormalization III”; it supplies no automatic YM4 continuum bounds. |

The Alpoge–Sussman working repository is a source of architecture and clues. No unpublished completion or explicitly unfinished proposition is assumed. The [source catalogue](SOURCES.md) gives the inspected revision and limitations; its 23 October pin is a historical snapshot, not a claim about current HEAD.

## What is still open

| Gate | Status | Required result |
|---|---|---|
| **G1a–G1b — Literal complex transport interface** | **Open; immediate frontier** | Identify the ordinary-average / relative-`Q` endpoint and coarse-frame return. Carry the actual independently selected current through the true maps and source localizers. Control complex gauge-return products with original real noise variables fixed. |
| **G1c–G1d — Complete source admission and catalogue** | **Open** | Prove simultaneous old/current pair-domain inclusion, all response norms, complete primitive reads, normalized costs, radius evolution and genuine reblocking across the required finite logarithmic delay. Then match the admitted source census to the dated recurrence. |
| **G2 — Full original law** | **Open** | Cover all original mixed histories and complementary sectors with their masses, companions, source/contact terms and terminal covariance. |
| **G3 — Observable and contact contract** | **Open** | Specify the observable algebra, physical calibration and collision/contact topology, with calibrated joint estimates and local volume control sufficient for the limit. |
| **G4 — Common limiting state and reconstruction** | **Open** | Construct a compatible continuum and infinite-volume state from the actual full finite laws; establish positivity, Euclidean symmetry, consistency, regularity, locality and reconstruction. Independently tuned finite horizons do not already provide this state. |
| **G5 — Yang–Mills identification and interaction** | **Open** | Identify the intended nonabelian dynamics; prove a nonzero observable/reflection norm and a justified interaction witness in the same reconstructed state, excluding the relevant free/generalized-free alternatives. |

These IDs match the [open-problem work packages](OPEN-PROBLEMS.md), which give acceptance criteria. The detailed immediate contract is in [the frontier report, §§2–6](../guide/frontier.txt), with the broader architecture in manuscript §§9–10. **No completed complex common-frame producer or scoped audit was saved at this snapshot.** Proposed estimates for that route are observations, not theorem inputs.

## Obstructions and superseded shortcuts

These records prevent collaborators from repeating approaches that already failed at a specified scope.

| Shortcut | What the records actually show |
|---|---|
| “The homogeneous trajectory is still missing.” | Superseded at the finite homogeneous scope by R08. The typed regular core in R09 is also available; the new admission problem concerns masks, cavity marks and their generated catalogues. |
| “Bound the full raw Wilson energy uniformly in L².” | At unchanged physical calibration, the recorded lower bound `C_f |c_a|² a⁻⁴ t_a⁻²` diverges on the registered weak trajectory. Deterministic centering does not remove it. Separated/collision-flat observables or a justified distributional/contact treatment remain possibilities. See [variance producer, MAIN FINDING (A) and §3](../evidence/current/outputs/YM4-Wilson-variance-and-locality-20261023.txt) and [audit](../evidence/current/outputs/YM4-Wilson-variance-audit-20261023.txt). |
| “Rare under the original law means rare under every exterior condition.” | False; the [defect-gate note](../evidence/current/outputs/YM4-original-P0-defect-mass-20261024.txt) records a frustrated-staple obstruction. The annealed result survives. |
| “Real whole-product control is a complex source theorem.” | R07 permits original masks to vanish. It neither proves complex pair tests nor permits complex rotation of original real noise variables. |
| “A tiny amplitude fixes a domain problem.” | A source value must first be defined on its actual substituted image. Fixed shrink at each step does not automatically span the logarithmic delay; increasing `L` alone is not a proof because `B₃` depends on `L`. |
| “Real positivity bounds complex normalized means.” | Phase cancellation can cause large normalized complex norms; C03 gives exact criteria and counterexamples. |
| “An analytic action removes moving-mask corners.” | Intersecting hard cuts can give a nonzero `|t|` response. Local completed fibers have a specific cancellation; their exterior and history complements remain. |
| “Logarithmic rarity pays every root count.” | It does not pay arbitrary-age `L^(4s)` counts or uncontrolled `C^s` amplification. C02 can pay a specified finite delay only after its image and reblocking premises are proved. |
| “A nonzero coefficient or higher cumulant proves interaction.” | A regular-core coefficient need not survive full-law reconstruction as a nonzero reflection norm. Nonlinear observables of free fields can have higher cumulants. G5 requires a suitable witness in the same identified state. |

## Snapshot and review boundaries

The frozen checkpoint has **249 referenced TXT documents plus the checkpoint itself**. Its dated filename and historical ACTIVE wording do not describe a new proof result or a current instruction. Five later producer/audit pairs add ten files; [their register](../guide/latest-reviewed-addenda.json) preserves the original source paths, and the [archive path guide](ARCHIVE.md#resolving-historical-paths) explains translation into this edition.

The manuscript is a readable synthesis. The restricted second image, complex read-cost criterion and rectangular cavity are separate addenda, so reading only the manuscript misses useful scoped results. Conversely, the [manuscript scope audit](../guide/manuscript-scope-audit.txt) checks framing and finite algebra; it explicitly does not recertify all imported Balaban or inherited TURN77 dependencies.

When using a result, cite its producer, the matching audit, the exact section/equation and the hypotheses actually used. When changing its scope, record a new argument and review instead of silently editing a historical PASS into a stronger claim.
