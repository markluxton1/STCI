# Independent audit: constant initial relations and the strict C0 socle budget

Date: begun 2026-10-13, completed 2026-10-14. Status: **PROVED**, with the
accepted P-010 nonzero quadratic direction classes used as inputs. This
audits only the new relation-lifting and factor-extraction argument in
`2026-10-13-generalization-thick-equality-geometry.md`, plus the new
first-relation defect extension proposed by `thick_extension`.
Previously verified direction coefficients and their nonvanishing are
not recomputed. No canonical-state file is edited.

## 1. Verdict

The argument is valid. It excludes every zero-defect equality model for
C0 in characteristic zero simultaneously, and proves a positive degree
defect for a unique first initial relation whenever no independent
initial relation appears at the next normal order.

The essential hypothesis is the constant quotient map from the actual
conormal algebra, rather than an abstract isomorphism of graded fibers.
The earlier equality theorem supplies that hypothesis. No assertion
that the filtered embedded neighborhood splits is needed.

## 2. General relation-obstruction theorem

Let C = P1 be smoothly embedded in a smooth threefold, with

    E = N_C^* = O(-lambda) tensor V, dim V=2.

Let K be the ideal of an embedded thickening Y with reduced support C.
Suppose its initial ideal has

    in(K)_r = O(-lambda r) tensor k f,
    in(K)_(r+1) = O(-lambda(r+1)) tensor fV,

for a fixed nonzero binary form f of degree r >= 1. Thus f is the unique
first relation, and the next normal order has only its linear multiples.
Let h_m in H1(O(-lambda)) denote the quadratic embedded obstruction
associated to a constant linear direction m in V.

Then for every factor m of f of multiplicity t whose image in the field
is nonzero,

    h_m = 0.                                   (A)

In characteristic zero every factor satisfies this conclusion. Hence
if every h_m is nonzero, the displayed initial-relation pattern is
impossible for every r simultaneously.

## 3. Independent check of relation lifting

Choose the two usual affine charts of P1 and ambient formal normal
parameters u,v lifting its fixed balanced conormal frame. On the overlap
write the transition through quadratic order as

    (u',v') = z^(-lambda)[(u,v)+(q_u,q_v)] mod I_C^3.

Let delta = q_u partial_u + q_v partial_v. The second chart base
coordinate W equals 1/z modulo I_C; it need not equal 1/z in the
embedded neighborhood.

The definition of the initial relation and affine coherent lifting
provide local ideal elements

    P_U = f(u,v)+R_U(z;u,v),
    P_V = f(u',v')+R_V(W;u',v') mod I_C^(r+2),

where R_U,R_V have normal degree r+1. Multiplying P_V by the chosen
unit z^(lambda r) preserves membership in K. Its expansion is

    z^(lambda r)P_V
      = f + delta(f) + z^(-lambda)R_V(1/z;u,v)
        mod I_C^(r+2).

The moving base coordinate creates no omitted term: substituting 1/z
for W changes R_V by normal order at least r+2. The polynomial f is
constant, so there is no derivative of a coefficient function in its
degree-r symbol. A first-normal correction to the scalar transition or
to the chosen leading lift produces a multiple of f by a linear form.

Subtracting P_U from the normalized P_V gives an ideal element of
normal order at least r+1. Its degree-(r+1) symbol belongs to fV.
Therefore

    [delta(f)] = 0
       in H1(O(-lambda)) tensor [Sym^(r+1)V/fV].  (B)

Changing either local lift only changes its representative by a Cech
coboundary. This proves (B) for the actual embedded ideal, with every
moving-coordinate contribution accounted for at the relevant order.

## 4. Independent check of repeated-factor extraction

Factor f = m^t H, with H mod m = c ell^(r-t), c != 0, and ell a
constant complement to m. Take the coefficient functional extracting

    m^(t-1) ell^(r+2-t)

from Sym^(r+1)V. It kills fV because every element of fV is divisible by
m^t. Applying the Leibniz rule gives

    delta(f) = t m^(t-1) H delta(m) + m^t delta(H).

The extracted coefficient is t c times the coefficient of ell^2 in
delta(m) modulo m. That is exactly the quadratic direction cocycle h_m.
All spaces have the same scalar transition z^(-lambda), so this constant
coefficient functional induces a map on the Cech cohomology in (B).
Its image is t c h_m. For t nonzero in the field, (A) follows.

This argument handles every repeated factor. It does not assume that
the root set is reduced or infer a bound on higher contact from the
first tangent cone. In positive characteristic, a factor with
multiplicity divisible by the characteristic is invisible to this
first derivative; no exclusion is claimed there.

## 5. Uniform consequence for C0 equality

The accepted P-010 premise says h_m != 0 for every constant direction
m on C0 in characteristic zero. The accepted full socle equality gives
the actual constant graded CI

    k[u,v]/(f_r,g_s), r <= s,
    ab = 4rs,
    4(a+b) = 7(r+s),
    d = r+s-2.

Its ordinary hypersurface degree discriminant implies

    49(s-r)^2 >= 60rs.

Thus r=s is impossible. If s=r+1, the left side is 49 while the right
side is at least 120. Hence s >= r+2, so the first two initial relation
spaces are precisely k f_r and f_r V. Every f_r has a linear factor
over the algebraically closed field. The theorem above contradicts the
accepted nonzero direction class.

