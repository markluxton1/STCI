# The entire conductor of a two-quadric quartic projection

Date: 2026-10-09. Author: root. Status: **PROVED HERE as an algebraic
reduction**, pending a separate written audit of its application to the
complete genus-one normalization lane. The universal STCI problem and
the unrestricted fixed-C0 problem remain **OPEN**.

This note is subsequent to the earlier October 9 continuation seal. It
does not modify that seal or treat its counts as including the present
proof. The signs in this note are fixed by the displayed equations.

## 1. Exact hypotheses and equations

Let k be algebraically closed of characteristic zero. Suppose a normal
integral nondegenerate surface S in P4 is the complete intersection of
two quadrics, and projection from P=[0:0:0:0:1] is finite and birational
onto an integral quartic X in P3. Write the four retained coordinates
as x0,x1,x2,x3 and the missing coordinate as z. Assume the pencil is
written

    Q1=z^2-A(x)z-R1(x),     Q2=L(x)z+R(x),

where A,L are linear forms, R1,R quadratic forms, and L is nonzero.
This normalization is possible whenever the center misses S and the
projection is birational: one pencil member has a nonzero z^2 term,
and an independent member can have that term cancelled. If its
remaining z coefficient were zero, S would map into a quadric, contrary
to a finite birational quartic image.

Put T=k[x0,x1,x2,x3],

    F=R^2+A L R-R1 L^2,
    A_X=T/(F),
    B=T[z]/(Q1,Q2),
    J=(L,R) in A_X.

Eliminating z on L nonzero gives z=-R/L and F=0. The degree-four
polynomial F is nonzero: otherwise the image on this nonempty open
would have dimension three. Since the image X is an integral quartic,
F is its defining equation up to a nonzero constant, and A_X injects
into B. Here B is the actual homogeneous coordinate ring of S. The
complete-intersection model is projectively normal, so this injection
also represents the finite normalization in the graded rings.

## 2. L and R cut an actual plane conic

L,R form a regular sequence in T. If R were a multiple L T1 with T1
linear, Q2 would factor as L(z+T1). Since B is a domain, one of these
linear forms would vanish on S, contradicting nondegeneracy. Thus R
is nonzero modulo L. In particular

    C=T/(L,R)

is the homogeneous coordinate ring of an actual plane conic Gamma.
The conic may be smooth, two lines, or a doubled line. Its degree is
two and it has no embedded point. No reducedness assumption occurs.

F belongs to (L,R), hence A_X/J=C.

## 3. Determine the conductor, including all scheme structure

The monic Q1 relation makes B generated over A_X by 1,z. Its relations
give

    Lz=-R,
    Rz=A R-L R1.

Consequently J kills B/A_X and J is contained in the conductor. There
is a surjection of graded modules

    C(-1) -> B/A_X,        a |-> az mod A_X.

Compute the Hilbert series using the actual complete intersections:

    HS(B)=(1-t^2)^2/(1-t)^5=(1+t)^2/(1-t)^3,
    HS(A_X)=(1-t^4)/(1-t)^4=(1+t+t^2+t^3)/(1-t)^3,
    HS(C)=(1-t)(1-t^2)/(1-t)^4=(1+t)/(1-t)^2.

Their difference is exactly t HS(C). The displayed surjection therefore
has zero kernel in every graded degree:

    B/A_X = C(-1).

The annihilator of this module is exactly J. Thus the entire conductor
ideal is

    conductor(A_X,B)=(L,R).

This is equality of ideals, not an assertion about reduced support or
generic conductor multiplicity. Sheafification yields

    nu_*O_S/O_X = O_Gamma(-1).

The same argument retains the vertex of the affine homogeneous cone;
no discarded finite-length module can account for an omitted embedded
component.

## 4. The entire upstairs conductor is a quadratic algebra

Since R=-Lz in B, JB=(L). Therefore the upstairs conductor scheme is
the actual Cartier hyperplane section D=V_S(L), and

    B/JB = C[z]/(z^2-Az-R1).

