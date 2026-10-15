# Saturated first relations turn an actual CI into a primitive root-curve multiple

Date: 2026-10-14. Author: root. Status: **WRITTEN GEOMETRIC THEOREM;
independently audited under the stated hypotheses**. The
[independent bridge audit](2026-10-14-generalization-blowup-root-curve-bridge-independent-audit.md)
includes separate local-algebra and conormal reviews, a shorter local
proof, and a defect-boundary family. The spectral root-curve criterion and its
already reviewed ambient obstruction class are premises. This note
supplies a bridge from an actual supported complete intersection to
that obstruction. It does not assert that the obstruction is nonzero.

## 1. Hypotheses

Let C be a smooth curve in a smooth threefold X over an algebraically
closed field of characteristic zero. Let Y=(F,G) be an actual complete
intersection supported exactly on C. Use the ordinary I_C-adic initial
ideal. Assume:

1. Its first nonzero generic normal relation has degree r and its actual
   degree-r relation sheaf R is a saturated line subbundle of Sym^r N_C^*.
2. Both actual equations F,G have generic normal order r. Their leading
   symbols generate R at every point. Equivalently their coefficient
   pair in local frames of R has no common zero on C.
3. The full generic initial ideal is a binary regular sequence (f_r,g_s),
   with s>r, and g_s coprime to f_r. Set k=s-r and assume k>=2.
4. The actual Cartier root divisor Z of f_r on the exceptional divisor
   of Bl_C X is smooth, hence reduced. Smoothness of its reduced support
   alone is insufficient. It may be treated componentwise if disconnected.

The first hypothesis often forces the second when the two equations
generate the whole actual relation sheaf; it is nevertheless stated
explicitly here. A divisor where both leading coefficients vanish is a
genuine excluded hypothesis, not a set to be saturated away. At such
points vertical exceptional components may occur.

Let B=Bl_C X, let E be its exceptional divisor, and let D_F,D_G be the
strict-transform Cartier divisors. Their local equations are obtained
by dividing the pullbacks of F,G by the r-th power of an exceptional
equation. Write Y'=D_F intersect D_G.

## 2. The strict intersection has support exactly Z

Off E the blowup is an isomorphism and the original intersection has
no point off C. Hence Y' is supported on E. On E the two transformed
equations are a f_r and b f_r, where a,b are the actual leading
coefficients. Since a,b have no common zero, their common zero set on
E is exactly Z. In particular no exceptional fiber P1 over a point of
C is a curve component of Y'. Such a fiber could be shared only if
both leading coefficients vanished there, or if f_r vanished on the
whole fiber; both possibilities are excluded by the hypotheses.

The two strict divisors have no common surface component, since their
images would be a common surface component of F,G. They form a
regular sequence on the smooth threefold B. Thus Y' is a pure
one-dimensional complete intersection with reduced support Z; there
is no discarded isolated or embedded component.

At the generic point of C, the usual normal blowup calculation for
the binary regular sequence (f_r,g_s) gives transverse length k=s-r
on every root branch. Indeed one may choose a standard basis of
normal orders r,s generating the actual completed generic ideal: a
lift of g_s together with an original equation whose leading symbol
is f_r generates the full initial ideal, hence the actual ideal by
filtered division. Both original equations were divided by u^r, so
this invertible change of generators preserves their strict-intersection
ideal. On a chart with exceptional parameter u, its generators reduce to

```
f_r+O(u),   u^(s-r)(g_s+O(u)) modulo the first equation.
```

A smooth root is simple over the generic point, and g_s is nonzero
there. Eliminating the first equation leaves u^k. Therefore the
generic algebra of Y' along each component of Z is curvilinear of
length k. This calculation uses the full generic initial regular
sequence, not merely two chosen original normal orders.

## 3. The first normal layer is a line bundle everywhere

The conormal sequence for Z subset E subset B is

```
0 -> O_Z(-E) -> N_(Z/B)^* -> O_Z(-Z_E) -> 0.          (1)
```

Project the first normal symbols of D_F,D_G to the last term. They
are precisely a df_r,b df_r. Smoothness of Z makes df_r a local
generator of O_Z(-Z_E), and the coefficient pair is basepoint-free.
Thus their joint normal-symbol map surjects onto the last term.
Here df_r is the full conormal differential on E, including its base
direction; it is not just the fiber derivative. Smooth ramification
of Z over C causes no failure of this surjectivity.

Their determinant vanishes generically on every component of Z:
the intersection has transverse length k>=2 and is generically
curvilinear. The determinant is a regular section of a line bundle
on the smooth reduced Z, so it vanishes identically. The two first
symbols therefore have rank one at every point, and at least one
has a unit projection to the last term of (1). Their image K is a
line subbundle, with an isomorphism

```
K -> O_Z(-Z_E).
```

This splits (1). Its quotient is canonically O_Z(-E). In particular
the **actual** first ordinary normal layer of Y' is

