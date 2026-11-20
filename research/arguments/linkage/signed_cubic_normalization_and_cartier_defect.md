# Signed cubic normalization and intrinsic Cartier defect

Work over an algebraically closed field \(k\) of characteristic zero. Fix

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

For an integral signed degree-\(m\) surface normal near \(D\) and generically
regular along it, a proper sole-support mate forces the common conormal-zero
length to satisfy

\[
g\ge 4m-10+\lceil8/m\rceil.
\]

For \(m=3\), this says \(g\ge5\), with exact intrinsic Cartier defect
\(g-14/3\). This is a necessary condition without an ADE or crepancy
hypothesis, not an exclusion of the remaining non-Du-Val sector.

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
column, so the table is also a small exact rank certificate.

| Weight \(w\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number of columns | 1 | 1 | 2 | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 2 | 1 | 1 |
| Rank over \(\mathbf Q\) | 1 | 1 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 1 |

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
containing \(D\), normal on a neighborhood of \(D\) and regular at its
generic point. Suppose a nonzero degree-\(b\) section cuts \(S_m\) properly
with sole reduced support \(D\). Its Cartier divisor is
\(\lambda D\sim bH\); intersecting with \(H\) gives

\[
4\lambda=2mb,\qquad \lambda=mb/2,\qquad D^2=4b/\lambda=8/m.
\]

Only normality near \(D\) is needed for these rational Cartier intersections
and the divisorial ideals below. A separate global normality hypothesis is
unnecessary. The signed-surface [conormal transition](one_lift_sextic_conormal_exclusion.md#one-lift-sextics-the-conormal-zero-budget)
gives \(N^*_{D/X}=\mathcal O_D(-4)\oplus\mathcal O_D(-6)\), with degrees
on \(D\simeq\mathbf P^1\). Thus the defining equation induces

\[
\mathcal O_D(-4m)\longrightarrow
\mathcal O_D(-4)\oplus\mathcal O_D(-6).
\]

It is generically nonzero by generic regularity. Let \(g\) be the length
of its common-zero divisor, with multiplicities, and saturate its image.
The resulting torsion-free rank-one quotient is a line bundle \(L\), of
degree

\[
\deg L=(-4-6)-(-4m+g)=4m-10-g.
\]

Intrinsically, put \(J_i=\mathcal O_{S_m}(-iD)\) on the normal neighborhood.
The quotient \(J_1/J_2\) is exactly \(L\): it is the torsion-free quotient
of \(I_{D/S_m}/I_{D/S_m}^2\), since ordinary and divisorial second powers
agree at the generic DVR. The [divisorial-conormal lemma](../carriers/quintic_conormal_and_factor_geometry.md#the-conormal-defect-of-a-marked-cartier-multiple)
applies directly, independently of its original quintic ambient geometry.
For clarity, multiplication gives generically nonzero maps
\(L^{\otimes i}\to J_i/J_{i+1}\) of line bundles on \(D\), and

\[
J_\lambda/J_{\lambda+1}
 \simeq\mathcal O_D(-\lambda D)
 \simeq\mathcal O_D(-bH).
\]

The effective zero divisor of the multiplication map at \(i=\lambda\)
therefore has degree \(-4b-\lambda\deg L\ge0\). Consequently

\[
\deg L\le-D^2=-8/m,
\qquad
\boxed{g\ge4m-10+\lceil8/m\rceil}.
\]

More precisely, at each \(p\in D\) let \(\rho_p\) be the local Cartier
index of \(D\), dividing \(\lambda\), and let \(h\) generate
\(J_{\rho_p}\). Lift a local basis of \(L\) to \(u\in J_1\), and define
\(\delta_p\) to be the vanishing order on \(D\) of \(u^{\rho_p}/h\).
This is a nonnegative integer, independent of these choices. Its normalized
value contributes to the exact identity

\[
\sum_{p\in D}\frac{\delta_p}{\rho_p}
=-D^2-\deg L
=g-4m+10-\frac8m.
\]

Indeed at the global multiple \(\lambda\), the local multiplication zero
has order \((\lambda/\rho_p)\delta_p\). A contribution is zero exactly
when \(D\) is Cartier at \(p\): a unit ratio makes \(u^{\rho_p}\) generate
\(J_{\rho_p}\), hence \(\operatorname{div}(u)=D\) locally. No resolution,
Gorenstein condition or ADE classification is used.

For a signed cubic, \(\deg L=2-g\), so

\[
g\ge5,\qquad
\sum_p\delta_p/\rho_p=g-14/3.
\]

If its degree-six derivative component is nonzero, then \(g\le6\), hence
\(g\in\{5,6\}\); the respective total intrinsic defects are \(1/3\)
and \(4/3\). In particular \(D\) must be non-Cartier somewhere in this
normal sector.

## Hypotheses, implications and remaining scope

The cubic uniqueness and normalization use this fixed smooth quadric and
its rational normal quartic, with characteristic zero ensuring the displayed
ranks and separable chord parameters. The normalization argument excludes
all sections of positive degree with sole support \(D\), stronger than
requiring a downstairs mate. In the [one-lift split setting](split_carrier_norm_and_conductor.md#split-carrier-the-conductor-is-an-actual-complete-intersection),
an actual downstairs mate induces exactly such a section, so this closes the
generically singular signed-cubic alternative there. Combined with the
[smooth/Du Val closure](one_lift_sextic_conormal_exclusion.md#the-same-length-budget-controls-all-du-val-types),
the surviving fixed-cover one-lift sextic sector is generically regular along
\(D\) and has non-Du-Val behavior somewhere on \(D\).

The Cartier-defect restriction adds intrinsic information in the part of
that sector normal near \(D\). Normality supplies divisorial orders and
local Cartier indices; generic regularity supplies the nonzero conormal map;
the actual mate supplies the Cartier multiple and its rational square.
The numerical lemma itself uses none of the special endpoint monomial
conditions of a one-lift norm. Its generality is every signed degree-\(m\)
surface with the stated embedding and Cartier multiple.

The intrinsic defect sum is distinct from the exceptional-curve correction
\(14/3\) in a crepant cubic resolution: the latter includes the strict
transform square, whereas the former measures the failure of powers of the
divisorial conormal line to generate the Cartier layer. Their shared
conormal-zero source explains the comparison, but does not identify the two
invariants. The restriction alone bounds neither all non-Du-Val local
models nor their possible intrinsic defects. Nonnormal points along \(D\)
remain outside this second argument. Neither conclusion gives a general
sextic exclusion, closes generic singularity for arbitrary covers or higher
signed degrees, or decides unrestricted STCI.

## Independent review

The integrated proof was independently reconstructed on 2026-11-20,
including all thirty rational jet columns and their rank-29 matrix,
the finite birational ruled-surface map, its full endpoint inverse,
and the divisorial-power saturation and Cartier-layer multiplication.
The review confirms the stated fixed-cover and normal-near-\(D\) scopes;
it does not extend the result to other covers or exclude the remaining
non-Du-Val models.
