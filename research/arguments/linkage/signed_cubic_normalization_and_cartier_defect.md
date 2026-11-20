# Signed cubic normalization and intrinsic Cartier defect

Work over an algebraically closed field \(k\) of characteristic different
from two, unless a consequence explicitly requires characteristic zero. Fix

\[
X=V(z^2-2x_1x_2+x_0x_3)\subset\mathbf P^4,
\qquad
D=[s^4:s^3t:s^2t^2:st^3:t^4],
\]

where the coordinate order is \((x_0,x_1,z,x_2,x_3)\). Write
\(H=\mathcal O_X(1)\), also for its restrictions and pullbacks.

**Conclusions.** The only cubic section of \(X\) singular generically along
\(D\), up to scalar, is

\[
H_{\rm sec}=2x_0x_3z-x_0x_2^2-x_1^2x_3.
\]

Its integral surface has finite normalization \(\mathbb F_2\), on which
the full reduced inverse of \(D\) is two sections of class \(E+2f\), whereas
the hyperplane class is \(E+4f\). Consequently **no positive-degree section
can cut that surface properly with sole reduced support \(D\)**. In the
fixed quadratic-cover one-lift sextic setting this removes the
generic-singularity alternative, in every mate degree.

For an integral signed degree-\(m\) surface generically regular along
\(D\), an actual proper sole-support mate forces the common conormal-zero
length to satisfy, without normality,

\[
g\ge 4m-10+\lceil8/m\rceil.
\]

For \(m=3\), the complete necessary list is \(g\in\{5,6,8\}\), with exact
intrinsic defect \(g-14/3\in\{1/3,4/3,10/3\}\). Some local principal
symbolic index is divisible by three. These are necessary conditions
without an ADE or crepancy hypothesis; in characteristic zero they restrict,
but do not exclude, all generically regular one-lift survivors, including
nonnormal hits.

## The unique sheaf-square cubic

The precise source space is
\(H^0(X,\mathcal I_D^2(3))\), with the **ideal sheaf square**. The ordinary
homogeneous ideal of the rational normal quartic has no linear elements,
so its unsaturated ordinary square has no cubic elements.

On \(x_0\ne0\), put

\[
t=x_1/x_0,\qquad u=z/x_0-t^2,\qquad v=x_2/x_0-t^3.
\]

Then
\(x_3/x_0=t^4+2tv-2t^2u-u^2\). Degree-three sections have the thirty
normal-form monomials \(z^\epsilon x_0^{e_0}\cdots x_3^{e_3}\), where
\(\epsilon\in\{0,1\}\) and \(\sum e_i+\epsilon=3\), as a basis. For
weight \(w=e_1+3e_2+4e_3+2\epsilon\), their first jets are

\[
t^w+(\epsilon-2e_3)t^{w-2}u+(e_2+2e_3)t^{w-3}v.
\]

Negative exponents in this display have zero coefficient whenever needed.
Different weights give independent coefficient equations. The ranks of
the three-row blocks with columns
\((1,\epsilon-2e_3,e_2+2e_3)\) are as follows; the formula specifies every
column. For an exact integral certificate, order each block's columns by
descending lexicographic \((e_0,e_1,e_2,e_3,\epsilon)\), and number rows
\((1,u,v)\). The final row gives one maximal minor in that order.

