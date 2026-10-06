# Residual intersection cycles from the quasiprimitive lattice

Date: 2026-10-05. Status updated 2026-10-06: the (A\le D_{m-1}) bound and
the stronger pointwise cycle identity are independently audited under the
stated quasiprimitive hypotheses. The complete audit, including the
higher-order mate restriction, is `2026-10-05-residual-cycle-audit.md`.

This note concerns a hypothetical complete-intersection multiple structure,
not the existence of one. The calculation is local over the smooth reduced
curve and retains all defect divisors and normal-order jumps.

## Local statement

Let R=k[[t]] and let B be a finite free R-algebra of rank m, with reduced
support Spec R and generically curvilinear algebra K[y]/(y^m). Assume its
saturated order filtration has invertible graded pieces
E_i=L^i(D_i), 0<=i<=m-1, with D_0=D_1=0. Let q belong to the nilradical,
and suppose its first class q_1 in L is nonzero generically. If Z(q_1) is
the zero divisor in the chosen local trivializations, then

    length_R tors(B/qB) = (m-1) ord_t(q_1) + ord_t(D_{m-1}).

The global version twists q_1 by the degree of its ambient hypersurface.

Choose an R-basis adapted to the saturated filtration. Multiplication by q
raises the filtration. Its first row and last column are zero. Its remaining
(m-1)-square block is triangular; diagonal entries are the maps
q:E_i -> E_{i+1}. The generic algebra is curvilinear and q_1 is nonzero,
so this block has nonzero determinant. Every other maximal minor is zero.
The Smith-normal-form valuation of this determinant is exactly the length
of the torsion in B/qB. The adjacent multiplication coefficients have
divisors Z(q_1)+D_{i+1}-D_i. Summing telescopes to the displayed formula.
Higher coefficients of q do not affect the determinant.

This uses the saturated filtration and its multiplication maps. It would
not be justified for an arbitrary unsaturated I-adic associated graded.

## Application to a quartic carrier on a smooth rational quartic

Work in characteristic zero. Let C=C_0, let Q be its unique smooth quadric,
and suppose X=(F_4,G_b) has reduced support C and generic multiplicity b.
The quartic has generic normal order one. Write L=O(e-7), and write
E_i=L^i(D_i) for the quasiprimitive filtration. The socle is

    E_{b-1}=omega_C tensor O_C(-b)=O(-4b-2),

so deg D_{b-1}=(3-e)(b-1)-6.

The first class of q in L tensor O_C(2) is nonzero: otherwise F_4|Q would
vanish twice along C, but O_Q(4,4)(-2C)=O_Q(2,-2) has no sections, forcing
q to divide F_4 and contradicting the quadric-carrier obstruction.
Its zero divisor T therefore has degree e+1.

On Q write F_4|Q=h rho and G_b|Q=h sigma_b, where h cuts out C and
rho,sigma_b have classes (3,1),(b-1,b-3). Their intersection Z is proper:
a common residual component would be another curve in X. Every point of
Z lies on C. Locally on Q,

    0 -> O_Z(-C) -> O_{X intersect Q} -> O_C -> 0.

Use a completed parameter t on C, lifted to the ambient ring. The torsion
over k[[t]] in the middle algebra is exactly O_Z(-C). Hence the local
determinant formula gives the effective zero-cycle identity

    [rho intersect sigma_b] = (b-1)T + D_{b-1}.

This is an identity of length cycles on C; it does not assert that the
residual zero-dimensional scheme is annihilated by I_C or has the same
scheme structure as the divisor on the right. Taking degrees recovers
(3,1).(b-1,b-3)=4b-10, but the pointwise equality is stronger.

For b=6, the existing numerical types give D_5=D_2+D_3, so

    [rho intersect sigma_6] = 5T + D_2+D_3.

In the regular-ratio branch after subtracting a quadratic multiple of F,
G_6|Q=h^2 sigma with sigma of class (4,0). If H is the quartic vertical
divisor, [rho intersect C]=T+H. Subtracting yields

    [rho intersect sigma] = 4T + D_2+D_3-H.

The right side must be effective and supported at actual intersections of
the four residual rulings with rho. This is a new pointwise constraint;
it does not by itself identify H with a BF defect or exclude all pairs.

## A uniform first-normal bound

Let A be the divisor of the first-normal image I_X -> I_C/I_C^2, with
primitive horizontal kernel line M. Choose local ambient normal coordinates
x,y so x spans M and y maps to a unit of the quotient L. Apply the local
determinant formula to multiplication by y. The quotient has a direct
R-module decomposition B/yB=R plus N, where N is its nilradical and is
finite torsion. Its length is ord D_{m-1}. On the other hand,

    N/N^2 = R x / (t^{ord A}x),

since this quotient is exactly the first-normal cokernel in the kernel
direction, after killing y. Therefore length(N/N^2)=ord A and

    A <= D_{m-1} coefficientwise.

No characteristic restriction is required for this local inequality.
Equality is false in general: (t^a x-y^2,x^3) has A=a[t=0] and
D_5=2a[t=0]. The proof uses finite flatness and the saturated curvilinear
filtration, rather than a selected binomial local normal form.

For a regular-ratio (4,b) pair, A equals the quartic vertical divisor H.
Consequently

    9-e <= (3-e)(b-1)-6.

In characteristic zero the balanced quartic conormal bundle also gives
e in {0,1,2}, and the resulting necessary regular-branch bounds are

    e=0: b>=6;   e=1: b>=8;   e=2: b>=14.

In particular, the entire regular-ratio e=1 branch at (4,6) is impossible.
For its e=0 branch, deg H=deg D_5=9, so the coefficientwise inequality
forces D_5=H and the cycle identity gives [rho intersect sigma]=4T.
Here T is a single point. Because sigma has class (4,0), and each ruling
meets rho in length one unless it is a common component, sigma must be
the fourth power of the ruling through T. This supplies a geometric
normalization for the remaining mixed e=0 analysis.

The inequality does not exclude nonregular quotients: there A is the
common part of two vertical divisors and may have smaller degree.
