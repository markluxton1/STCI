# Intrinsic quadruple algebras and the singularities of a general pencil member

Date: 2026-10-23. Status: **new proof proposal and supporting local-algebra
audit; not a promoted canonical result**. This note supplies the local step
for the proposed intrinsic K3 proof of the fixed characteristic-zero (4,4)
exclusion. It uses no classification of normal directions, primitive triples,
quartic carriers, or quartic contact pencils.

## Precise local hypotheses

Let k be an algebraically closed field of characteristic zero, R=k[[t]],
and K=k((t)). Let B be a finite-free local R-algebra of rank four, with
reduction R and generic algebra B_K=K[z]/(z^4). Suppose B is a relative
Gorenstein algebra. Put

    N_i = B intersect (z^i)B_K,   E_i=N_i/N_(i+1).

The saturated pairing theorem gives an isomorphism

    E_1 tensor E_2 -> E_3.

Write d for the valuation of the multiplication E_1^2 -> E_2. In the
global notation E_i=L^i(D_i), this is the local multiplicity of D_2;
perfect pairings give D_2=D_3. The pairing theorem is the accepted general
local-algebra premise in
[the MF6 pairing audit](2026-10-05-mf6-pairing-audit.md), sections 1--2.
It is independent of any quartic-carrier classification.

For the assertion about ambient formal coordinates, assume additionally

    B = k[[t,x,y]]/J,   radical(J)=(x,y).

A complete intersection supported on the smooth curve satisfies these
finite-flat hypotheses: its Cohen--Macaulay property makes t a
nonzerodivisor, and its Artin special fibre is Gorenstein. The choice of
the lift t of a parameter of the reduced curve supplies the R-algebra
structure. This is a local choice, not a claimed global retraction.

## 1. A normal form from multiplication, with no direction classification

Choose a in N_1 lifting a generator of E_1 and b in N_2 lifting a
generator of E_2. The product ab generates N_3=E_3, by the perfect pairing.
The elements 1,a,b,ab form an R-basis, by the saturated filtration. Since
N_i N_j is contained in N_(i+j),

    b^2=0,  a(ab)=0,
    a^2 = t^d u b + lambda ab,

where u is a unit and lambda belongs to R. Rescale b by u, and then replace
a by a-lambda b/2 (with the coefficient lambda interpreted after the
rescaling). Because b^2=0, this gives exactly

    a^2=t^d b,   b^2=0.

The algebra R[A,B]/(A^2-t^d B,B^2) is free on 1,A,B,AB, so the resulting
surjection onto B is an isomorphism. Thus

    B is isomorphic over R to R[A,B]/(A^2-t^d B,B^2).

This is an isomorphism of algebras with the saturated filtration. Its proof
uses the complete multiplication, rather than just an associated graded
algebra. In particular, the possible correction lambda ab was removed
explicitly. In characteristic two this removal is unavailable, which is a
real restriction on this argument.

If d>0, the special fibre is k[A,B]/(A^2,B^2). Hence A,B give an independent
basis of its cotangent space. Any lifts of A,B to the ambient formal ring,
together with t, form formal coordinates by the formal inverse function
theorem. The embedded ideal therefore has the exact normal form

    J=(x^2-t^d y, y^2).                                      (1)

There is no omitted higher-order ambient correction: after the coordinate
change the quotient by the displayed two generators is already free of
rank four and maps isomorphically onto B.

For d=0 the special fibre has embedding dimension one. A smooth relative
normal coordinate belongs to J, and a lift u of its remaining nilpotent
generator gives formal coordinates with

    J=(v,u^4).                                               (2)

Equivalently, the abstract normal form in this case is R[A]/(A^4), and a
surjection from the smooth ambient ring can be completed by one element
of its kernel to a formal coordinate system.

## 2. The fixed divisor of the first normal symbols is exactly D_2

At d>0, reduce (1) modulo (x,y)^2. Its image in the ambient conormal
module R x direct sum R y is

    t^d R y.

The saturated image is R y. Thus the vanishing multiplicity of the actual
first-normal image relative to its saturation is exactly d. At d=0,
(2) has a primitive first-normal image. Consequently, globally the fixed
divisor A of the first symbols of a generating pair is exactly D_2=D_3,
not only bounded above by D_3.

