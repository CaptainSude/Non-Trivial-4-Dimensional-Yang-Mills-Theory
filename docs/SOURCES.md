# Primary literature and provenance

The project uses published Balaban results at their original hypotheses, internal deductions at their recorded scopes, and public working manuscripts as clues. A bibliographic citation is not itself a proof that a native source satisfies the cited theorem's assumptions. The [status ledger](PROOF-STATUS.md) separates these roles.

The table below transcribes the supplied manuscript's bibliography and the handoff's primary-paper map. It does not claim a new audit of every printed theorem. The [frontier report](../guide/frontier.txt) records the exact primary-page readings behind the historical cavity interface; the new [dependency ledger](../research/2026-10-26-full-history-checkpoint/PROOF-DEPENDENCIES.txt) gives the current application locators. Use the printed mathematics to resolve OCR ambiguities.

| Alias | Published reference | Role in the recorded dependency chain |
| --- | --- | --- |
| B98 | T. Balaban, *Averaging Operations for Lattice Gauge Theories*, CMP **98** (1985), 17–51. [DOI](https://doi.org/10.1007/BF01211042) | Ordinary/relative averaging, gauge return, and relative-field estimates under their hypotheses. |
| B99 gauge | T. Balaban, *Spaces of Regular Gauge Field Configurations on a Lattice and Gauge Fixing Conditions*, CMP **99** (1985), 75–102. [DOI](https://doi.org/10.1007/BF01466594) | Regular configuration spaces and gauge representatives. |
| B99 propagator | T. Balaban, *Propagators for Lattice Gauge Theories in a Background Field*, CMP **99** (1985), 389–434. [DOI](https://doi.org/10.1007/BF01240355) | Background propagators. This is a different paper from B99 gauge. |
| B102 / CMP102 | T. Balaban, *The Variational Problem and Background Fields in Renormalization Group Method for Lattice Gauge Theories*, CMP **102** (1985), 277–309. [DOI](https://doi.org/10.1007/BF01229381) | Constrained minima and relative response machinery. |
| B102 UV3D | T. Balaban, *Ultraviolet Stability of Three-Dimensional Lattice Pure Gauge Field Theories*, CMP **102** (1985), 255–275. [DOI](https://doi.org/10.1007/BF01229380) | The supplied `paper6.pdf`; specific preparation formulas and finite-order stability, not an exact all-order four-dimensional source theorem. |
| B109 | T. Balaban, *Renormalization Group Approach to Lattice Gauge Field Theories. I. Generation of Effective Actions in a Small Field Approximation and a Coupling Constant Renormalization in Four Dimensions*, CMP **109** (1987), 249–301. [DOI](https://doi.org/10.1007/BF01215223) | Complete native field/current domains, selected current, and small-field action generation. |
| B116 | T. Balaban, *Renormalization Group Approach to Lattice Gauge Field Theories. II. Cluster Expansions*, CMP **116** (1988), 1–22. [DOI](https://doi.org/10.1007/BF01239022) | Native response maps and cluster expansion/localization. |
| B119 | T. Balaban, *Convergent Renormalization Expansions for Lattice Gauge Theories*, CMP **119** (1988), 243–285. [DOI](https://doi.org/10.1007/BF01217741) | Convergent renormalization expansion input. |
| LI | T. Balaban, *Large Field Renormalization. I. The Basic Step of the R Operation*, CMP **122** (1989), 175–202. [DOI](https://doi.org/10.1007/BF01257412) | Large-field R-operation step. |
| LII | T. Balaban, *Large Field Renormalization. II. Localization, Exponentiation, and Bounds for the R Operation*, CMP **122** (1989), 355–392. [DOI](https://doi.org/10.1007/BF01238433) | Localization and bounds for the R operation. |
| BOC | T. Balaban and M. O'Carroll, *A Simple Method for Correlation Functions via the Effective Actions in the Renormalization Group Framework*, Annals of Physics **260** (1997), 1–8. [DOI](https://doi.org/10.1006/aphy.1997.5690) | Effective-action correlation identities; its illustrative model does not supply the missing YM4 source estimates. |

## Printed locators for the historical cavity interface

| Question | Primary locator recorded in the frontier |
| --- | --- |
| Literal gauge return and its background hypotheses | B98 (104)–(108), (130)–(135), Proposition 4; printed p.33 for the ordered return product. |
| Relative axial versus Landau representative | B99 gauge, printed pp.88–89, (1.70)–(1.74); B109 printed p.265. |
| Complete direct and reconstructed domain tests | B109 printed pp.262–263, (i)–(iv), (1.15)–(1.17). |
| Selected independent-current companion | B109 printed pp.272–273, (3.10)–(3.17). |
| Native noise/response maps and source localization | B116 printed pp.2–6, especially (1.18)–(1.21). |
| Relative minimum response and axial return | B102 printed pp.305–309, (170)–(190), Proposition 9; printed pp.296–297, (124). |

For example, B98's stated complex relative-field estimate over a regular real background is not, without further work, a uniform estimate over the changing complex background required by G1. The frontier distinguishes what was read from what was proved.

## Public working material

The supplied handoff records the Alpoge–Sussman [Yang–Mills LLM experiment](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment) at [commit ee1cbcf5c3065d361961a535f0307ecc9732ee05](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/ee1cbcf5c3065d361961a535f0307ecc9732ee05). This is a historical pin reported by the handoff, not a claim about the current upstream head. That material supplies possible mechanisms and a roadmap; this project imports no completed existence theorem from it. Its recorded two-point nontriviality notion must not silently replace this project's interaction target.

## Internal evidence

Read a producer together with its audit and actual imported premises. Current research is indexed in the [evidence catalogue](../catalog/README.md). The manuscript is an overview of that evidence, not an independent reconstruction of every dependency. The source-scope audit states this explicitly in [its review boundary](../guide/manuscript-scope-audit.txt).

Third-party article caches and OCR are retained in the original ZIP, not republished in this edition. The official links above identify the sources; the [archive index](../catalog/archive-index.tsv) locates the supplied copies and page renders when consulting that ZIP.

## Primary checks used in the 26 October addition

The current [source/stability readback](../research/2026-10-26-full-history-checkpoint/work/full-history-source-stability-and-packing-independent-readback-20261026.txt) records B119 printed pp.261–262 and 276–279, Large-I pp.187–192, and Large-II pp.375–390. The distinction between old private A and new preliminary noise, exact deferred integration, original rooted constituent costs and the original unnormalized operation are essential.

The [from-bare audit](../research/2026-10-26-full-history-checkpoint/work/from-bare-fine-M-R-constructor-independent-audit-20261025.txt) identifies the T/preliminary-R/final-R formula scopes; the [mixed-domain audit](../research/2026-10-26-full-history-checkpoint/work/old-mixed-noise-scalar-disc-and-phased-R-image-audit-20261025.txt) and [radius compatibility check](../research/2026-10-26-full-history-checkpoint/work/native-large-R-analytic-radius-power-compatibility-audit-20261025.txt) retain the actual source images and parameter restrictions.

The later hints snapshot used in this research is [d5baf0c5304adb2df286ad37d18076c0c16c0262](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/d5baf0c5304adb2df286ad37d18076c0c16c0262). This supplements the older handoff pin above; neither pin is a claimed proof of a completed construction. Third-party PDFs, OCR and equation-page caches are not included in the public research addition.
