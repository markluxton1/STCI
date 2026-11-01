# Section defects and exceptional-cover controls

These two mechanisms test proposed implications in the global STCI
problem. Both are independently reviewed **provisional** results; neither
is an exclusion or construction for arbitrary homogeneous pairs on the
fixed quartic. Each retains an exact geometric object that scalar
normal-degree or genus data would lose.

**Review status (2026-10-31).** Independent mathematical and preservation review reconstructed this replacement and its explicit characteristic extensions. The varying-Hilbert-function local control, degree-four defect notation, and ribbon section calculation were checked in their corrected homes. No material finding remains unresolved within the stated scopes. These remain reviewed provisional deductions, with no canonical promotion; no computation or inherited certificate rerun was needed.

## The specified missing coordinate and the graph-normal extension

Work in characteristic zero with
\(C=[s^4:s^3t:st^3:t^4]\subset P=\mathbf P^3\), \(I=\mathcal I_C\),
\(H=\mathcal O_P(1)\), \(E=I/I^2=\mathcal O_{\mathbf P^1}(-7)^2\), and
\(X=V(I^2)\), the first ordinary infinitesimal neighborhood. The balanced
conormal is the promoted input [R-0020](../results/quartic_conormal_characteristic_jump.md).
Let \(e=s^2t^2\in H^0(C,H|_C)\), the omitted fifth coordinate of the
rational normal quartic

\[
D=[s^4:s^3t:s^2t^2:st^3:t^4]\subset\mathbf P^4.
\]

Projection from \(z=[0:0:1:0:0]\) identifies \(D\) with \(C\).
The space \(\mathbf P^4\setminus\{z\}\) is \(\operatorname{Tot}_P(H)\),
and \(D\) is the graph of this specified section \(e\). The normal sequence
and rational-normal-curve normal bundle give

\[
0\to\mathcal O(4)\to N_{D/\mathbf P^4}=\mathcal O(6)^3
\to N_{C/P}\to0,
\]

hence after dualizing and twisting,

\[
0\to E\otimes H|_C=\mathcal O(-3)^2\to\mathcal O(-2)^3
\to\mathcal O_C\to0. \tag{1}
\]

