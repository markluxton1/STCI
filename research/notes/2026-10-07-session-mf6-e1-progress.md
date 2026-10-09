# MF6 e=1 primitive-triple frontier

Date: 2026-10-07. Fixed C0, characteristic zero. **Status: structural
reconstruction and exact exploratory quartic data; no full e=1 exclusion
claimed at this checkpoint.** This continues the accepted e=0 type(4,5)
exclusion in `2026-10-06-session-mf6-progress.md`.

For e=1 the quotient of the balanced conormal bundle O(-7)^2 has
L=O(-6), kernel M=O(-8), and is specified by coprime homogeneous linear
sections A=a0+a1z, B=b0+b1z. Its projective basepoint-free condition is
`d=a0*b1-a1*b0 !=0`.

The exact moving-chart quadratic cocycle is

    h2=-(2A+zB)(12A^2+3z^2B^2+4z^2(A'B-AB'))/(8z^5).

Its primitive triple obstruction lies in H1(O(-4)), so it vanishes iff
the coefficients of z^-1,z^-2,z^-3 vanish. These are

    -b1(2a0b1+12a1^2+16a1b0+9b0^2)/8,
    -(2a1+b0)(8a0b1+12a1^2+4a1b0+3b0^2)/8,
    -a0(2a0b1+36a1^2+16a1b0+3b0^2)/4.

Exact saturation by d supplies the relations
`a0(2a1+b0)=b1(2a1+b0)=0`. On the locus where at least one of a0,b1
is nonzero, both must be nonzero and the complete solution is

    a1=-b0/2, a0b1=-2b0^2, b0!=0.

After quotient scaling and the actual ambient torus symmetry, this is
represented by `A=1+z,B=-2-8z`. The torus acts on the split frame by
`U_new=lambda^4 U,V_new=lambda^3 V,z_new=lambda z`; after scaling the
quotient parameter this transports `(A,B)` to
`(lambda A(z_new/lambda),B(z_new/lambda))`, justifying the normalization
without assuming an arbitrary frame GL2 or support PGL2 symmetry.

On the remaining boundary a0=b1=0, basepoint freedom says a1b0!=0.
After b0=1 the solutions are

    A=r z,B=1,
    (2r+1)(12r^2+4r+3)=0.

Thus all primitive e=1 triples lie in four torus orbits. This
classification's quadratic cocycle and saturation are still to be added
to a standalone verifier and independently audited; do not generalize
the finite representative calculations to e=1 triples with positive D2.

On each primitive direction the embedded triple is unique, since
H0(Hom(M,L^2))=H0(O(-4))=0. In the first chart let gamma be the
nonnegative Laurent part of h2 and use the constant Bezout gauge
`s A+t B=1`, where `s=b1/d,t=-a1/d`. The actual triple embedding is

    U=A y-t gamma y^2,
    V=B y+s gamma y^2.

The full 18-dimensional quartic ideal basis, reconstructed from the
original homogeneous generators, gives the following complete spaces:

- At A=1+z,B=-2-8z, gamma=192z+96 and the space of quartics containing
  the triple has dimension two. Its full matrix and two quartics are in
  `../scratch/session-mf6-e1-primitive.json`.
- At A=-z/2,B=1, gamma=0 and the complete quartic space is
  `q*H0(P3,O(2))`, dimension ten. Every such carrier has the unique
  quadric factor; the retained unique-quadric STCI obstruction excludes
  this primitive direction from a defining pair.
- The two conjugate roots of 12r^2+4r+3 are being checked over the exact
  quadratic field. No conclusion for these roots is claimed yet.

The next question is the cubic pole divisor for the two-dimensional
quartic pencil of the first orbit, followed by the full conjugate-root
fibers. The MF6 type `(d2,d3)=(0,4)` permits cubic poles of total degree
four. Both moving support charts must be included. The types `(1,3)`
and `(2,2)` still require defect-killed triple incidence and are open.

## Complete classification without relying on the saturation output

Here is a direct case argument for completeness. Write
`p=a0*b1`, and retain `d!=0`.

