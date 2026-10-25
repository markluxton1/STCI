# The singular scheme of the restricted quartic discriminant

Date: 2026-10-24. Author role: `singular_scheme`.

**Status: new proved propositions within a provisional geometry package;
exact ideal presentations have reproducible computational verification.
No canonical promotion or STCI conclusion.** Work over an algebraically
closed field of characteristic zero, with the fixed marked embedding
\(C=[s^4:s^3t:st^3:t^4]\).

## 1. Scope and retained input

The [merged dual-incidence derivation](2026-10-24-special-dual-incidence-derivation.md)
and [independent geometry audit](2026-10-24-special-lines-planes-geometry-audit.md)
already establish that the dual surface is the restricted binary-quartic
discriminant, of degree six. Its reduced singular locus has four
components: the osculating quartic, the bitangent quartic, and the two
endpoint triple-contact pencil lines. Those results are retained, rather
than reproved here. They are reviewed exploratory evidence, not canonical
STCI result records. No normal-bundle splitting or carrier exclusion is
used in this note.

This note determines the additional scheme structure. In particular, the
four reduced components do **not** account for the whole Jacobian scheme:
there is an embedded point of length one at each hyperosculating plane.
The proof below includes a local determinantal argument ruling out further
embedded structure. Generic transverse multiplicities alone would not
justify that conclusion.

## 2. A compact global equation and the exact Jacobian ideal

Write a plane section as
\[
f(s,t)=As^4+Bs^3t+Cst^3+Dt^4.
\]
In the dual projective space \(\mathbf P^3_{[A:B:C:D]}\), put
\[
L=BC-4AD,\qquad K=AC^2+B^2D.
\]
The [dual-intersection calculation](2026-10-24-quartic-dual-intersections.md)
uses the classical invariant presentation
\[
\Delta=-4L^3-27K^2
=256A^3D^3-192A^2BCD^2-27A^2C^4
 -6AB^2C^2D-27B^4D^2-4B^3C^3.
\]
For the statements here it suffices to expand the displayed identity;
it does not require a choice of normalization of classical invariants.

Let \(S=k[A,B,C,D]\) and
\[
J=(\Delta_A,\Delta_B,\Delta_C,\Delta_D).
\]
Then
\[
\operatorname{Sing}(C^\vee)=\operatorname{Proj}(S/J).
\]
This is the scheme-theoretic singular locus defined by the relevant
Fitting ideal of differentials. Euler's identity makes \(\Delta\)
redundant in characteristic zero. The four partials, or equivalently
\(-12L^2dL-54K\,dK\), give an exact global definition, including all
endpoints and nilpotents. The replay below verifies that \(J\) is already
irrelevant-ideal saturated. Thus it also gives the homogeneous ideal of
this projective scheme without a hidden saturation step.

The endpoint pencil lines are
\[
\ell_0=V(A,B),\qquad\ell_\infty=V(C,D),
\]
and the two hyperosculating planes, viewed as points of the dual space, are
\[
e_0=[0:0:0:1],\qquad e_\infty=[1:0:0:0].
\]

## 3. Generic transverse structures

**Proposition.** Away from \(e_0,e_\infty\), the singular scheme is a
curvilinear double structure along the osculating quartic and each pencil
line, and is reduced along the bitangent quartic. The transverse surface
singularities are respectively ordinary cusps and ordinary nodes.

**Proof.** For a section having a triple zero and one distinct simple
zero, étale factorization separates the simple root. The discriminant of
the remaining cubic has the ordinary cusp equation
\(4x^3+27y^2=0\), times a unit. Its Jacobian scheme is
\((x^2,y)\). The missing-middle-coefficient condition is transverse to
the triple-root stratum whenever the residual root differs from the
triple root. One can see this on a chart of the stratum by expanding
\((z-u)^3(z-r)\): its middle coefficient is \(3u(u+r)\).
At a nonendpoint point satisfying \(r=-u\), differentiation in \(r\)
is nonzero. At \(u=0,r\ne0\), differentiation in \(u\) is nonzero.
Homogeneous charts cover a residual root at infinity and the opposite
endpoint. Consequently the restriction retains the cusp model, also on
the two pencil lines away from their quadruple-root members.

For a section having two distinct double zeros, étale factorization into
two quadratic factors gives discriminant \(xy\), times a unit, in the
two independent double-root smoothing parameters. The missing coefficient
is transverse to the double-double stratum: on squares of quadratics its
equation is the smooth bitangent conic, and its differential is nonzero
away from the quadruple-root endpoints. Thus the transverse model is a
node, whose Jacobian scheme \((x,y)\) is reduced. These arguments apply
at **every** nonquadruple section on the four components, not only their
generic points. The four components meet only at the two quadruple-root
sections. \(\square\)

The degree of the singular curve, including its generic nilpotent
multiplicities, is therefore
\[
2\deg(\text{osculating quartic})+
\deg(\text{bitangent quartic})+2\deg\ell_0+2\deg\ell_\infty=16.
\]
Zero-dimensional embedded pieces do not change this degree.

## 4. The two embedded endpoint points

Define a homogeneous quintic
\[
h=(BC+8AD)K=(BC+8AD)(AC^2+B^2D),\qquad U=J+(h).
\]

**Proposition.** The ideal sheaf \(\widetilde U\) defines the unmixed
one-dimensional part of the singular scheme. There is an exact sequence
\[
0\longrightarrow k(e_0)\oplus k(e_\infty)
\longrightarrow\mathcal O_{\operatorname{Sing}(C^\vee)}
\longrightarrow\mathcal O_{\operatorname{Proj}(S/U)}
\longrightarrow0.
\]
In particular there is precisely one embedded point of length one at each
hyperosculating plane, and no other embedded associated points.

