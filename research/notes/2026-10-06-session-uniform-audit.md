# Uniform BF audit, degree strengthening, and the surviving e=2 branch

Date: begun 2026-10-06, completed after resumption on 2026-10-07.
Status: **DIRECT PROOF AUDIT AND NECESSARY NUMERICAL REDUCTIONS**.
This note does not prove that C0 is not STCI. It does not assert a global
exclusion of every quartic carrier with e=2.

## 1. Inputs, independent representation, and scope correction

The canonical state, resume reconciliation, uniform order-one note,
primitive-fourth audit, and finite-flat pairing audit were compared.
The BF duality/effectivity statements survive the direct local argument
below. Their use still requires the smooth characteristic-zero rational
quartic normal bundle N*=O(-7)^2, complete-intersection adjunction,
and generic normal order one. The quartic assertion that the carrier has
generic normal order one is the repository's separately checked P-011
input; this note does not reprove P-011.

There is a genuine scope discrepancy in the pre-session canonical state.
Section B proves the e=2 branches of (4,7) and (4,8), whereas section H
says broadly that the quartic e=2 branch is excluded. The resume
reconciliation correctly states that larger pairs with early defects
remain open. The primitive-fourth argument applies to a larger pair
when D2=D3=0; those vanishings are not uniform consequences of BF
duality. Sections 4--6 below give exact local CI controls and small-degree
reductions showing why this distinction matters.