If a0 and b1 are both nonzero, the first and third obstruction brackets
must vanish. Subtracting them gives
`6(2a1-b0)(2a1+b0)=0`. If `a1=b0/2`, the first bracket gives
`p=-10b0^2`, while the middle bracket then gives `b0=0`, contradicting
p!=0. Hence `a1=-b0/2`, and the remaining brackets give
`p=-2b0^2`; in particular b0!=0.

If a0!=0,b1=0, basepoint freedom gives a1*b0!=0. The third bracket and
the middle equation require either `2a1+b0=0`, which makes the third
bracket `4b0^2!=0`, or both quadratic brackets

    36a1^2+16a1b0+3b0^2=0,
    12a1^2+4a1b0+3b0^2=0.

Subtracting three times the second from the first forces
`a1=3b0/2`, which contradicts the second. Thus this case is empty.
If a0=0,b1!=0, the first bracket and middle equation similarly require
both `12a1^2+16a1b0+9b0^2=0` and
`12a1^2+4a1b0+3b0^2=0`, unless `2a1+b0=0` already contradicts the first.
Subtracting the two forces that same excluded relation. This case is
also empty. The remaining a0=b1=0 case gives exactly the three r roots
already displayed. Thus no basepoint-free primitive direction is omitted.

On the principal branch scale the quotient so b0=-2 and a1=1. Then
`a0*b1=-8`. The ambient torus sends a0 to lambda*a0 and b1 to
b1/lambda. Taking lambda=1/a0 gives the specified representative. On
the boundary the ratio r=a1/b0 is unchanged by that torus, so its three
roots are retained individually.

## Complete generic-orbit pencil and all cubic poles

At `A=1+z,B=-2-8z` the constant Bezout pair is
`s=4/3,t=1/6`. The complete coefficient matrix obtained by substituting
`U=A*y-t*gamma*y^2,V=B*y+s*gamma*y^2` into all eighteen quartics and
requiring the y and y^2 coefficients to vanish has rank sixteen. Its
full kernel is a pencil `F=alpha*F0+beta*F1`; the exact bases are
reconstructed rather than assumed in
`../computations/verify_mf6_e1_primitive_type04.py`.

Use `m=B U-A V`, `ell=s U+t V`. Their inverse transformation is
`U=t m+A ell,V=-s m+B ell`. The quartic first coefficient h and cubic
coefficient T, defined by

    m=-gamma ell^2+(T/h)ell^3+...,
    T=gamma E-K,

are exactly

    h=(4z^2+2z+1)(64alpha z^3+64beta z^6+8beta z^3+beta)/1024,
    T=(2z+1)(1536alpha z^5+1152alpha z^4+448alpha z^3
              +48alpha z^2-24alpha z+4alpha
              +1536beta z^8+1152beta z^7+448beta z^6
              +240beta z^5+120beta z^4+60beta z^3
              +30beta z^2+15beta z+8beta).

Since D2=0 and the primitive quadratic root is regular, the exact local
third-piece lattice lemma gives `ord D3=max(0,ord h-ord T)` in this
chart. This includes repeated zeros with their actual multiplicities.

For beta!=0 normalize beta=1. Then h has degree eight and

    Res_z(h,T)=-27(8alpha-1)(8alpha+3)^3/2^26.

Every parameter except `alpha=1/8,-3/8` has gcd degree zero, giving
finite polar degree eight. At alpha=1/8 the exact gcd is proportional
to `2z+1`, degree one, giving degree seven. At alpha=-3/8 it is
proportional to `(2z-1)^2`, degree two, giving degree six. These are all
exceptional pencil parameters, and each already exceeds the required
four without an infinity inference.

At beta=0 normalize alpha=1. The finite h has degree five and its gcd
with T has degree two, giving finite polar degree three. A direct second
chart is required because h, as an O(8) section, has an infinity zero.
Here

    A_infinity=1+w, B_infinity=-8-2w,
    s_infinity=-1/3,t_infinity=-1/6,
    gamma_infinity=3w+6.

Substitute into the actual ambient chart

    U'=t_infinity m'+A_infinity ell',
    V'=-s_infinity m'+B_infinity ell',
    x3=1,x2=w,x1=w^3+2U',x0=w^4+V'/2+3wU'.