The equality uses the rank-four Gorenstein multiplication. It is not
asserted for arbitrary lengths or arbitrary non-Gorenstein algebras.
The linearized image belongs to J modulo I_C^2; it must not be confused
with the torsion-free quotient of the ordinary nilradical conormal.

## 3. The defect singularity for coefficient functions of all variables

Let d>0. A general element of a pencil generating J is

    f=U(t,x,y)(x^2-t^d y)+V(t,x,y)y^2,

where U and V are units. This unit condition excludes at most two members
of the pencil at each defect point: the local change from the original
two generators to the generators in (1) has invertible coefficient matrix.
After dividing by U, put v=V/U, a unit, and write

    f=x^2-t^d y+v(t,x,y)y^2.                                (3)

The Hessian in x,y is invertible at the origin. The formal implicit
function theorem gives its critical section x=x(t),y=y(t). The critical
equations imply

    y(t)=t^d/(2v(t,0,0))+O(t^(2d)),
    x(t)=O(t^(2d)).

Substitution gives the critical value

    h(t)=-t^(2d)/(4v(0,0,0))+O(t^(2d+1)).

The formal Morse lemma with parameter t therefore transforms (3) into a
nondegenerate quadratic form in two variables plus h(t). As k is
algebraically closed of characteristic zero, a unit root and a linear
change of the quadratic variables identify it with

    X Y + T^(2d).

The surface has rational double point type A_(2d-1), whose minimal
resolution has 2d-1 independent exceptional (-2)-curves. This proves the
claim for general unit coefficient functions, not only for constant
linear combinations of the displayed normal-form generators.

## 4. A simple moving zero gives type A3

At a primitive point use (2). Write a member of the global pencil as

    f=A(t,u,v)v+B(t,u,v)u^4.

Suppose A(t,0,0) has a simple zero at t=0. Since the two original members
generate J, B(0,0,0) is nonzero for the member whose first coefficient
vanishes. Because the t derivative of A is a unit, t'=A(t,u,v),u,v are
formal coordinates. Then

    f=t'v+B'(t',u,v)u^4.

A fourth root of the unit B' gives the further coordinate
u'=u(B')^(1/4), producing exactly f=t'v+(u')^4. Thus the singularity is A3.
This also proves that varying coefficients cannot lower its exceptional
rank below three.

## 5. Application to the two numerical quadruple types

For the fixed C=[s^4:s^3t:st^3:t^4], use the accepted
E=O(-7)^2 and the general saturated Gorenstein duality, together with
omega_Z=O_Z(4) for a hypothetical (4,4) intersection. These give

    L=O(e-7),  E_3=O(-18),
    deg D_2=deg D_3=3-3e,  e=0 or 1.

Let M be the kernel of E -> L. Then M=O(-7-e). The first symbols of the
two quartics are sections of M(4)=O(9-e), and section 2 proves that their
fixed divisor is D_2. Removing it yields a basepoint-free pencil of degree

    n=(9-e)-(3-3e)=6+2e.

The pencil is nonconstant because the pullback of O_P1(1) is the generated
line bundle O(n), whose degree is positive. A nonconstant map of smooth
curves in characteristic zero is separable, so a general fibre has n
distinct points avoiding the finitely many defect points.

For e=1 this produces eight A3 points, hence exceptional rank 24.
For e=0 it produces six A3 points, hence rank 18, and every defect of
multiplicity d adds rank 2d-1. Since deg D_2=3, its three possible
partitions have total extra ranks

    1+1+1 -> 3,   2+1 -> 4,   3 -> 5.

Every case therefore has exceptional rank at least 21. The K3 Picard bound
then finishes the proposed global proof, once integrality, Bertini
smoothness away from C, and the K3-resolution hypotheses are supplied by
the principal note. Those global facts are not replaced by this local
note.

## Evidence, status, and reproducibility

The new elementary identities and representative Jacobian algebras are
checked without external packages by

    python3 research/computations/verify_intrinsic_quadruple_local_algebra_2026_10_23.py

The calculation checks local formulas and the numerical rank budget; the
proof above establishes the classification-free normal form and the
variable-coefficient assertion. The script does not by itself prove the
global exclusion. The unbounded-degree STCI problem is unaffected.
