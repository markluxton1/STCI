# Independent geometric audit of the principal mate-candidate reduction

Date: 2026-10-09. Auditor: `normal_global_adversarial`. Status:
**PROVED HERE / independently accepted** for the geometric necessity.
The exact polynomial reconstruction and modular nonzero certificate
are separate computational obligations, not certified by this note.

Owner source:
[Principal weighted candidate](2026-10-09-session-mf6-principal-weighted-candidate.md),
especially section 2. This bounded audit checks the actual conductor
meeting, Hessian, formal branches, and the resulting necessary
multiple-root condition. No canonical frontier documents were edited.

## 1. A nonnormal mate carrier necessarily meets its conductor

Let X subset P3 be an integral quartic containing the fixed smooth
rational quartic C0. It is automatically regular at the generic point
of C0: a general integral plane quartic would otherwise have four
distinct singular points, contradicting arithmetic genus three.
The full argument is appended to the
[sectional-genus audit](2026-10-09-session-normalization-genus-zero-independent-audit.md).

Suppose a form G of degree b>0 has intersection support exactly C0.
For the finite normalization nu:S->X, the accepted full-support
argument gives a unique reduced smooth curve c isomorphic to C0,
div(nu^*G)=b c, and singleton entire normalization fibers above C0.
Normality of S supplies the purity needed to exclude isolated extra
zero components; no smoothness of the whole S is assumed.

If X is nonnormal, it has a codimension-one normalization defect.
Indeed X is a hypersurface and satisfies S2, so a defect supported
only in codimension two would leave R1 and force normality by Serre's
criterion. The actual conductor consequently has a curve component
upstairs E. It is distinct from c, since X is generically regular
along C0. The section nu^*G restricts generically nonzero to E, and
its line bundle is a positive power of the ample nu^*O_X(1).
On an integral projective curve such a section must have a zero;
otherwise it would trivialize a line bundle of positive degree.
Its zero lies on c by full inverse support. Thus there is a point
P in C0 which is actually nonnormal on X and whose normalization
fiber is nevertheless a singleton.

This argument uses an actual conductor curve, not a curve in a
Jacobian scheme or an arbitrarily chosen inverse-image branch. It
also remains valid if the point of S above P is singular.

## 2. A simple first-normal zero gives a nondegenerate quadratic pair

On the stated basepoint-free contact open, use regular ambient
parameters (x,m,y) with C0=(m=y=0) and write the first-normal term
of the actual quartic equation as h(x)m. At a nonnormal point P
the hypersurface is singular, so h(P)=0. Translate x(P) to zero.
If h has a simple zero at P, its quadratic Taylor part has the form

    a x m + A m^2 + B m y + C y^2,       a=h'(P)!=0.

There is no x^2 term because the equation vanishes on C0, and no
x y term because the first-normal y coefficient vanishes identically
in this direction frame. The x,m principal minor of the symmetric
quadratic matrix has determinant -a^2/4. Hence the Hessian rank is
at least two, independently of the other quadratic terms.

The basepoint-free condition on the direction frame is material:
it makes m,y regular normal parameters at every point where this
argument is used. A first-normal coefficient taken in a frame with
a pole or a zero would not justify this calculation. On the second
curve chart the same local argument applies, so an infinity point
is covered by the homogeneous multiple-root test.

## 3. Hessian rank at least two contradicts the allowed meeting

In characteristic zero, the formal splitting lemma puts a hypersurface
with a nondegenerate quadratic pair into the form

    Ahat = k[[u,v,w]]/(uv+g(w)).

For completeness, the two formal partial derivatives in the pair
variables have an invertible Jacobian. The formal implicit-function
theorem shifts their critical section to zero, and successive
formal coordinate changes eliminate higher terms involving that
pair. Completeness makes these degreewise changes converge; the
remaining function involves only w. This is the formal Morse argument
used here, not an assertion about an arbitrary tangent-only model.

If g is nonzero, write it as w^r times a unit and absorb the unit by
a formal coordinate change. At the singular point r>=2, the ring
k[[u,v,w]]/(uv+w^r) is a domain with isolated singular locus: its
partials are v,u,r w^(r-1). It is a hypersurface, hence S2, and is
regular in codimension one, hence normal. Normality of the completion
implies normality of the original local ring by faithful-flat descent;
see [Stacks, Lemma 15.44.7](https://stacks.math.columbia.edu/tag/07NU).
This contradicts P being an actual nonnormal conductor point. A
regular formal model would of course give the same contradiction.

If g=0, the completion has precisely two minimal branches, u=0 and
v=0, with normalization

    k[[u,w]] x k[[v,w]].

The algebraic local ring is excellent, since X is of finite type
over k. For an excellent local ring, the number of branches agrees
with that of its completion, and for a domain these branches count
the maximal ideals of its finite integral closure. Thus the actual
normalization fiber at P has two points. This follows directly from
[Stacks, Lemma 15.110.8](https://stacks.math.columbia.edu/tag/0C27).
It contradicts the singleton full fiber required by the mate.

Neither formal alternative is compatible with the conductor meeting
in section 1. Therefore the actual first-normal coefficient has a
multiple zero at some point of C0.

## 4. Accepted determinant implication and computational boundary

The geometric conclusion is: every hypothetical nonnormal mate carrier
on the specified contact open has a multiple zero of its actual
first-normal binary octic. If the checked chosen polynomial generator
is nonzero and spans the unique quartic carrier there, multiplication
by its parameter scalar and the frame unit d preserves multiplicities.
If that generator or its entire coefficient vector vanishes, its
binary-gradient determinant vanishes automatically. Thus the owner's
fixed binary-gradient Sylvester polynomial Delta gives a necessary
condition Delta=0, provided the claimed coefficient reconstruction
and spanning statement are independently certified.

The arithmetic argument for the stated bound is also valid conditional
on those exact inputs: H is an integral weighted sextic, Delta has
weight 210 and is nonzero on H. The finite cover

    P2 -> P(2,1,1),       [a:r:b] -> [a^2:r:b]

lifts the equations to ordinary degrees six and 210. Every irreducible
component of the lifted sextic dominates H, so no component lies in
the lifted Delta. Bezout bounds the intersection length by 1260.
At a principal point p!=0 with (r,b)!=(0,0), there are two distinct
projective lifts: [a:r:b] and [-a:r:b] cannot differ by scaling since
at least one of r,b is nonzero and a is nonzero. Hence at most 630
distinct principal points lie in that necessary candidate locus.

This audit does not independently replay the degree-210 determinant
weights, all eighteen ambient polynomial columns, or the modular
nonvanishing certificate. Their computational audit must be reported
separately. The bound is a bound on a necessary candidate locus, not
the exact nonnormal parameter set and not a survivor exclusion.

`git diff --check` passed after this independent geometric note was saved.
