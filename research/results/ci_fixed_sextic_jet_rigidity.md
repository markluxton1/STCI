---
id: STCI-R-0025
title: "Fixed sextic: sharp mate bounds from boundary valuations"
kind: theorem
scope:
  characteristic: "0"
  curve: "fixed C0"
  hypotheses:
    - "The selected sextic Fstar and arbitrary positive-degree proper mates"
statement: "For the selected Fstar, every proper degree-b mate has branch order at most floor(b/2); in characteristic zero every even-degree maximizer is a carrier multiple plus a nonzero scalar times q^(b/2). At degree sixteen the sharp multiplicity and residual-degree bounds are 16 and 32."
dependencies: []
evidence:
  - "research/results/ci_fixed_sextic_jet_rigidity.md"
  - "research/results/ci_fixed_sextic_jet_rigidity.support/verify.py"
independent_audits:
  - "research/results/ci_fixed_sextic_jet_rigidity.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Only one selected sextic; no arbitrary-carrier or unrestricted STCI theorem"
  - "Saved certificates were source-inspected; independent normal-division replay passed in GitHub Actions run 40434021004 (2026-10-26). Macaulay2 was not rerun in that workflow."
  - "Primary theorem and metadata are characteristic zero; numbered Corollaries 1 and 2 state the separate positive-characteristic assertions"
---
<a id="fixed-sextic-jet-rigidity"></a>

# Fixed sextic: sharp mate bounds from boundary valuations

## Statement

Fix an algebraically closed field of characteristic zero and
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). Put
\[
q=x_0x_3-x_1x_2,\qquad D=x_2^3-x_1x_3^2,\qquad
F_*=-q^2x_3^2-qDx_2+D^2/4+q^3.
\]
For **every** positive integer \(b\) and every degree-\(b\) homogeneous
form \(G\) meeting this fixed sextic properly, the common order \(n\)
on its two conjugate branches over the generic point of \(C\) satisfies
\[
 n\le\lfloor b/2\rfloor.
\]
If \(G\) contains \(C\), its generic intersection multiplicity is
\(m_C=2n\), and its residual fundamental cycle satisfies
\[
 \deg R=6b-8n\ge6b-8\lfloor b/2\rfloor>0.
\]
These bounds are sharp: use \(q^{b/2}\) for even \(b\), or
\(q^{(b-1)/2}x_3\) for odd \(b\). The odd-degree example contains
\(C\) when \(b\ge3\); no linear form contains this nondegenerate curve.

For even \(b\), every mate attaining \(n=b/2\) has the stronger form
\[
 G=F_*H_{b-6}+c q^{b/2},\qquad c\in k^*,
 \qquad (F_*,G)=(F_*,q^{b/2}),                         \tag{1}
\]
where a negative-degree \(H\) means zero. Thus **no mate degree on this
one carrier** gives sole support \(C\). This does not exclude other
sextics or solve unrestricted characteristic-zero STCI.

In particular, at degree sixteen the sharp bounds are \(m_C\le16\)
and \(\deg R\ge32\), and every maximizer defines the same complete
intersection as \((F_*,q^8)\). If \(\mathcal K_j\) denotes the global
degree-sixteen kernel modulo \((F_*)+\mathfrak m^j\) at the generic
point, then
\[
 \mathcal K_8=F_*H^0(\mathcal O(10))\oplus kq^8,
 \qquad \mathcal K_9=F_*H^0(\mathcal O(10)).           \tag{2}
\]
The former order-twelve kernel theorem follows as a weaker corollary.
The retained rank-683 replay remains an independent check of that older
statement; it is not an input to the geometric proof below.

## Hypotheses and quantifiers

