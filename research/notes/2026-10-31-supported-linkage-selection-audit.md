# Independent audit: supported linkage selection

Date: 2026-10-31. Reviewer: fresh independent `gpt-6.1-sol/high`
worker; no nested delegation. Outcome: **scoped PASS** for the
provisional deductions and stopping decision in
[the source, §§1–5](2026-10-31-supported-linkage-selection.md).
No canonical promotion or unrestricted STCI exclusion is accepted.

## State and dependencies

Reviewed source SHA-256:
`2466caa05e8ab689c18de7c778c8b9c4f2a26913df8d1b66814c48299415ff38`.

The scope is the fixed curve
`C=[s^4:s^3t:st^3:t^4]` over an algebraically closed field of
characteristic zero, and its fixed quadratic cover
`E=k[a,b,c,d,z]/(z^2-2bc+ad)`. Reviewed the current source in full,
the relevant preceding quadratic-boundary and projection-source
arguments, and the promoted
[STCI-R-0001 record](../results/quartic_carrier_exclusion.md), including
its explicit factor-reduction consequence. Its inherited quartic
proof and linked historical audits were reused, not rerun or newly
certified. The quadratic-boundary results remain independently reviewed
provisional inputs.

## Independent reconstruction and challenges

1. **Rao comparison.** From the preceding canonical sequence, the
   cokernel of `T(e-1) -> omega_T` is
   `Ext^3_S(B,S(-4))(-1)=M_W^vee(-1)`. Its degree `1-n` part gives
   exactly `delta-H_Delta(n-1)-H_Delta(e-n)`. The source's complementary
   degree involution is correct. Nonnegativity repeats the existing
   restriction-function inequality; dimensions do not recover module
   multiplication or an embedded direct conjugate link.
2. **Ribbon control.** The two displayed monomial sections have no
   common zero and therefore give a conormal quotient for all stated
   large degrees. The ideal-sheaf kernel contains `I_D^2` and produces
   an embedded ribbon on the same quadric. Euler characteristic gives
   genus `-l-1`. For large `l`, its global functions exceed the constants,
   excluding ACM. This refutes a support-and-multiplicity-only lower
   genus bound, not a bound assuming an ACM branch or the actual AG
   union. No explicit conormal splitting degrees are needed.
3. **Actual BDL source.** Independently reconstructed sequence (3):
   cancellation by `g^v` modulo `f^u` gives its injectivity. Both end
   modules are CM of dimension two, so the source is saturated,
   unmixed and ACM. The support is exactly `D`; the degree and cycle
   follow from that sequence. These are actual projective schemes,
   not only generic or formal models.
4. **Uniform generic gate.** On `a=1`, substitution gives
   `g=(c-bz)^2-z^2f`. At the generic point of `D`, `z` is a unit and
   `x=g,y=c-bz` are regular parameters. For `u>=2`, none of the three
   generators in (4) can be omitted: the first is not divisible by
   `x`; cancellation of `x^v` for either other generator reduces to
   the two explicitly nonzero residue classes in the source. A
   height-two Gorenstein ideal in a two-dimensional regular local
   ring would be a CI. The defect is consequently generic, and the
   conjugate component cannot repair it there. For `u=1`, the nonzero
   quartic norm in the image ideal contradicts the promoted minimum
   defining-degree consequence. Swapping the two endpoints and `f,g`
   preserves this proof.
5. **Quadratic-multiplier extension.** Independently checked
   `q=bc-ad in P intersect S`, `qN(G) in I intersect S`, and its
   nonvanishing: `E` is a domain and conjugation is an automorphism.
   The norm is an invariant quartic, so every irreducible factor of
   this sextic has degree at most four. The CI argument is exhaustive:
   minimum degree at least seven gives no sextic; degree five and
   `4|alpha beta` force the other degree at least eight; degree six
   gives either a unique sextic generator or a constant basis change
   in degree `(6,6)`. A defining generator would divide, or equal,
   the factored sextic, contradicting accepted factor reduction.
   The argument still works after saturation and does not require
   purity or ACM. It is not an argument for multipliers of degree
   greater than two.

## Primary-source attribution checks

Read the cited passages directly, rather than relying on search
snippets:

- [Hartshorne–Migliore–Nagel, §5, pp. 3335–3338](https://academicweb.nd.edu/~jmiglior/HMN.pdf)
  distinguishes CI-biliaison data `(M,P,alpha)` from the Rao-module
  invariant for even G-liaison. This supports the limited assertion
  about additional presentation data, not a new support-specific bound.
- [Notari–Ojeda–Spreafico, §2, p. 4](https://arxiv.org/pdf/0812.2578)
  recalls Ferrand's quotient/kernel construction and the two exact
  sequences used here. Applying the kernel construction on the smooth
  quadric is independently justified by the same ideal-sheaf argument.
- [Migliore–Nagel, Definition 2.1, p. 4](https://www3.nd.edu/~jmiglior/MN7.pdf)
  gives the cited standard BDL construction in projective three-space.
  The source correctly proves the needed properties directly in `E`.
- [Jaffe, Theorem 10.3, p. 41](https://arxiv.org/pdf/alg-geom/9410008)
  explicitly assumes the curve is not contained in either surface's
  singular locus. The source correctly declines to apply it to arbitrary
  normal orders or common generic singularities. The introduction also
  separates stronger conclusions with additional singularity hypotheses.

This was a focused verification of the cited statements, not a complete
literature search or reproof of those papers.

## Disposition and geometric scope

No established material defect remains in the reviewed source. The
earlier prospective MCM degree-sum test was not used: the actual BDL
presentation already supplies an earlier uniform failure. No spinor
degree or vanishing-Rao inference is needed.

The source adds an actual ACM thickening construction and identifies
why it cannot yield the desired AG conjugate union: generic canonical
failure in one regime and a descended low-degree factor obstruction
in the other. The quadratic-multiplier lemma closes arbitrary changes
to its containing section at once. These failures do not exhaust
supported thickenings or predict the answer to the unrestricted STCI
question. Stopping without exponent searches, finite BDL-closure
classification or higher-multiplier expansion is supported. A specified
different operation remains eligible for a bounded test without proof
of success in advance.

No computational experiment or proof rerun was needed or performed.

## Assessment preservation check

Also reviewed [strategy assessment §22](2026-10-31-unrestricted-strategy-assessment.md#22-liaison-comparison-and-a-supported-basic-double-link-operation).
Its mathematical claims and stopping disposition preserve the source's
scope: the Rao identity is a dependency, the whole positive-power BDL
source fails an early viability condition, and the broader multiplier
lemma covers quadratic multipliers but not higher multipliers or
arbitrary finite chains. The maximum-genus observation has the correct
direction, since `g_Y=g_W+delta`: an upper bound for `g_W` supplies a
lower bound for `delta`, not the needed upper bound. No speculative
spinor degree-sum equality is retained. The assessment selects no new
technical experiment and keeps unrestricted STCI open. **Scoped PASS**
for this preservation check as well.
