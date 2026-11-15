# Arithmetic root collision in the quartic pencil

Retain the actual pencil F=x1^4-x0^3*x3, G_a=x2^4-a*x1*x2*x3^2+(a-1)*x0*x3^3, with the marked root lambda=1. Work over a complete rank-one valued field of characteristic zero and residue characteristic two, extending its valuation to algebraic roots when needed. This exact local computation is reviewed evidence, not a characteristic-zero nonexistence theorem or a characteristic-p support construction.

## Two mixed-characteristic scales and the root collision tree

## 1. The experiment and its three distinct scales

Retain
\[
F=x_1^4-x_0^3x_3,\quad
G_a=x_2^4-a x_1x_2x_3^2+(a-1)x_0x_3^3.
\]
Over a complete rank-one valued field \(K\) of characteristic zero with
residue characteristic two, write
\[
\varepsilon=a-4,\qquad h=v(2)>0,\qquad
\gamma=v(\varepsilon)>0.
\]
Extend the valuation to an algebraic closure when discussing roots. We
initially exclude \(\varepsilon=0\) and the two residual discriminant
parameters, so the four geometric roots are distinct. Odd rational
integers are units. The root coordinate \(\lambda=1+w\) gives
\[
f_a(1+w)=w\bigl(w^3+4w^2+6w-\varepsilon\bigr).
\tag{1}
\]
The marked curve \(C\) is \(w_0=0\). The other three sheets correspond to
the roots of the cubic in parentheses. Since all their valuations below
are positive, every \(\lambda=1+w\) is a unit and all four generic
components are smooth conjugate quartics.

There are two arithmetic scales: \(h\), the size of the prime two, and
\(\gamma\), proximity of the pencil parameter to the characteristic-zero
double-\(C\) member. A local endpoint parameter later introduces a third,
horizontal scale. These should be recorded separately before any weighted
sum is chosen.

