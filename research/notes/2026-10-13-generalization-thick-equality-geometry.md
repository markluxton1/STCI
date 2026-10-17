# A quadratic formal-neighborhood obstruction to every zero-defect C0 thickening

Date: begun 2026-10-13; completed 2026-10-14. Owner:
`thick_extension/equality_geometry`. Status: **PROVED new reduction and
C0 equality exclusion; Sections 2--3 and the gap deduction independently
audited by socle_audit**. This note uses
the accepted socle/equality theorem and accepted P-010 quadratic line
obstruction as inputs. Those results are not reverified. It does not
exclude positive-defect thickenings or resolve whether C0 is STCI.

## 1. Statement and antecedents

Let C be a smooth rational curve with balanced conormal bundle

    N_C^* = O_P1(-lambda) tensor V,  dim V=2.

Suppose an embedded thickening Y of C has constant normal algebra

    gr_J O_Y = direct_sum_j O_P1(-lambda*j) tensor B_j,
    B = k[u,v]/(f,g),  deg f=r, deg g=s, r+2<=s.

Here the isomorphism includes the actual quotient map from
`Sym N_C^*`; f and g are constant polynomials in one fixed balanced
frame, not merely a pointwise abstract description of each fiber.

For every constant linear direction m in V, let h_m be the quadratic
obstruction class to the embedded primitive triple with constant ideal
`(m,ell^3)`, where ell is any complementary constant direction. It is a
class in H1(O(-lambda)), up to nonzero scalar changes of m and ell.

**Direction-support theorem.** In characteristic zero, every linear
factor m of f must satisfy h_m=0. More generally, in positive
characteristic this conclusion holds for every factor whose multiplicity
in f is nonzero in the field. Consequently, if every h_m is nonzero,
no such constant graded complete-intersection thickening with r+2<=s
can exist.

For C0=[s^4:s^3*t:s*t^3:t^4] in characteristic zero, the accepted P-010
calculation gives lambda=7 and h_m!=0 for every m. Therefore the
zero-defect equality boundary in the accepted full socle theorem is
empty, in every hypersurface degree pair.

The P-010 coefficients are recorded, with the full balanced charts, in
`2026-10-05-typea-audit.md`, Section 1. The socle/equality theorem is
`2026-10-13-evening-entirely-thick-rees-progress.md`, Sections 2--7.

## 2. The obstruction to lifting the smallest initial relation

Write X=P3 and K=I_Y. Work modulo I_C^(r+2). On each standard affine
chart of C, choose normal parameters u,v lifting the fixed balanced
conormal frame, together with a local parameter on C. The completed
local ambient algebra on that chart has the form O_U[[u,v]]. On the
overlap the first-order normal transition is scalar z^(-lambda), and
through quadratic degree it has the form

    u' = z^(-lambda) (u+q_u) mod I_C^3,
    v' = z^(-lambda) (v+q_v) mod I_C^3,

where q_u,q_v are quadratic in u,v with Laurent-polynomial coefficients.
The other chart's base parameter W equals 1/z modulo I_C; its deviation
from 1/z is of normal order at least one. Define the quadratic
derivation on constant normal polynomials by

    delta = q_u*d/du + q_v*d/dv.

Because f is the unique lowest-degree relation and s>=r+2, the actual
initial ideal in degrees r and r+1 is

    in(K)_r = k f,
    in(K)_(r+1) = f V.

On each affine chart choose a lift in K of the leading relation f.
Modulo I_C^(r+2) it can be written

    P_U = f(u,v)+R_U(z,u,v),
    P_V = f(u',v')+R_V(W,u',v'),

with R_U,R_V homogeneous of normal degree r+1. The choices exist
locally by the definition of the initial ideal. They exist on the full
affine chart as well: the short exact coherent sequence for the relevant
truncated ideals has vanishing first cohomology on that affine chart.

Expanding the second lift in the first chart gives

    z^(lambda*r) P_V
       = f + delta(f) + z^(-lambda) R_V(1/z,u,v)
         mod I_C^(r+2).

Replacing W by 1/z in R_V is valid at exactly this stage: R_V already
has normal order r+1, so the resulting error has order at least r+2.
This argument does not freeze the moving base coordinate at an order
where it contributes.

The difference of these two ideal elements has order at least r+1.
Its symbol therefore belongs to fV. Passing to

    Q = Sym^(r+1) V / f V

