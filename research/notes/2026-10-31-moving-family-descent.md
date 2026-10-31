# Moving punctual families can have both endpoint contractions locally CI

Date: 2026-10-31. Status: **independently reviewed provisional diagnostic
construction; no canonical promotion**; see the
[bounded audit](2026-10-31-moving-family-descent-audit.md). Throughout k is algebraically
closed of characteristic zero and

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]

The construction works for **every integer m≥2**. It does not propose a
new defining pair for C, exclude any hypothetical pair, or classify a
degree range. Its purpose is to test an intermediate assertion in the
[full tropical descent problem](2026-10-31-tropical-descent.md): positive
movement and Gorensteinness of both weighted endpoint contractions can
coexist, even when the full family upstairs is locally a complete
intersection and every punctual fiber is curvilinear. Global generation
of the image ideal by two homogeneous equations is an additional condition.

## 1. Prior inputs and the exact diagnostic

The primary source
[Bănică–Forster, *Multiplicity Structures on Space Curves*, §§2.1–2.3](https://www.mathematik.uni-muenchen.de/~forster/eprints/multip_struct.pdf)
gives the standard primitive local model `(x,y^m)`, its powers of the
conormal line, and adjunction restricted to the reduced curve. Those
facts are used below; constructing Cartier multiples on a smooth surface
is classical, not claimed as new theory.

The repository already contains:

- [arbitrary Cartier multiples and partial absorption](2026-10-27-absorption-deformation-interface.md), on smooth carriers;
- [the constant-family control nC on the quadric](2026-10-30-four-streams-linear-series.md), §4;
- [R-0032](../results/full_conormal_socle_budget.md), whose conormal/socle identity requires an actual supported homogeneous CI;
- [the normal-torsion account](2026-10-26-normal-torsion-spectral-genus-budget.md), distinguishing a multiple curve's intrinsic filtration from its actual homogeneous equation module;
- [the full fixed-twist formal-pair criterion](2026-10-27-formal-neighborhood-residual-visibility.md), §6, which already handles algebraization when its full globally glued equation hypotheses hold.

The new diagnostic combines a single explicit smooth cubic with the
**actual** tropical morphism, in every multiplicity, and computes the
embedded movement and both endpoint contractions. It strengthens the
constant quadric control by making the full family nonconstant. It is
not an improvement to an inherited genus or conductor identity, and no
claim of literature priority is made.

**Proposition.** For every m≥2 there is a projective curve Z_m supported
exactly on C whose full tropical closure W_m has these properties:

1. Z_m and W_m are locally complete intersections. The morphism
   W_m→P1 is finite flat of degree m; every fiber is the curvilinear
   algebra `k[epsilon]/(epsilon^m)`.
2. W_m is an embedded moving family, with
   \[
   \deg\pi_*\mathcal O_{W_m}=6\binom m2=3m(m-1)>0.
   \tag{1}
   \]
3. Its finite image in P3 is Z_m, with exactly the weighted endpoint
   contractions of the descent problem. Each contraction is itself
   primitive and hence Gorenstein, and
   \[
   \delta_0=\delta_\infty=4\binom m2=2m(m-1).
   \tag{2}
   \]
4. Z_m cannot be the scheme-theoretic intersection of two homogeneous
   surfaces of any degrees. Thus this is a counterexample to deriving
   a contradiction solely from properties 1–3, not to the possibility
   that the additional global two-equation condition is obstructed.

## 2. One smooth cubic and all its Cartier multiples

Take

\[
F=x_0^2x_2-x_1^3+x_2^3-x_1x_3^2,
\qquad S=V(F).
\tag{3}
\]

Both binomials vanish on C. The four partial derivatives are

\[
(2x_0x_2,\ -3x_1^2-x_3^2,\ x_0^2+3x_2^2,\ -2x_1x_3).
\]

Their common vanishing forces x0=x2=0 and x1=x3=0, impossible
projectively. Hence S is smooth. On S, C is Cartier; let

\[
Z_m=mC\subset S,\qquad
\mathcal I_{Z_m}=(F)+\mathcal I_C^m\subset\mathcal O_{\mathbf P^3}.
\tag{4}
\]

Its local equations have the form `(f,y^m)` with f a smooth surface
parameter and y a local equation of C in S. It is therefore a
projective primitive locally CI curve with sole support C.

Adjunction on the cubic gives

\[
-2=(K_S+C)\cdot C=-4+C^2,
\qquad C^2=2.
\]

Thus the conormal line of C in S is L=O_P1(-2), and the ordinary
nilpotent layers of Z_m are L^i for 0≤i<m. Consequently

\[
\deg Z_m=4m,\qquad
\chi(\mathcal O_{Z_m})=m-2\binom m2=2m-m^2,
\qquad p_a(Z_m)=(m-1)^2.
\tag{5}
\]

These are the intrinsic invariants of these Cartier multiples. They
are not the complete-intersection genus formula in hypothetical degrees.

## 3. The full tropical closure is primitive and moving

Use

\[
Y=\mathbf P^1\times\mathbf G_m^2,
\quad \phi(t,u,v)=[1:t:ut^3:vt^4],
\quad U=u-1,\ V=v-1.
\]

The pullback of F on the finite chart is

\[
F\circ\phi=t^3\{U+t^6(u^3-v^2)\}.
\]

Its strict surface transform T is the global Cartier divisor on Y
with equations

\[
f_0=U+t^6(u^3-v^2),\qquad
f_\infty=\tau^6U+u^3-v^2,\qquad \tau=t^{-1}.
\tag{6}
\]

The transition is `f_infinity=tau^6 f_0`, so T has divisor class
O_P1(6). Along the section `U=V=0`, the relative derivatives on the
finite chart are `(1+3t^6,-2t^6)` and at infinity are `(3,-2)`.
They never vanish simultaneously. Thus T→P1 is smooth near the
section, and the section is Cartier in T. Define

\[
W_m=m(\mathbf P^1\times\{(1,1)\})\subset T.
\tag{7}
\]

Equivalently, its ideal is locally `(f_0,(U,V)^m)` or
`(f_infinity,(U,V)^m)`. Each local quotient has the form
`R[w]/(w^m)` after formal completion in the base, because one relative
normal derivative is a unit. Hence W_m is finite flat of rank m,
locally CI, and has curvilinear fibers.

Over the dense torus it is exactly the pullback of (4): phi is an
isomorphism there, F differs from f_0 by a unit, and the ideal of C
is `(U,V)`. Since W_m is flat over P1, it has no endpoint parameter
torsion. Therefore its ideal is already contracted from the punctured
base at both endpoints. This proves that (7) is the **full
scheme-theoretic closure**, not a selected partial transform.

Write M for the conormal of the section in T. Its exact sequence is

\[
0\longrightarrow O(-6)
\xrightarrow{(s^6+3t^6,\,-2t^6)}O^2
\longrightarrow M\longrightarrow0.
\tag{8}
\]

The displayed entries have no common zero, so M=O(6). The nilpotent
layers of W_m are M^i. Taking degrees in their filtration gives (1).
No splitting of the entire algebra is assumed in this argument.

Already its first transverse direction is the degree-six map

\[
[s:t]\longmapsto[2t^6:s^6+3t^6]
\tag{9}
\]

to the line of one-dimensional quotients of kU⊕kV. Thus the movement
is visible geometrically in the embedded tangent direction; it does
not require a change in the abstract fiber algebra. All fibers retain
the same abstract curvilinear isomorphism type.

## 4. Both actual endpoint algebras are primitive

At zero put `t=x1/x0`,

\[
A=x_2/x_0-t^3,\qquad B=x_3/x_0-t^4.
\]

Then

\[
F/x_0^3=(1+3t^6)A-2t^5B+3t^3A^2+A^3-tB^2.
\tag{10}
\]

The coefficient of A is a unit at zero, so the completed ring of
Z_m is `k[[t]][B]/(B^m)`: solve (10) for A as a formal series in B,
which is finite after imposing B^m=0. Upstairs f_0 solves for U in
V, and the completed ring is `k[[t]][V]/(V^m)`. Since

\[
A=t^3U,\qquad B=t^4V,
\]

the actual inclusion is

\[
k[[t]][t^4V]\subset k[[t]][V]/(V^m).
\tag{11}
\]

In particular, adjoining t^3U adds nothing to the left side: (10)
expresses that element in t and B. The two free bases are
`1,t^4V,...,t^(4(m-1))V^(m-1)` and `1,V,...,V^(m-1)`.
Their index is `4 binom(m,2)`.

At infinity it is essential to use the **actual** projective parameter
and full changed transverse coordinates:

\[
z=x_2/x_3=\tau u/v,\quad
U'=v^2/u^3-1,\quad V'=v^3/u^4-1.
\]

Set `X=x1/x3-z^3=z^3U'` and
`Y'=x0/x3-z^4=z^4V'`. The affine equation is

\[
F/x_3^3=-(1+3z^6)X+2z^5Y'-3z^3X^2-X^3+z(Y')^2.
\tag{12}
\]