Therefore every complete-intersection thickening of C0 in
characteristic zero has

    mu = 7d+14-4(a+b) > 0,
    n mu = 7 Asym + 2 Delta, n=ab/4.             (C)

This applies to the entirely thick and order-one branches. It excludes
all equality models at once, independently of the degrees of their
hypersurfaces or the degree of the first relation. For the retained
entirely thick (a,b)=(6,8) pair, d=6 is excluded and hence d >= 7,
mu >= 7. Positive-defect models remain unresolved.

## 6. New extension beyond equality: the first relation pays a defect

For any C0 presentation, put

    K_j = ker(Sym^j N_C^* -> L_j).

The kernel is a vector bundle on C0. The exact sequence, with torsion
in L_j retained, gives

    deg K_j = -7j rank K_j - Delta_j.           (D)

Suppose rank K_r = 1 and rank K_(r+1) = 2. The first assumption says
there is a unique initial relation in degree r; the second says its
linear multiples are the only relations at degree r+1. If Delta_r = 0,
twisting K_r by O(7r) gives a degree-zero line subbundle of a trivial
bundle on P1. It is O and its inclusion is a fixed nonzero binary form f.

Multiplication by the conormal bundle gives an injection

    O(-7(r+1)) tensor fV -> K_(r+1).

Its source and target have rank two. Their determinant degree
difference equals -Delta_(r+1) by (D), and also equals the nonnegative
length of their torsion cokernel. Since Delta_(r+1) >= 0, both are zero.
Thus K_(r+1) is exactly the constant bundle fV.

Sections 2--4 now contradict the accepted nonzero direction class.
Therefore, in characteristic zero,

    rank K_r = 1, rank K_(r+1) = 2
        imply Delta_r >= 1.                   (E)

No generic Gorenstein associated graded algebra, no zero total defect,
and no bounded degree pair is assumed in (E). This is a strict local
cost in the global degree/torsion budget. For example, inserting (E)
into (C)'s original nonnegative budget gives n mu >= 7 Asym + 2 whenever
these relation-rank hypotheses hold.

## 7. Fixed-direction effective-divisor extension

There is a further valid conditional extension. Suppose the generic
first relation direction is a fixed f, but

    K_r = O(-7r)(-D) tensor k f

for an effective divisor D, and rank K_(r+1) = 2. Since K_(r+1) has
generic direction fV and is a subsheaf of the conormal bundle, it is a
subsheaf of O(-7(r+1)) tensor fV globally. Projection to the quotient
by this saturated constant bundle annihilates its next-order symbols.
Relation lifting as above therefore gives an obstruction in

    H1(O(D-7)) tensor [Sym^(r+1)V/fV].

The new leading coefficient is the defining inclusion section of D.
The moving-base derivative of that coefficient contributes a multiple
of f and disappears in this quotient. Factor extraction gives, for
every factor m of invertible multiplicity,

    h_D h_m = 0 in H1(O(D-7)),                 (F)

where h_D is the section defining D. Thus the familiar pole-clearing
condition extends from a linear direction to every factor of an
arbitrary constant binary first relation. Here deg D = Delta_r by (D).

Any claimed numerical lower bound on deg D beyond (E), or restriction
on how many distinct factors f can have for a given deg D, must use the
specific apolar kernels of the accepted h_m classes. Such apolar claims
are not needed for the uniform equality exclusion proved above.

The accepted kernel descriptions cited in
`2026-10-06-localcoh-constant-direction-apolar.md` give the stronger
small-divisor classification now recorded in Section 6 of
`2026-10-13-generalization-thick-equality-extension.md`. Those accepted
kernels are used as inputs. The new comparison of their possible
common divisors was independently checked:

* No nonzero divisor of degree at most one annihilates a direction.
* A mixed finite direction theta != 0 first has a degree-three
  annihilator, uniquely proportional to st(t+2 theta s).
* The two endpoint directions require a divisor divisible by t^2 or
  s^2, respectively.

The mixed cubic has each endpoint only once, so it cannot kill either
endpoint class. Distinct mixed directions have nonproportional unique
cubics. A divisor killing both endpoint classes is divisible by s^2t^2
and has degree at least four. Therefore, under the fixed-direction
first-relation hypotheses,

    Delta_r >= 2;
    Delta_r <= 3 forces f to be a power of one linear form;
    f with at least two distinct linear factors forces Delta_r >= 4.

At degree two the single direction must be an endpoint, with its
doubled endpoint divisor. At degree three a mixed direction has the
unique divisor [0]+[-2 theta]+[infinity], while an endpoint has its
doubled endpoint plus one additional point. This is a necessary
classification of support directions and divisors, not a proof that
any surviving model has all higher obstructions zero.

## 8. Boundary of the result

The proof controls a fixed first relation and the actual next normal
layer. It fails if a new independent relation already appears at degree
r+1, or if the first relation varies in projective direction along C.
Those failures are concrete continuation strata, not silently excluded
cases. Positive defects can also clear the cohomological class as in
(F). The current results do not rule out those strata or resolve C0's
STCI status.