gives

    [delta(f)] + z^(-lambda)[R_V(1/z)] - [R_U] = 0.

Thus the Cech class

    o_f = [delta(f)] in H1(O(-lambda)) tensor Q

must vanish. Changing local lifts changes it by a Cech coboundary.
Multiplying an ideal lift by a unit with a first-normal correction
changes the expression by fV, already zero in Q. Changes in the lift of
the scalar conormal transition, including moving-coordinate changes,
likewise contribute only fV. No global retraction of Y to C or splitting
of its filtered algebra is assumed.

## 3. A constant factor extracts an accepted line obstruction

Over the algebraically closed field, take a linear factor m of f with
multiplicity t>=1. Choose a complementary linear form ell and write

    f = m^t H,
    H mod m = c ell^(r-t), c!=0.

The homogeneous polynomial delta(f) has degree r+1. Take the constant
linear functional on Sym^(r+1)V extracting the coefficient of

    m^(t-1) ell^(r+2-t).

It descends to Q because every element of fV is divisible by m^t. The
Leibniz rule gives

    delta(f)= t m^(t-1) H delta(m) + m^t delta(H).

The extracted coefficient is therefore

    t c times the ell^2 coefficient of delta(m) mod m.

But the latter coefficient is exactly the quadratic line-obstruction
cocycle h_m: modulo m, the normalized normal transition for m has the
form

    m' = z^(-lambda)(m+h_m ell^2) mod (m,I_C^3).

The constant linear functional commutes with both Cech restrictions and
the scalar transition z^(-lambda). Hence it takes o_f to t c h_m in
H1(O(-lambda)). If o_f=0 and t is invertible, then h_m=0. This proves
the direction-support theorem.

This is also the elementary logarithmic factor argument: a derivation
delta(f) divisible by f can occur only when each factor of f with
invertible multiplicity is preserved by the derivation. The coefficient
extraction makes that argument valid directly in the cohomological
quotient, including repeated factors.

## 4. Applying accepted P-010 data to C0

Use the accepted balanced frames

    u=b-(3/2)za, v=a,
    u'=a'/2, v'=-3Wa'+2b',
    W=(z^3+a)/(z^4+b),
    a'=z/(z^4+b)-W^3,
    b'=1/(z^4+b)-W^4.

For m=u+theta*v and ell=v, the accepted quadratic line-obstruction is

    h_theta = 3 theta^3 z^(-5) - (3/2) theta^2 z^(-4)
            + (3/4) theta z^(-3) - (3/8) z^(-2).

For the missing direction m=v, ell=u, it is

    h_infinity = 3 z^(-5).

In H1(O(-7)), z^(-1),...,z^(-6) are the usual Cech basis. In
characteristic zero, h_theta is nonzero for every theta because its
z^(-2) coefficient is -3/8. The missing-direction class is also
nonzero. The direction-support theorem consequently excludes every
constant graded CI(r,s) with s>=r+2, regardless of the size of r and s.

## 5. Every C0 zero-defect equality has the required gap

The accepted socle/equality theorem gives, for any hypothetical
zero-defect complete intersection Y=V(F_a,G_b) with support C0,

    ab=4rs,
    4(a+b)=7(r+s),
    d=r+s-2.

We order r<=s. The discriminant of a,b is nonnegative. Substitution
gives

    49(s-r)^2 >= 60rs.

This immediately excludes r=s. It also excludes s=r+1 because then
the left side is 49 and the right side is at least 120. Hence s>=r+2.
No generator-filtration theorem is needed for this gap deduction.

In the order-one case the constant algebra may have embedding
dimension one; it can still be written as k[u,v]/(f,g), with r=1 and
f linear. The same argument applies whenever it occurs on equality:
the two displayed degree relations again imply s>=r+2. In the entirely
thick case r>=2, so the result applies directly to the branch requested.

Therefore every hypothetical complete-intersection thickening of C0
in characteristic zero has the strict full-normal budget

    mu = 7d+14-4(a+b) > 0,
    n mu = 7 Asym + 2 Delta,
    n=ab/4.

Since mu is integral, mu>=1. If arithmetic forces mu to be a multiple
of four, its smallest permitted value is four. This strict inequality
uses the full higher-normal algebra through d and its initial relation;
it is not a tangent-only cap on horizontal multiplicity.

