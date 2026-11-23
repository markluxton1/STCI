---
id: STCI-R-0079
type: result
title: Quartic pencils with the fixed Chow polytope
scope: "#scope"
statement: "#statement"
proofs:
  - name: endpoint contact, liaison residual genus, and canonical-module rigidity
    at: "research/arguments/torus/quartic_chow_pencils.md#proof-route"
    using: [STCI-R-0074]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Quartic pencils with the fixed Chow polytope

## Scope

For the **classification**, let \(k\) be an algebraically
closed field of **characteristic zero**. Take a proper
\((4,4)\) CI with full Chow polytope \(4P_{C_0}\), where
\(C_0=[s^4:s^3t:st^3:t^4]\), and at least two distinct components.
Write \(H\) for the torus of weights \((0,1,3,4)\), and
\(C_{u,v}=[s^4:s^3t:u st^3:v t^4]\).

## Statement

### Principal classification (characteristic zero)

The \(H\)-invariant proper quartic pencils in the stated
Chow-polytope fiber are precisely the
[line-and-quartic model](../arguments/equations/chow_polytope_rigidity.md#quartics-including-invariant-collision-lifts).
Every other proper pencil has cycle
\[
 2[C_{u,v}]+2[C_{u,-v}].
\]
After diagonal normalization its actual two-dimensional
equation space is uniquely of the form
\[
 \left\langle
 \lambda x_2A+x_1B,\
 D+\lambda x_1A+\lambda^{-1}x_2B
 \right\rangle,\qquad\lambda\in k^\times,
\]
with \(A,B,D\) as in the
[complete classification proof route](../arguments/torus/quartic_chow_pencils.md#proof-route).
This classifies the **proper \((4,4)\) complete-intersection
pencils** over the full fixed Chow-polytope fiber; it does
not classify arbitrary subschemes with the same Chow cycle.

### Closely related geometric consequences

For each exceptional cycle, the proper-CI ideals
form a nonconstant \(H\simeq\mathbf G_m\)-orbit
**inside the Hilbert fiber** over a single Chow point.
The normalization of its closure is
\(\mathbf P^1\), with the two distinct full Hilbert
limits at \(0,\infty\). The associated
[Grassmannian orbit closure](../arguments/torus/quartic_hilbert_chow_limits.md#two-compactifications-of-the-exceptional-orbit)
is a smooth rational normal cubic in its Plücker \(\mathbf P^3\);
its two endpoint planes of quartics are improper and have
a common cubic factor. The classification does **not**
describe every Hilbert lift over that point. In fact, the
[embedded-point detachment theorem at the two toric limits](../arguments/torus/quartic_hilbert_chow_limits.md#detaching-the-embedded-endpoint)
shows that the fixed one-cycle locus has local dimension
at least six at \(J_0\) and \(J_\infty\), coming from the
six-dimensional family of the pure doubled curve together
with two isolated points.
The [two opposite flat limits](../arguments/torus/quartic_hilbert_chow_limits.md#chow-closure-and-full-opposite-limits)
preserve the fundamental cycle and acquire embedded
length two at opposite endpoints. Exceptional cycles
lie outside the Chow closure of invariant
\((4,4)\) realizations. The entire characteristic-zero
quartic classification also implies the
[first Chow moment](../arguments/torus/chow_arrangement_moments.md)
\[
 \sum_i n_i u_i/v_i=0.
\]

The mechanism for the exceptional uniqueness is
[liaison/canonical-module rigidity](../arguments/torus/quartic_chow_pencils.md#proof-route)
of \(Y=C_+\cup C_-\): an lci, arithmetically
Cohen--Macaulay curve with two planar \(A_7\)
singularities. The residual line
\(L_{\mathrm{res}}\) in the \((3,3)\) intersection
of the cubics directly produces its canonical module,
\(\omega_Y(-2)\simeq I_{L_{\mathrm{res}}}/(A,B)\),
and its restriction condition determines the
pencil's actual generators. The first-normal
degeneracy locus is a
[Plücker-linear section of \(\operatorname{Gr}(2,9)\)](../arguments/torus/quartic_chow_pencils.md#hilbert--burch-and-first-normal-interpretation). This is the geometric proof of the
exceptional fiber, while the initial support reduction
continues to use the distinguished torus weights
and endpoint coordinates.

### Complementary geometry and separate constructions

The [two-sided endpoint contact and ten-nodal K3
carrier](../arguments/torus/quartic_exceptional_carrier_geometry.md#two-sided-contact-and-the-nodal-even-eight-carrier)
give an explicit even-eight divisor identity and
nontrivial \(2\)-torsion in the carrier's class group.
The [Nikulin three-quadric double cover](../arguments/torus/quartic_exceptional_carrier_geometry.md#the-nikulin-double-cover-and-a-square-root-of-the-mate)
makes the actual quartic mate a square, while the
[class-group torsion parity condition](../arguments/torus/quartic_exceptional_carrier_geometry.md#parity-of-mates-from-the-even-eight-class)
forces even equal multiplicities for mates on these
normal nodal carriers. These explain a fixed-carrier
doubled divisor, **not uniqueness of the moving pencil**.
The separate
[retained-carrier theorem](../arguments/torus/quartic_exceptional_carrier_geometry.md#all-mate-degrees-on-a-retained-exceptional-carrier)
classifies translated mates of a member in arbitrary
degrees under its own characteristic-zero hypotheses.

Independently, the
[characteristic-two specialization](../arguments/torus/quartic_hilbert_chow_limits.md#hilbert-over-chow-and-the-characteristic-two-collision)
of the normalized family at \(\lambda=1\)
is a non-invariant single-support \((4,4)\)
STCI presentation of \(C_0\). It is an explicit
construction, **not** a positive-characteristic
classification.

## Limitations

The separate
[quartic-pair exclusion](quartic_44_filtered_exclusion.md)
rules out sole support in characteristic zero, so
the principal theorem, together with that exclusion,
covers all characteristic-zero quartic pencils in
this Chow-polytope fiber. The exceptional uniqueness
proof uses the balanced characteristic-zero normal
splitting \(N_{C/\mathbf P^3}\simeq\mathcal O(7)^{\oplus2}\);
odd positive characteristics are not covered.
The invariant model and the characteristic-two
construction have separately stated scopes.

The theorem concerns **proper quartic complete
intersections**, not the entire Hilbert fiber,
all Ferrand doubles, or unrestricted higher-degree
realizations. It proves neither a general
higher-degree STCI obstruction nor a classification
of singular sextic carriers. The endpoint different,
arbitrary-line trace obstruction and fixed-carrier
multiplicity lattice are independent theorems with
their own hypotheses and proof owners, not steps
needed for quartic-pencil uniqueness.

## Review

The original coefficient-based classification was accepted for
its mathematical scope. The replacement
[linkage/canonical-module argument](../arguments/torus/quartic_chow_pencils.md#proof-route)
now closes the remaining uniqueness and triple-branch gates
without coefficient elimination: residual genus excludes
the asymmetric multiplicities, and the canonical module of
the Hilbert--Burch union plus the residual-line restriction
classifies all proper doubled pencils.
The argument relies on established Peskine--Szpiro linkage,
Ferrand doubling and the accepted balanced normal splitting
of the fixed rational quartic.
The Hilbert--Burch proof also replaces the earlier
weight/parity monomial enumeration, while a second
Hilbert--Burch resolution and exact sequence replace the
full-flat-limit Gröbner calculation. The sextic conormal
rank table is replaced at its canonical argument owner.
A subsequent **independent mathematical review of
the updated geometric proof (PR #171, head \`f323856\`)**
reconstructed the residual genus/Ferrand obstruction,
the canonical-module relations, the residual-line
restriction and its signs, and the full flat-limit
and sextic syzygy arguments. It found no substantive gap
in the **characteristic-zero quartic uniqueness proof**,
but correctly identified the previously overstated
characteristic scope and the separate degree-independent
involution--Bézout regularity hypothesis; both
statements have now been restricted at their owners.
That earlier review was a scoped independent correctness reconstruction.
The combined integration of November 23, 2026 (integration base
`94dfe44d`, combining the cross-degree-exclusion-synthesis and
chow-quotient-arrangement-blowups branches) subsequently received all six
independent perspectives: correctness, journal editorial review, seasoned
algebraic geometry, generalizations/implications/connections, relevant
literature, and the general research picture. The correctness review
reconstructed the endpoint/weight exhaustion, residual-genus and
canonical-module classification, full special ideal, retained-carrier
mate theorem and weighted polarization arguments. It retained the accepted
single-support quartic exclusion, balanced normal splitting and Chow-polytope
rigidity as inherited inputs, and did not reprove all of their proofs.
The combined review repaired a separate relative-union base-change error,
norm normalization and characteristic qualifications at their owners; it
does not establish unrestricted higher-degree moment vanishing. The six
perspectives cover the combined integration, rather than replacing the
precise scope of the earlier reviews below.
The earlier separate reviews of the characteristic-two
specialization, opposite full limits, and retained-carrier
theorem preserve their stated scopes. The liaison/self-linkage,
Ferrand doubling, even-eight/Nikulin, Grassmannian torus-orbit,
and embedded-point detachment mechanisms used here are classical
inputs. What is specific to this result is their application to
the fixed rational quartic: the full characteristic-zero
Chow-polytope pencil classification, the explicit exceptional
proper-CI orbit and its opposite embedded limits, and the
associated fixed-carrier formulas. A targeted literature search
found no prior source proving that entire specific classification,
but no claim of first publication or exhaustive novelty is made.
No unrestricted higher-degree STCI claim follows.