The standard Newton-polygon rule reads root valuations, counted with
multiplicity, from negative slopes and horizontal lengths of the lower
hull; see [Sharifi, Algebraic Number Theory, Proposition 5.4.11](https://math.ucla.edu/~sharifi/notes/algnum-ch05.html).
Everything specific to this pencil is calculated below.

## 2. First break: which sheets approach the marked curve fastest?

The Newton points of the residual cubic are
\[
(0,\gamma),\quad(1,h),\quad(2,2h),\quad(3,0).
\]
The point \((2,2h)\) never contributes a lower-hull vertex. The first break
is at \(\gamma=3h/2\):

| Parameter scale | Valuations of the three differences from the marked root |
| --- | --- |
| \(0<\gamma<3h/2\) | \(\gamma/3,\gamma/3,\gamma/3\) |
| \(\gamma=3h/2\) | \(h/2,h/2,h/2\) |
| \(\gamma>3h/2\) | \(\gamma-h,h/2,h/2\) |

The sum is always \(\gamma\), as it must be from the constant coefficient
\(-\varepsilon\). Above the break, label the uniquely closest root
\(w_1\), so \(v(w_1)=\gamma-h\), and call the other roots \(w_2,w_3\).

The critical equality does **not** produce a residue collision. To see
this, choose \(t^2=2\), divide the cubic at \(w=tz\) by \(t^3\), and reduce.
The result is
\[
\bar z^3+\bar z+\beta,\qquad
\beta=\overline{\varepsilon/t^3}\ne0.
\]
Its derivative is \((\bar z+1)^2\), but its value at \(\bar z=1\) is
\(\beta\ne0\). Thus the residual cubic has three distinct nonzero roots.
All six pairwise differences among \(0,w_1,w_2,w_3\) have valuation
\(h/2\) at this equality. Below it, the reduced equation after scaling is
\(z^3-\beta\), also separable in residue characteristic two; all six
pairwise differences then have valuation \(\gamma/3\).

This corrects a tempting first guess: a change in Newton slopes need not
be a collision of residual roots. Here the tree changes from four equal
branches to two closer pairs only *after* the first break.

## 3. Second break: a residual pair can collide independently of C

The first Newton polygon does not determine the mutual separation of
\(w_2\) and \(w_3\). Above the first break, they share a leading residue.
Their discriminant supplies the missing coordinate. Set
\[
B(\varepsilon)=-288-176\varepsilon-27\varepsilon^2.
\tag{2}
\]
This is both the discriminant of the residual cubic and the factor
\(-27a^2+40a-16\) of the quartic discriminant. In particular
\[
\operatorname{disc}(f_a)=\varepsilon^2B(\varepsilon).
\tag{3}
\]
The three terms in (2) have valuations
\[
5h,\qquad4h+\gamma,\qquad2\gamma.
\]
The middle term is never minimal. Therefore
\[
v(B)=
\begin{cases}
2\gamma,&\gamma<5h/2,\\
5h,&\gamma>5h/2,
\end{cases}
\tag{4}
\]
whereas at \(\gamma=5h/2\) cancellation may increase \(v(B)\).

For \(\gamma>3h/2\), put \(\delta=v(w_2-w_3)\). The two differences
\(w_1-w_2,w_1-w_3\) have valuation \(h/2\), so the cubic discriminant gives
\[
v(B)=2(h+\delta),\qquad
\delta=\frac{v(B)}2-h.
\tag{5}
\]
Thus the full collision pattern is:

| Region | Marked pair depth \(v(w_1-w_0)\) | Other pair depth \(\delta\) | Cross-pair depth |
| --- | --- | --- | --- |
| \(3h/2<\gamma<5h/2\) | \(\gamma-h\) | \(\gamma-h\) | \(h/2\) |
| \(\gamma=5h/2\) | \(3h/2\) | \(v(B)/2-h\ge3h/2\) | \(h/2\) |
| \(\gamma>5h/2\) | \(\gamma-h\) | \(3h/2\) | \(h/2\) |

The marked pair and the other pair initially deepen at the same rate.
Beyond the second break, only the marked pair continues to deepen for a
parameter approaching zero \(\varepsilon\); the other pair stabilizes.
But in a different parameter direction through the critical shell,
the *residual* pair can deepen arbitrarily while the marked pair stays
at depth \(3h/2\). This is an actual distinction between concentration
onto \(C\) and collisions elsewhere in the residual curve.

A schematic tree above the first break is

```text
all four roots, common depth h/2
  ├── {marked root 0, w1}: additional depth (gamma-h) - h/2
  └── {w2, w3}:             additional depth delta - h/2
```

Depth is a valuation of a coordinate difference. No choice of a global
metric on the ambient projective space is being asserted.

## 4. The exceptional shell retains residue information

At \(\gamma=5h/2\), use \(t^2=2\) and write
\(\varepsilon=t^5e\), with \(e\) a unit. After dividing (2) by \(t^{10}\),
the residue is
\[
\overline{B/t^{10}}=\bar e^2+1=(\bar e+1)^2.
\]
Thus \(\bar e\ne1\) gives \(v(B)=5h\); the residue \(\bar e=1\) requires
further terms and can give deeper collisions. If the residue field is
\(\mathbf F_2\), every unit has residue one, so cancellation on this
critical shell is automatic. A generic noncancelling residue exists
after a suitable residue-field extension.

An explicit ramified example is
\(K=\mathbf Q_2(\sqrt2)\), \(h=1\),
\(\varepsilon=4\sqrt2\), so \(\gamma=5/2\). Then
\[
B=-1152-704\sqrt2,\qquad v(B)=13/2,
\]
because the summands have distinct valuations \(7\) and \(13/2\).
Consequently the residual-pair depth is \(\delta=9/4\), larger than the
naive \(3/2\) value on the critical shell.

More precisely, the two zeros of \(B\) are
\[
\varepsilon_\pm=
\frac{-88\pm4\sqrt{-2}}{27}.
\]
Each has valuation \(5h/2\), while
\(v(\varepsilon_+-\varepsilon_-)=7h/2\). Writing
\(r_\pm=v(\varepsilon-\varepsilon_\pm)\), one has the exact refinement
\[
v(B)=r_++r_-,\qquad
\delta=\frac{r_++r_-}{2}-h.
\tag{6}
\]
Away from the zeros themselves these numbers are finite. If one distance
is below \(7h/2\), both distances equal that smaller value. If one exceeds
\(7h/2\), the other is \(7h/2\). At equality the residue of the next
coefficient matters again. This describes the full critical-shell
refinement in terms of the actual two discriminant points, rather than
pretending that \(\gamma\) alone determines the tree.

At \(\varepsilon=\varepsilon_\pm\), the residual pair is genuinely double;
at \(\varepsilon=0\), the marked pair is double instead. These are
separate characteristic-zero strata in the same arithmetic neighborhood.

## 5. Recovering the fourth roots of unity and the elliptic marker

The original \(\mu_4\) member has \(a=0\), hence \(\varepsilon=-4\) and
\(\gamma=2h\). The marked differences are
\[
-2,\quad i-1,\quad-i-1,
\]
with valuations \(h,h/2,h/2\); the other close pair has difference \(2i\)
and depth \(h\). Thus the two pairs have equal depths. The derivative
budget is \(h+h/2+h/2=2h=v(4)\), and the full quartic discriminant has
valuation \(8h=v(-256)\), as predicted by (3).

For \(\gamma>3h/2\), choose the cross-ratio adapted to the two pairs,
\[
x=\frac{(w_0-w_1)(w_2-w_3)}{(w_0-w_2)(w_1-w_3)}.
\]
Its depth is
\[
\ell=v(x)=\gamma+\delta-2h>0.
\tag{7}
\]
This combines the two short-pair depths after subtracting the common
cluster depth. The elliptic double cover from the root-pencil note has
\[
j=256\frac{(1-x+x^2)^3}{x^2(1-x)^2}.
\]
Since \(v(x)>0\), the factors \(1-x\) and \(1-x+x^2\) are units. Therefore
\[
v(j)=8h-2\ell
=14h-v(\operatorname{disc}f_a).
\tag{8}
\]
The second equality also follows directly from the exact pencil formula
for \(j\), since \(a-1\) is a unit in this neighborhood.
At the \(\mu_4\) member \(\ell=h\) and \(v(j)=6h\), agreeing with
\(j=1728\). This is a useful consistency bridge between a root-collision
tree and the coarse elliptic modulus. We do not infer a model of stable
reduction or a reduction type from this numerical identity alone.

## 6. Endpoint contact adds a horizontal contribution

Near \(p\), a branch has transverse coordinate \(Y=w u^3\) relative to
\(C\). If an endpoint valuation assigns \(v(u)=\alpha\ge0\), then
\[
v(Y_i-Y_j)=v(w_i-w_j)+3\alpha.
\tag{9}
\]
The first-normal determinant is \(-\varepsilon u^9\), and its valuation
is exactly
\[
\gamma+9\alpha
=\sum_{i=1}^3\bigl(v(w_i)+3\alpha\bigr).
\tag{10}
\]
The full local quartic discriminant similarly has valuation
\(v(\operatorname{disc}f_a)+36\alpha\). These equations separate
arithmetic coalescence of coefficients from the order-three geometric
contact at the endpoint.

At the other endpoint, the leading coefficients are \(\lambda^{-3}\).
They are obtained from the first endpoint by
\[
\lambda\longmapsto\frac{\lambda}{a\lambda+1-a}.
\]
In the present neighborhood its determinant \(1-a\) and all denominators
\(\lambda^4\) are units. Hence it preserves every pairwise valuation of
the coefficient differences. The same arithmetic collision tree occurs
at both endpoints, with the local horizontal factor then added as in
(9). This agreement is stronger than equality of the two elliptic
\(j\)-invariants.



## Relation to the geometric model

The [geometric root pencil](root_pencil_geometry.md) supplies actual component cycles, flatness, conductor and branch cross-ratio. The present calculation additionally retains coefficient-prime scale, parameter scale and endpoint scale. Newton slopes alone do not encode a residual-root collision; the residue polynomial is necessary.


## Exact arithmetic support

The historical collision-tree Python verifier checked the discriminant and scale calculations and was retired during Phase 3B. Its previously recorded 50 checks and [historical output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/ci_cycle_root_collision_valuations_2026_10_25.json) remain available through Git history; no new replay is claimed. The proof above uses the actual Newton polygons and residue polynomials; a list of root valuations alone would miss the residual collision.


## Consolidated historical supplement: `research/supplements/ARITHMETIC_EQUATIONS_AND_JET_GAPS.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Arithmetic degree bounds, missing jets, and actual non-binomial equations

The embedded curve is the fixed integral model \(C_0=[s^4:s^3t:st^3:t^4]\). All defining forms have actual scalar coefficients over the algebraically closed field in question. The arithmetic reduction and restricted constructions below have inherited independent review. Their minima range over specified carriers or sources, not every homogeneous pair.

## Bounded degree and characteristic-zero existence

## 1. The exact characteristic limit that would settle the question

Define the minimum over **all** supported pairs
\[
\delta(p)=\min\{\max(a,b):V(F_a,G_b)_{\mathrm{red}}=C_0
\text{ over }\overline{\mathbb F}_p\}.
\]
The convention is \(+\infty\) if no pair exists. Known positive-
characteristic constructions make it finite for this curve.

The precise form of the arithmetic strategy is
\[
\boxed{C_0\text{ is not an STCI in characteristic zero}
\quad\Longleftrightarrow\quad
\delta(p)\longrightarrow\infty\text{ as primes }p\longrightarrow\infty.}
\tag{1}
\]
It is enough to prove an unbounded sequence of actual values of
\(\delta(p)\) along distinct primes. Exact minimality of the known
Frobenius constructions is stronger than needed.

For completeness, the proof uses finite type rather than an assumed
lifting theorem. At fixed \((a,b)\), take the projective coefficient
space of pairs containing the parametrized curve. In its universal
intersection remove the fixed copy of \(C_0\). The image of the remaining
open subscheme in coefficient space is constructible by
[Chevalley's theorem, Stacks Tag 054K](https://stacks.math.columbia.edu/tag/054K).
Its complement is the geometric sole-support locus. For a fixed degree
bound \(D\), its finite union over \(a,b\le D\) has constructible image
in \(\operatorname{Spec}\mathbb Z\). That image either contains the
generic point and all but finitely many primes, or misses the generic
point and contains only finitely many primes. This proves (1).

The finite rank-locus construction below supplies an actual integral
incidence scheme for the same condition. A nonempty finite-type
characteristic-zero fiber has a closed point over a number field; hence
existence over any algebraically closed characteristic-zero field is
equivalent to existence over \(\overline{\mathbb Q}\). Transcendental
coefficients create no loophole in (1).

Two equivalent measurements are
\[
\mu(p)=\min ab,\qquad \tau(p)=\min m_C=\mu(p)/4.
\]
They diverge exactly when \(\delta(p)\) does, since
\(\delta(p)\le\mu(p)\le\delta(p)^2\). In contrast,
\(\min\min(a,b)\) cannot diverge: known constructions keep one equation
quartic. All minima here allow finite extensions of \(\mathbb F_p\);
failure to find rational coefficient pairs over \(\mathbb F_p\) is not
geometric emptiness.

## Quantitative transfer and covered degree bounds

The [effective characteristic-transfer proof](EFFECTIVE_CHARACTERISTIC_TRANSFER.md)
gives an explicit constant \(B_D\): if \(p>\exp(B_D)\), a supported
pair of degrees at most \(D\) in characteristic \(p\) would give a
characteristic-zero pair with the same ordered degrees. The resulting
unrestricted growth rate is conditional on characteristic-zero
nonexistence. In contrast, its growing mate-degree bound over **all
quartic carriers** is unconditional, using the accepted
characteristic-zero quartic exclusion. It remains a bound for that
carrier class, rather than the unrestricted \(\delta(p)\).

The [torus-weight proof](EQUIVARIANT_DEGREE_BOUNDS.md) extends the sharp
large-prime lower bound from one binomial equation to one
weight-homogeneous equation with an arbitrary mate, and to pairs with at
most two weights per equation. It also constrains the extreme components
of arbitrary pairs when the degree product is prime to \(p\). The
three/two-weight residual example there explains why controlling a common
extreme locus does not control zeros created by cancellation outside it.

## The full simultaneous equation incidence

The parametrization defines a closed copy of \(\mathbf P^1_{\mathbb Z}\) in
\(\mathbf P^3_{\mathbb Z}\): on \(x_0\ne0\) its coordinates are
\((x_1,x_2,x_3)=(t,t^3,t^4)\), and on \(x_3\ne0\) the ratio \(x_2/x_3\)
is the local parameter at infinity. This description works in every
characteristic.

Let \(P_{a,b}\) be the closed subscheme of the product of the two full
projective coefficient spaces obtained by setting every coefficient of
\(F(s^4,s^3t,st^3,t^4)\) and of the corresponding substitution in \(G\)
equal to zero. This avoids assuming any cohomology base-change statement
about a chosen basis of global sections. Its geometric points are exactly
the nonzero degree-\(a,b\) forms containing the fixed curve.

Inside \(P_{a,b}\), the proper-pair locus \(U_{a,b}\) is open. Indeed,
the common-factor locus is the finite union, for
\(1\le e\le\min(a,b)\), of the images of the projective multiplication
maps
\[
\mathbf P(S_e)\times\mathbf P(S_{a-e})\times\mathbf P(S_{b-e})
\longrightarrow\mathbf P(S_a)\times\mathbf P(S_b),
\qquad(H,A,B)\longmapsto(HA,HB).
\]
These images are closed. Here \(S_d\) is the free module of homogeneous
degree-\(d\) forms, including \(S_0\).

If \(4\nmid ab\), the STCI locus is empty by the degree identity. Otherwise
put \(M=ab/4\). On the chart above, use
\[
u=x_2-t^3,\qquad v=x_3-t^4,\qquad K=k(t),\qquad
A_M=K[u,v]/(u,v)^{M+1},\qquad n=\binom{M+2}{2}.
\]
Substituting \((1,t,t^3+u,t^4+v)\) in the universal forms and taking all
truncated monomial multiples gives a multiplication matrix
\(T:A_M^2\to A_M\). Every entry is a polynomial in \(t\), with integral
polynomial expressions in the original scalar coefficients.

For a proper geometric pair let \(\ell\) be its generic transverse length
along \(C_0\). The degree identity gives \(4\ell\le ab\). In the generic
transverse Artin quotient, length \(\ell\) implies that its maximal
ideal to power \(\ell\) vanishes. Truncation at \((u,v)^{M+1}\)
therefore preserves that quotient, and the multiplication matrix presents
it. Hence
\[
\ell\le M,\qquad n-\operatorname{rank}_{k(t)}T=\ell.
\]
Consequently
\[
\sqrt{(F,G)}=I_{C_0}
\quad\Longleftrightarrow\quad
\operatorname{rank}_{k(t)}T\le n-M.\tag{Rank}
\]
The radical here describes projective reduced support, equivalently the
radical of the saturated homogeneous ideal. Degree exhaustion and purity
are essential for (Rank); the same rank equations outside the proper locus
are not an STCI certificate.

Set every coefficient in \(t\) of every \((n-M+1)\)-minor to zero.
This is a finite collection of equations over \(\mathbb Z\), valid after
specialization to every characteristic. It defines a closed condition
on each affine coefficient chart, invariant under nonzero rescaling of
either form. Therefore the STCI locus \(Z_{a,b}\) is closed relative to
\(U_{a,b}\), in particular a scheme of finite type over \(\mathbb Z\).
This construction keeps coefficients in \(k\), rather than allowing
arbitrary choices in \(k(t)\).

## Mixed-characteristic lifting on the full incidence

Fix a characteristic-\(p\) point \(z\in Z_{a,b}\). A DVR trait in
\(Z_{a,b}\) with closed point mapping to \(z\) and characteristic-zero
generic point exists, allowing residue extension and ramification, exactly
when
\[
p\notin\sqrt{0}\quad\text{in }\mathcal O_{Z_{a,b},z}. \tag{Trait}
\]
Indeed, nonnilpotence says that \(z\) lies in the closure of
\(Z_{a,b}[1/p]\). Applying the finite-type closure-to-trait lemma to
that open immersion produces the trait. Conversely, a local map to a DVR
of mixed characteristic sends \(p\) to a nonzero element, so \(p\)
cannot have been nilpotent. No properness of the incidence over
\(\mathbb Z\) is asserted or needed. This is a reformulation of the
horizontal-component question, not a calculation of (Trait).
[Stacks, Lemma 32.15.1](https://stacks.math.columbia.edu/tag/0CM1).

There is also a precise formal route. Let \(R\) be one complete
mixed-characteristic DVR with uniformizer \(\pi\). Suppose compatible
embedded flat subschemes \(W_n\subset\mathbf P^3_{R/\pi^n}\) are supplied
for every \(n\). They algebraize to a proper embedded subscheme over
\(R\), by [Stacks, Lemma 76.43.1](https://stacks.math.columbia.edu/tag/0A00).
To obtain the desired supported complete intersection, retain compatible
actual degree-\((a,b)\) generators and the support containments as part
of this system: for one fixed \(N\), require
\[
\mathcal I_{C_R}^{N}\mathcal O_{\mathbf P^3_{R/\pi^n}}
 \subset \mathcal I_{W_n}
 \subset \mathcal I_{C_R}\mathcal O_{\mathbf P^3_{R/\pi^n}}
\quad\text{for every }n. \tag{Support}
\]
The compatible coefficients have limits in \(R\); the resulting two
forms have exactly these reductions. Exactness and faithfulness of
completion for coherent sheaves on the proper ambient space transport
(Support) and identify their ideal with the algebraized ideal. Flatness and
the given complete-intersection presentation likewise persist. Thus the
generic fiber is an actual supported pair. This implication presupposes
the compatible global lifts; it does not construct them. Reduced support
at each infinitesimal level alone cannot replace the uniform containments
(Support), which control the generic fiber.

An unramified second-Witt-vector obstruction does not exclude a ramified
lift. For example, the special point \(x=0\) of \(x^2=p\) has no lift
to \(\mathbb Z/p^2\mathbb Z\): every possible lift is divisible by
\(p\), whose square is zero there, whereas \(p\ne0\). It does lift
to the ramified complete DVR
\(\mathbb Z_p[\varpi]/(\varpi^2-p)\), by \(x=\varpi\). Therefore the
[known higher-degree \((16,p)\) examples](#a-larger-source-with-an-actual-transverse-jet-gap)
remain unresolved under simultaneous deformation of both equations.
Their fixed-carrier jet obstruction cannot decide the local ring of the
full incidence. The [Granger–Schulze construction](https://arxiv.org/abs/1804.01316)
concerns deformations of monomial space-curve singularities; its analytic,
equicharacteristic semigroup setting supplies no support-preserving
projective mixed-characteristic lift here.

The remaining arithmetic input is a support-preserving lifting operation
or a structural calculation on this full simultaneous-pair incidence.
One horizontal component would establish characteristic-zero existence;
excluding selected special-fiber points or fixed carriers would not
establish nonexistence without an exhaustive reduction. No such
horizontal-component calculation or compatible lifting system is claimed.

For a special pair of torus eigenforms, the
[integral mixed-characteristic trace calculation](MIXED_CHARACTERISTIC_TRACE_OBSTRUCTION.md)
forces \(ab\in J_R^2\), where \(J_R\) measures the coefficients breaking
the symmetry. It imposes a ramification/valuation restriction; its
ramified zero-trace example still has a residual curve. Its stronger
\(W_2\) nonlifting conclusion requires \(p\ge7\), \(v_p(ab)=1\),
generic curvilinearity and the displayed uniform ideal containments. Formal nilpotence alone does not justify the
same trace argument over a nonreduced base.

An actual supported trait supplies more structure. The
[prime-to-\(p\) power-extraction theorem](PRIME_TO_P_POWER_EXTRACTION.md)
recovers a lower-degree equation from a prescribed powered special fiber.
Applied to the known \((p,4n)\) special pairs with \(p\nmid n\), it
excludes supported lifts at **every** ramification index. This is a
theorem about specified points of the full incidence, not a coverage
theorem for arbitrary characteristic-zero pairs.

For the prescribed \((F_p,H_4^n)\) family with \(p\ge7\), the
[Frobenius-power precision theorem](FROBENIUS_POWER_LIFTING_PRECISION.md)
gives exact maximum unramified **strong** precision \(1+v_p(n)\).
The naive powered equations attain that level. The finite-level statement
requires flat complete intersections and the displayed uniform
curve-ideal containments, not merely topological support or field-valued
rank equations. For any still-possible actual supported trait, the theorem
also gives
\[
p\mid n,\qquad \deg G=4n\ge4p,\qquad v_\pi(p)\ge p-1.
\]
Existence or exclusion at those ramification indices remains unresolved.
These are growing bounds for liftability in this specified family; they
are not bounds for arbitrary STCI presentations. The non-eigen
\((16,p)\) source remains outside both extraction results.

There is a further [root-specialization restriction](FROBENIUS_POWER_LIFTING_PRECISION.md#root-specialization-and-the-remaining-endpoint-defects)
at every ramification index. Close the generic multiplicity-\(p\)
root on the lifted degree-\(p\) carrier. Its special fiber must
have a nonzero embedded-point defect over the base \((p,4)\)
complete intersection, supported at the two endpoints of \(C\).
If the defect vanished, flat Cartier extension and hypersurface Picard
rigidity would supply a characteristic-zero quartic mate. This is a
necessary defect condition on a hypothetical actual trait, not a proof
that such a defect or trait exists.

In characteristic zero or odd characteristic, the
[canonical projection section](TAME_PROJECTION_SECTIONS.md) exists away from the pencil's branch points and has pole order at most
\(m-1\), where \(m=ab/4\). The local complete-intersection control
attains that bound in the stated characteristics. A meromorphic section
with a module pole bound need not extend to a regular algebra retraction;
it supplies no automatic global lift or identification with a
normal-filtration defect.

## One binomial equation, with an arbitrary mate

## 3. A broader exact bound: every pair with a binomial equation

**Reviewed proposition.** Let \(k\) be algebraically closed of
characteristic \(p>0\). If \(C_0\) is the sole reduced support of a
degree-\((a,b)\) pair and at least one defining equation is a binomial,
then
\[
p\mid m_C=ab/4,
\qquad ab\ge4p,
\qquad \max(a,b)\ge p.
\tag{3}
\]
The mate may be an arbitrary homogeneous polynomial. No hypothesis of
two binomial equations is imposed.

The carrier reduction used below is classical. In
[Thoma's primary paper, Theorems 2.3 and 2.4](https://www.researchgate.net/publication/303334542_Monomial_space_curves_in_as_binomial_set_theoretic_complete_intersections),
an admissible irreducible binomial carrier of a monomial space curve
must have a pure power of an interior coordinate as one monomial. The
excluded mixed-support types cannot admit a mate in any characteristic.
For the present curve the two possible interior coordinates are exchanged
by \((x_0,x_1,x_2,x_3)\mapsto(x_3,x_2,x_1,x_0)\). The following
coefficient argument extracts a positive-characteristic divisibility
consequence of that reduction; no novelty claim is made.

### 3.1 Reduction of powers and factors

Every irreducible factor of either defining equation must contain
\(C_0\). Otherwise its intersection with the other positive-degree
surface contains a curve outside \(C_0\), or a common surface component.
This is the usual factor reduction, also used in R-0001.

A monomial factor cannot contain \(C_0\). After removing a common
monomial from a binomial and extracting the gcd of its exponent
difference, its factors over an algebraically closed field are primitive
binomials indexed by roots of unity. Exactly the factor of phase one
contains the dense torus of \(C_0\). Consequently a binomial defining
equation in a supported pair is a scalar times
\(F_0^{p^e}\), with \(F_0\) irreducible binomial. In particular
\((F_0,G)\) itself is supported on \(C_0\).

Write \(a_0=\deg F_0\), so \(a=p^e a_0\), and let
\(m_0=a_0b/4\), an integer by degree exhaustion. It suffices to prove
\(p\mid m_0\). Then \(m_C=p^e m_0\) gives (3).

The carrier reduction can also be reconstructed directly. Grade
\(R=k[x_0,x_1,x_2,x_3]/(F_0)\) by weights \((0,1,3,4)\).
It is a domain, and \(\sqrt{(\overline G)}=I_{C_0}/(F_0)\) is
homogeneous for this grading. Every nonzero weight component \(g_i\)
of \(\overline G\) consequently has \(g_i^N=H\overline G\) for
some \(N>0\). In a graded domain the difference between largest and
smallest occurring weights adds under multiplication. The left side
has difference zero; hence \(\overline G\) is weight-homogeneous.
It has a representative of ordinary degree \(b\) and one weight,
obtained from the corresponding weight component of the original \(G\).

If neither monomial of \(F_0\) is a pure power of \(x_1\) or
\(x_2\), both coordinate points \([0:1:0:0]\) and \([0:0:1:0]\)
lie on its carrier and outside \(C_0\). The representative mate must
be nonzero at both. Thus it must contain both \(x_1^b\) and
\(x_2^b\), which have different weights \(b\) and \(3b\).
This is impossible. A pure power of \(x_0\) or \(x_3\) cannot be
a term in a nonzero binomial relation of \(C_0\), because its torus
weight is extremal. This proves the required pure-interior-power
reduction in every characteristic without relying on OCR of the source.

### 3.2 The finite cover and the missing first coefficient

By the carrier reduction and coordinate reversal, write
\[
F_0=x_1^{a_0}-x_0^{n_0}x_2^{n_2}x_3^{n_3},
\qquad n_0+n_2+n_3=a_0,
\qquad 4n_0+n_2=3a_0.
\tag{4}
\]
Primitivity means \(\gcd(a_0,n_0,n_2,n_3)=1\). The two equations in
(4) imply
\[
n_2=3a_0-4n_0,\qquad n_3=3n_0-2a_0,
\qquad \frac{2a_0}{3}\le n_0\le\frac{3a_0}{4}.
\tag{5}
\]
There is no solution at \(a_0=1,2\). Therefore \(a_0\ge3\) and
\(n_0\ge2\).

Consider the finite, basepoint-free morphism
\[
\phi:\mathbf P^2\longrightarrow V(F_0),\quad
[U:V:W]\longmapsto
[U^{a_0}:U^{n_0}V^{n_2}W^{n_3}:V^{a_0}:W^{a_0}].
\tag{6}
\]
Its finiteness follows because the coordinate subring contains
\(U^{a_0},V^{a_0},W^{a_0}\); its image is the integral hypersurface
\(V(F_0)\). The full reduced inverse image of \(C_0\) is the
irreducible plane quartic
\[
B=V^4-UW^3=0.
\tag{7}
\]
Here is a direct check of full inverse support. On \(UW\ne0\), put
\(z=V^4/(UW^3)\). Membership of the image in \(C_0\), applied to its
quartic and cubic toric relations, implies
\(z^{a_0}=z^{n_2}=z^{n_3}=1\). The gcd of these exponents is one,
because it equals \(\gcd(a_0,n_0)\), which is one by primitivity and
(5). Thus \(z=1\) in every characteristic. Conversely, the
parametrization \([U:V:W]=[s^4:st^3:t^4]\) of (7) maps to \(C_0\)
with parameters \((s^{a_0},t^{a_0})\). If \(UW=0\), the relation
\(x_2^4=x_0x_3^3\) forces \(V=0\), which is again in (7).

Since \(G\) cuts out precisely \(C_0\) on the carrier, its pullback
is a homogeneous polynomial with sole reduced zero support (7).
Unique factorization gives
\[
\phi^*G=c(V^4-UW^3)^N,
\qquad a_0b=4N,
\qquad N=m_0>0.
\tag{8}
\]
But \(\phi^*G\) belongs to the subring
\[
k[U^{a_0},\ U^{n_0}V^{n_2}W^{n_3},\ V^{a_0},\ W^{a_0}].
\]
Every monomial in this subring has \(U\)-exponent
\(a_0r_0+n_0r_1\), with \(r_0,r_1\ge0\). Because
\(a_0\ge3\) and \(n_0\ge2\), exponent one is impossible.
The coefficient of \(UV^{4N-4}W^3\) on the right of (8) is
\(-cN\). It must vanish. Thus \(p\mid N\), proving (3).
The last inequality in (3) follows from the stronger divisibility:
\(p\mid ab\) forces \(p\mid a\) or \(p\mid b\).

### 3.3 Exact minimum in this restricted class for large primes

Let \(\delta_{\mathrm{bin}}(p)\) minimize \(\max(a,b)\) over supported
pairs having at least one binomial equation, with arbitrary mate.
Combining (3) with the actual \((4,p)\) pair from Section 2 gives
\[
\boxed{\delta_{\mathrm{bin}}(p)=p\quad\text{for every prime }p\ge7.}
\tag{9}
\]
This is a minimum over all binomial carriers, rather than only the fixed
quartic. It remains a restricted-class statement. The inequality
\(\delta(p)\le\delta_{\mathrm{bin}}(p)\) has the wrong direction to
turn (9) into an unrestricted lower bound.

The [independent arithmetic audit, Sections 5–6](ARITHMETIC_EQUATIONS_AND_JET_GAPS.md#exceptional-prime-minima-with-their-proof)
also proves the exceptional-prime minima and displays a chart-verified
characteristic-five \((3,20)\) pair:

| Prime | Exact minimum \(\delta_{\mathrm{bin}}(p)\) | One attaining pair |
| --- | --- | --- |
| 2 | 4 | \((4,4)\) |
| 3 | 4 | \((4,3)\) |
| 5 | 20 | \((3,20)\) |
| \(p\ge7\) | \(p\) | \((4,p)\) |

For a fixed degree bound \(D\), choosing a prime \(p>D\) therefore
removes the entire one-binomial class from a bounded-degree search.
Any surviving pair of degrees at most \(D\) must use two non-binomial
equations. This is a useful search filter and leaves the class where a
bounded-degree arithmetic route to characteristic zero could occur.

## Why degeneration does not cover every pair

An equivariant degeneration is a possible way to compare these classes,
but contains a precise obstruction. The diagonal torus preserving
\(C_0\) acts on the projective coefficient spaces. An orbit has limits
whose equations are weight-homogeneous. Even if a stronger theorem about
such limiting equations is available, these limits can acquire a common
surface factor. The sole-support rank locus is closed **inside the
proper-pair open subset**, not across that boundary. The full flat-limit
ideal can require more generators than the two displayed limiting forms.
Therefore a torus degeneration does not reduce every supported pair to
a binomial pair unless it also preserves properness or supplies a new
argument retaining the entire flat-limit ideal. This is a missing
implication, not an exclusion theorem.

For candidate searches, a positive-characteristic example of bounded
degrees with two non-binomial equations and \(p\nmid m_C\) would directly
test the proposed all-pairs divisibility target. Such a pair at a single
prime would refute that target at that prime; persistence at infinitely
many distinct primes with one fixed degree bound would produce
characteristic-zero existence by (1). A failed search proves only the
emptiness of the actual family or fixed-degree locus tested.

## A larger source with an actual transverse jet gap

## 1. A specified twenty-three-parameter source

On \(\mathbf P^2_{s:t:z}\), put
\[
\begin{aligned}
 U_0&=s^4+s^2zL_0,&U_1&=s^3t+s^2zL_1,\\
 U_2&=st^3+\alpha z^4+szC_2,&U_3&=t^4+zB_3,
\end{aligned}\tag{1}
\]
where \(\alpha\ne0\), \(L_0,L_1\) are arbitrary linear forms,
\(C_2\) an arbitrary quadratic, and \(B_3\) an arbitrary cubic.
There are \(1+3+3+6+10=23\) scalar parameters. Every system restricts
on \(c=(z=0)\) to literal \(C_0\). This enlarges the inherited
eleven-parameter family by varying both formerly fixed coordinates and
the transverse terms of the third.

Retain basepoint-free systems with **full** reduced inverse support of
\(C_0\) equal to \(c\). Basepoint freeness makes the map finite onto
its integral image because its pullback of \(\mathcal O(1)\) is the
ample \(\mathcal O_{\mathbf P^2}(4)\). Birationality is separate;
when present the image has degree sixteen and the map is its normalization.
The admissible locus of this enlarged source is not classified here, and
a generic member is not asserted admissible.

The family is nonempty: \(L_0=L_1=C_2=0\),
\(\alpha=1,B_3=s^3\) gives the inherited finite birational map
\[
U=(s^4,s^3t,st^3+z^4,t^4+s^3z).\tag{2}
\]
Its full singleton support and degree-sixteen image are recorded in
[R-0017](../results/singleton_plane_conductor_descent.md) and its cited
evidence. Those accepted characteristic-zero proofs are inputs, not
replayed computations. The same literal map works in every characteristic:
on \(s\ne0\) its inverse uses \(t/s=X_1/X_0\) and
\(z/s=X_3/X_0-(X_1/X_0)^4\); on \(s=0\), membership in \(C_0\)
forces \(z=0\). These formulas do not divide by a characteristic.

## 2. Higher jets turn descent failure into degree divisibility

**Jet-gap lemma.** Let \(A\) be a target local ring inside a source
DVR with uniformizer \(r\) and residue field \(E\). Suppose that,
modulo \(r^e\), \(e\ge2\), every element of \(A\) has the form
\(R(w)\), where \(R\in k(W)\) and the residue \(w_0\) is
transcendental over \(k\). Let
\[
q=c+ar+O(r^2),\qquad c\in k^*,\quad a\in E^*.
\]
If \(q^b\in A\), for \(b>0\), then characteristic zero is
impossible; in characteristic \(p>0\), necessarily
\[
\boxed{p^{v_p(b)}\ge e.}\tag{3}
\]

The residue of \(R(w)=q^b\bmod r^e\) is \(c^b\). Injectivity
of \(k(W)\to E\) forces \(R(W)=c^b\), so the whole jet must be
constant. In characteristic zero its coefficient of \(r\) is
\(bc^{b-1}a\ne0\). In characteristic \(p\), write
\(b=p^vn\), \(p\nmid n\). Frobenius gives the first nonconstant
term \(nc^{b-p^v}a^{p^v}r^{p^v}\), with nonzero coefficient. This
proves (3). Localized denominators are allowed: a denominator with nonzero
residue is invertible modulo \(r^e\). Ordinary differentiation detects
only \(p\mid b\); the first surviving Hasse order records the necessary
\(p\)-power.

Apply this at \(D=(s=0)\), using \(z=1\), \(r=s/z,y=t/z\) and
the target frame \(X_2\). Put
\(u=U_2=\alpha+r[y^3+C_2(r,y,1)]\). The coordinates
\(U_0/u,U_1/u\) vanish modulo \(r^2\), while
\[
w=U_3/u,\quad w_0=\frac{y^4+B_3(0,y,1)}\alpha,\quad q=1/u.
\]
The element \(w_0\) is transcendental: its numerator has degree exactly
four in \(y\). The linear coefficient of \(q\) is
\(-\alpha^{-2}[y^3+C_2(0,y,1)]\ne0\), since the quadratic term
has degree at most two. The target local ring at the image line reduces
modulo \(r^2\) to rational functions of \(w\), with the denominator
check in the lemma.

A sole-support mate \(G_b\) pulls back to
\(G_b(U)=\lambda z^{4b}\), \(\lambda\ne0\), by full inverse
support and unique factorization. Division by \(\lambda U_2^b\)
forces \(q^b\) to descend. Every retained member of (1) therefore has
no characteristic-zero mate and, in characteristic \(p>0\), every mate
satisfies
\[
\boxed{p\mid b.}\tag{4}
\]
Neither equation has a binomial hypothesis. On the sublocus
\(L_0=l_0s,L_1=l_1s\), the first two target coordinates vanish
modulo \(r^3\), strengthening (3) to \(p^{v_p(b)}\ge3\), in
particular \(4\mid b\) in characteristic two. For a birational
degree-sixteen image, \(m_C=4b\); thus \(p\mid m_C\) for every odd
prime, and \(\max(16,b)\ge p\).

## 3. A carrier admitting no binomial relation

For (2), set
\[
A=x_0^3x_3-x_1^4,\quad B=x_0^2x_2-x_1^3,\quad
F=A^4-x_0^{13}B.\tag{5}
\]
Its image is the integral degree-sixteen surface \(X=V(F)\), and
\[
A(U)=s^{15}z,\qquad B(U)=s^8z^4.\tag{6}
\]
The polynomial \(F\) is primitive and linear in \(x_2\), with
coefficient \(-x_0^{15}\). Its constant coefficient is not divisible
by \(x_0\), since at \(x_0=0\) it is \(x_1^{16}\). Hence it is
irreducible in every characteristic.

The image lies on **no nonzero homogeneous binomial hypersurface**.
The source polynomials \(st^3+z^4\) and \(t^4+s^3z\) are distinct
irreducibles: each is primitive linear in one variable, with coprime
coefficients in the polynomial ring of the other two. They are not
associates of \(s\) or \(t\). In a relation \(U^a=cU^b\), unique
factorization forces equal exponents of \(U_2,U_3\); the \(t\)-
exponents then force equality for \(U_1\), and the \(s\)-exponents
force equality for \(U_0\). Only the trivial relation remains.

This proves that the carrier itself is genuinely non-binomial. A
binomial containing \(C_0\) need not contain \(X\), so this argument
alone does not exclude binomial mates. The explicit mates below are
proved non-binomial separately.

## 4. Explicit degree-p mates and exact minimum for p at least 43

Let \(p\ge43\) be prime. Set
\[
r\equiv3p\pmod4,\quad0\le r<4,\qquad
n=(3p-r)/4,\qquad E=(p-3r)/4.
\]
Here \(r=1\) or \(3\), and \(E\ge9\). For \(j=4h+\ell\),
\(0\le\ell<4\), define
\[
P_p=x_1^r\sum_{j=0}^{n}(-1)^j\binom nj
x_0^{E+h-3\ell}x_3^{n-j}B^hA^\ell,
\qquad G_p=x_2^p-P_p.\tag{7}
\]
All exponents are nonnegative because \(E+h-3\ell\ge E-9\ge0\).
Each summand has ordinary degree \(p\). The bound \(E\ge9\) holds
for primes \(p\equiv3\pmod4\) at \(p\ge43\), and for
\(p\equiv1\pmod4\) at \(p\ge53\); the only primes from 43 to 52
are 43 and 47. Thus (7) covers every prime at least 43.

In \((k[x]/(F))_{x_0}\), the identities
\(x_1^4=x_0^3x_3-A\) and \(A^4=x_0^{13}B\) give
\[
\frac{x_1^{3p}}{x_0^{2p}}
=\frac{x_1^r(x_0^3x_3-A)^n}{x_0^{2p}}=P_p.\tag{8}
\]
For \(j=4h+\ell\), the exponent of \(x_0\) after replacing
\(A^{4h}\) is \(3(n-j)-2p+13h=E+h-3\ell\), as in (7).
Pullback gives \(P_p(U)=s^pt^{3p}\), initially on \(s\ne0\),
then as a polynomial identity. Frobenius therefore gives
\[
\boxed{G_p(U)=(st^3+z^4)^p-s^pt^{3p}=z^{4p}.}\tag{9}
\]
The form \(G_p\) does not vanish identically on \(X\). The finite
surjective map and full singleton inverse support prove
\[
V(F,G_p)_{\rm red}=C_0,\qquad [V(F,G_p)]=4p[C_0].\tag{10}
\]
Thus the actual pair is proper and has degrees \((16,p)\).

Both equations are non-binomial. Every term of \(P_p\) is divisible
by \(x_1^r\), with \(r>0\), so \(G_p\) has the pure monomial
\(x_2^p\) with coefficient one. If \(G_p\) were a binomial
\(x_2^p-cM\), (9) would force \(cM(U)=s^pt^{3p}\).
Unique factorization forces the \(x_2,x_3\) exponents of \(M\) to
vanish, because \(U_2,U_3\) are irreducibles distinct from \(s,t\).
Writing \(M=x_0^ax_1^b\), its pullback is
\(s^{4a+3b}t^b\). Hence \(b=3p\), impossible for a
degree-\(p\) monomial. Thus \(G_p\)
is not binomial. This is a literal two-non-binomial construction.

Combining (4) and (9), the minimum positive mate degree on this
particular non-binomial carrier is exactly
\[
\boxed{b_{\min}(p)=p\qquad(p\ge43).}\tag{11}
\]
The minimum maximum defining degree in (1), restricted to birational
admissible members, is also exactly \(p\) for \(p\ge43\): (4) is
the lower bound and (2),(7) attain it. This is a restricted-source
minimum, not the unrestricted \(\delta(p)\).

The dependency-free [exact verifier](../computations/stci_arithmetic_beyond_2026_10_29.py)
checks homogeneity, nonnegative exponents and sparse polynomial pullbacks
at \(p=43,47,53,59,61,101\), with every input explicit in the source. Run
`python3 research/computations/stci_arithmetic_beyond_2026_10_29.py`.
These are finite controls; the uniform proof is (8)--(9).

## Full conductor explanation of eventual Frobenius descent

For (2), normalization is an isomorphism off \(D=(s=0)\). Finite
duality identifies its conductor upstairs with
\(\omega_{\mathbf P^2}\otimes\nu^*\omega_X^{-1}\), since \(X\)
is a hypersurface and hence Gorenstein. The finite-duality input is
[Stacks, Lemma 48.11.4](https://stacks.math.columbia.edu/tag/0AX2);
the hypersurface calculation is given in
[de Jong's lecture notes, Lemma 1.2](https://www.math.columbia.edu/~dejong/courses/schemes-spring-2020/lecture-notes-b.pdf).
Locally the conductor identification follows because
\(\operatorname{Hom}_A(B,A)\) consists of multiplication by common-
fraction-field elements carrying \(B\) into \(A\).

Here \(\omega_X=\mathcal O_X(12)\), so the conductor ideal has
class \(\mathcal O(-3-48)=\mathcal O(-51)\). Being invertible and
supported on the single line \(D\), it is exactly
\(\mathcal O(-51D)\). With \(Q=z^4\) and
\(Q-U_2=-st^3\), every Frobenius power \(q=p^e\ge51\) has
\(Q^q-U_2^q\) in the conductor twisted by \(\mathcal O(4q)\).
Hence \(Q^q\) descends to a global section of \(\mathcal O_X(q)\),
which lifts to an ambient degree-\(q\) form by the hypersurface sequence
and \(H^1(\mathbf P^3,\mathcal O(q-16))=0\). This independently
explains how Frobenius removes the nilpotent defect, with the weaker
large-prime threshold 53. Formula (7) supplies threshold 43 without
depending on this duality calculation.

To force unrestricted \(\delta(p)\to\infty\), one still needs an
obstruction for every possible carrier/pair, or a valid reduction to
sources with a gap such as (3). This note proves neither. Arbitrary
normalizations may have nonconstant reduced phases, multiple inverse
branches, or no suitable boundary gap. The concrete advance is a
restricted-source growing lower bound, attained by explicit pairs whose
two equations are non-binomial, and a first surviving Hasse order that
retains the characteristic power invisible to ordinary differentiation.

## Geometric interpretation and exact support

The jet-gap lemma measures the first infinitesimal variation upstairs that the target local ring cannot represent. Ordinary differentiation sees only divisibility by \(p\); the first surviving Hasse order sees the whole \(p^{v_p(b)}\). Conversely, once a Frobenius difference vanishes in the full conductor, it descends. This is a relation between infinitesimal gluing and an actual homogeneous equation, and it persists for a carrier with no nonzero binomial relation.

The [dependency-free sparse verifier](../computations/stci_arithmetic_beyond_2026_10_29.py) checks the literal identity at \(p=43,47,53,59,61,101\), all exponents and ordinary degrees. Independent direct four-variable Macaulay2 substitution at \(43,53\) was recorded in the source audit. The uniform proof is the localization identity followed by Frobenius; no inference across all primes is made from the finite controls. No fresh run was needed to preserve the proof.

[Positive-characteristic constructions](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md) supplies the family-wide rational-quartic theorem and fixed-cubic minima. [The exact binomial-family analysis](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#exact-two-binomial-reduced-support-and-endpoint-contacts) preserves the distinct characteristic-five minimum 25 in its quartic-plus-binomial family. The minimum 20 in the one-binomial class uses a different cubic carrier. A family minimum is never a lower bound for the unrestricted minimum without a coverage theorem.


## Exceptional-prime minima with their proof

## 5. A concrete characteristic-five comparison

The fixed quartic's inherited minimum mate degree is \(25\) in
characteristic five. The inherited cubic-carrier family has a smaller
maximum defining degree there. One explicit member is
\[
\begin{aligned}
F&=x_1^3-x_0^2x_2,\\
G&=x_2^{20}-3x_0x_1x_2^{13}x_3^5
 +3x_0^2x_1^2x_2^6x_3^{10}-x_0^5x_3^{15}.
\end{aligned}
\tag{A8}
\]
Its degrees are \((3,20)\). On \(x_0=1\), \(F=0\) gives
\(x_2=x_1^3\), and direct substitution gives
\[
G(1,u,u^3,v)=(u^4-v)^{15}\quad\text{in characteristic five}.
\]
Thus the affine reduced intersection is exactly
\([1:u:u^3:u^4]\). On \(x_0=0\), \(F=0\) gives
\(x_1=0\), and then \(G=x_2^{20}\); the only projective point
is \([0:0:0:1]\). This proves full projective support equality,
not only generic contact. Its generic thickness is \(15\), in
accord with (A1).

## 6. A sharper small-prime consequence

The same audited argument yields the exact restricted minima
\[
\delta_{\rm bin}(2)=\delta_{\rm bin}(3)=4,
\qquad\delta_{\rm bin}(5)=20.
\tag{A9}
\]
For \(p=2,3\), a smaller maximum would force both degrees at most
three. No degree-one equation contains \(C_0\), an admissible
binomial cannot have degree two by Section 2, and \((3,3)\) has
degree product nine, not divisible by four. The inherited
\((4,4)\) and \((4,3)\) pairs attain four.

For \(p=5\), assume a binomial pair has maximum degree less than
20 and reduce to \(F_0\) as above. If \(n_2=0\), primitivity
forces the fixed quartic \((a_0,n_0,n_3)=(4,3,1)\), whose
inherited minimum mate is 25. If \(n_3=0\), primitivity forces
the cubic \((a_0,n_0,n_2)=(3,2,1)\). The endpoint monomial
\(U^NW^{3N}\) in the pullback identity above, since \(n_2>0\), forces
\(a_0\mid N\) and hence \(4\mid b\); then \(5\mid N\)
forces \(20\mid b\), a contradiction.

In the remaining case \(n_2,n_3>0\), the same endpoint gives
\(4\mid b\), so \(b\in\{4,8,12,16\}\). From \(5\mid a_0b\)
we obtain \(a_0\in\{5,10,15\}\). The interval in the carrier reduction has no
integer solution for \(a_0=5\). For \(a_0=10\), its only
solution is \(n_0=7\). For \(a_0=15\), \(n_0=10\) is
nonprimitive, leaving \(n_0=11\). In both remaining cases
\(v_5(N)=1\). Therefore the coefficient with binomial index five
in the pullback identity above is nonzero: writing \(N=5M\), it is the index-one
coefficient in \((V^{20}-U^5W^{15})^M\), with \(5\nmid M\).
It has \(U\)-exponent five, absent from the image semigroup
\(\langle a_0,n_0\rangle\), whose smallest positive element is
at least seven. This contradiction rules out maximum degree below
20, and the displayed cubic pair attains it.

The only imported input in this small-prime sharpening is the reviewed
[fixed-quartic mate minimum](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#all-mate-degrees-on-a-fixed-cuspidal-quartic)
and its [independent reconstruction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#all-mate-degrees-on-a-fixed-cuspidal-quartic).
The finite arithmetic cases above are proved explicitly, rather than
being presented as an incomplete enumeration.



## Consolidated historical supplement: `research/supplements/Z4_INTRINSIC_ARITHMETIC_MECHANISM.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Embedded primitive towers: gluing, arithmetic variation, and actual pairs

An abstract rational curve or its normal bundle does not determine the obstruction to extending an embedded ribbon. This chapter owns the full primitive-stage extension, the comparison under quadratic gluing changes, the marked divided leading-class theorem, and explicit counterexamples showing why the full neighborhood and integral lift are essential. It then records what an actual supported complete intersection does and does not supply. These are independently reviewed results.

The embedded ribbon-to-triple extension is proved in [higher embedded structures](HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#2026-10-21-intrinsic-embedded-ribbon-triple-obstruction). The exact arithmetic example is [R-0012's nonlifting proof](Z4_LIFTING_AND_DEFORMATION.md). The full extension—not any chosen quadratic summand—has invariant meaning. Standard square-zero derivations and cotangent-complex deformation theory contextualize the construction, but do not identify it with a Frobenius-lifting or Witt-vector obstruction. Abstract primitive-multiple-curve results likewise do not by themselves solve fixed-ambient compatibility over a mixed-characteristic DVR.

## Comparing two marked quadratic neighborhoods

## Statement and source

Work over a base scheme S. Let C have two marked quadratic ambient
neighborhoods A₂ and A₂′ with a common first neighborhood A₁, common
conormal E, and identified square-zero kernels

    0 → B → A₂ → A₁ → 0,       B = Sym²(E),
    0 → B → A₂′ → A₁ → 0.

Here A₂ denotes O_X/I³, A₁ denotes O_X/I², and the action on B
factors through O_C. The neighborhoods come from regular codimension-two
immersions, so multiplication identifies I²/I³ with Sym²(E).
Fix q:E→L, a line quotient with line kernel M.

**Comparison hypothesis:** A₂ and A₂′ are locally isomorphic as
S-algebras by isomorphisms inducing the specified identity on A₁ and B.
This is a hypothesis, not a consequence asserted for arbitrary regular
immersions. All classes below use these markings.

Define the sheaf of O_C-modules

    D₂ = Der_S(A₁,B).

There is a canonical O_C-linear map

    ρ_q:D₂ → Hom(M,L²),
    ρ_q(δ) = (Sym²(q)) ∘ (δ restricted to M).

The local isomorphisms define a difference class
β(A₂′,A₂) in H¹(C,D₂). With the overlap orientation specified in the
proof, the canonical embedded obstruction classes satisfy

    o_(A₂′)(q) − o_(A₂)(q) = H¹(ρ_q)(β(A₂′,A₂)).       (1)

Thus a genuine arithmetic *gluing-defect cocycle*, if independently
constructed in D₂ with the stated compatibility, has a natural comparison
to the Yoneda obstruction. A binomial cross-effect by itself does not
supply β or a map into D₂.

The general square-zero derivation principle is described in the
[Stacks Project, Lemma 91.2.1](https://stacks.math.columbia.edu/tag/08S3).
Formula (1) is proved directly below; it is not quoted from that source.
The target obstruction is the corrected canonical extension of the
[independent intrinsic audit](HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#2026-10-21-intrinsic-embedded-ribbon-triple-obstruction).

## Proof

An automorphism f of A₂ inducing the identity on A₁ and B has
f−id valued in B. Since this difference vanishes on B, it factors uniquely as
δ:A₁→B. Multiplicativity and B²=0 give the Leibniz identity.
Conversely, writing π:A₂→A₁ for the projection, id+δπ is an
automorphism with inverse id−δπ. Composition adds derivations.
This identifies the automorphism sheaf with the additive sheaf D₂.

For e,e′ in the square-zero ideal E of A₁,

    δ(ee′) = e δ(e′) + e′ δ(e) = 0.

For a local section a of O_C, the identity
δ(ae)=aδ(e)+eδ(a)=aδ(e) shows that δ restricted to E is
O_C-linear, independently of a choice of lift of a. Restricting to M
and projecting B to L² defines ρ_q canonically. The same identity
shows this is a morphism of O_C-modules.

Choose local isomorphisms φ_i:A₂′→A₂ on an affine trivializing cover.
Define δ_ij by

    φ_i φ_j⁻¹ = 1 + δ_ij.

The δ_ij are a Čech cocycle since automorphisms add. Replacing φ_i
by (1+ε_i)φ_i changes δ_ij by ε_i−ε_j, so their cohomology
class is independent of the local isomorphisms. We take this orientation
as the definition of β(A₂′,A₂).

Each φ_i induces an isomorphism of the canonical module extensions

    Q = J₂/(I J₂+I³),       0→L²→Q→M→0,

and its counterpart Q′, inducing identity on the end terms. On Q the
automorphism 1+δ_ij acts by adding ρ_q(δ_ij) to a lift of M:
δ kills quadratic terms, and the quotient of B in Q is precisely L².
Choose local splittings s_i of Q→M and transport to Q′ by
t_i=φ_i⁻¹s_i. Then, transporting differences back via φ_i,

    t_j−t_i  corresponds to  (s_j−s_i)+ρ_q(δ_ij).

The two splitting cocycles therefore differ by ρ_q(δ_ij).
The corrected intrinsic audit identifies those splitting cocycles with
the Yoneda classes. This proves (1).

## Coordinate changes, base movement, and arithmetic scope

No normal-coordinate decomposition was used. Isomorphisms of the full
marked data transport A₁, B, D₂, ρ_q, and (1). Derivations in D₂ may
move base functions into B. Restricting them to chosen normal variables
without carrying the full A₁ structure would lose this functoriality.
The comparison fixes A₁; a coordinate change with a first-order base
displacement must first be transported to the common marked A₁.

Over a DVR with uniformizer π, if the difference cocycle is divisible
by π, its leading reduction can be sent through the reduction of ρ_q,
provided the relevant sheaves, cohomology modules, and base-change maps
have the flatness/exactness needed for division. It then computes the
leading *difference* of embedded obstruction classes. A claim about a
persistent cokernel further needs a specified quotient-lift torsor and
its divided variation map D. These conditions are not consequences of
the arithmetic polynomial Δ_(p^r).

This comparison is useful because it names the exact missing datum:
a coordinate-equivariant arithmetic class in the sheaf of quadratic
gluing derivations, rather than an isolated coefficient of a transition.
It does not identify divided Frobenius with that class, and it imposes
no additional condition on arbitrary characteristic-zero STCI pairs.

## Primitive stages and divided leading obstructions

For a regular immersion \(C\hookrightarrow X\), let \(I\) be its ideal,
\(E=I/I^2\), and fix \(q:E\twoheadrightarrow L\) with invertible kernel
\(M\). Put \(J_2=\ker(I\to L)\). The canonical extension is

\[
0\longrightarrow L^2\longrightarrow
Q_2:=J_2/(IJ_2+I^3)\longrightarrow M\longrightarrow0.       \tag{1}
\]

Its Yoneda class is
\(o_X(q)\in H^1(C,M^\vee L^2)\); it vanishes exactly when this fixed
embedded ribbon admits a primitive triple. In particular, \(I/I^3\) must
not be substituted for \(Q_2\) as an allegedly canonical
\(\mathcal O_C\)-module. Multiplication by \(I\) annihilates \(Q_2\),
which makes (1) a literal module extension.

<a id="primitive-stage-hierarchy"></a>

## 2. A primitive-stage hierarchy

**Proved proposal B1.** Let \(C\hookrightarrow X\) be a regular immersion
of codimension two, in any characteristic. Fix an embedded primitive
\(n\)-fold structure \(Z_n\), \(n\ge2\), with ideal \(J_n\), having
local form

\[
I=(z,y),\qquad J_n=(z,y^n).
\]

Its ribbon quotient has conormal line \(L\), with kernel \(M\subset E\).
There is a canonical exact sequence

\[
0\longrightarrow L^n\longrightarrow
Q_n:=J_n/(IJ_n+I^{n+1})\longrightarrow M\longrightarrow0.     \tag{2}
\]

Its splittings correspond precisely to primitive embedded
\((n+1)\)-fold ideals \(J_{n+1}\) with

\[
I^{n+1}\subset J_{n+1}\subset J_n,\qquad
J_{n+1}+I^n=J_n.                                          \tag{3}
\]

The obstruction is

\[
o_n(X,Z_n)=[Q_n]\in
\operatorname{Ext}^1(M,L^n)=H^1(C,M^\vee L^n).               \tag{4}
\]

If it vanishes, the set of compatible global extensions is a torsor under
\(H^0(C,M^\vee L^n)\).

**Proof.** In the displayed local form,

\[
IJ_n+I^{n+1}=(z^2,zy,y^{n+1}),
\]

so \(Q_n\) is freely generated over \(\mathcal O_C\) by the classes
of \(z,y^n\). The map to \(E\) has image \(M\), generated by the
linear class of \(z\), and kernel generated by \(y^n\). The image of
\(I^n\) is this kernel. The induced map from
\(\operatorname{Sym}^n E\) factors through
\(\operatorname{Sym}^n E/(M\operatorname{Sym}^{n-1}E)=L^n\),
and is an isomorphism onto the kernel. This constructs the injection
canonically rather than by a chosen frame.

A local splitting of (2) has image generated by \(z-a y^n\). Its
inverse image in \(J_n\) is

\[
(z-a y^n,y^{n+1}).                                        \tag{5}
\]

It is an ambient ideal since the action on \(Q_n\) factors through
\(\mathcal O_C\); (5) has the required primitive local form and
satisfies (3). Conversely any ideal satisfying the primitive form and
(3) gives such a splitting. Differences of splittings are exactly
\(\mathcal O_C\)-linear maps \(M\to L^n\), so the standard splitting
cocycle is the Yoneda class (4). This proves all assertions.

The construction depends only on \(\mathcal O_X/I^{n+1}\) and the
specified \(J_n\) in that neighborhood. For \(n=2\) it is the
inherited corrected theorem. For \(n>2\) it gives a useful explicit
embedded hierarchy. It does not say that varying all lower structures is
a single linear problem: each torsor is defined **after fixing** \(Z_n\).

The hierarchy is functorial under isomorphisms carrying the whole
embedded data to one another. Flat pullback preserves the constructions;
other base changes require the relevant ideals, products, and exact
sequences to remain compatible. It does not identify cohomology groups
across arbitrary base changes.

## 3. The relative divided leading-class theorem

**Proved proposal B2, with explicit relative hypotheses.** Fix a DVR
\(R\) with a chosen uniformizer \(\pi\) and residue field \(k\).
Fix an integral marked embedded lifting problem and a special quotient
\(\bar q\). Suppose:

1. The admissible lifts modulo \(\pi^2\), including the specified gauge
   normalization, form a nonempty torsor \(P\) under a \(k\)-vector
   space \(T\).
2. The canonical embedded extensions give a relative obstruction bundle
   \(\mathcal H\), locally free over the relevant parameter space.
   Its reductions at all points of \(P\) identify canonically with the
   same \(H=\operatorname{Ext}^1(M_k,L_k^2)\). These identifications
   require the asserted relative cohomology and base-change properties.
3. Each integral obstruction \(o(q)\) reduces to zero modulo \(\pi\).
   Consequently the leading reduction
   \[
   \lambda(q)=\frac{o(q)}\pi\bmod\pi\in H                 \tag{6}
   \]
   is defined using
   \(\pi\mathcal H/\pi^2\mathcal H\simeq\mathcal H/\pi\mathcal H\).
4. The leading section is affine-linear: for one, hence every, base
   point \(q_0\in P\),
   \[
   \lambda(q_0+t)=\lambda(q_0)+D(t)
   \]
   with \(D:T\to H\) \(k\)-linear.

Then \(D\) is independent of \(q_0\), and

\[
\mathfrak o(P):=[\lambda(q_0)]\in\operatorname{coker}D        \tag{7}
\]

is independent of every base-point choice and every compatible integral
trivialization. It is natural under isomorphisms of the marked integral
problem. If \(\mathfrak o(P)\ne0\), no admissible lift in \(P\)
has zero leading obstruction, so no integral primitive triple in the
specified family exists. If the class is zero, the leading obstruction
can be cancelled within this torsor, but higher precision or later
primitive stages may still obstruct.

**Proof.** Freeness makes multiplication by \(\pi\) an isomorphism
\(\mathcal H/\pi\mathcal H\to\pi\mathcal H/\pi^2\mathcal H\),
so (6) is unambiguous in the canonically reduced fiber. A frame change
\(F=F_0+\pi F_1\) changes the leading vector by \(F_0\) only:
\((F\pi v)/\pi\equiv F_0v\pmod\pi\). In particular, changes of
integral kernel frames reducing to the identity have no effect.
Replacing \(q_0\) by \(q_0+t_0\) replaces its leading vector by
\(\lambda(q_0)+D(t_0)\), and
\(\lambda(q_0+t_0+t)-\lambda(q_0+t_0)=D(t)\).
This proves base-point independence and (7). The relative extension
and reduction are functorial; under a compatible change of tangent and
obstruction frames, \(D\) changes by the corresponding source and
target isomorphisms, so its cokernel and (7) transport naturally.
Nonvanishing follows directly from the affine equation.

This proof is elementary once the relative hypotheses are established.
It does not assume that unrelated integral Ext fibers can be compared
before reduction. It also does not infer affine linearity from the word
"obstruction." A smooth first-order lift problem and a regular section
often give affine linearity by the square-zero Taylor rule, but the
admissible parameterization, gauge quotient, and base-change comparison
must still be established in the actual embedded problem.

The relevant \(D\) is the variation of the **divided first-order**
section on the marked congruence torsor. We do not identify it
unqualifiedly with the ordinary differential of the undivided section
on a reduced congruence special fiber. A uniformizer change rescales
(6) by its residue unit; vanishing is preserved, while a numerical
normalization depends on the chosen uniformizer. The formal statement
works with \(\pi\) over a ramified DVR when its hypotheses hold;
division by \(p\) then has a different valuation. The audited quartic
calculation is not thereby extended to all ramified DVRs.

## The missing arithmetic comparison

A sufficient **conditional arithmetic comparison** is now exact. An
arithmetic construction must provide a coordinate-equivariant sheaf
map \(\chi:\mathcal A\to\mathcal D_2\) and a cocycle
\(a\in H^1(C,\mathcal A)\) whose image is the actual gluing
difference \(\beta\). Its image in the embedded obstruction is then
\(H^1(\rho_q\chi)(a)\), by [the marked quadratic-gluing comparison](#comparing-two-marked-quadratic-neighborhoods). If the cocycle is divisible by
\(\pi\), compatible flatness and base change allow leading division;
if B2's affine hypotheses hold, one may then pass to the persistent
cokernel.

The universal polynomial

\[
\Delta_{p^r}(a,b)=\frac{(a+b)^{p^r}-a^{p^r}-b^{p^r}}p
\]

supplies neither \(\chi\) nor the gluing class \(\beta\).
Its additive polynomial cocycle identity is not the descent condition
for the full embedded quadratic neighborhood. No such arithmetic
\(\chi\) has been constructed here for the quartic. This names a
precise missing lemma rather than treating a numerical coefficient as
an operation in deformation theory.

The derivation source has the usual cotangent-complex interpretation
\(\operatorname{Hom}(\mathbb L_{A_1/S},B)\) in degree zero.
This does not identify the embedded group with an arbitrary
Frobenius-lifting or Witt-vector obstruction group. Those deformation
problems require their own source objects and comparison maps.

## 5. Recovery of the quartic class and its persistence

Use the accepted full Laurent coefficients, with the fixed marked
frames of the persistent audit:

\[
\begin{aligned}
C_1&=h(ah+3b^2-5bd+3d^2),\\
C_2&=(b-d)(4ah+3b^2-8bd+6d^2),\\
C_3&=a(ah+9b^2-23bd+15d^2).
\end{aligned}                                             \tag{10}
\]

The full canonical class is represented by
\(C_1[u^{-1}]+C_2[u^{-2}]+C_3[u^{-3}]\) in
\(H^1(\mathbf P^1_R,\mathcal O(-4))\).
At \(a=b=h=0,d=1\), (10) gives exactly

\[
o_X(q_0)=-6[u^{-2}].                                      \tag{11}
\]

Substitute \(a=2\alpha,b=2\beta,h=2\gamma,d=1+2\delta\).
Dividing the full coefficients by two and reducing modulo two gives

\[
\lambda(\alpha,\beta,\gamma)
=\gamma[u^{-1}]+[u^{-2}]+\alpha[u^{-3}],\qquad
D(\alpha,\beta,\gamma)
=\gamma[u^{-1}]+\alpha[u^{-3}].                            \tag{12}
\]

Here \(\delta\) is quotient-frame gauge. The inherited exhaustiveness
and surjectivity proof supplies the full admissible torsor. The image
of \(D\) has dimension two, its kernel is the \(\beta\)-direction,
and the image of \(\lambda\) in its one-dimensional cokernel is
\([u^{-2}]\ne0\). B2 explains exactly the lift independence and
relative functoriality of this cokernel class. This recovers the
known value through the full extension cocycle; it does not construct
a divided-Frobenius preimage of (11).

Coordinate invariance can be tested without isolating a raw summand.
In adapted normal coordinates an embedded triple is
\((x-a(t)y^2,y^3)\). Under an integral change with units
\(\alpha,\delta\) on \(C\),

\[
\begin{aligned}
x'&=\alpha(t)x+C(t)y^2+A(t)xy+B(t)x^2,\\
y'&=\beta(t)x+\delta(t)y+D(t)y^2+E(t)xy+F(t)x^2,
\end{aligned}
\]

its new coefficient is

\[
a'=\frac{\alpha a+C}{\delta^2}\quad\bmod I.               \tag{13}
\]

A base change \(t'=t+e(t)y+f(t)x+O(I^2)\) changes coefficients
only in order \(I\); multiplication by \(y^2\) pushes that effect
to \(I^3\). Formula (13) therefore includes moving-base changes.
For two splittings, \(a'-b'=(\alpha/\delta^2)(a-b)\), exactly
the transition of \(\operatorname{Hom}(M,L^2)\). The complete
cocycle and the relative leading class transport; its individual
coordinate summands need not.

For a nontrivial chartwise nonlinear change of the local splitting
representatives by \(1+u\) and \(v+v^2\), the normalized Laurent
representative changes by

\[
-(1+u)+u^{-4}(u^{-1}+u^{-2}),                               \tag{14}
\]

an integral Čech coboundary in \(\mathcal O(-4)\). Thus the
representative \(-6u^{-2}\) and its leading cokernel class are
unchanged. The new script verifies (13) including nonconstant base
coefficients and moving-base displacement, and (14). This is a check
of the full splitting-cocycle rule, not a fresh re-expansion of the
previously audited ambient rational chart divisions or of the
user-reported Laurent supplement.

## 6. Same conormal, different geometric obstruction

**Counterexample B3.** Work over any field \(k\). On the standard
charts of \(C=\mathbf P^1_k\), glue two copies of \(\mathbf A^2\)
by the triangular polynomial isomorphism

\[
v=u^{-1},\qquad
y_\infty=u^{-6}y_0,\qquad
x_\infty=u^{-8}x_0+c u^{-10}y_0^2.                         \tag{15}
\]

This gives an actual smooth algebraic threefold \(X_c\to C\),
affine over \(C\), with zero section \(C\). The inverse transition
is polynomial in the normal variables over \(k[u,u^{-1}]\).
For every \(c\), the conormal and quotient are identically

\[
E=M\oplus L=\mathcal O(-8)\oplus\mathcal O(-6),\qquad
q(x)=0,\quad q(y)=y.
\]

The ribbon ideal \((x_i,y_i^2)\) glues. In (1) its two local
generators are \(x_i,y_i^2\), and (15) gives normalized extension
cocycle

\[
\frac{c u^{-10}}{u^{-8}}=c u^{-2}.
\]

Since

\[
H^1(\mathbf P^1_k,\mathcal O(-4))
=\frac{k[u,u^{-1}]}{k[u]+u^{-4}k[u^{-1}]},
\]

\(o_{X_c}(q)=c[u^{-2}]\) with the chosen Čech sign. It is nonzero
if \(c\ne0\). For \(c=0\), every ideal \((x_i,y_i^n)\) glues,
so all primitive multiplicities exist compatibly.

Consequently there is no rule depending only on the identified pair
\((E,q)\), or only on functorial symmetric or divided powers of it,
whose value equals the embedded obstruction for every regular
embedding. The two examples have the **same globally split conormal**;
only the split ambient model has the asserted tower. This does not
disprove the existence of zero maps or of a more sophisticated
arithmetic comparison retaining the full neighborhood.

It also makes the distinction between symmetric and divided powers
concrete. The regular-immersion graded algebra is
\(\operatorname{gr}_I\mathcal O_X=\operatorname{Sym}E\).
The functor \(\Gamma(E)\) is determined by the same bundle and is
identical for both models. It does not supply a divided-power
structure on the ambient ideal. The divided-power identity
\(n!\gamma_n(x)=x^n\) is
[Stacks Project, Lemma 23.2.2](https://stacks.math.columbia.edu/tag/07GK).
Over an integral DVR, a nonzero
ordinary normal generator \(x\) in a polynomial algebra cannot
generally satisfy \(p!\gamma_p(x)=x^p\), since \(x^p\) is not
divisible by \(p!\) in that algebra. A divided-power envelope or a
chosen Frobenius lift is additional data, not a consequence of having
a conormal bundle.

## 7. Same special fiber, different divided obstruction

**Counterexample B4.** Over \(R=\mathbf Z_{(p)}\) or
\(\mathbf Z_p\), replace the coefficient in (15) by \(p^h c\),
where \(h\ge1\). Then

\[
o_{X_{p^h c}}(q)=p^h c[u^{-2}]
\in H^1(\mathbf P^1_R,\mathcal O(-4))\simeq R^3.            \tag{16}
\]

All these smooth integral ambients have literally the same split
special fiber, with the same \(C_k,E_k,q_k\) and the same special
neighborhoods of every order. Nevertheless the first nonzero
\(p^h\)-divided obstruction in (16) is \(\bar c[u^{-2}]\);
the split integral lift has zero obstruction. If \(h>1\), division
by \(p\) alone still gives zero modulo \(p\), as it should.

There is an equally explicit persistence statement for \(h=1\).
For the split integral ambient, every quotient \(E\twoheadrightarrow L\)
extends to a compatible primitive tower: the surjection of symmetric
algebras \(\operatorname{Sym}E\to\operatorname{Sym}L\) constructs
the embedded line subbundle, whose zero-section powers give the tower.
Its obstruction section is therefore identically zero. The difference
from this split ambient in (15) is \(p\) times a gluing derivation.
If \(q'=q+p t\) is any admissible first-order quotient lift reducing
to the same special \(q\), both restriction to its kernel and
\(\operatorname{Sym}^2(q')\) have the same reduction as for \(q\).
The [marked quadratic-gluing comparison](#comparing-two-marked-quadratic-neighborhoods) consequently gives

\[
\lambda(q')=\bar c[u^{-2}],\qquad D=0.                     \tag{17}
\]

The compatible special-fiber Ext identification is the one in B2;
here the line bundles on \(\mathbf P^1_R\) have the displayed
free cohomology modules. Thus these integral lifts can have different
persistent cokernel classes even though their entire special
geometries agree. The marked integral lift is an essential argument
of any general comparison theorem, not optional provenance.

## 8. Characteristic \(p\), normal order, and arbitrary failure stages

The inherited arithmetic identity is

\[
v_p\binom{p^r}{j}=r-v_p(j),\qquad
\Delta_{p^r}(a,b)\equiv
\sum_{k=1}^{p-1}\frac{(-1)^{k-1}}k
a^{(p-k)p^{r-1}}b^{kp^{r-1}}\pmod p.                       \tag{18}
\]

If \(a\) is a unit along \(C\) and \(b\) has normal order one,
the least normal order displayed in (18) is \(p^{r-1}\).
If **both** arguments have normal order one, every monomial instead
has total normal order \(p^r\). This distinction must be retained
when applying the polynomial to ambient coordinates.

| \(p,r\) | \(\Delta_{p^r}\bmod p\) | least order if \(a\) is a unit, \(b\) normal |
| --- | --- | --- |
| \(2,1\) | \(ab\) | 1 |
| \(2,2\) | \(a^2b^2\) | 2 |
| \(2,3\) | \(a^4b^4\) | 4 |
| \(3,1\) | \(a^2b+ab^2\) | 1 |
| \(3,2\) | \(a^6b^3+a^3b^6\) | 3 |
| \(5,1\) | \(a^4b+2a^3b^2+2a^2b^3+ab^4\) | 1 |
| \(5,2\) | \(a^{20}b^5+2a^{15}b^{10}+2a^{10}b^{15}+a^5b^{20}\) | 5 |

For example, a particular unit-versus-normal term of degree three
is invisible modulo \(I^3\). That observation does not determine
the first geometric obstruction: other transition terms, quotient
changes, or lower-order compositions may contribute. Even a visible
arithmetic term can project to zero, be a Čech coboundary, or be
cancelled by quotient variation. The split model in B3 has all
primitive powers while every polynomial in (18) is nonzero as a
universal polynomial.

There is a stronger geometric independence. For any \(n\ge2\),
replace (15) by

\[
y_\infty=u^{-6}y_0,\qquad
x_\infty=u^{-8}x_0+c u^{-10}y_0^n.                         \tag{19}
\]

The prescribed structures \((x_i,y_i^j)\) glue for every \(j\le n\).
The stage-\(n\) extension (2) has normalized cocycle

\[
c[u^{-2}]\in H^1(\mathbf P^1_k,\mathcal O(8-6n)),           \tag{20}
\]

which is nonzero for \(c\ne0\), since \(8-6n\le-4\). Equivalently,
a compatible extension would require polynomials
\(b_0\in k[u]\), \(b_\infty\in k[u^{-1}]\) solving

\[
b_0-u^{8-6n}b_\infty=-c u^{-2},
\]

which is impossible by the Laurent quotient. Hence the first failure
of this specified primitive tower can occur at an arbitrary chosen
stage over **every** characteristic. It is not predicted solely by
\(p\) or \(p^r\). This is an actual smooth ambient construction,
not a formal analogy or a generic-point calculation.

At each fixed higher stage (2), a relative analogue of B2 can be
applied if its Ext module is locally free and its divided leading
section is affine on the specified lift torsor. Those hypotheses
are substantive. At higher precision the leading section can be
nonlinear. For the elementary section \(o(q)=4+q^2\) over
\(\mathbf Z_{(2)}\), restrict to \(q=2t\). It is divisible by four,
and

\[
\frac{o(2t)}4\bmod2=1+t^2.
\]

Its ordinary differential is zero, yet it vanishes at \(t=1\).
Quotienting by the image of that differential would incorrectly
declare a persistent nonzero class at \(t=0\). This is a counterexample
to an unrestricted higher-order linear-cokernel recipe, not a claimed
geometric realization of that elementary section. The fixed-stage
torsor theorem remains valid; the family of earlier choices need not
be affine-linear in a higher divided obstruction.

## Relative Ext construction in the marked quartic problem

Let R=Z_(2), C=P1_R, E=I/I², L=O(-6). The space of surjections E→L is the open locus U in the affine R-space Hom(E,L), and its kernel M is a line bundle on C×U. Over C×U the canonical construction
`0→L²→J₂/(IJ₂+I³)→M→0`
defines a relative extension. Its obstruction section belongs to the relative sheaf `H=R¹π_*(M^∨⊗L²)`. The degree of M on every fiber is -8; on P1 over a base, a degree -8 line bundle may differ from O(-8) by pullback of a base line bundle. Thus H is a locally free rank-three bundle, not *a priori* a fixed copy of A=H¹(O(-4)). Cohomology and base change hold here because H⁰(O(-4))=0 and H¹ has constant dimension three. Over the special quotient, H_k canonically identifies with Ext¹(M_k,L_k²), without choosing an integral trivialization.

Restrict to the congruence neighborhood of the fixed special quotient. The already audited integral cocycle proves the relative obstruction is zero modulo 2 and has coefficients divisible by 2 for all integral lifts; the same polynomial identities hold universally over the mod-4 first-order parameter ring. Consequently its reduction modulo 4 belongs to `2H/4H`. Because H is locally free over the unramified base, multiplication by 2 canonically identifies `H/2H` with `2H/4H`. This gives a *leading* section λ over the first-order congruence space. The special-fiber identifications of H are canonical: changing a lift of a frame by 1+2r acts trivially on λ modulo 2. The same observation handles changes of the integral kernel identification. One must not compare integral Ext classes in distinct fibers before this reduction.

The first-order congruence fiber modulo 4 is a torsor under Hom(E_k,L_k); dividing by quotient-frame scalars reducing to 1 gives tangent `T=H⁰(Hom(M_k,L_k))=H⁰(O(2))`. The tangent identification follows from the exact sequence `0→Hom(L_k,L_k)→Hom(E_k,L_k)→Hom(M_k,L_k)→0` on global sections: the connecting obstruction lies in H¹(O)=0. A base point q0 is used to identify the torsor with T. The affine-linear λ has canonical difference map `D:T→H¹(Hom(M_k,L_k²))`; it is independent of q0 because the difference is linear. This is the differential of the *divided first-order obstruction section*, not the ordinary differential of the undivided obstruction at the special point. Its construction is natural for automorphisms of the entire marked integral embedded problem. It is not asserted invariant under arbitrary automorphisms of an unmarked P1.

## Exhaustiveness and surjectivity

The raw conormal transition from the audited main report yields exactly
`p=a+bu+3hu², q=d+2hu, P=3ac²+(3b-4d)c+h, Q=2ac+2b-3d`.
Higher coefficients vanish because the two linear relations have unit determinant. Reduction to the prescribed special quotient gives a,b,h∈2R, d∈1+2R. On the special fiber (p,q)=(0,1), so the quotient is surjective everywhere on C_k. Its cokernel is coherent on the proper R-curve; if nonzero, its closed support would meet the special fiber (properness over the local base), a contradiction. Therefore **every** such integral parameter choice is surjective. This proof does not assume q=d+2hu is a unit in R[u]. The scalar direction δ is gauge, leaving α,β,γ as the three tangent coordinates.


## Serre duality

With the usual residue convention, [u^-1],[u^-2],[u^-3] pair respectively with 1,u,u² in H⁰(O(2)). Hence `V^⊥=k·u=k·st` and the pairing of the persistent class with st is 1. The intrinsic object is the annihilator line of D, not a preferred monomial on an abstract unmarked P1.

## A coordinate summand really changes

Fix the distinguished quotient p=0,q=1,P=-4c,Q=-3, so m_V=-3A+4cB. Along X=0,Y=epsilon the quadratic coefficients are A2=-6u^-10, B2=-3u^-9, and c1=u^-4. The quadratic cocycle decomposition in the original normal coordinates is K_A=18u^-2, K_B=-12u^-2, K_move=-12u^-2, giving total K=-6u^-2.

Make the invertible integral normal-coordinate change A'=A+B, B'=B on V. Then m_V=-3A'+(4c+3)B'. The quadratic coefficient A2'=A2+B2=-6u^-10-3u^-9. Thus K_A'=18u^-2+9u^-1, K_B'=-12u^-2-9u^-1, and K_move'=-12u^-2. The total remains -6u^-2.

The difference [K_A']-[K_A]=9[u^-1] is nonzero in H^1(P1_R,O(-4))=R[u,u^-1]/(R[u]+u^-4 R[u^-1]); it even survives mod 2. Therefore the naive 'first normal coordinate' quadratic contribution does not define an intrinsic cohomology class. This disproves invariance of that decomposition, but does not disprove the existence of a more sophisticated canonical divided-Frobenius-to-obstruction construction.

## A reported Laurent stress test

This calculation was reported independently without a standalone derivation or script; it remains a reported test, not independent proof of the general invariance theorem. Its displayed difference is an explicit coboundary.

For the distinguished conormal quotient, the original Laurent cocycle is
\[
K=-6u^{-2}.
\]
Under the reported nonlinear adapted changes
\[
m_U'=X+(1+u)Y^2,\qquad
m_V'=(-3A+4cB)+(c+c^2)B^2/9,
\]
the re-expanded cocycle is
\[
K'=1+u-6u^{-2}+u^{-5}+u^{-6}.
\]
Consequently,
\[
K'-K=(1+u)+u^{-4}(u^{-1}+u^{-2}),
\]
an explicit Čech coboundary in the stated Laurent trivializations, so the two cocycles represent the same class.

**Verification boundary:** This calculation was reported after the independent audit branch was committed. No standalone calculation script or full derivation was supplied for this supplement. It tests one nontrivial global change, not the general coordinate-invariance theorem, which relies on the relative-Ext construction in the independent audit.


---

## Consequences for actual characteristic-zero pairs

## 1. Exact setup and inputs

Unless a statement specifies otherwise, k is an algebraically closed field of characteristic zero,

\[
C=C_0=\{[s^4:s^3t:st^3:t^4]\}\subset X=\mathbf P^3_k,
\qquad I=I_C.
\]

Let F,G be homogeneous forms of degrees d,e, with no common surface component, and put J=(F,G), Z=V(J). First one may consider only C contained in the reduced intersection; then the fundamental cycle is m[C]+R with R effective and not containing C. The STCI hypothesis used here is the stronger equality Supp(Z)=C, equivalently R=0 together with the asserted set-theoretic support. Exceptional curves above points of C on a blow-up are not additional curves downstairs.

The following are inherited premises, rather than computations repeated in this report.

* [STCI-R-0001](../results/quartic_carrier_exclusion.md), with its accepted lower-degree and factor reduction, gives d,e at least five for any characteristic-zero STCI presentation of this C. Its complete quartic-carrier exclusion is not reopened here.
* The fixed normal bundle is N=O(7) squared, hence E=I/I²=O(-7) squared. The basic generic local intersection and blow-up restrictions are recorded in [the simultaneous-surfaces synthesis](../synthesis/02-two-surfaces.md); the entirely-thick inequalities are not asserted to exclude that branch.
* [STCI-R-0012](../results/prescribed_z4_arithmetic_nonlifting.md) rules out the prescribed flat embedded Z4 lift over exactly Z_(2) and Z_2. It does not exclude arbitrary characteristic-zero STCI presentations or arbitrary ramified bases.
* The [corrected independent ribbon-to-triple audit](HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#2026-10-21-intrinsic-embedded-ribbon-triple-obstruction) constructs, for a line quotient q:E onto L with kernel M, the canonical extension

  \[
  0\longrightarrow L^2\longrightarrow B_q
  :=J_2/(I J_2+I^3)\longrightarrow M\longrightarrow0,
  \qquad J_2=\ker(I\to L).
  \tag{1}
  \]

  Its Yoneda class o_X(q) in H¹(M dual tensor L²) vanishes precisely when the fixed embedded ribbon admits an ambient embedded primitive triple. This is independently audited evidence. The distinction matters: the ambient triple need not be contained in a given Z.
* The [persistent independent audit](#relative-ext-construction-in-the-marked-quartic-problem) proves the fixed marked integral first-order calculation and its precise relative meaning. In particular, every admissible integral quotient reducing to the specified q0 has a middle obstruction coefficient 2 modulo 4. This additional relative conclusion is audited evidence, rather than a broader restatement of R0012.

The [existing literature assessment](#the-missing-arithmetic-comparison) has been consulted. Its distinction between abstract multiple curves and fixed-ambient embedded extension is retained. No claim of priority over the multiple-curve literature is made for the elementary consequences proved here. The reports and the present proofs establish the stated scope; a familiar analogy with abstract extension or divided Frobenius is not being used as a theorem.

## 2. What an actual STCI presentation forces

### 2.1 Complete intersection, purity, and generic length — proved

The two equations have height two. Thus Z is a one-dimensional local complete intersection and is Cohen–Macaulay, Gorenstein, and unmixed. In the STCI situation its only associated support component is C; it has neither a residual curve nor an isolated embedded component.

At the generic point eta of C, the completed transverse regular local ring is K[[u,v]], K=k(C), and

\[
A_\eta=K[[u,v]]/(F,G)
\]

is a zero-dimensional complete intersection of length

\[
m=de/4\in\mathbf Z_{>0}.
\tag{2}
\]

The equality uses the full STCI support condition. With residual curves one only has de=4m+deg(R). If r,s are the normal orders of the displayed equations, m is at least rs; equality holds when their initial binary forms are coprime. Their first symbols need not generate the full initial ideal: (u²,u²+v³)=(u²,v³) is the basic cancellation example.

The maximal ideal of a local Artin algebra of length m has m-th power zero. Since O_Z injects into its localization at the unique generic associated point, this gives, sheaf-theoretically,

\[
I^m\subset J\subset I.
\tag{3}
\]

The injection follows from unmixedness: every function outside the prime of C is a nonzerodivisor. It is not inferred merely from equality of cycles. A larger finite power also suffices for every spreading argument below.

### 2.2 First-normal information and its exact limitations — proved

Write N1=image(J to E). If at least one equation has generic normal order one, N1 has generic rank one and A_eta is curvilinear, isomorphic to K[z]/(z^m). The saturation M of N1 in E is a line subbundle; its quotient L=E/M is invertible. On the smooth curve there is a unique effective divisor D such that

\[
N1=M(-D).
\tag{4}
\]

Here D is the common zero divisor of the *actual two first-normal symbols*, measured in their saturated line. It is not one of the divisors D_i of a saturated quasiprimitive order filtration. In particular it should not be silently substituted into [R0019](../results/quasiprimitive_residual_cycles.md).

If L=O(epsilon-7), then M=O(-7-epsilon), epsilon is nonnegative, and the two symbols are sections of

\[
M(4d)=O(4d-7-epsilon),\qquad
M(4e)=O(4e-7-epsilon).
\tag{5}
\]

One symbol can be zero identically. Where both vanish, both surfaces are singular along C in their normal directions. Saturation extends the generic direction, but does not supply a primitive triple in Z.

If both generic orders are at least two, N1=0; there is no preferred line quotient of E forced by the pair. The higher first relation, horizontal common-direction curve, and full initial ideal then require the additional hypotheses in such results as [R0006](../results/actual_ci_smooth_root_bridge.md). Neither the arithmetic Z4 result nor the construction (1) fills those interfaces.

<a id="defect-twisted-vanishing"></a>

## 3. A new necessary condition: defect-twisted obstruction vanishing

### Proposition A — proved

Let C be a smooth integral curve regularly embedded with codimension two in a smooth threefold, over any field. Let J be an ideal with support C, whose generic transverse algebra is curvilinear of length m at least three. Assume its first-normal image has rank one, and define M,L,D by (4). Set H=M dual tensor L². Then

\[
o_X(q)\longmapsto0
\quad\text{under}\quad
H^1(C,H)\longrightarrow H^1(C,H(D)).
\tag{6}
\]

Equivalently,

\[
o_X(q)\in
\operatorname{im}\bigl[H^0(C,H(D)/H)\longrightarrow H^1(C,H)\bigr].
\tag{7}
\]

Thus the ambient extension may have a nonzero obstruction, but the actual pair supplies a meromorphic splitting with poles bounded by its first-normal defect divisor. This assertion does not claim that the corresponding triple is globally contained in Z.

**Proof.** Since the first symbols of J lie in M, one has J contained in J2. Map J into B_q in (1), and let P be its image. This is an O_C-module: multiplication by I kills B_q. Its image under B_q to M is exactly N1=M(-D).

At eta choose adapted transverse parameters f,y with J_eta=(f,y^m); the existence of f with nonzero linear part follows from generic curvilinearity. For m at least three, y^m maps to zero in B_q because I³ is killed. The image of f spans a line that projects isomorphically to M_eta. Hence P_eta meets L²_eta trivially.

The kernel of P to M is a subsheaf of the line bundle L². It has generic rank zero, so it is zero on the integral curve. Consequently P is isomorphic to N1. Its inclusion in B_q is a lift of N1 to B_q and therefore a splitting of the pullback of (1) along N1 to M. Pullback of extensions induces the map

\[
\operatorname{Ext}^1(M,L^2)\to
\operatorname{Ext}^1(M(-D),L^2)
=H^1(H(D)),
\]

which proves (6). The long exact sequence of 0 to H to H(D) to H(D)/H to 0 proves (7). All images here are sheaf images; no unproved flatness of an ordinary associated graded is used. The proof fails for m=2 because the second generator y² survives in L². End of proof.

For projective C, Serre duality gives the equivalent incidence condition

\[
\langle o_X(q),V\rangle=0
\quad\text{for every}\quad
V\in H^0(C,\omega_C\otimes H^{-1}(-D)).
\tag{8}
\]

This form makes explicit which divisor data would have to be imposed on the actual homogeneous first symbols.

### Concrete corollary for the distinguished q0 — proved, restricted direction

For the fixed quartic and the distinguished marked characteristic-zero quotient q0 from the integral calculation,

\[
L=O(-6),\quad M=O(-8),\quad H=O(-4),\qquad
o_X(q0)=-6[u^{-2}].
\]

If a characteristic-zero STCI pair has generic normal order one and its saturated quotient is this q0, then its divisor D in (4) satisfies

\[
\deg D\ge2.
\tag{9}
\]

If deg D=2, write its defining binary quadratic in the marked coordinates as

\[
Q_D=A s^2+B st+C t^2.
\]

Then a further necessary condition is B=0. For deg D at least three the first obstruction in (6) is automatically killed, so this argument gives no further restriction.

**Proof.** Under the audited Laurent/Serre pairing, [u^-2] is the functional extracting the middle coefficient of a binary quadratic. For D=0 it is nonzero. For D=P a point, H0(O(2)(-P)) is the kernel of evaluation at P. A nonzero functional annihilates this kernel exactly if it is proportional to evaluation at P. The evaluation functionals have coordinates [a²:ab:b²]; none equals [0:1:0] in characteristic zero. Thus degree one cannot work. In degree two, H0(O(2)(-D)) is spanned by Q_D and (8) is exactly B=0, including nonreduced divisors. In degree at least three H¹(O(-4+D))=0. End of proof.

This is a condition on actual surface singularity/common-zero data. It does not assert that any such pair exists, or that the incidence condition suffices to lift all later stages. The q0 label includes the chosen integral embedding and marking; it is not assigned to every quotient of degree -6.

### Size of the unrestricted first obstruction — proved

For any line quotient of E=O(-7) squared with L=O(epsilon-7),

\[
H=M^\vee\otimes L^2=O(3epsilon-7),\qquad
h^1(H)=\max(0,6-3epsilon).
\tag{10}
\]

Therefore the first embedded ribbon-to-triple obstruction vanishes for **every** such quotient when epsilon is at least two. All those ribbons have ambient embedded primitive triples, irrespective of whether a particular STCI scheme contains them. In the accepted order-one range 0 at most epsilon at most 6, only epsilon=0 or 1 can be detected at this first stage.

Even epsilon=1 does not uniformly obstruct. The inherited full cubic coefficient formulas are

\[
\begin{aligned}
C_1&=h(ah+3b^2-5bd+3d^2),\\
C_2&=(b-d)(4ah+3b^2-8bd+6d^2),\\
C_3&=a(ah+9b^2-23bd+15d^2).
\end{aligned}
\tag{11}
\]

The distinguished parameters (a,b,d,h)=(0,0,1,0) give (0,-6,0). By contrast (0,1,1,0) gives (0,0,0). The latter quotient is surjective on both charts: its local pairs are (p,q)=(u,1) and (P,Q)=(-c,-1). Thus there is an actual unobstructed quotient of the same degree. It does not reduce to the prescribed q0 modulo two, so there is no conflict with the marked integral obstruction.

## 4. Exactly when an actual pair supplies a primitive triple

### Proposition B — proved: an all-points sufficient condition

Suppose locally at **every** point of C there is f in J with nonzero linear normal coefficient, and

\[
J\subset(f)+I^3.
\tag{12}
\]

Then J3=J+I³ is a globally defined embedded primitive triple, contained in Z. Its local ideal is (f,y³) for I=(f,y); its ribbon is induced by the first-normal image, and its obstruction (1) vanishes.

Indeed (12) and f in J give J+I³=(f)+I³=(f,y³). These local expressions concern one global ideal J+I³, so no extra gluing choice is being assumed. The condition is pointwise, rather than merely generic.

In particular, if Z is an actual local complete intersection with support exactly C, generic multiplicity m at least three, and its first-normal image is a line subbundle of E **everywhere** (D=0), then it is locally a primitive m-fold structure and Proposition B applies. To prove this, choose f in J generating the first-normal image at a given point. The surface W=(f) is smooth there and C is Cartier on W, say with equation y. The remaining equation has zero support exactly C on W. The regular local ring of W is factorial, so that equation is a unit times y^m. Its exponent is the generic multiplicity. Thus J=(f,y^m), and (12) follows. The same proof works relatively over a DVR for a smooth relative setup with this everywhere rank-one condition and the asserted total support.

Proposition A recovers ambient vanishing when D=0; the local support argument in this paragraph additionally proves containment of the primitive triple in Z.

<a id="generic-primitivity-counterexample"></a>

### Counterexample C — generic primitivity does not globalize

Let C be the line V(x,y) in projective three-space with coordinates [t:x:y:w], and consider the complete intersection

\[
Y=V(x^2,y^2+t x).
\tag{13}
\]

Its support is exactly C. The two *integral* quadrics

\[
F=x^2+y^2+t x,\qquad G=x^2+2y^2+2t x
\tag{14}
\]

generate the same ideal, since 2F-G=x² and G-F=y²+t x. Each has rank three in characteristic zero, hence is irreducible even over the algebraic closure.

On w=1 the algebra is free over k[t] with basis 1,x,y,xy: it is a monic quadratic extension of k[t][x]/(x²). Where t is invertible,

\[
(x^2,y^2+t x)=(x+y^2/t,y^4),
\]

so Y is generically primitive of multiplicity four. At the point t=0, however, its transverse algebra is k[x,y]/(x²,y²). There is no surjection from this algebra to k[z]/(z³). Any such map sends x to az+bz² and y to cz+dz²; squaring forces a=c=0, so the images cannot generate z. A primitive triple inside Y near that point would be finite flat of rank three over the local t-axis and would give exactly this forbidden quotient after setting t=0. Hence no global primitive triple is contained in Y.

There is nevertheless a global embedded ribbon V(x,y²) contained in Y. Its quotient has M=L=O_C(-1), so its *ambient* obstruction lies in H¹(O(-1))=0. The ambient primitive triple V(x,y³) exists, but is not contained in Y: y²+t x maps to y². Thus even an actual induced ribbon and a vanishing ambient Yoneda class do not establish the missing containment implication. The generic triple kernel x+y²/t displays the unavoidable pole.

This example disproves the general implication using a smooth projective support and integral defining surfaces. Its support is a line, not C0. It does not disprove a possible special theorem using extra geometry of C0. Such a theorem must supply that additional argument; generic local complete intersection or generic curvilinearity is insufficient.

For completeness, even generic primitivity itself need not hold for a complete intersection: (u²,v²) in K[[u,v]] has embedding dimension two and no curvilinear length-three quotient by the same argument. Its Gorenstein property does not change this fact.

## 5. Spreading out: what survives, and what does not

### Proposition D — proved: support-preserving finite-type spread

For a characteristic-zero STCI pair of the fixed C there is a finite-type integral Z-algebra A contained in k and forms F_A,G_A of the same degrees such that

\[
I_A^N\subset(F_A,G_A)\subset I_A
\tag{15}
\]

as ideals, for some finite N, and every field fiber has reduced support exactly C. One may arrange that Z_A is a flat relative complete intersection of type (d,e).

**Proof.** Projective support equality gives height two for (F,G). Its homogeneous quotient is Cohen–Macaulay of depth two, so (F,G) is saturated. Hence its homogeneous radical is I_C and some homogeneous power I_C^N lies in (F,G). This explains the passage from sheaf support to homogeneous polynomial identities.

The fixed integral model of C can be given by

\[
\begin{aligned}
q&=x_0x_3-x_1x_2,& f&=x_1^3-x_0^2x_2,\\
h&=x_1^2x_3-x_0x_2^2,& g&=x_2^3-x_1x_3^2.
\end{aligned}
\]

It is the standard relative P¹: on x0 nonzero the chart is A[u] with coordinates (1,u,u³,u⁴), and on x3 nonzero it is the analogous chart A[c]. These charts cover the projective scheme, since x0=x3=0 forces x1=x2=0 at every homogeneous prime.

Choose finite membership identities expressing F,G in this ideal and each monomial generator of its N-th power in (F,G). Adjoin to Z every coefficient in those identities and in F,G. The resulting domain A is finite type, and the identities hold over A and after **every** base change. Thus every field fiber has the prescribed radical. This argument does not assume that tensor product preserves injections.

Every field fiber is then a height-two intersection of the same two positive-degree forms, hence a regular sequence. The fiberwise regular-sequence flatness criterion gives A-flatness of O_Z and the relative regular sequence; see [Stacks, Lemma 10.99.3, tag 00MG](https://stacks.math.columbia.edu/tag/00MG). Alternatively, generic flatness followed by a principal-open shrink suffices, and leaves the identities intact. End of proof.

The fixed Hilbert polynomial is

\[
P_Z(n)=de\,n+de(4-d-e)/2.
\tag{16}
\]

Generically defined conormal quotients can also be spread after enlarging A and shrinking: descend the morphism to O(l) on P¹_A, then remove the proper image of its nonsurjectivity locus. Properness of C_A makes that image closed, and the kernel is then a line bundle. This is an existence statement after localization; it gives no control over which residue characteristics survive. A primitive triple that actually exists over k can similarly be spread, but that does not mean its flat closure is primitive over every originally chosen special point.

Over a general finite-type integral Z-algebra, the locus removed by shrinking is a proper closed locus, **not necessarily finitely many points or rational primes**. In particular, A[1/2] is always another valid spread of the same characteristic-zero data. Therefore no existence theorem for a spread can force a characteristic-two fiber. Nor does a finite-type coefficient ring supply a map to Z_(2) or Z_2: coefficient fields, transcendental parameters, residue fields, and possible ramification all matter.

### Direct reduction to Z4 is numerically impossible for a surviving pair

By R0001 and its accepted lower-degree/factor consequences, d,e are at least five; by (2), four divides de. The smallest possible product is 36, from (6,6), so

\[
m\ge9.
\tag{17}
\]

The prescribed Z4 has degree 16 and generic multiplicity four. A flat complete-intersection family of degrees (d,e) specializing to it must satisfy equality of (16) with 16n-32. This forces de=16 and d+e=8, hence d=e=4. Thus the **whole** intersection scheme of a hypothetical surviving STCI pair cannot specialize flatly to Z4. This degree obstruction is independent of its arithmetic nonlifting.

Extracting a degree-16 intermediate structure would avoid that particular degree mismatch, but requires a global primitive fourth stage, a compatible integral extension of that stage, and the exact marked special fiber. None is forced by an arbitrary STCI. Counterexample C shows why generic primitive stages are not enough.

### Conditional arithmetic corollary — proved under explicit model hypotheses

Suppose a hypothetical characteristic-zero pair admits a model over R=Z_(2) or Z_2, in the fixed relative quartic embedding, such that the total support is C_R, the family is flat, its first-normal image is a line subbundle at every point of C_R, its generic multiplicity is at least three, and its induced quotient reduces to the distinguished q0 of the marked arithmetic problem. Then this model cannot exist.

Indeed Proposition B gives a relative primitive triple. Its canonical extension (1) must split over R. The audited full admissible-quotient calculation gives middle coefficient 2 modulo 4 for every integral quotient reducing to q0, contradicting such a splitting. This rules out a particular kind of *good marked reduction*, for any multiplicity at least three. It does not assert that a hypothetical characteristic-zero STCI must possess such a model. For a total special fiber equal to prescribed Z4, the independently stronger full nonlifting statement is precisely the R0012, with its two-DVR limitation.

Flatness cannot be omitted in descent arguments. Over a DVR, generic containments extend to the total scheme when the target quotients O_Z and O_C are torsionfree, but quotient flatness is what also identifies the base-changed ideal with the actual special-fiber ideal via Tor vanishing. An ideal itself is torsionfree without its quotient being flat: (2x,x²) in Z_2[x] is an elementary counterexample.

## Verification and the unproved bridge

The [general-mechanism verifier](../computations/verify_z4_general_mechanism_2026_10_21.py) retains the full Laurent variation, nonlinear adapted coordinate change, arbitrary-stage local models, binomial order examples and nonlinear divided-section counterexample. The [actual-pair consequences verifier](../computations/verify_z4_stci_consequences_2026_10_21.py) retains the quotient values, Serre-dual incidence, integral-quadric ideal identities and CI Hilbert-polynomial arithmetic. The mathematical proofs carry the uniform and global statements; the finite controls do not replace them. The inherited independent review reconstructed the gluing comparison, defect-twisted vanishing, all-points containment bridge, projective counterexample and spreading argument. Those inherited mechanism and consequence scripts were not rerun during consolidation; the separate raw-frame reconstruction below was executed.

A general arithmetic explanation still requires a coordinate-equivariant source cocycle and a map to the actual gluing derivations that reproduces the embedded difference. An unrestricted STCI application additionally requires actual homogeneous symbols to force an incompatible quotient/defect incidence or a global compatible primitive stage. Neither follows from generic primitivity, the existence of a ribbon, a vanishing ambient obstruction, or spreading out alone. The explicit counterexamples above are mathematical limits on those proposed bridges.


## Raw-frame attribution of the middle Laurent coefficient

This exact decomposition is made only in the prescribed raw integral coordinates. The counterexample above proves that its summands do not define invariant classes. The complete raw-frame calculation was reconstructed exactly and independently reviewed during consolidation. Its individual summands remain coordinate dependent; the total obstruction and its arithmetic nonvanishing are the invariant conclusions.

Let p=a+bu+3hu^2, q=d+2hu; P(c)=3ac^2+(3b-4d)c+h, Q(c)=2ac+2b-3d. Set c0=u^-1, c1=u^-4q-u^-5p, A1=3u^-8p-4u^-7q, B1=2u^-7p-3u^-6q,
A2=-9u^-12p^2+16u^-11pq-6u^-10q^2,
B2=-5u^-11p^2+9u^-10pq-3u^-9q^2.

The quadratic cocycle K=u^8([epsilon^2]m_V+u^-8[epsilon^2]m_U) decomposes as
K_A=u^8 Q(c0) A2,
K_B=-u^8 P(c0) B2,
K_move=u^8 c1(Q'(c0) A1-P'(c0) B1).
Terms involving arbitrary quadratic embedding corrections cancel against the linear kernel transition. These formulas are an **exact equality in the chosen frame**, not an invariant direct sum of cohomology classes.

For the distinguished quotient p=0,q=1,P=-4c,Q=-3:
K_A=18u^-2, K_B=-12u^-2, K_move=-12u^-2;
K=-6u^-2. The -6 in A2 comes directly from binomial(4,2); the other contributions are divisible by four.

For the full admissible quotient family, individual summands can acquire nonzero middle residues that cancel. Their exact middle Laurent coefficients are needed; parity of one factor alone does not show its product vanishes modulo four.

Exact symbolic extraction gives middle Laurent coefficients:
[K_A]_-2 = -88abh+114adh-18b^3+59b^2d-60bd^2+18d^3;
[K_B]_-2 = 82abh-102adh+15b^3-47b^2d+45bd^2-12d^3;
[K_move]_-2 = 10abh-16adh+6b^3-23b^2d+29bd^2-12d^3.
Their sum is C2=(b-d)(4ah+3b^2-8bd+6d^2).
Substitute a=2α,b=2β,h=2γ,d=1+2δ. Modulo four the three middle coefficients are respectively **2,2β,2β**. The latter two cancel in the total, leaving C2=2 modulo four. The earlier raw-frame source attributed residues (2,0,0) to all quotients; that claim was incorrect when β is odd. At the distinguished quotient β=0 the displayed (18,-12,-12) values remain correct. This correction changes the attribution, not the reviewed total cocycle or nonlifting theorem.

This does not construct a natural map from divided-power polynomials to H^1(O(-4)). In particular, a change of raw normal coordinates changes the allocation among K_A, K_B and K_move. The total class is intrinsic for the fixed quotient, but the decomposition is not proved invariant.


The source cited a verifier that is absent from the covered snapshots. Its necessary support is replaced by [the exact Laurent reconstruction](../computations/verify_z4_raw_source_decomposition.py), which derives all three middle polynomials from the displayed raw-frame definitions, checks their sum against C2, and performs the formal parameter substitution modulo four. It was executed successfully during consolidation. This fixed-frame identity does not assert invariance of individual pieces.