| Weight \(w\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number of columns | 1 | 1 | 2 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 2 | 1 | 1 |
| Rank | 1 | 1 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 1 |
| Certified maximal minor | 1 | 1 | \(-1\) | \(-1\) | \(-1\) | \(-1\) | 1 | \(-1\) | 1 | \(-1\) | \(-1\) | 1 | 1 |

For one-column blocks take row 1; for two-column blocks take rows 1,2.
For three-column blocks take all rows and columns. At weight six take all
rows and columns 1,2,4. These minors are units over \(\mathbf Z\), hence
over \(\mathbf Z[1/2]\) and every residue field of odd characteristic.
The ranks and the rank-29 total therefore require no sampled-prime test.

At weight six, order the monomials as
\((x_1^2x_3,x_0x_2^2,zx_1x_2,zx_0x_3)\). Their columns are

\[
(1,-2,2),\quad(1,0,2),\quad(1,1,1),\quad(1,-1,2),
\]

with kernel \((-1,-1,0,2)\). Hence

\[
H^0(X,\mathcal I_D^2(3))=k\,H_{\rm sec}.
\]

Indeed zero restriction and zero first normal jet on the dense chart imply
zero global restriction and conormal section on the smooth curve \(D\).
Since \(D\subset X\) is a regular embedding, this is exactly membership in
the sheaf square, including both omitted endpoints. Conversely a section
vanishing on \(D\) whose surface is singular at the generic point of \(D\)
has zero first normal jet there and therefore everywhere. Thus the rank
calculation covers every generically singular cubic through \(D\).

## Finite normalization and full inverse support

Choose \(\kappa\in k\) with \(\kappa^2=-1\), and put

\[
p(s,t)=(s^4,s^3t,s^2t^2,st^3,t^4),\qquad
d(s,t)=\frac{p(s,\kappa t)-p(s,t)}{st}
       =(0,(\kappa-1)s^2,-2st,-(\kappa+1)t^2,0).
\]

Characteristic different from two ensures \(\kappa\ne\pm1\) and
\(2\kappa\ne0\), the only characteristic restrictions in this construction.

The columns \(p,d\) are independent at every base point: away from the
endpoints \(p\) has nonzero first and last coordinates while \(d\) has both
zero; at \(t=0\), respectively \(s=0\), their nonzero coordinates include
\((x_0,x_1)\), respectively \((x_3,x_2)\). They define a morphism

\[
\nu:T=\mathbf P_{\rm quot}
       (\mathcal O_{\mathbf P^1}(4)\oplus\mathcal O_{\mathbf P^1}(2))
       \longrightarrow\mathbf P^4,
\]

whose fiber line is spanned by \(p,d\), and
\(\nu^*\mathcal O(1)=\mathcal O_T(1)\). This uses the subbundle with columns
\(p,d\) in the trivial rank-five bundle, or equivalently its dual quotient.
The surface \(T\) is \(\mathbb F_2\). With \(E^2=-2\), \(E\cdot f=1\),
its tautological class is \(H_T=E+4f\), ample, with \(H_T^2=6\).
Thus \(\nu\) is finite onto its image: a positive-dimensional fiber would
contain a curve of hyperplane degree zero.

For \(st\ne0\) these are the chords joining \(p(s,t)\) and
\(p(s,\kappa t)\). Direct substitution puts each chord on \(X\).
It also lies on the rational-normal-quartic chordal cubic

\[
\det\begin{pmatrix}x_0&x_1&z\\x_1&z&x_2\\z&x_2&x_3\end{pmatrix}
=H_{\rm sec}-z(z^2-2x_1x_2+x_0x_3).
\]

The same holds on the limiting fibers by closure. On \(x_0=1\), write the
base parameter as \(\tau\) and a fiber point as \(p(1,\tau)+a d(1,\tau)\).
The rational inverse recovers the base by

\[
\tau=\frac{x_2-zx_1}{(1+\kappa)(z-x_1^2)}.
\]

The denominator equals \((1+\kappa)2\kappa a(a-\tau)\), so is nonzero on
a dense open; the fiber coefficient is then recovered from \(x_1\).
Thus \(\nu\) is birational onto its image. The image has degree six, equal
to the degree of the complete intersection
\(S=X\cap V(H_{\rm sec})\). Consequently it is all of \(S\), with generic
multiplicity one. The hypersurface section of the smooth threefold is
Cohen–Macaulay and has no embedded components, so \(S\) is integral.
The finite birational map from smooth \(T\) is its normalization.

There are two sections \(A,B\subset T\), mapping respectively by
\(p(s,t)\) and \(p(s,\kappa t)=p(s,t)+st\,d(s,t)\). Each maps
isomorphically to \(D\), has \(H_T\)-degree four, and therefore has class
\(E+2f\). They meet only over \(st=0\); their fiber coordinates differ
by the simple base factor \(st\), so each endpoint intersection has
length one.

These sections exhaust the **full reduced inverse** of \(D\). On a
nonendpoint chord, any three distinct points of a rational normal quartic
are linearly independent, so its only intersections with \(D\) are its
two defining points. The endpoint fiber at \(t=0\) is the tangent line
\(\langle x_0,x_1\rangle\), which meets \(D\) only at \(p(1,0)\);
the fiber at \(s=0\) is \(\langle x_2,x_3\rangle\), meeting it only at
\(p(0,1)\). The two sections coincide at the appropriate point in each
of these fibers. There is no additional inverse point at either endpoint
and no fiber contained in the inverse support.

If a nonzero degree-\(b\) section on \(S\), \(b>0\), had zero scheme with
sole reduced support \(D\), its pullback would be an effective Cartier
divisor supported exactly on \(A\cup B\). For positive integers
\(\lambda,\mu\), its class would give

\[
b(E+4f)=(\lambda+\mu)(E+2f).
\]

The coefficients of \(E\) and \(f\) imply
\(b=\lambda+\mu\) and \(4b=2(\lambda+\mu)\), impossible for \(b>0\).
This proves the all-mate exclusion on \(S\).

## The Cartier-defect restriction in signed degree \(m\)

Let \(S_m\subset X\) be an integral degree-\(m\) hypersurface section
containing \(D\), regular at its generic point. Suppose an actual nonzero
degree-\(b\) section cuts \(S_m\) properly with sole reduced support \(D\).
Let \(\lambda\) be its generic order along \(D\). The intersection cycle
has degree \(2mb\), so

\[
4\lambda=2mb,\qquad \lambda=mb/2.
\]

The surface is Cohen–Macaulay as a hypersurface section of smooth \(X\).
At a closed point \(p\in D\), put \(R=\mathcal O_{S_m,p}\), \(P=I_{D,p}\), and

\[
J_i=R\cap P^iR_P\quad(i\ge0).
\]

The local ring \(R_P\) is a DVR, and \(R/P\) is the regular local ring
of the smooth curve \(D\). These coherent symbolic ideals glue near \(D\).
Each \(E_i=J_i/J_{i+1}\) is killed by \(P\), has rank one over \(R/P\),
and is torsion-free: multiplication by an element outside \(P\) does not
change its DVR order. Hence the \(E_i\) are line bundles on \(D\).
In particular \(L=E_1\) is the torsion-free conormal quotient, since
\(P^2\subset J_2\) and equality holds after localization at \(P\).

Let \(f\in R\) be a local mate equation. Since \(R\) is a domain,
\(f\) is a nonzerodivisor. The quotient \(R/(f)\) is Cohen–Macaulay of
dimension one and has sole minimal prime \(P\), hence no embedded primes.
Thus \((f)\) is \(P\)-primary. These purity inputs are
[Stacks, Lemmas 10.103.5 and 10.103.7](https://stacks.math.columbia.edu/tag/00N2).
Contraction from the DVR gives

\[
(f)=J_\lambda,\qquad J_{\lambda+i}=fJ_i\quad(i\ge0).
\]

For the second equality, an element of \(J_{\lambda+i}\subset(f)\)
is \(fa\) with \(a\in R\), and its DVR order forces \(a\in J_i\).
The local equations glue as the image of \(\mathcal O_{S_m}(-bH)\), so

\[
E_\lambda=J_\lambda/J_{\lambda+1}
\simeq\mathcal O_D(-bH).
\]

The signed-surface [conormal transition](one_lift_sextic_conormal_exclusion.md#one-lift-sextics-the-conormal-zero-budget),
whose displayed coordinate identities hold in every characteristic other
than two, gives
\(N^*_{D/X}=\mathcal O_D(-4)\oplus\mathcal O_D(-6)\), with degrees on
\(D\simeq\mathbf P^1\). The defining equation induces a generically nonzero
map

\[
\mathcal O_D(-4m)\longrightarrow
\mathcal O_D(-4)\oplus\mathcal O_D(-6).
\]

Let \(g\) be the length of its common-zero divisor, with multiplicities.
Saturating the image gives torsion-free quotient \(L\), and therefore
\(\deg L=4m-10-g\). Multiplication induces generically nonzero maps
\(L^{\otimes i}\to E_i\). At \(i=\lambda\), the effective zero divisor
has degree \(-4b-\lambda\deg L\ge0\). Consequently

\[
\deg L\le-\frac{4b}{\lambda}=-\frac8m,
\qquad
\boxed{g\ge4m-10+\lceil8/m\rceil}.
\]

This extends the [divisorial-conormal argument](../carriers/quintic_conormal_and_factor_geometry.md#the-conormal-defect-of-a-marked-cartier-multiple)
to the possibly nonnormal surface using symbolic layers and the actual mate.
When the surface is normal near \(D\), \(4b/\lambda=D^2\); that divisor
interpretation is unnecessary for the inequality.

For the exact local defect, let \(\rho_p\) be the least positive index for
which \(J_{\rho_p}\) is principal; it exists because \(J_\lambda=(f)\).
If \(J_r=(h)\), the same contraction argument gives
\(J_{r+i}=hJ_i\). Write \(\lambda=q\rho_p+r\), with
\(0\le r<\rho_p\). Then \(J_\lambda=h^qJ_r\) is principal, forcing
\(J_r\) principal by cancellation in the domain. Minimality gives \(r=0\),
so \(\rho_p\mid\lambda\).

Lift a local basis of \(L\) to \(u\in J_1=P\), let \(h\) generate
\(J_{\rho_p}\), and define

\[
\delta_p=\operatorname{ord}_p\bigl((u^{\rho_p}/h)|_D\bigr)\ge0.
\]

The ratio belongs to \(R\) and is generically nonzero on \(D\). A change
of lift adds an element of \(J_2\), so changes \(u^{\rho_p}\) by an element
of \(J_{\rho_p+1}=hP\). Changes of bases multiply its restriction by a
unit. Thus \(\delta_p\) is well-defined. It is zero exactly when \(D\)
is Cartier at \(p\). Indeed a unit ratio gives
\(J_{\rho_p}=(u^{\rho_p})\), hence \(\sqrt{(u)}=P\).
Cohen–Macaulay purity for \(R/(u)\) makes \((u)\) \(P\)-primary;
its generic order is one, so contraction gives \((u)=P\).
Conversely if \(P\) is principal its symbolic powers are ordinary powers,
\(\rho_p=1\), and \(\delta_p=0\).

The zero order of \(L^{\otimes\lambda}\to E_\lambda\) at \(p\) is
\((\lambda/\rho_p)\delta_p\). Summing gives the exact identity

\[
\boxed{\sum_{p\in D}\frac{\delta_p}{\rho_p}
=-\frac{4b}{\lambda}-\deg L
=g-4m+10-\frac8m}.
\]

For a signed cubic, \(\deg L=2-g\), so \(g\ge5\) and the defect is
\(g-14/3\). Its derivative components have degrees eight and six and are
not both zero. A nonzero degree-six component gives \(g\le6\); if that
component vanishes identically, the nonzero degree-eight component gives
\(g=8\). Thus the complete necessary list is

\[
\boxed{g\in\{5,6,8\}},\qquad
\boxed{\sum_p\delta_p/\rho_p\in\{1/3,4/3,10/3\}}.
\]

In every case some \(\rho_p\) is divisible by three: otherwise a common
denominator of the finitely many nonzero summands would be prime to three.
In particular \(D\) is non-Cartier somewhere. These are necessary strata,
not assertions that any of them is realized by a sole-support mate.

## Hypotheses, implications and remaining scope

The cubic uniqueness and normalization use this fixed smooth quadric and
its rational normal quartic in every characteristic other than two. The
integral maximal minors prove the jet ranks uniformly, and the explicit
rational inverse proves birationality without a separability assumption.
The normalization argument excludes
all sections of positive degree with sole support \(D\), stronger than
requiring a downstairs mate. In the [one-lift split setting](split_carrier_norm_and_conductor.md#split-carrier-the-conductor-is-an-actual-complete-intersection),
an actual downstairs mate induces exactly such a section, so this closes the
generically singular signed-cubic alternative there. Combined with the
[smooth/Du Val closure](one_lift_sextic_conormal_exclusion.md#the-same-length-budget-controls-all-du-val-types)
**in characteristic zero**, the surviving fixed-cover one-lift sextic sector
is generically regular along \(D\) and has non-Du-Val behavior somewhere on
\(D\). No positive-characteristic extension of the Du Val/K3 exclusion is
asserted.

The intrinsic defect restriction applies in every characteristic other than
two to every generically regular signed degree-\(m\) surface with an actual
proper sole-support mate. Its local algebra needs only an integral
Cohen–Macaulay surface, smooth \(D\), a DVR at its generic point, and that
mate; no normality or characteristic restriction enters the symbolic-layer
proof. The fixed conormal splitting and polarization supply the displayed
numbers. Generic regularity supplies the nonzero conormal map and DVR;
Cohen–Macaulay purity identifies the mate ideal with its symbolic order;
actual sole support supplies that primary ideal and the global mate layer.
No special endpoint monomial condition of a one-lift norm enters this
numerical argument.

The intrinsic defect sum is distinct from the exceptional-curve correction
\(14/3\) in a characteristic-zero crepant cubic resolution: the latter
includes the strict transform square, whereas the former measures the
failure of powers of the symbolic conormal line to generate the mate layer.
Their shared
conormal-zero source explains the comparison, but does not identify the two
invariants. The restriction fixes a short list of total intrinsic defects;
it does not classify the local models or their individual symbolic indices,
or prove that a listed stratum admits a mate. Nonnormal closed points on
\(D\) are included provided the surface is regular at the generic point
of \(D\); generic singularity is handled separately only for this fixed cubic.
Neither conclusion gives a general
sextic exclusion, closes generic singularity for arbitrary covers or higher
signed degrees, or decides unrestricted STCI.

## Independent review

The integrated proof was independently reconstructed on 2026-11-20:
all thirty jet columns and the thirteen unit maximal minors, the finite
birational ruled-surface map and its full endpoint inverse, and the
Cohen–Macaulay symbolic-layer argument without normality. The review
checks principal-power periodicity, the least principal index, lift
independence of the defect, zero defect exactly at Cartier points, and
the complete cubic defect list. The fixed-cover cubic conclusions hold
in characteristic different from two; the separate Du Val/K3 closure
remains characteristic zero. No remaining non-Du-Val stratum or arbitrary
cover is excluded by this proof.