The quartic has

    h_infinity=w^3(w^2+2w+4)/16,
    T_infinity=-(w+2)(w^2+2w+4)(3w^3+3w^2-4w+2)/16.

The second numerator is a unit at w=0, so infinity adds three exact pole
units and `deg D3=6`. The generic orbit therefore satisfies
`deg D3>=6` for every nonzero quartic containing its primitive triple.

## The quadric-factor orbit

At r=-1/2 the full coefficient matrix has rank eight, and its
complete kernel is `q*H0(P3,O(2))`, dimension ten. This also contains
some order-two forms, but every form has the unique quadric factor and
none can occur in a defining pair for C0. If q divides the mate the
pair has a common surface. Otherwise the mate cuts a nonempty divisor
on the smooth quadric of class `(b,b)`. If its support were the integral
C0 of quadric class `(1,3)`, it would have to be a positive multiple of
that class, which is impossible. This is the retained unique-quadric
obstruction, applied to a factor rather than only to a degree-two
carrier.

## The two algebraic direction orbits

Let `q_r=12r^2+4r+3=0`; its roots are nonzero and distinct in
characteristic zero. They are two conjugate directions, not identified
by the torus. Their exact quadratic cocycle is identically zero, so
both primitive triple charts have gamma=0.

Over the exact quadratic field the full eighteen-column triple matrix
has rank sixteen. Its kernel is the complete pencil spanned by

    F0=x0^3x3-(r+3/2)x0^2x1x2+(r+1/2)x1^4,
    F1=x0x3^3+(r-7/6)x1x2x3^2+(1/6-r)x2^4.

The rank assertion is over Q(sqrt(-2)); conjugation verifies the other
root. Every displayed polynomial identity is checked modulo q_r, so
no special root or extra kernel is omitted.

In the finite frame `m=U-r z V,ell=V`, the pencil has

    h=alpha+beta(2r+2/3)z^8,
    T=beta(8r/9)z^3,
    m=(T/h)ell^3+... .

Both r and `2r+2/3` are units modulo q_r. If alpha*beta!=0, h has no
zero at z=0 and T has no zero away from zero, so the total finite cubic
polar degree is eight. If alpha=0,beta!=0 it is five at z=0.

The last member beta=0 has h=1 in the finite chart, so its entire pole
calculation is on the moving second chart. Now

    A_infinity=r,B_infinity=w,
    U'=r ell', V'=w ell'-m'/r.

Direct expansion of F0 gives

    h_infinity=w^8,
    K_infinity=(16r/27+4/9)w^3,
    T_infinity=-K_infinity.

The scalar `16r/27+4/9` is a unit modulo q_r, so infinity contributes
exactly five pole units. Thus every member of either algebraic direction
orbit satisfies `deg D3>=5`.

## Result, precise scope, and current audit status

Together the four complete primitive direction orbits either force an
inadmissible unique-quadric factor or have `deg D3>=5`. Therefore the
MF6 numerical type `e=1,(d2,d3)=(0,4)` is excluded on fixed C0, subject
to the independent audit now in progress. No e=1 direction with positive
D2 is covered by this proof: those triples are not primitive and need
additional defect-killing sections.

The full verifier reconstructs the universal moving-chart quadratic
cocycle, checks the primitive-direction constraints and their coprime
boundary, derives every complete quartic fiber, proves the exact finite
resultant and exceptional gcds, and expands both infinity boundary
members directly. Its assertions are exact over Q or the quadratic
field, with all roots and all pencil members retained. The companion
stdout is `../scratch/session-mf6-e1-primitive-type04-output.txt`.
The source is being freshly rerun after replacing a structural equality
comparison of two differently arranged resultant expressions by their
zero polynomial difference. That correction changes no mathematical
input or assertion. Root delegated an independent audit to the
`dx1_saturation` agent; its outcome will be appended here.

The types `(1,3),(2,2)` remain open. A useful next analogue is the
intrinsic annihilator of their cubic residue: their permitted excess
`deg(D3-D2)` is two and zero respectively. The degree-one normal quotient
changes the second-frame complement by a kernel multiple, so its cubic
transition can contain a quadratic f2 term; the constant-direction
transition must not be transferred verbatim.
