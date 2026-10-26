# Notation bridge

This is an orientation aid, based on the preserved [notation and conventions](../guide/NOTATION-AND-CONVENTIONS.txt). Each producer's local definitions prevail. Symbols are reused across the archive.

| Symbol or term | Meaning and caveat |
| --- | --- |
| SU(2), U, U_p | Gauge group, link field, and ordered plaquette product; orientation determines inverses. Haar measure is normalized. |
| h_p | Wilson plaquette action `1 − ½ Tr(U_p)` on SU(2). It is not the logarithmic contact `h_e`. |
| β in the Wilson weight | Positive inverse coupling in `exp(−β Σ h_p)`, with `β = C_W/g₀²` in the chosen normalization. |
| β(F) in drift notes | Maxwell-coefficient extractor, not the Wilson inverse coupling. |
| c_a | Actual observable calibration. Keep it explicit; do not insert a new microscopic volume factor. |
| L, j, η_j | Fixed block factor, ordinary grade, and fine mesh `η_j = L^(−j)` in the real-prefix comparison. Constants may depend on fixed L. |
| g_j, q_j, x_j | Running coupling, `q_j = g_j²`, and `x_j = g_j^(−2)` in trajectory notes. **In prefix formulas x_j may instead denote an original real noise variable.** |
| X, G | A terminal inverse-coupling target and a weak floor in trajectory estimates. The letter G also denotes the gauge group or a Gaussian coefficient elsewhere. |
| ε₀, τ, δ_j | Cavity threshold/tube scales and native noise caps, with their stated fixed cutoff hierarchy. A window-error τ_j in regular-source notes is a different object. |
| F_e, Q_e | Actual normalized conditional kernel including original cuts, constraints, Jacobians/coarea, action, and scalar normalizers. |
| f_(e+1) = F_e f_e | Transported conditional mean. It is a generated source with its complete reads, not a new microscopic insertion. |
| c_e | Covariance emission `F_e(f_e g_e) − (F_e f_e)(F_e g_e)`. |
| h_(e+1) = F_e h_e + c_e | Independent logarithmic-contact evolution; the final outer covariance remains. |
| (U,J) | Independent analytic field/current pair. Equality of J with the physical current holds on the physical graph, not automatically after localization. |
| Selected current | The carried analytic companion schematically `θ³J + ΔA − P₁A + F₁(U,A)`; even at zero noise it is scaled, not an unscaled J. |
| s-localization / t_D | Source argument weakening versus an action-only auxiliary response circle. Their admitted domains differ. |
| Complete read / carrier | Every block, gauge, descendant, collar, and old/current datum determining a coefficient. Initial observable support alone may be smaller. |
| M_j, U_j(v), W_j | Literal recursive ordinary average; original-Wilson constrained minimum on the fine grid; and real-prefix minimum `W_j = U_j(V_j)`. |
| Ordinary average / relative Q | Distinct coordinate descriptions. The current declared maps have their own scoped registration; this does not settle every alternative cavity/source extension. |
| a_p | Raw marked cavity numerator divided by the original unmarked cavity denominator. The exterior partition weight stays in the original law. |
| Source-zero | The original physical operation before source derivatives. An analytic source extension must agree there where physical agreement is claimed. |
| Root census | The original number of fine source locations represented in a later block; its cost must be accounted for separately from rarity. |

For status labels, see [contribution vocabulary](../CONTRIBUTING.md#status-vocabulary). A gain in amplitude, a domain margin, a root count, and an observable calibration are distinct quantities; combine them only through a proved inequality in the same setting.

## Current checkpoint conventions

| Symbol | Meaning in the 26 October argument |
| --- | --- |
| `x_j`, `y_j` | Old frozen real inverse-coupling history and new source-zero `Gamma_j^new(0)`. They are compared, not assumed identical. |
| `C[Gamma]`, `D` | Fixed-cap core replayed at the entire realized coupling history, and the same-coupling body discrepancy. |
| `R′`, `R″` | Fresh completed outer birth and ordinary young birth; both keep their actual function-birth dates. |
| `A_old`, new noise | Retained real private coordinates and newly introduced noise. Pair analyticity does not imply analyticity in old smooth cutoff variables. |
| `W_j(C)` | Actual dated component cost `M⁴ R_j⁵ (d′_j(C)+1)`, with unique primitive identifiers. |
| `chi_j^N` | `L^(-(N-j)/2)`, the spatial-source age factor; obtained by the value-before-gradient construction. |
| `r(x)` | A bare source radius with a fixed polynomial lower formula, independent of the desired later rarity power. |
| `E_abs`, `E(w)` | New absolute universal vacuum and its source-zero-subtracted version. History-dependent scalars stay in the remainder. |
| `h(w)` | One normalized source remainder, `exp(-E(w)) Z(w)/Z(0)`, with `h(0)=1`. It need not be zero-free away from zero. |
| `c_a` | Fixed original calibration `x_n/e_n^old`; no extra `a⁴` factor in the original plaquette sum. |
| `C_orig`, `C_old`, `C_new` | Original covariance, original registered homogeneous reference, and the auxiliary **packed average** of the nearby new-core covariances. |
| `X`, `Y`, `tau` | Probe-entry inverse-coupling scale, later fixed weak terminal floor, and physical probe separation. Fix Y before X and keep probes fixed during regulator removal. |

See the [contract](../research/2026-10-26-full-history-checkpoint/work/full-history-four-entry-checkpoint-contract-20261025.txt) and [assembly](../research/2026-10-26-full-history-checkpoint/work/full-history-four-entry-assembly-20261026.txt) for exact definitions and quantifiers.