The normal-bundle formula is [Bayer–Eisenbud, Appendix, Proposition 5A.2](https://www.math.columbia.edu/~bayer/papers/Ribbons_BE95.pdf).
For this instance there is also an explicit proof: the kernel of the
parametrization derivative \(\mathcal O(-4)^5\to\mathcal O(-1)^2\) has
three consecutive shifted syzygies \((t^2,-2st,s^2)\). Their band matrix
has rank three everywhere, by its first three rows for \(t\ne0\) and
last three for \(s\ne0\). Thus the conormal is \(\mathcal O(-6)^3\).

The extension class of (1), up to Čech sign, is exactly the boundary
\(\delta_X(e)\) from

\[
0\to E\otimes H|_C\to H|_X\to H|_C\to0. \tag{2}
\]

To check the identification rather than merely the ranks and degrees,
choose ambient local extensions \(e_i\). Their differences modulo \(I^2\)
are the boundary cocycle. In \(\operatorname{Tot}(H)\), the graph
conormal lift is \(w-e_i\), whose differences are the negative of that
same cocycle, giving (1). On \(x_0=1\), with \(u=x_1,a=x_2-u^3,b=x_3-u^4\),
the endpoint lifts have difference

\[
u^2-\frac{(u^3+a)^2}{u^4+b}=-2u^{-1}a+u^{-2}b\pmod{(a,b)^2}. \tag{3}
\]

No retraction \(X\to C\) or \(\mathcal O_C\)-algebra splitting is used:
(2) is a sequence of ambient sheaves, and the graph sequence is on \(C\).
Because \(H^0(\mathcal O(-2)^3)=0\), the boundary of the constant section \(1\) in (1) is
nonzero. The four ambient sections lift in (2), and
\(H^0(E\otimes H|_C)=0\), so \(h^0(X,H)=4\). Moreover its tensor class
in \(k^2\otimes H^1(\mathcal O(-3))\) has rank two. If it had rank at most
one, a change of balanced summands would split off \(\mathcal O(-3)\)
from the middle term of (1), impossible since
\(\operatorname{Hom}(\mathcal O(-2)^3,\mathcal O(-3))=0\).

All higher ordinary neighborhoods \(V(I^r)\), \(r\ge2\), also have four
linear sections: their twisted layers are
\(\operatorname{Sym}^jE\otimes\mathcal O(4)=\mathcal O(4-7j)^{j+1}\),
with no sections for \(j\ge1\). Restriction injects their section spaces
backwards, and the four ambient sections persist. This concerns ordinary
neighborhoods, not arbitrary multiple-curve normal layers.

### Persistence through full limits and their pure hulls

Let \(Y\) have reduced support \(C\) and ideal sheaf
\(\mathcal I_Y\subset I^2\). Let a one-parameter subgroup preserve \(C\),
and let \(Z\) be either full projective Hilbert limit of its translates.
If \(T\subset\mathcal O_Z\) is the maximal zero-dimensional subsheaf and
\(\mathcal O_{\bar Z}=\mathcal O_Z/T\), then

\[
X\subset\bar Z\subset Z,\qquad
\delta_Y(e)\ne0,\quad\delta_Z(e)\ne0,\quad\delta_{\bar Z}(e)\ne0. \tag{4}
\]

For a direct proof, let \(K=H^0_*(I^2)\) be the **saturated** homogeneous
ideal of \(X\). It is invariant. If \(J\) is the saturated ideal of \(Y\),
then \(J\subset K\) gives
\(\operatorname{in}_{\pm w}J\subset K\), and saturation preserves that
inclusion because \(K\) is saturated. Thus the actual full limits contain
\(X\), without assuming two initial equations generate their ideals.
The neighborhood \(X\) is pure CM: locally it is the quotient by
\((a,b)^2\), and a support parameter is regular. The finite-support image
of \(T\) in \(\mathcal O_X\) is zero, so the quotient map factors through
\(\mathcal O_{\bar Z}\), giving its containment. Naturality sends every
boundary class in (4) to the nonzero \(\delta_X(e)\).

This applies to the torus weights \((0,1,3,4)\) and to every hypothetical
supported CI whose equations have zero first normal image. Generic zero
first symbols vanish everywhere, being sections of vector bundles on
integral \(C\). It supplies no claim for a nonzero first normal image.
The nonvanishing is compatible with an actual CI, whose ACM property
already gives four linear sections. In the entirely thick branch it
cannot be turned into a contradiction by asking that either limit or
its pure hull lift \(e\): the same fixed neighborhood prevents that lift.

### Gorenstein multiples still need higher-twist information

On the smooth quadric \(Q=(x_0x_3-x_1x_2)=\mathbf P^1\times\mathbf P^1\),
label the rulings so \(C=(1,3)\) and \(H|_Q=\mathcal O(1,1)\). For every
\(n\ge2\), its Cartier multiple \(W_n=nC\subset Q\) is torus invariant,
locally CI/Gorenstein, and has sole reduced support \(C\). Yet

\[
h^0(W_n,H)=4,\quad\delta_{W_n}(e)\ne0,\quad
h^1(P,\mathcal I_{W_n}(n))=2n-1. \tag{5}
\]

At twist one the restriction kernel on \(Q\) is
\(\mathcal O_Q(1-n,1-3n)\), whose \(H^0,H^1\) vanish by Künneth, so
all sections come from the four ambient ones. At twist \(d\), the ideal
sequence is
\(0\to\mathcal O_P(d-2)\to\mathcal I_{W_n}(d)
\to\mathcal O_Q(d-n,d-3n)\to0\). The intermediate line-bundle
cohomology on \(\mathbf P^3\) vanishes; at \(d=n\) the remaining first
cohomology is \(H^1(Q,\mathcal O(0,-2n))\), dimension \(2n-1\).
Thus local Gorensteinness and the correct linear section count do not
force ACM. These controls have a first-order quadric equation and do not
satisfy the hypothesis \(\mathcal I_Y\subset I^2\) of (4).

## Full-ideal exceptional covers can have unbounded genus

A different control shows why resolving an actual full ideal does not
force rational or unramified exceptional covers solely from rational
support and integral entirely thick carriers. This example uses a **line**,
not the fixed quartic.

In characteristic zero choose \(r\ge2,e\ge1\), set \(n=r(e+1)\), and put

\[
A=Z^{re}-W^{re},\quad G=Y^n+X^rA,\quad F=G+X^n,\quad L=(X=Y=0).
\tag{6}
\]

Both degree-\(n\) surfaces are integral and singular along all of \(L\).
Their proper intersection has sole support \(L\) and generic multiplicity
\(n^2\), since \((F,G)=(X^n,G)\) and over \(k(L)\) its quotient has basis
\(x^iy^j\), \(0\le i,j<n\). Irreducibility of \(G\) is Eisenstein in
\(Y\) at any simple factor \(Z-\zeta W\) of \(A\). For \(F\) use a prime
factor of \(X^{re}+Z^{re}-W^{re}\): this polynomial is squarefree, since
a repeated factor would divide its three partials, whose divisorial gcd
is one; it has no \(X\) factor. Eisenstein and Gauss apply again. Every
normal order is at least \(r\ge2\), proving singularity along \(L\).

Blow up the **full ideal** \((F,G)\) and normalize the blowup. Its reduced
exceptional surface is \(L\times\mathbf P^1\), because a regular immersion
has exceptional divisor the projectivization of its conormal, here
\(\mathcal O_L(-n)^{\oplus2}\). The second factor is the actual equal-degree
pencil, equivalently generated by \(X^n,G\).
There is a unique exceptional prime \(T\) on the normalized blowup, and

\[
T^\nu=D\times\mathbf P^1,\quad k(D)=k(t)(\beta),\quad
\beta^r=1-t^{re},\quad \nu^*E=n(e+1)T. \tag{7}
\]

The finite map to \(L\times\mathbf P^1\) is the product of \(D\to L\)
with the identity, and has degree \(r\). Here is the actual normalization
calculation. At the generic point of \(L\), write \(K=k(t)\) and take the
blowup chart
\(\lambda x^n=y^n+(t^{re}-1)x^r\), localized at \((x,y)\).
Since the ideal is a regular sequence, this is its Rees chart. In its
fraction field \(\beta=y^{e+1}/x\) is integral, with
\(\beta^r=\lambda x^{re}-(t^{re}-1)\). Modulo \((x,y)\), its polynomial
is irreducible over \(K(\lambda)\), by Eisenstein at \(t-1\) over \(K\)
and preservation under pure transcendence. The finite birational
extension adjoining \(\beta\) is local with this residue field.
The element \(\beta\) is a unit and \(x=y^{e+1}/\beta\); hence its maximal
ideal is \((y)\). It is a DVR and therefore the full local normalization.
Its valuation is
\(v(y)=1,v(x)=e+1,v(G)=v(x^n)=n(e+1)\), proving the coefficient in (7).

No additional exceptional prime can appear over a closed point: normalization
is finite, so a prime divisor has a two-dimensional image, while a blowup
fiber over a closed point of \(L\) is one-dimensional. Thus \(T\) is unique.
Its residue extension is exactly \(k(L)(\lambda)\subset k(D)(\lambda)\).
The normal finite surface \(D\times\mathbf P^1\to L\times\mathbf P^1\)
has that same field inclusion; uniqueness of integral closure gives (7)
globally. This proves the normalization of \(T\), not that \(T\) itself
is normal. The coefficient-degree identity reads
\(n(e+1)r=n^2\), the actual transverse multiplicity.

The \(re\) simple finite roots of \(1-t^{re}\) are totally ramified of
index \(r\). At infinity, \(s=t^{-1},\gamma=\beta s^e\) give
\(\gamma^r=s^{re}-1\), with \(r\) distinct nonzero roots at \(s=0\), so
infinity is unramified. Riemann–Hurwitz yields

\[
g(D)=\frac{(r-1)(re-2)}2. \tag{8}
\]

For \(r=2\) this is every genus \(e-1\ge0\); for \((r,e)=(2,1)\) the
pair has degrees \((4,4)\), multiplicity sixteen, coefficient eight and
rational exceptional cover; for \((2,2)\) it has degrees \((6,6)\),
multiplicity thirty-six, coefficient eighteen and elliptic cover.
These are exact specializations, not numerical experiments. The relative
algebraic closure of \(k(L)\) in \(k(T)\) is \(k(D)\); the absolute constant
field is still \(k\).

The ramification fibers are whole pencil-direction curves in the
exceptional surface; they create no extra support curve downstairs.
Consequently rational support, separability, integral carriers, and an
actual supported CI do not imply a rational exceptional normalization,
unramifiedness, unchanged relative constants, or a support-genus bound
on its cover. The quartic's particular embedding, normal bundle and
actual equation spaces are additional data, not used by this control.
[Jaffe's iterated-blowup arguments](https://arxiv.org/pdf/alg-geom/9410008)
assume no common singularities, or that the support is not contained in
either carrier singular locus; (6) is deliberately outside those hypotheses.
The normalization-of-Rees-chart method is standard; compare
[Swanson, §2](https://www.math.purdue.edu/~iswanso/reesvals.pdf).

For unequal equation degrees \(a,b\) on the quartic, the original full-ideal
exceptional reduction is
\(\mathbf P_C(\mathcal O_{\mathbf P^1}(-4a)\oplus\mathcal O_{\mathbf P^1}(-4b))\simeq\mathbb F_{4|a-b|}\),
where the displayed line-bundle degrees are on the normalized curve. The raw
ratio \([F_a:G_b]\) takes values in that projective bundle, not a fixed
pencil line. Taking powers to equalize the degrees changes the full ideal
and its blowup and cannot identify these exceptional constructions.

## Smooth models and dynamical source hypotheses

The full-ideal line-supported examples above already allow ramified
exceptional covers of arbitrarily large genus. Rational support therefore
does not force rational or unramified normalized covers. Generic ruledness
does not supply an everywhere smooth \(\mathbf P^1\)-bundle model, and
singular fibers cannot be counted as additional support curves downstairs.

The checked dynamical sources require more structure.
[Petsche–Szpiro–Tepper, Theorem 1](https://arxiv.org/pdf/0806.1364)
concerns projective-space endomorphisms with potential good reduction at
every place. [Silverman, Theorem 1.1](https://arxiv.org/pdf/math/9609212)
uses moduli under simultaneous source-target conjugacy. A cover of the fixed
pencil line is not automatically such a dynamical system; changes of source
coordinates alone are not conjugacy. Even a smooth ruled model would not
by itself provide the dynamical morphism and reduction data required by
these theorems. The missing operation would have to connect actual ambient
equations with those extra conditions or constrain exceptional degeneration
in a way not already allowed by the supported controls.

These application limits received independent review at source checkpoint
`57fb49b`, including the existing line-supported example. They introduce no
new universal theorem about normalized exceptional surfaces.

## Characteristic boundaries of these controls

The graph-cocycle identification, ideal containment through full limits,
and pure-hull factorization are scheme-theoretic arguments in any
characteristic with their stated smoothness hypotheses. The explicit
normal-bundle calculation and rank-two section obstruction above extend
to odd characteristic: the balanced conormal input remains valid by
R-0020, and both two and four are invertible in the derivative/normal
calculation. In characteristic two that conormal is unbalanced; the
characteristic-zero normal sequence and its tensor-rank assertion cannot
be transferred as written. The Künneth argument for the quadric multiples
and its failure of ACM in (5) work in every characteristic. These local
Gorenstein controls do not depend on a characteristic-zero exclusion.

For the exceptional-cover family (6)–(8), the same proof extends when
\(p\nmid re\): the branch polynomial has simple roots, the Eisenstein
primes are simple, and the cyclic cover is separable and tame of degree
\(r\), so the stated Riemann–Hurwitz contribution is valid. No invertibility
of \(e+1\) or \(n=r(e+1)\) is needed for the displayed DVR calculation or
monic standard-monomial length. When \(p\mid re\), the squarefree and
tame-ramification steps fail; the same formulas are not asserted. The
general regular-immersion exceptional-divisor and finite-normalization
frameworks are characteristic free, but they do not repair that loss.
Thus this control is not tied intrinsically to characteristic zero; its
extension is bounded by explicit separability and squarefreeness, rather
than by analogy with the zero-characteristic genus formula.

## What the two controls have in common

The section defect belongs to the marked embedded neighborhood and survives
because that neighborhood survives. The exceptional cover belongs to the
normalization of the full Rees construction and survives because the
transverse root directions need a finite extension of \(k(L)\). Neither
is read off from a scalar normal degree. Neither is itself an actual
residual curve. The shared lesson is a precise limitation: translating
these defects into residual support requires an additional theorem about
the original homogeneous equations and their endpoint compatibility.
The controls demonstrate failure of the indicated general shortcuts;
they do not assert that every quartic-specific bridge fails.