This is a finite free rank-two graded C-module, with basis 1,z. After
sheafification its algebra is

    p_*O_D = O_Gamma direct_sum O_Gamma(-1),

with multiplication supplied by the displayed monic equation. In
particular p:D->Gamma is finite flat of degree two over every part of
the actual conic, including nilpotents when Gamma is a doubled line.
D need not be reduced or smooth and may pass through Sing(S).

The trace involution is z |-> A-z. In characteristic zero set

    w=z-A/2,       delta=A^2/4+R1.

Then w^2=delta and the involution sends w to -w. This description is
valid over a reducible or nonreduced C; it does not infer a single
constant sign from an equality of powers on a reducible D.

## 5. Exact coordinates for the fixed rational quartic

Suppose the lift c is the rational normal quartic

    [x0:x1:x2:x3:z]=[U^4:U^3V:UV^3:V^4:U^2V^2].

Its six independent quadrics are

    E0=x0z-x1^2,       E1=x0x2-x1z,
    E2=x0x3-x1x2,      E3=x1x2-z^2,
    E4=x1x3-zx2,       E5=zx3-x2^2.

A convenient normalized pair is Q1=-E3-aE0-bE1-cE2-dE4-eE5
and Q2=fE0+gE1+hE2+iE4+jE5. It has

    A=a x0-b x1-d x2+e x3,
    R1=x1x2-a x1^2+b x0x2+c(x0x3-x1x2)+d x1x3-e x2^2,
    L=f x0-g x1-i x2+j x3,
    R=-f x1^2+g x0x2+h(x0x3-x1x2)+i x1x3-j x2^2.

Writing z_c=U^2V^2, the exact restrictions are

    R_C=-z_c L_C,       R1_C=z_c^2-A_C z_c.

At a zero of L_C the two roots of Q1 above the corresponding C0
point are z_c and A_C-z_c. A hypothetical mate forces full inverse
support to be just c, so these roots must coincide. Hence

    support(div(L_C)) is contained in support(div(A_C-2z_c)).

L_C has zero U^2V^2 coefficient, while A_C-2z_c has coefficient -2.
Thus a squarefree L_C is impossible: four distinct roots would force
two degree-four binary forms to be proportional. Repeated-root
strata are retained; this support argument alone does not exclude
them. In particular an isolated rank-one differential at a smooth
point of S is not silently treated as the generic-rank obstruction
along an entire conductor prime.

## 6. Where the reduction is used and where it stops

The accepted genus-one theorem already gives a Gorenstein degree-four
del Pezzo normalization with ADE singularities. The standard weak
del Pezzo anticanonical embedding and projective-normality theorem
identifies its complete |H| image in P4 as a complete intersection of
two quadrics. This additional application, and the spanning assertion
for c needed for the exact fixed-C0 coordinates, are being independently
checked in a separate note. The primary input is Dolgachev,
Classical Algebraic Geometry, section 8.3, especially Theorems 8.3.2
and 8.3.4:

<https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/CAG.21.pdf>.

Once that application is accepted, the actual conductor part has no
further reducedness or smoothness gap. A global doubled-curve quadric
Q with div(Q)=2c gives a further descent problem: a mate of even degree
2n must be a scalar multiple of Q^n on S, and its restriction to the
entire D must belong to O_Gamma(2n). The power-descent obstruction on
singular D and doubled/reducible Gamma remains under investigation.
Neither this conductor theorem nor the squarefree-L exclusion closes
the whole genus-one or genus-two lane.

## 7. Exact symbolic companion

The checker is
`research/computations/verify_session_genus_one_entire_conductor_2026_10_09.py`.
It checks all six actual quadrics' lifted-curve restrictions, the
normalized equations and elimination signs, both conductor-multiplication
identities, the Hilbert-series equality, the trace involution, and the
fixed-C0 middle-coefficient obstruction. The ideal equality and coverage
are proved by the argument above; identities alone are not that proof.