**Proof.** Three polynomial identities give
\[
Bh=-\frac{2A}{27}\Delta_B-\frac C{54}\Delta_D,
\qquad
Ch=-\frac B{54}\Delta_A-\frac{2D}{27}\Delta_C,
\]
\[
ADh=-\frac{AC}{216}\Delta_B-\frac{BD}{24}\Delta_C
       +\frac{C^2}{108}\Delta_D.
\]
Hence \(U/J\) is supported at \(e_0,e_\infty\), and is at most one
copy of their residue field at each. To establish nonvanishing and
unmixedness, take the chart \(D=1\), with coordinates \(a,b,c\).
The exact local equation is
\[
F=256a^3-192a^2bc-27a^2c^4-6ab^2c^2-27b^4-4b^3c^3.
\]
It is weighted homogeneous of degree 12 for weights \((4,3,1)\).
Set \(g_A=-F_a/6,g_B=-F_b/12,g_C=-F_c/12\), and continue to write
\(h=(bc+8a)(ac^2+b^2)\). Weighted Euler shows that the localized
Jacobian ideal is \((g_A,g_B,g_C)\); no extra equation \(F\) is needed.

The signed maximal minors of
\[
M=\begin{pmatrix}
-b&-ac&ac^2\\
0&-8a-bc&-ac+bc^2\\
-8&c^2&-9b-c^3\\
9c&9b&18a
\end{pmatrix}
\]
are exactly \(9(g_A,g_B,g_C,h)\), in that order. These identities can
be checked directly by four determinants. This ideal has height two:
its support is the same union of curves as that of the Jacobian, because
\(h\) differs from a Jacobian element only at the endpoint. The
Hilbert–Burch theorem now makes the quotient by \((g_A,g_B,g_C,h)\)
Cohen–Macaulay of dimension one. In particular it has no embedded point.
The use here is the standard converse for maximal minors of a matrix
whose ideal has height two; see, for example, the author-hosted paper
[Eisenbud–Huneke, *Cohen–Macaulay Rees Algebras and Their
Specialization*, proof of Theorem 3.4](https://eisenbud.github.io/papers/pdfs/1983-005.pdf)
for the Hilbert–Burch framework. The specific converse used is the standard
Hilbert–Burch theorem for height-two maximal-minor ideals. No novelty
claim is made for this method.

The weights of \(g_A,g_B,g_C,h\) are \(8,9,11,10\).
If \(h\) belonged to \((g_A,g_B,g_C)\), its weight-10 part would be
a linear combination of \(c^2g_A\) and \(cg_B\). Neither contains the
monomial \(ab^2\), whereas \(h\) has coefficient eight on that
monomial. Thus \(h\) is nonzero modulo the Jacobian ideal, including
after localization at the origin. The three displayed identities imply
that its class is annihilated by \((a,b,c)\), so it spans exactly one
copy of \(k(e_0)\).

Coordinate reversal \((A,B,C,D)\mapsto(D,C,B,A)\) preserves \(\Delta\)
and \(h\), so the same proof applies at \(e_\infty\). Away from these
points \(U=J\), and Section 3 excludes embedded structure there. This
proves the assertion. \(\square\)

The residue-field terms carry no preferred trivializations; globally
the generator \(h\) has degree five. At the graded-module level the
exact algebraic statement is
\[
U/J\cong (S/(B,C,AD))(-5),
\qquad J:h=(B,C,AD).
\]
The elementary local proof proves the corresponding sheaf statement;
the exact graded equality is independently checked in the replay.

## 5. A finite global presentation of the unmixed part

For readers who need explicit ideals, set
\[
P_O=(L,\ C^3+4BD^2,\ K,\ B^3+4A^2C),
\]
\[
P_B=(BC+8AD,\ C^3+8BD^2,\ AC^2-B^2D,\ B^3+8A^2C),
\]
and
\[
T_O=(K,\ C^4+8BCD^2-16AD^3,\ L^2,
                 B^4+8A^2BC-16A^3D).
\]
Here \(P_O,P_B\) define the osculating and bitangent quartics. The
following is an **exact computed ideal presentation**, with independent
geometric interpretation provided by Sections 3–4:
\[
U=(A,B^2)\cap(D,C^2)\cap T_O\cap P_B,
\qquad \sqrt{T_O}=P_O.
\]
The replay verifies equality of ideals, the radical, and associated
primes. Thus the endpoint pencil components are the literal planar
double lines \((A,B^2)\) and \((D,C^2)\); the bitangent primary
component is reduced. The osculating component has generic length two.
Together with the preceding short exact sequence this is a complete
scheme description; printing arbitrary embedded primary components
would add noncanonical choices without refining it.

The saturated Jacobian scheme has Hilbert polynomial
\(16n-43\). Its unmixed part has Hilbert polynomial \(16n-45\), and
their difference is the two residue-field contributions. These polynomial
values are exact computational outputs, not deductions from generic
transverse multiplicities alone.

## 6. Reproduction, scope, and boundaries

Run

```sh
M2 --script research/computations/verify_quartic_dual_singular_scheme_2026_10_24.m2
```

The [saved output](../computations/quartic_dual_singular_scheme_2026_10_24_m2.txt)
records exact equalities over \(\mathbf Q\), the global saturated ideal,
associated primes, Hilbert polynomials, and local minors. The ideals and
determinant/syzygy proofs extend to every algebraically closed
characteristic-zero field. The independent package audit reconstructs
the endpoint correction separately.

Characteristic two or three requires a separate calculation: the cusp
equation, Euler arguments, constants divided by 2 or 3, and the
transversality arguments above do not transfer unchanged. This note makes
no claim about the singular scheme after such specialization. It changes
neither canonical STCI records nor any carrier-exclusion scope.