The primary statement is characteristic zero, one displayed carrier,
and arbitrary mate degree. Properness is essential. The bound also holds
in every characteristic other than 2 and 37. The even-degree classification
(1) is proved here in characteristic zero or characteristic \(p>b\),
\(p\ne37\); see [the characteristic discussion](#characteristic-boundary-of-the-argument).
In particular (1) and (2) hold in characteristic 65521 at degree sixteen.
No classification of odd-degree maximizers is asserted.

## Proof

### Normalization lemma and the marked branch order

Adjoin a degree-one coordinate \(W\) with equations
\[
 W^2-2x_2W-x_3^2+q=0,\qquad 2qW=D.                  \tag{3}
\]
On \(x_3=1\), put \(y=x_2\), \(w=W\). Eliminating gives exactly
\[
 Q=1+2yw-w^2,\qquad q=Q,\qquad
 x_1=y^3-2Qw,\qquad x_0=Q+x_1y.                    \tag{4}
\]
Thus the graph chart is \(\operatorname{Spec}k[y,w]\), finite over
the carrier chart because the first equation in (3) is monic in \(W\).
After inverting \(q\), the inverse is \(w=D/(2q)\), so the localized
carrier ring is \(k[y,w,Q^{-1}]\), a domain. In the affine ambient
polynomial ring, \(q=x_0-x_1y\) is a prime coordinate and does not
divide \(F_*\), since \(F_*\bmod q=D^2/4\ne0\). Consequently
\(F_*\) is irreducible there: any extra factor becoming a unit after
localization would be a power of \(q\). It is irreducible homogeneously
as well, since \(x_3\nmid F_*\). The finite birational normal chart
(4) is therefore the normalization of this affine carrier chart.
This is the usual integral-closure characterization of normalization,
not a claim about an uncomputed projective graph at every point.

The marked ideal on \(x_3=1\) is \((q,D)\): indeed
\(D=y^3-x_1\) and \(x_0-y^4=q-yD\). Its pullback is \((Q)\).
The prime divisor \(Q=0\) is smooth and has coordinate ring
\[
 k[y,w]/(Q)=k[w,w^{-1}],\qquad y=(w^2-1)/(2w).
\]
Its residue extension over \(k(C)=k(y)\) is the separable quadratic
\(w^2-2yw-1\), irreducible because \(y^2+1\) has simple zeros and
is not a square in \(k(y)\). In local coordinates \((q,D)\), the
carrier has ordinary quadratic term \(D^2/4-yqD-q^2\).
After the residue-field extension it has two transverse smooth branches,
exchanged by Galois. The pullback of the marked ideal is the uniformizer
\(Q\); therefore \(\operatorname{ord}_Q(g)=n\) is the common branch
order, not twice that order, for the restriction \(g\) of an actual
mate. The nonsplit-node argument in the
[retained local proof](#local-node-lemma-and-legacy-order-twelve-kernel-proof)
gives exact normal-jet order \(n\). If \(G\) contains \(C\), then \(n>0\) and the local intersection length is \(2n\); this is the hypothesis under which we speak of the component multiplicity \(m_C\) and its residual cycle. If it does not contain \(C\), then \(n=0\) and the restriction is a unit at that generic point.

Properness makes \(g\) a nonzero polynomial in \(k[y,w]\). Since
\(Q\) is prime, write
\[
 g=Q^nP(y,w),\qquad P\ne0.                           \tag{5}
\]
Here all coefficients of \(P\) are constants in \(k\), not rational
functions of a parameter on a boundary divisor.

### Three actual boundary valuations

Use the other graph chart \(x_2=1\), writing \(u=x_3\), \(z=x_0\)
and retaining \(W\). The equations eliminate \(x_1\) to give
\[
 f(W)+W^2u^2-u^4+zu^3=0,\qquad
 f(W)=-2W^3+4W^2-1.                                 \tag{6}
\]
Its overlap with (4) is \(y=1/u\), \(w=W/u\).
The cubic has discriminant \(148\), and its three roots \(r_i\)
are distinct and nonzero in the stated characteristics. At the generic
point of each line \(u=0,W=r_i\), the derivative \(f'(r_i)\ne0\).
The chart is regular there; its DVR has uniformizer \(u\) and residue
field \(k(z)\). These are valuations \(v_i\) on the same carrier
function field, not valuations on an unrelated surface model.

Expanding (6) in this DVR yields
\[
 W=r_i+\beta_i u^2+\gamma_i zu^3+O(u^4),\qquad
 \beta_i=-r_i^2/f'(r_i),\quad\gamma_i=-1/f'(r_i).
\]
Set \(S_i=W-r_i-\beta_i u^2\), so its initial term is
\(\gamma_i zu^3\). For a nonzero polynomial in \(u,S_i\) with
constant coefficients, its valuation is the least weight \(a+3j\)
of its nonzero monomials \(u^aS_i^j\). Indeed, terms tied at this
weight have distinct powers \(z^j\) in their initial residues. They
cannot cancel in \(k(z)\). This explicitly addresses cancellation
between different homogeneous parts of a global equation.

On the boundary, \(q/x_2^2=-W^2+2W+u^2\) specializes to
\(r_i(2-r_i)\ne0\), because \(f(0)=f(2)=-1\). Hence
\(v_i(Q)=-2\). A degree-\(b\) homogeneous form has
\(g=u^{-b}(G/x_2^b)\), with the parenthesized factor regular on
this chart. Thus (5) implies
\[
 v_i(P)\ge2n-b\quad\text{for every }i.               \tag{7}
\]

### Boundary polynomial lemma

**Lemma.** Let \(k[y,w]\) be a polynomial ring, and let three valuations
on \(k(y,w)\), trivial on \(k\), have boundary coordinates \(y=u^{-1},w=W/u\).
Suppose their centers have three distinct nonzero constants \(r_i\),
\(u\) is a uniformizer, their residue fields contain a transcendental
coordinate \(z\) over \(k\), and
\(S_i=W-r_i-\beta_i u^2\) satisfies \(v_i(S_i)=3\) and
\(\overline{u^{-3}S_i}=\gamma_i z\), with
\(\beta_i\in k\) and \(\gamma_i\in k^*\).
Then every nonzero \(P\in k[y,w]\) satisfies
\(\min_i v_i(P)\le0\).

These hypotheses are verified above for the three actual boundary lines.
The independence needed is of the powers of each residue coordinate
\(z\) over \(k\), not independence of coordinates across different
lines. The proof is the standard initial-form noncancellation principle
for valuations, applied to the leading homogeneous polynomial.

**Proof.** Let \(d=\deg P\), with homogeneous parts \(p_j(y,w)\). Then
\[
 u^dP(1/u,W/u)=\sum_{\ell=0}^d u^\ell p_{d-\ell}(1,W).
\]
Let \(m_i\) be the multiplicity of \(r_i\) in the nonzero polynomial
\(p_d(1,W)\). After substituting
\(W=r_i+\beta_i u^2+S_i\), the coefficient of
\(u^0S_i^{m_i}\) is nonzero. Lower homogeneous parts carry positive
powers of \(u\) and cannot alter it. The preceding noncancellation
argument proves
\[
 v_i(P)\le3m_i-d.
\]
Since \(\sum_i m_i\le\deg_W p_d(1,W)\le d\), at least one of
these upper bounds is nonpositive. This includes \(d=0\), when all
three valuations are zero, proving the lemma. Applying it to (7) gives
\(2n\le b\) for the fixed carrier.

### Equality for even degrees

Suppose \(2n=b\). Then all \(v_i(P)\ge0\). The inequalities just
proved force \(d=3m\), \(m_i=m\) for all three roots, and
\[
 p_d(1,W)=c f(W)^m,\qquad c\ne0.
\]
If \(d>0\), write the polynomial \(u^dP\) in the independent formal
variables \(u,S_i\) by the **exact identity**
\(W=r_i+S_i+\beta_i u^2\), which is the definition of \(S_i\).
This is not a claim that the actual DVR series for \(W\) has only even
powers: its order-three term is contained in \(S_i\).
The least weight of a nonzero coefficient is its valuation. At any fixed
weight the initial residues of distinct monomials are distinct powers
of \(z\), so no nonzero combination cancels. Since \(v_i(P)\ge0\),
every coefficient of weight below \(d=3m\) must vanish.

In particular the coefficient of \(u^1\), as a polynomial in \(S_i\),
is exactly \(p_{d-1}(1,r_i+S_i)\). Its coefficients of \(S_i^j\)
for \(j\le m-1\) have weights \(1+3j<3m\) and must vanish.
This would force divisibility of \(p_{d-1}(1,W)\) by \(f(W)^m\);
its degree is at most \(3m-1\), so it is zero. We do not need this
stronger conclusion below, but it accounts for the order-one terms.

The coefficients \(u^2S_i^j\) for \(j\le m-1\) likewise vanish.
The coefficient of \(u^2\), as a polynomial in \(S_i\), is exactly
\[
 \beta_i p_d'(1,r_i+S_i)+p_{d-2}(1,r_i+S_i).          \tag{8}
\]
The term \(u p_{d-1}\) contributes nothing to this coefficient:
in the formal substitution there is no order-\(u\) shift of \(W\),
so its first possible correction has order \(u^3\). This justification
concerns only coefficient (8), not parity of the actual DVR expansion.
The coefficients with \(j\le m-2\) in (8) force
\[
 p_{d-2}(1,W)=f(W)^{m-1}L(W),\qquad \deg L\le1.
\]
For \(m=1\) this divisibility is vacuous, but the same degree bound
holds. The coefficient with \(j=m-1\), divided by the nonzero
\(f'(r_i)^{m-1}\), now gives
\[
 L(r_i)+mc\beta_i f'(r_i)=0,
 \quad\text{or}\quad L(r_i)=mc r_i^2.
\]
If \(m\ne0\) in \(k\), a polynomial of degree at most one cannot
agree with this nonzero quadratic at three distinct points. Thus in
characteristic zero \(d=0\), and \(P\) is a nonzero constant.

For the asserted positive-characteristic refinement, (4) gives
\(\deg x_0\le4\), \(\deg x_1\le3\), \(\deg y=1\), so
\(\deg g\le4b\). At \(2n=b\), (5) gives \(d\le3b\), hence
\(m=d/3\le b\). If \(p>b\), the same contradiction applies.
No conclusion about equality is drawn from this step when \(p\mid m\).

We have proved \(g=cQ^{b/2}\) on \(x_3=1\). Therefore
\(G-cq^{b/2}\) vanishes on the integral carrier after inverting
\(x_3\). Since \(F_*\) is irreducible and not divisible by \(x_3\),
it divides this difference homogeneously. This proves (1), including
its degree and its assertion about the full intersection ideal.

### Sharpness, residual cycle, and jet kernels

The pair \((F_*,q^j)\) is proper: \(q\) is irreducible and
\(F_*\bmod q=D^2/4\ne0\). On the smooth quadric \(q=0\), use
\([x_0:x_1:x_2:x_3]=[ac:ad:bc:bd]\). Then
\[
 D=b^2(bc^3-ad^3),\qquad \operatorname{div}_Q(D)=2L_0+C,
 \qquad L_0=V(x_2,x_3).
\]
Consequently
\[
 [V(F_*,q^j)]=2j[C]+4j[L_0].
\]
This proves sharpness and gives \(16[C]+32[L_0]\) at degree sixteen.
An odd-degree extra factor \(x_3\) is a unit at the generic point
of \(C\), so it leaves the branch order unchanged. The cycle-degree
formula and the local-node order equivalence give (2). In fact for
any \(b\), the kernel at cutoff \(\lfloor b/2\rfloor+1\) is
\(F_*H^0(\mathcal O(b-6))\): a nonmultiple would be proper and
violate the bound. No coefficient-rank computation is needed.

### Standard theory and the fixed-carrier contribution

The normalization step uses the standard
[integral-closure construction](https://stacks.math.columbia.edu/tag/035E).
The nonsplit-node local length calculation is retained below. The
[adjacent selected-carrier study](../arguments/spectral/actual_sextic_mate_certificates.md)
already uses the auxiliary coordinate and the mate \(q^8\), but its
finite table does not include this \((t,\kappa)=(0,1)\) carrier. The
new contribution here is the three-boundary argument and its all-degree
consequence for this fixed carrier, not a novelty claim about
normalization or valuations themselves.

## Characteristic boundary of the argument

**Corollary 1 (bound).** The geometric bound works over an algebraically closed field of any
characteristic other than 2 and 37. Characteristic two is excluded by the
carrier's coefficient 1/4 and the quadratic residue argument. At 37 the
boundary cubic has a repeated root, so this three-distinct-lines proof
does not apply; no conclusion for that prime is asserted here.

**Corollary 2 (even-degree rigidity).** Even-degree maximal-contact rigidity uses m nonzero in the field and is
proved here in characteristic zero or p>b, p!=37. In particular the sharp
degree-sixteen statement and both kernels in (2) hold at 65521. For smaller
allowed primes the sharp bound still holds, but this proof does not classify
all maximizers. No odd-degree equality classification is asserted.

The retained finite certificate independently proves the older degree-sixteen
order-twelve kernel in characteristic 65521. Its 683 rank and 286 global
multiples give equality directly there; the separable-node argument gives
the weaker bounds 22 and eight. The newer geometric result subsumes that
consequence without using the matrix. These are distinct proof routes,
not an extrapolation of one finite-field rank to untested primes.

This is compatible with a quartic-carrier STCI in every positive
characteristic: the present theorem concerns a different, single sextic.
See [the curve and characteristic account](../arguments/curve/fixed_quartic_geometry.md).

## Conditional interface for other carriers

The following is a **sufficient criterion**, not a theorem that arbitrary
carriers satisfy its hypotheses. Let \(X\subset\mathbf P^3\) be an
integral carrier, \(U\) an affine open of its normalization, and
\(A=\Gamma(U,\mathcal O_U)\). Suppose the marked preimage on \(U\)
is Cartier with specified equation \(Q\), and suppose:

1. For every proper degree-\(b\) mate under consideration, its restriction
   in the chosen trivialization is \(g=Q^nP\) with \(0\ne P\in A\).
   This **global divisibility in \(A\)** must be checked; a generic
   vanishing order or an unnamed conductor alone is insufficient.
2. There is a nonempty finite family of boundary valuations \(v_i\) of \(k(X)\) with
   \(v_i(Q)=-a_i<0\), and a verified degree pole budget
   \(v_i(g)\ge-bc_i\), where \(c_i\ge0\).
3. No nonzero element of \(A\) has simultaneously positive order at
   all these boundaries: \(\min_i v_i(P)\le0\) for every \(P\ne0\).

Then \(v_i(P)\ge na_i-bc_i\). If
\(n>b\max_i(c_i/a_i)\), all these orders would be positive,
contradicting hypothesis 3. Hence
\[
 n\le b\max_i(c_i/a_i).
\]
To turn this into a residual-degree obstruction one must **separately**
verify the relation between \(n\) and the component multiplicity along
the marked curve, as well as proper intersection and the relevant degree
formula. For a curve of degree \(e\) on a degree-\(a\) carrier, if
\(m_C=\rho n\), this gives
\(\deg R=ab-e\rho n\ge b(a-e\rho\max_i c_i/a_i)\).
Strict positivity of this last constant is a sufficient exclusion on
that carrier; it is not automatic.

For \(F_*\), this note proves all three inputs with \(A=k[y,w]\),
the marked Cartier equation \(Q\), \(a_i=2,c_i=1\), and proves
\(\rho=2,e=4,a=6\), yielding \(\deg R\ge2b\). On other carriers,
none of these inputs is asserted here: in particular the marked preimage
may not be globally principal, its divisibility may fail, or the available
boundary valuations may admit simultaneous positive orders. Identifying
such data is a concrete research interface for the residual-construction
framework, not a carrier-independent exclusion or a resolution of the
open global STCI problem.

<a id="local-node-lemma-and-legacy-order-twelve-kernel-proof"></a>

## Appendix: local node lemma and independent legacy proof

The following independent route is retained with its exact source and
sample qualifications. Its order-twelve kernel and bounds 22 and eight
are valid but weaker than (1)–(2). Its rank computation is no longer a
premise of the sharp theorem.

Write \(K=k(z)=k(C)\). At the generic point use the actual ambient chart
\[
x=(1,z,z^3+v,z^4+u+3zv/2).
\]
Its two transverse parameters generate the marked ideal. Direct substitution
into the displayed four-term carrier gives quadratic term
\[
z^8\bigl((1+z^2)u^2-z^2v^2/4\bigr).
\]
The discriminant class \(1+z^2\) is nonsquare in \(K\): it has simple
zeros at \(z=\pm i\) even though \(k\) is algebraically closed. Thus the
ordinary double point splits into two smooth transverse branches over the
separable quadratic extension \(K(\sqrt{1+z^2})\), exchanged by its Galois
automorphism. Extending the **constant** field does not split this function-field
quadratic class.

For any actual \(G\) meeting the carrier properly, its orders along those
two conjugate branches are equal, say \(n\). Over the splitting extension,
formal transverse coordinates \(U,V\) make the node \((UV)\). The residue of
\(G\) modulo \(UV\) is the sum of a one-variable series of order \(n\)
in \(U\) and one of order \(n\) in \(V\). When \(G\) contains \(C\), its intersection length is
\(2n\): equivalently apply the normalization exact sequence of the node,
whose finite conductor quotient has multiplication kernel and cokernel of
equal length, and sum the two branch orders. The same expression proves
\[
G\in(F_*)+(u,v)^n,\qquad G\notin(F_*)+(u,v)^{n+1}.
\]
Formal coordinate changes preserve maximal-ideal powers and membership
descends through the faithfully flat splitting field. Finite length is
essential; a mate with a carrier factor is excluded by properness.

It remains to prove the **global constant-coefficient** jet-kernel identity.
The source has dimension \(\binom{19}{3}=969\). Over
\[
B=\mathbf Z[1/2,z,z^{-1},(1+z^2)^{-1}],
\]
the coefficient of \(u^2\) in the carrier is a unit. Reducing modulo
\((F_*,(u,v)^{12})\) leaves the 23 normal monomials
\[
1,v,\ldots,v^{11},u,uv,\ldots,uv^{10}.
\]
In the basis ordered by increasing total degree and then decreasing
\(u\)-exponent, the 55 relations obtained by multiplying \(F_*\) by all
monomials of degree at most nine have distinct pivots with unit coefficients.
They span all multiples of \(F_*\) at order twelve. The pivot monomials
are precisely those divisible by \(u^2\), so the 23 remaining monomials
form a basis over \(B\). Reduction in this basis evaluates every actual
degree-16 ambient monomial. This constructs a map from the **969-dimensional constant
coefficient** global source into \(B^{23}\); it does not permit arbitrary
\(k(z)\)-coefficients on those source monomials.

Evaluate its entries at \(z=1,\ldots,30\) modulo \(65521\). All values
are good: \(z\) and \(1+z^2\) are nonzero. Stacking the maps gives the
690-by-969 matrix checked by the replay below. Its certified rank is 683.
The matrix obtained by evaluating at the same thirty integers in
characteristic zero has entries in \(\mathbf Z_{(65521)}\). A nonzero
modular 683-minor lifts to a nonzero minor of that stacked rational
matrix. Any constant-coefficient vector in the generic jet kernel is
killed at every good sample, so the characteristic-zero constant-source
map has rank at least 683. Conversely
all 286 independent forms \(F_*H_{10}\) vanish **identically** in this
quotient. Multiplication by nonzero \(F_*\) is injective and
\(h^0(\mathcal O(10))=\binom{13}{3}=286\); hence the rank is at most
\(969-286=683\). It follows that
\[
\ker\bigl(H^0(\mathcal O(16))\longrightarrow
 K[[u,v]]/(F_*,(u,v)^{12})\bigr)
 =F_*H^0(\mathcal O(10)).
\]
The good samples provide a lower rank bound; the identity on all carrier
multiples provides the opposite bound. A recorded rank without this source
identification and kernel inclusion would not prove the statement.

If \(n\ge12\), the kernel identity forces \(G=F_*H_{10}\), contrary
to properness. Thus \(m_C=2n\le22\). The actual complete-intersection
cycle gives \(\deg R=96-4m_C\ge8\). This bounds residual degree without
inferring any residual component from exceptional vertical geometry.

## Exact evidence and independent verification

The [normal-division verifier](ci_fixed_sextic_jet_rigidity.support/verify.py) constructs the actual
four-term carrier and reduces all 969 degree-sixteen monomials at each of
the thirty good samples in \(\mathbf F_{65521}\). It checks the quadratic
symbol, annihilation of all 286 carrier multiples, the matrix digest, and
the exact modular rank. The proof establishes why these samples suffice for
the full constant-coefficient kernel. Run from the repository root with
Python 3 and a C++17 compiler (Clang or GCC).

```sh
python3 -B research/results/ci_fixed_sextic_jet_rigidity.support/verify.py
```

The maintained verifier was replayed during consolidation. It recovered
rank 683 and nullity 286 and matched SHA-256
`a3e546424d11200e1d8075c7f9d5d342787bd925a303901bd2b33b2661f56445`
for the row-major matrix of little-endian unsigned 32-bit entries.

The historical [quotient-ring Macaulay2 certificate](https://github.com/markluxton1/STCI/blob/f11123c0ab9fc4231ed0e5b21fc14a1b5fdecef7/research/computations/endpoint4_fixed_m2_2026_10_25.m2),
[execution metadata](https://github.com/markluxton1/STCI/blob/f11123c0ab9fc4231ed0e5b21fc14a1b5fdecef7/research/computations/endpoint4_fixed_m2_2026_10_25.json),
and [log](https://github.com/markluxton1/STCI/blob/f11123c0ab9fc4231ed0e5b21fc14a1b5fdecef7/research/computations/endpoint4_fixed_m2_2026_10_25.txt)
record rank 683, rank 286 for the ambient coefficient matrix of the known
multiples, and annihilation of all those multiples. The separate historical
[normal-division implementation](https://github.com/markluxton1/STCI/blob/f11123c0ab9fc4231ed0e5b21fc14a1b5fdecef7/research/computations/endpoint4_fixed_jet_independent_2026_10_26.py)
and [record](https://github.com/markluxton1/STCI/blob/f11123c0ab9fc4231ed0e5b21fc14a1b5fdecef7/research/computations/endpoint4_fixed_jet_independent_2026_10_26.json)
use the basis reproduced by the maintained verifier. GitHub Actions
[run 40434021004](https://github.com/markluxton1/STCI/actions/runs/40434021004),
job `replay-r0025`, reproduced the finite calculation and matrix hash using
that implementation. The recorded Macaulay2 run supplies a distinct quotient
construction and was source-inspected during review.

## Consequences
No proper positive-degree mate for this selected sextic has sole reduced support C0 in the characteristics covered by the bound.

## Limitations
No general sextic or unrestricted STCI theorem.