```
J/J^2 = O_Z(-E),   J=I_Z O_(Y'),                    (2)
```

without a point-supported torsion term. This conclusion would be
false if joint leading base points had been removed instead of
retained.

## 4. The entire strict intersection is primitive

The preferred proof is local on the smooth strict surface and works
before completion. At a point p of Z, choose one transformed equation
h whose leading coefficient is a unit. Since h|E=a f_r with a(p)!=0
and Z is smooth in E, the surface S=(h) is smooth at p and meets E
transversely along Z. An exceptional equation u therefore cuts out
Z as a reduced Cartier divisor on S.

The other transformed equation h_2 restricts to a nonzero equation
on S supported exactly on Z. The regular local surface ring is a
UFD, so h_2|S is a unit times u^e. Its generic multiplicity is the
already computed k=s-r; consequently e=k and

```
I_(Y',p)=(h,u^k).
```

This proves embedded primitivity everywhere and identifies its
surviving conormal with O_Z(-E). It also realizes Y' locally as a
Cartier divisor on the exceptional thickening E_k=V(I_E^k).

For completeness, the original formal argument is consistent with
this direct proof. At a point of Z complete and lift a curve parameter
t. Purity makes t a nonzerodivisor, and the local ring A of Y' is finite free of
rank k over R0=Bbbk[[t]]. Its nilradical J has J^k=0 everywhere, by
purity and the generic nilpotence bound. From (2), Nakayama makes
J a principal ideal generated by a lift z of its free first layer.
The reduction of A modulo t is consequently generated by z. Thus
R0[z]/(z^k) maps surjectively to A; both are free of rank k, so the
map is an isomorphism.

Hence Y' is an actual embedded primitive k-fold curve everywhere
along Z. Its local smooth containing equation has first relation
K from Section 3, and its surviving conormal is O_Z(-E). This is
stronger than generic curvilinearity or a numerical socle match.
No socle-degree enumeration is needed to obtain primitivity here.

## 5. Consequence for the ambient root-curve obstruction

Let J_E=O_E(-E). The square-zero first neighborhood of E has the
reviewed class

```
kappa in Ext1_E(Omega_E,J_E).
```

For its smooth Cartier root divisor Z, restriction and contraction
with df_r gives the conormal extension (1), whose class is

```
kappa(df_r) in H1(Z,O_Z(Z_E) tensor J_E|Z).           (3)
```

Section 3 splits that extension. Therefore every actual supported
complete intersection satisfying the hypotheses must have

```
kappa(df_r)=0.                                     (4)
```

The local ideal (h,u^k) shows that I_E^k is contained in I_(Y'),
and I_(Y')/I_E^k is locally the invertible ideal generated by h on
E_k. Thus the primitive k-fold structure is an actual global Cartier
lifting of Z into E_k and supplies compatibility of the same
Cartier relation through every exceptional order strictly below k.
Those are the root-curve obstruction bundles already identified in
the spectral note. If their relevant H0 groups vanish, compatible
finite principal ideals are unique, but their actual obstruction
classes must still be evaluated; negative bundle degree is not
itself a nonvanishing theorem.

For the accepted C0 conormal O(-7)^2, E=P1 x P1 and
J_E=O(-7,1). A first quadratic relation of movement degree two
has root divisor of type (2,2). The entire family has first target

```
H1(Z,O_Z(-5,3))
 = coker[H1(O(-7,1)) --f--> H1(O(-5,3))],
dimensions 12 -> 16 -> 4.
```

Thus one universal lifting incidence on the coefficients of f is
necessary for every actual CI in this lane, independently of
both hypersurface degrees. This is the appropriate shared next
problem, rather than enumerating the numerical profiles of the
abstract elliptic graded families.

## 6. Boundaries and audit disposition

The theorem leaves nonzero first-relation defects, singular or
nonreduced root divisors, noncoprime next relations and k=1 outside
the primitive conclusion. The generic normal order of the chosen
two equations, their joint leading base points, and full original
set-theoretic support are substantive hypotheses. None is inferred
from generic Hilbert data alone.

The independent audit passes the generic blowup multiplicity, exact
support and absence of vertical fiber components, global conormal
splitting, entire embedded primitivity, and necessity kappa(df_r)=0.
It retains the first-relation defect boundary explicitly: the family
F=t f_r+h_(r+1), G=F+f_r^q, with f_r squarefree, h_(r+1) coprime,
and q>=2, is supported exactly on C=(x,y) but has actual first
relation t O_C f_r. Both leading coefficients vanish at t=0, and
the strict intersection contains that entire exceptional fiber.
Saturating the first relation cannot discard this boundary.

The actual ambient class still has to be evaluated. The accepted
spectral criterion, normal bundle, ambient chart and earlier carrier
exclusions were not reverified.
The universal STCI question and unrestricted C0 remain open.