For the formerly retained thick pair (a,b)=(6,8), the socle theorem had
d>=6 and equality d=6 forced graded degrees (r,s)=(2,6). That equality
model is now excluded; every such hypothetical thickening must have
d>=7 and mu>=7.

## 6. Limits and continuation

There is a useful extension that does not assume equality or a complete
intersection. Define the actual normal relation bundles

    K_j=ker(Sym^j N_C^* -> J^j/J^(j+1)).

They are vector bundles because they are subsheaves of vector bundles
on the smooth curve. With the accepted normal defects Delta_j,

    deg K_j = -7j rank K_j - Delta_j.

This formula includes the torsion length of the quotient. Suppose the
generic first relation is unique in degree r, and there is no independent
relation in degree r+1. Thus rank K_r=1 and rank K_(r+1)=2. If
Delta_r=0, then K_r(7r) is a degree-zero line bundle with an injection
into a trivial bundle. Its inclusion is constant and its cokernel is
locally free, so K_r=O(-7r)f for a constant f.
Multiplication gives a rank-two injection

    O(-7(r+1)) tensor fV -> K_(r+1).

Its torsion cokernel has length

    deg K_(r+1) + 14(r+1) = -Delta_(r+1).

Nonnegativity of both this length and Delta_(r+1) forces
Delta_(r+1)=0 and makes this injection an isomorphism. The relation
lift and factor extraction therefore apply verbatim. Consequently, on
C0 in characteristic zero,

    Delta_r >= 1

whenever the generic first relation is unique and there is no independent
adjacent relation. This obstruction is local in the normal filtration;
it does not require zero defects in any higher layer, Gorenstein
duality, or a bounded hypersurface degree.

The result excludes the entire zero-defect boundary uniformly. It does
not bound d from above. Positive-defect thickenings can have variable
graded relation subbundles, normal-layer torsion, and effective defects;
those may kill or modify the obstruction. The accepted budget records
their total cost but does not currently exclude them.

The natural extension is to make the obstruction cost quantitative for
a nonconstant lowest relation line in Sym^r N_C^*, including its
coefficient divisor and possible order-(r+1) extra initial generators.
Any such theorem must preserve the moving-coordinate terms and all
special points; an abstract generic Artin model does not supply a
global two-hypersurface representation.

The cohomological proof applies to other smooth rational curves with
balanced conormal bundle if their quadratic direction obstructions are
known. It places the support of the first homogeneous relation in the
zero locus of the direction-obstruction map. C0 has empty zero locus,
which is the structural reason its equality boundary disappears.

More explicitly, over the direction projective line P(V), write M for
the tautological line O(-1). The quadratic derivation induces

    h in H1(O_C(-lambda)) tensor Hom(M,Sym^2(V/M)).

Since V/M=det(V) tensor M^(-1), choosing a determinant normalization
identifies this with a vector-valued cubic section of O_P(V)(3).
Changing the normal coordinate lifts changes the cohomology class by
a coboundary; radial terms are zero after projection to V/M. Thus,
unless this vector-valued cubic is identically zero, its common zero
set consists of at most three direction points. Every constant first
relation with an adjacent-degree gap has to factor over those points.

For C0 the accepted coefficients homogenize to

    h(A,B)=3B^3 z^(-5)-(3/2)AB^2 z^(-4)
          +(3/4)A^2B z^(-3)-(3/8)A^3 z^(-2).

Its four coordinates are the four cubic monomials with nonzero scalar
coefficients, so they have no common zero in P1. This identifies the
C0 mechanism with a general finite-direction reduction rather than a
separate degree-by-degree exclusion.

Characteristic-zero multiplicities are essential in this proof. If the
characteristic divides all factor multiplicities, delta(f) may vanish
for Frobenius reasons; moreover the displayed C0 coefficients use 2 and
3. No positive-characteristic exclusion is claimed.

## 7. Provenance and operational notes

The new proof uses accepted repository statements rather than repeating
their verification. One attempted scratch invocation of the old
`/private/tmp/stci-cas-venv/bin/python` failed because SymPy is no longer
installed in that environment. No result in this note depends on that
attempt; the accepted P-010 transition coefficients suffice, and the
new proof is symbolic and cohomological.

Memory was used only for the higher-normal-jet failure shield, then
replaced by current repository inspection: MEMORY.md lines 164--171;
rollout id `01a02fb1-2af7-7fa3-897c-9d6527951ac9`. No older
checkout-specific theorem status was transferred here.
