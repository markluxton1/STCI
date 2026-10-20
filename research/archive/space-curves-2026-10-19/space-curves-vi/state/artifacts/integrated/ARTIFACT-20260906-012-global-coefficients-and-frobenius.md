# Global coefficients and Frobenius: two exact tests of the jet formulation

Date: 2026-09-06. Operation: direct lead calculation and proof, with an independent
audit of the global-coefficient example.
Status: exact family statements and reproducible symbolic checks.

## Why these examples matter beyond their degree

Artifact 011 replaces an unspecified higher-jet state by a sufficient finite
state at fixed surface degrees. That does not make an arbitrary pair of
formal germs a pair of global surfaces. The following family detects the
precise error of extending the unknown coefficients from k to k(C).
A second calculation distinguishes a true Frobenius construction from
the same equations with residual components. These are tests of the
formulation, not a restriction of the research objective to rational curves.

Throughout let
\[
 C_n=(s^{n+1}:s^nt:st^n:t^{n+1}),\qquad n\ge2.
\]
It is a smooth rational curve of degree n+1 and class (1,n) on the
smooth quadric \(Q=xw-yz\), up to swapping the two rulings.

## 1. Scalar extension can manufacture a false global witness

Let \(S_n=yw^{n-1}-z^n\). Consider the degree-(n+1) forms
\[
 G_1=yS_n,\qquad G_2=wS_n.
\]
In the chart w=1 take the genuine generic coordinate T=z, and the
normal coordinates
\[
 u=y-T^n,\qquad v=x-yT.
\]
Thus \(Q=v\), \(S_n=u\), and \(K=k(C_n)=k(T)\). The jets satisfy
\[
 G_1=(T^n+u)u,\quad G_2=u,\quad G_1-T^nG_2=u^2.
\]
Consequently the relaxed K-linear combination with Q has local ideal
(v,\(u^2\)), of length two. This matches the proposed global degree
budget \(2(n+1)/(n+1)=2\), even at the sufficient cutoff.

But \(T^n\) is not a constant global surface coefficient. For every
nonzero pair \((\alpha,\beta)\in k^2\), the actual global combination
has
\[
 \alpha G_1+\beta G_2
 =u(\alpha u+\alpha T^n+\beta).
\]
Since T is transcendental, \(\alpha T^n+\beta\ne0\).
The second factor is a unit in the generic local ring, so the actual
intersection with Q has length one. No member of this global pencil
passes the degree-two target.

There is a stronger, pencil-independent exclusion on this Q. A
degree-(n+1) surface meeting Q properly and with generic multiplicity
two along C_n would require
\[
 (n+1)H-2C_n=(n-1,1-n)
\]
effective on \(\mathbf P^1\times\mathbf P^1\), impossible for n>=2.
Indeed C_n is not STCI on this smooth Q in any second degree because
its class is not proportional to H.

This does not contradict Artifact 011. The formal expression with
coefficient \(T^n\) is not a global degree-(n+1) form. Treating T as
the ambient coordinate z after dehomogenization would instead change
the polynomial to \(S_n^2\), of homogeneous degree 2n. Its degree
budget is different, and its intersection with Q has a residual ruling.
The generic formal coefficient field and homogeneous polynomial degree
must be retained together.

**Research delta:** the local matrix is computed over K, but the unknown
surface coefficients must remain in k. Existence of a K-point in a
relaxed coefficient problem is insufficient. The full jet liftability
map in Artifact 013 records what this relaxation discards.

## 2. The binomial pair: exact characteristic dependence

Now use the singular first surface S_n and the degree-(n+1) form
\[
 T_n=x^nw-y^{n+1}.
\]
Use normal coordinates \(u=y-T^n\), \(v=x-T^{n+1}\) in the same chart.
The target generic multiplicity is n. Modulo \(S_n=u\), the other
equation becomes
\[
 (T^{n+1}+v)^n-T^{n(n+1)}.
\]

In characteristic zero its linear term is
\(nT^{n^2-1}v\), with nonzero coefficient in K, so the length is one.
The pair therefore fails for every n>=2.

In characteristic p, write \(n=p^e r\), with \(p\nmid r\). Frobenius gives
\[
 (T^{n+1}+v)^n-T^{n(n+1)}
 =\left((T^{n+1}+v)^r-T^{r(n+1)}\right)^{p^e}.
\]
The inner expression has nonzero linear coefficient, so the generic
length is exactly \(p^e\). Artifact 011 proves
\[
 \boxed{\quad
 V_+(S_n,T_n)_{\mathrm{red}}=C_n
 \quad\Longleftrightarrow\quad n\text{ is a power of }p.
 \quad}
\]
This is an if-and-only-if for this particular binomial pair.
It is not an exclusion of other pairs when n is not a p-power; Moh's
broader projective monomial theorem supplies positive results in those
other cases by different equations.

There is a direct geometric check. Let r=n in characteristic zero and
r=n/p^e in characteristic p. On w=1 the support consists of the r
distinct curves
\[
 x=\zeta z^{n+1},\quad y=z^n,\qquad \zeta^r=1.
\]
Their closures each have degree n+1 and generic multiplicity p^e
(multiplicity one in characteristic zero). They account for the whole
degree \(n(n+1)\). At w=0 the equations force z=y=0 and leave just
(1:0:0:0), already on their closures. Thus no component at infinity
has been silently omitted.

Frobenius merges these distinct components scheme-theoretically into
one support exactly when r=1. It is a genuine global positive mechanism.
In characteristic zero the deficit relative to C_n alone is
\((n-1)(n+1)\); it is residual degree, not an abstract local defect.

## 3. A positive characteristic-zero control

For n=2 the twisted cubic is an STCI, but its second equation on S_2
needs the mixed term:
\[
 F=yw-z^2,\qquad G=x^2w-2xyz+y^3.
\]
For
\[
 I=(xz-y^2,\ xw-yz,\ yw-z^2),
\]
the exact computation gives
\[
 (F,G)\subset I,\qquad I^2\subset(F,G),
 \qquad\deg S/I=3,\quad\deg S/(F,G)=6.
\]
The generic finite jet length is two, exactly the target. These
containments independently certify the radical equality over QQ.
This keeps failure of the simpler binomial pair separate from failure
of the curve to be an STCI.

## Evidence and reproducibility

Run M2 --script scripts/finite_normal_jet_certificate.m2.
The script uses exact QQ(T) and finite-characteristic function fields.
It checks the twisted cubic, n=2,3,4,6 in characteristics 0,2,3,5,
the cutoff counterexample for M=1..6, and the coefficient trap for
n=2..6. The displayed general proofs, not those finite ranges, establish
the family statements. No sampling result is promoted to a
characteristic-zero nonexistence theorem.

The independent proof audit verified the Segre class computation:
with \(x=AC,y=AD,z=BC,w=BD\), the curve equation is
\(AD^n-BC^n=0\), and \(S_n=B^{n-1}(AD^n-BC^n)\).
This also checks the residual ruling used above.