The primary-source BF cross-check was refreshed from Manolache,
*Duality for Gorenstein multiple structures on smooth algebraic varieties*,
Rev. Roumaine Math. Pures Appl. 68 (2023), 141--148:
[publisher PDF](https://imar.ro/journals/Revue_Mathematique/pdfs/2023/1-2/10.pdf).
The theorem is on printed p.143, embedded structures in Remark 1 on
pp.144--145, and coincidence of the filtrations for quasiprimitive
structures in Remark 2 on p.145. The proof here is an independent local
algebra representation; agreement with the reference is not its proof.

## 2. Direct proof of the saturated duality and effective defects

At a support point complete the ambient local ring to k[[t,x,y]].
Let B be its complete-intersection quotient with smooth reduced support
R=k[[t]]. Smooth support and Cohen--Macaulayness make t a
nonzerodivisor. Nilpotence of the two normal coordinates makes B finite
over R, hence finite free. Its special fibre is an Artin complete
intersection, so it is Gorenstein. Lift a functional on the special
fibre that is nonzero on its socle to an R-linear functional lambda on
B. The determinant of the multiplication pairing modulo t is nonzero;
therefore B -> Hom_R(B,R), b -> lambda(b*_), is an isomorphism.

Suppose the generic transverse algebra is K[v]/(v^m), K=Frac(R).
This holds when one defining equation has nonzero linear normal term:
formal elimination reduces the other equation to a nonzero multiple
of v^m. Put

    N_i = B intersect v^i B_K,       E_i=N_i/N_(i+1),
    0 <= i <= m,                   s=m-1.

Every B/N_i is R-torsion free, so each saturated step is a direct
summand. The E_i are free rank-one R-modules. The nilradical is N1;
the constant-coefficient quotient B/N1 is an integral R-subalgebra of
K, hence R itself. Generically and then integrally by torsionfreeness,

    Ann_B(N_i)=N_(m-i).

For any ideal J the lambda-orthogonal equals Ann(J): if lambda(bJ)=0,
then lambda(bjc)=0 for all c in B, and nondegeneracy implies bj=0.
A functional on N_(s-i)/N_(s-i+1) extends to B because the saturated
filtration splits over R. Its representing element under the Frobenius
pairing lies in N_i, and the kernel of its restricted functional is
N_(i+1). Thus E_i pairs perfectly with E_(s-i). Taking i=0 shows that
lambda maps E_s isomorphically to R. Consequently the actual maps

    E_i tensor E_(s-i) -> E_s

are isomorphisms. This checks maps, not just degrees or line-bundle
classes. It also explains why ordinary nilradical powers cannot replace
the saturated filtration: their quotients may have R-torsion.

Globally let L=E1. The iterated multiplication L^i -> E_i is generically
an isomorphism of line bundles on the smooth curve and hence has an
effective zero divisor D_i. Therefore E_i=L^i(D_i), D0=D1=0.
Associativity gives, as actual effective-divisor statements,

    D_i+D_j <= D_(i+j),        D_i+D_(s-i)=D_s.          (BF)

The top layer is Ann(I_C). Gorenstein duality identifies
Hom_(O_X)(O_C,omega_X) with omega_C; therefore

    E_s = omega_C tensor (omega_X|C)^(-1).

This proves the exact input used in the uniform note. It applies to the
saturated quasiprimitive CI structure. It makes no assertion about
ordinary powers, standalone nongorenstein lattices, or the branch where
both equations have generic normal order at least two.

## 3. A uniform degree strengthening beyond the retained bounds

Assume a,b>=4, generic normal order one for at least one equation, and
N*=O(-7)^2. The conormal epimorphism onto L has

    L=O(e-7),     e>=0,     c=7-e,     m=ab/4, s=m-1.

Here ab must be divisible by 4. Adjunction gives

    deg D_s = c*(ab/4-1)+14-4(a+b).                   (1)

Effectivity first gives c>0, hence e<=6. Multiplying (1) by 4c and
completing the product gives the stronger necessary degree condition

    (c*a-16)(c*b-16) >= 256-56*c+4*c^2.               (2)

This is equivalent to top-defect effectivity, rather than an additional
geometric hypothesis. It displays degree restrictions missed by listing
only e<=6 or 16/a<=c. For the four highest direction degrees it becomes

| e | Exact necessary inequality | Each defining degree must be at least |
|---|---|---:|
| 3 | (a-4)(b-4)>=6 | 5 |
| 4 | (3a-16)(3b-16)>=124 | 6 |
| 5 | (a-8)(b-8)>=40 | 9 |
| 6 | (a-16)(b-16)>=204 | 17 |

For e=3 both factors are nonnegative because a,b>=4, and the right
side is positive. For e=4, if both factors were negative their product
would be at most 16; for e=5 the corresponding bound is 64 after
multiplying by four; for e=6 it is 144. Each is smaller than the
required right side. A mixed-sign product is also impossible, so both
factors must be strictly positive. This proves both degree lower bounds,
including for a mate that may be thick generically. It does not transfer
the geometric normal-sheaf inequality to a thick mate.

For completeness, (2) has right sides 60,64,76 for c=7,6,5
(e=0,1,2). None is negative. The exact constraints for e=1,2 are
(6a-16)(6b-16)>=64 and (5a-16)(5b-16)>=76.
At e=2,a=4 the latter is precisely b>=7. These conditions give no
upper bound on either degree and do not exclude the high-degree
order-one branch.

## 4. Why the primitive factorization stops at its stated hypotheses

For a quartic carrier m=b and the top formula is

    deg D_(b-1)=(3-e)*b+e-9.

At e=2 this is b-7. For b=7 the entire defect divisor vanishes.
For b=8, superadditivity forces D2=D3=0 because twice either one
is bounded by a divisor of degree one. The canonical primitive fourth
then exists, so its quotient lies on the audited fourth-obstruction
zero locus. On that locus the defining quartic lies in

    H0(I_(C3)(4))=T*H0(O_(P3)(1)).

Its nonzero plane factor forces an extra curve when intersected with
any mate, proving the two exclusions. The same argument works at
any larger b when D2=D3=0. It does not force these equalities once
b-7 permits nonzero early defects. The existing parity theorem does
give an all-b exclusion on its explicit parity quotient family with
D2=0, but it does not cover every quadratic quotient or D2=1.

## 5. Exact local CI controls against a numerical overclaim

Let R=k[[t]] and take integers r,h>=2. The local algebra

    B_(r,h)=R[x,y]/(t*x-y^r, x^h)

is finite free with basis x^i*y^j, 0<=i<h, 0<=j<r. One can see
this by first taking R[x]/(x^h) and adjoining the monic relation
y^r-t*x. It is a complete intersection supported on (x,y).
After inverting t it is K[y]/(y^(r*h)) with x=t^(-1)y^r.
Writing k=r*i+j shows that the saturated layer E_k has generator
t^(-i)y^k, whereas the image of E1^k has generator y^k. Hence

    d_k=ord_t D_k=floor(k/r),       0<=k<r*h.         (3)

This formula satisfies superadditivity and complement duality exactly:

    floor(i/r)+floor((r*h-1-i)/r)=h-1.

Two controls are directly compatible with the e=2 top degree:

| b=r*h | Local equations | (d2,d3,d_(b-1)) |
|---:|---|---|
| 9 | t*x-y^3, x^3 | (0,1,2) |
| 12 | t*x-y^2, x^6 | (1,1,5) |

In each case d_(b-1)=b-7 and the uniform early bounds are satisfied.
Thus even finite-flat, two-normal-generator, local CI and Gorenstein
duality do not promote the primitive exclusion to every b. These are
local numerical controls, not projectively embedded multiple curves
on C0 and not STCI counterexamples or constructions. They establish
the insufficiency of the proposed numerical inference.

## 6. A sharper small-degree surviving frontier

For e=2, repeated multiplication gives

    deg D2 <= floor((b-7)/floor((b-1)/2)),
    deg D3 <= floor((b-7)/floor((b-1)/3)).              (4)

In particular b=9,10,11 have D2=0 and deg D3<=1. A survivor must
have deg D3=1; otherwise the primitive factorization applies. Write
D3=p. At p, superadditivity and complement duality force every
top defect to lie at p:

* b=9: D3+D5=D8 and D5>=D3, so the top degree two is spent at p.
* b=10: 3D3<=D9, so the top degree three is spent at p.
* b=11: 3D3<=D9=D10. Moreover D10=2D5, so its coefficient
  at each point is even. Its coefficient at p is therefore at least
  four, exhausting the total degree four.

Consequently the complete divisor sequence is an integer profile
d_i*p. Exhausting the finitely many integers allowed by (BF) gives

| b | Complete permissible profiles (d0,...,d_(b-1)) |
|---:|---|
| 9 | (0,0,0,1,1,1,2,2,2) |
| 10 | (0,0,0,1,1,2,2,3,3,3) |
| 11 | (0,0,0,1,1,2,3,3,4,4,4); (0,0,0,1,2,2,2,3,4,4,4) |

The companion `verify_session_uniform_bf_profiles.py` independently
enumerates every complementary profile, imposes effectivity,
monotonicity (the i=1 multiplication case), all superadditivity
inequalities, and d2=0,d3=1. It checks exactly these lists.
The b=9 profile has the genuine local CI control above. The other
profiles remain necessary numerical possibilities; the verifier does
not assert their embedded or local nonmonomial existence.

## 7. Intrinsic fourth-layer annihilation and an isolated universal export

When D2=0 the primitive triple has ideal-generator bundle fitting in

    0 -> L^3 -> V=I_(C3)/(I_C*I_(C3)) -> M -> 0,
    L=O(-5), M=O(-9).

Its class c lies in H1(O(-6)). A fourth layer with
E3=L^3(D3) induces a quotient V->E3 whose restriction to L^3
is the canonical multiplication section. Applying Hom(-,E3) gives
the necessary annihilation

    c maps to zero in H1(O(-6+D3)).                   (5)

If c is represented by coefficients c1,...,c5 of z^-1,...,z^-5,
a quadratic annihilator exists exactly when

    det [[c1,c2,c3],[c2,c3,c4],[c3,c4,c5]]=0.           (6)

This is multiplication of Laurent cocycles, so it includes the moving
infinity point when sections are treated homogeneously. For b=9..11
the stronger degree-one annihilator is necessary: the four-by-two
matrix with rows (c1,c2),(c2,c3),(c3,c4),(c4,c5) must have nonzero
kernel. The condition is rank at most one, not merely (6).

The session exporter `session_uniform_e2_hankel.py` imports the retained
exact moving-coordinate generator and writes only
`scratch/session_uniform_e2_hankel.json`. It derived c_j with a
single homogeneous-resultant denominator Delta; the Hankel determinant
reduces to P16/Delta, with P16 homogeneous of degree sixteen and
1112 monomials. The numerator vanishes to order at least six in
(2a1+b0,2a2+b1). Its parity specialization is

    - (beta+2)^6*(beta^2+8beta+36)
       *(beta^4+8beta^3-24beta^2-256beta-432)/1024.

Division by the specialized Delta=beta^2 gives the actual determinant.
At beta=-6,-2,6 the fourth vectors are respectively
(64,0,-8,0,0), (0,0,0,0,0), and (-128,0,160,0,-192);
the determinants are 512,0,-163840, matching the independent retained
parity certificate. There was no useful general polynomial
factorization, and no universal incidence exclusion was completed.

This export is exact derived data from the established generator,
not an independent audit of that generator. The open primitive-triple
problem combines actual quartic contact, the resultant-open condition,
and (5). For D2=1 a defective-triple gluing state is needed before
using any fourth class. The primitive calculation does not apply there.

The exporter also saves all six exact minors of the four-by-two
degree-one annihilator matrix, with their resultant denominator powers.
Their reduced numerator term counts are 392,412,447,416,412,392.
Thus the sharper b=9..11 necessary condition has a reproducible complete
polynomial specification. No saturation or emptiness certificate for its
intersection with the full ambient quartic-contact incidence is claimed.

## 8. Reproduction and continuation boundary

The new finite profile check and isolated Hankel export use

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/verify_session_uniform_bf_profiles.py
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/session_uniform_e2_hankel.py
```

The first is a genuinely exhaustive numerical check under explicitly
listed inequalities. The second regenerates the existing universal
fourth class and a new determinant; it does not replace the independent
ambient quartic-contact audit. Neither is a global STCI certificate.

The durable frontier is: the BF input is valid under the order-one
quasiprimitive CI hypotheses; high-e order-one pairs satisfy the
stronger degree products (2); the e=2 quartic branch remains open in
larger degrees unless early defects or the full actual carrier/annihilator
incidence are excluded. The entirely-thick branch is separate.