Its X coefficient is a unit. After the full coordinate change, the
same argument gives the other exact inclusion

\[
k[[z]][z^4V']\subset k[[z]][V']/(V'^m),
\tag{13}
\]

with the same index. This proves (2) for both weighted contractions.
The map W_m→Z_m is finite: W_m is proper, and its underlying map
identifies the reduced section with C. It is an isomorphism off the
endpoints, and (11), (13) identify its full image at them. Thus the
scheme-theoretic image is precisely Z_m, with no additional components.

Geometrically each endpoint contraction multiplies the one surviving
normal parameter by the fourth power of the base parameter. The
conormal comparison is `O(-2)→O(6)` with zero divisor
`4p0+4pInfinity`. The index on every higher layer is its corresponding
multiple, explaining the sum in (2). The Euler characteristics in
(1), (2), and (5) agree, but no conductor-duality identity is needed
to establish the construction.

## 5. The global homogeneous equation condition still fails

Here is a direct proof for **all m≥2**, independent of the repository's
low-degree STCI exclusion. Since C is nonplanar, Z_m has no nonzero
linear equation. Its only possible quadric equation is a multiple of

\[
q=x_0x_3-x_1x_2.
\]

Indeed the four parametrizing monomials are linearly independent, and
their ten quadratic products give the nine distinct degree-eight
monomials in s,t, with only `x0*x3=x1*x2` repeated.

On the finite chart its linear normal part is `B-tA`. This and the
linear part in (10) have determinant `1+t^6`, which is nonzero in
k(t). Hence q vanishes to order exactly one on C inside S; it does
not vanish on Z_m for any m≥2. Since F is a cubic equation of Z_m,
the least degree of a nonzero homogeneous equation of Z_m is three.

If Z_m were a homogeneous scheme CI of degrees a≤b, its saturated
ideal would be generated by those two forms; hence a=3. Degree and
CI adjunction would then give

\[
3b=4m,\qquad
p_a(Z_m)=1+\frac{3b(b-1)}2.
\]

Combining with (5) and dividing by m>0 gives `m=2b`; together with
`3b=4m` this is impossible for b>0. This proves assertion 4.

Upstairs the [reviewed two-divisor lemma](2026-10-31-tropical-descent.md),
§4, also shows that no two global effective Cartier divisors of Y cut
out W_m, because its degree (1) is positive. The explicit surface T
in (6) is one global Cartier divisor; its Cartier multiple (7) within
T does not thereby acquire a second global Cartier equation in Y.

## 6. The two affine pieces are actual scheme complete intersections

This continuation is **independently reviewed provisional work**; see §6
of the [audit](2026-10-31-moving-family-descent-audit.md). It applies
classical affine Serre construction and Quillen–Suslin; it is not a new
general affine complete-intersection theorem.

**Lemma.** Let X be a closed locally complete-intersection curve in A3_k,
with reduced scheme isomorphic to A1_k. Then its entire ideal in
k[x,y,z] is generated by a regular sequence of length two.

**Proof.** Let N be the nilradical of O_X. Successive square-zero
thickenings have unit kernels identified additively with coherent modules.
Their positive cohomology vanishes because X is affine. The units
sequence consequently identifies Pic(X) with Pic(X_red)=0. In particular
the invertible module det N_(X/A3) is trivial.

Put R=k[x,y,z] and I=I_X. The codimension-two lci calculation identifies
Ext²_R(R/I,R) with that determinant module. From 0→I→R→R/I→0
we obtain Ext¹_R(I,R)=Ext²_R(R/I,R). Choose an extension
0→R→P→I→0 corresponding to a generator of this free rank-one R/I-module.
The local Koszul calculation shows that its middle module P is locally
free of rank two: at points of X the extension class is a unit in the
local Ext module, and outside X the sequence splits with I=R.
Thus P is projective. Quillen–Suslin makes P free, giving a surjection
R²→I. Its two entries generate a height-two ideal in the regular ring R,
so they form a regular sequence. ∎

The local extension criterion used here is explicitly reconstructed in
[Schnell, Serre construction, Lemma 1, equation (6), and §3](https://www.math.stonybrook.edu/~cschnell/pdf/notes/serre.pdf).
The projective-module triviality is the classical Quillen–Suslin theorem;
see the primary account and references in
[Forster, §IV, proof of Theorem 4.3, pp. 20–21, and references [28], [34]](https://www.math.lmu.de/~forster/eprints/Compl_inter.pdf).
The proof neither replaces X by a different thickening nor assumes X
reduced. It works over any field when X_red is A1 over that field.

For the characteristic-zero curves Z_m above, removing either endpoint
hyperplane gives precisely such an X. Therefore both entire affine
pieces of Z_m have two polynomial generators, for every m≥2.
No explicit generating pair or degree bound is asserted by this
existence argument.

There is also an all-presentations consequence for these fixed images.
Take **any** polynomial pair generating one of their affine ideals, and
ordinarily homogenize it. The resulting two homogeneous polynomials
have no common factor: a common factor other than the removed
hyperplane would dehomogenize to a common factor, while ordinary
homogenization is not divisible by that hyperplane coordinate. Hence
their intersection Y is a pure projective CI curve.

Its restriction to the affine chart is X, whose scheme closure is Z_m.
If Y had no other curve component, the hyperplane coordinate would be
a nonzerodivisor on O_Y and Y would equal that same scheme closure.
Section 5 rules this out. Thus Y necessarily has a residual curve,
all of whose support lies in the omitted hyperplane. Connectedness
of a projective CI forces the residual union to meet C, and the only
possible meeting point is the omitted marked endpoint.

This is a universal statement about presentations of these particular
affine thick schemes. It does not quantify over every affine
set-theoretic presentation of the reduced curve C. Its purpose is to
demonstrate that two genuine affine scheme-CI presentations, and locally
CI endpoint contractions, can still fail to admit a homogeneous
two-equation presentation of their shared projective thickening.
The missing datum is the compatibility of the actual equations and
their ambient twists, as in the previously reviewed
[fixed-twist affine gluing criterion](2026-10-30-four-streams-affine-endpoints.md).

## 7. Effect on the unrestricted problem and review boundary

This all-m construction rules out the proposed intermediate claim
that a moving punctual family with these two weighted contractions
must lose the local complete-intersection or Gorenstein property at
an endpoint. It even permits the entire Hilbert-scheme image to stay
inside the curvilinear locus. Consequently properness of the parameter
curve, positivity of the tautological degree, and endpoint Gorenstein
tests alone cannot yield an unrestricted STCI contradiction.

For an actual hypothetical pair, one must additionally retain the
global homogeneous generator module, prescribed twists and full
equation compatibility. Our Z_m fails that condition explicitly.
This construction does not show that the full condition can be met,
or that it cannot be met by a different moving family. The unrestricted
characteristic-zero question remains open.

All calculations here are direct symbolic identities and local smooth
coordinate arguments; no inherited proof or certificate was rerun.
The independent audit reconstructs the displayed local expansions,
all-m degree calculation, and the subsequent affine-generator extension.
No canonical result has been promoted.
