# Independent audit: a rank-deficient normalization prime obstructs a mate

Date: 2026-10-08. Auditor: `normal_global_adversarial`. Status: **PROVED HERE,
independently accepted**, with the hypotheses below. No claim about all
nonnormal quartics is made by this lemma alone.

## Statement

Let k be an algebraically closed field of characteristic zero. Let
nu:S->X subset P^N be a finite birational morphism from a smooth projective
surface. Put H=nu^*O_X(1). Suppose there is a smooth integral curve c on S,
a section f of O_S(H) with div(f)=c, and a homogeneous polynomial G of
degree n>0 such that

    nu^*G=lambda f^n,       lambda in k^*,

as sections of O_S(nH). Suppose also that nu|c maps isomorphically to a
smooth embedded curve in P^N. Let E be an integral curve on S distinct
from c, with H.E>0. Then the differential

    dnu:T_S|E -> nu^*T_(P^N)|E

has generic rank two.

Equivalently, a prime E of generic differential rank at most one and
positive H-degree contradicts this collection of hypotheses. The curve
E need not be smooth, and E need not be a conductor prime. In the
application, E is an actual conductor prime and c~H, with H ample.
The characteristic assumption can be weakened to n nonzero in k.

## Proof with the extension at f=0 retained

Since c.E=H.E>0, choose a closed point P in c intersect E. The immersion
nu|c into P^N implies that dnu_P is nonzero on the tangent line T_P c.
In particular its rank is at least one.

Assume that dnu has generic rank at most one on E. Every two-by-two
minor of a local matrix for dnu is then zero in the function field of
the integral curve E, hence zero in O_E wherever that matrix is defined.
Consequently the rank at every point of E is at most one. At P it is
exactly one. After shrinking an open neighbourhood of P in E, an entry
of the matrix is a unit, so the map has constant rank one on that
neighbourhood. Its kernel K is therefore a line subbundle of T_S|E.
This elementary constant-rank assertion holds over O_E even when E is
singular: use the unit entry to perform row and column operations; all
remaining matrix entries vanish because its two-by-two minors do.

Choose an ambient hyperplane section h with h(nu(P)) nonzero, and shrink
the neighbourhood in S so that nu^*h is a unit frame for O_S(H). Write

    f=g nu^*h,        A=G/h^n on the ambient affine chart.

The global equality of sections becomes the equality of regular
functions

    nu^*A=lambda g^n.

For any local generator v of K, the differential of every ambient
function annihilates v, so

    0=d(nu^*A)(v)=lambda n g^(n-1) dg(v) in O_E.

The section g is nonzero at the generic point of E because E is
distinct from div(f)=c. The local ring O_E is a domain. Since n is
invertible, cancellation in this domain gives dg(v)=0 as a regular
section along E, including at P. This is the precise extension step:
no division by the value g(P)=0 is made.

At P, g is a local defining equation of the smooth curve c. Thus dg_P
is nonzero and ker(dg_P)=T_P c. The nonzero line K_P lies in this
kernel; both are one-dimensional, so

    T_P c=K_P=ker(dnu_P).

This contradicts the immersion of nu|c. Hence the generic rank on E
is two.

If the generic rank on E were zero, all matrix entries would vanish
on E and already contradict the immersion at P. The proof therefore
also handles the rank-zero case.

## Applicability to the scroll frontier

The previously audited mate reduction supplies exactly the required
data when S is a smooth rational quartic-scroll normalization of an
integral quartic carrying C0: the full inverse image of C0 is a single
smooth curve c isomorphic to C0, div(nu^*G)=n c, the torsion-free Picard
group gives c~H, and a section f with div(f)=c satisfies the full power
identity up to a constant. Finiteness makes H ample, so H.E>0 for
every conductor prime E.

Therefore every surviving smooth-scroll mate must have differential
rank two at the generic point of every actual upstairs conductor
prime. In particular a generically cuspidal normalization branch,
where one tangent direction is killed by the normalization map, is
excluded if that rank-one statement is verified for the actual
surface morphism. A conductor multiplicity by itself does not verify
that statement; the local normalization or transverse singularity
must still be identified.

For the proposed residual F2 divisor D=4F+2C_min, the implication is
conditional only on the local geometric identification of F as a
rank-deficient cuspidal branch. Once that identification is proved,
the lemma excludes it without any Gorenstein assumption on the
downstairs conductor and without extending a trace involution through
a nongorenstein point.

## Adversarial checks

- The argument differentiates the entire power identity, not its first
  normal coefficient or a chosen jet truncation.
- It uses a hyperplane frame pulled back from the ambient space; a
  general local frame could have a nonzero derivative on K.
- It cancels g only in the domain O_E before specialization, then
  specializes the regular equality dg(v)=0 at P.
- A local kernel generator need only be defined along E. A lift to a
  vector field on a neighbourhood of S is unnecessary: differentials
  restricted to E already pair with T_S|E.
- Singular E is harmless because a unit matrix entry and vanishing
  two-by-two minors give a locally free kernel near P.
- The positive intersection and the smooth embedded image are
  essential. Without either, the tangency contradiction need not
  arise. Characteristic dividing n invalidates the cancellation.

This is a structural obstruction. It does not by itself classify the
remaining nonreduced nongorenstein ACM cubic conductors.

## 2026-10-09 addendum: the local unit factor is harmless

Status: **PROVED HERE, independently accepted**. This is a stronger
local version. It does not require a global root section, a constant
factor, rationality of S, or a prescribed carrier degree.

Let nu:S->X subset P^N be a morphism, let P belong to a smooth integral
curve c on S, and suppose S is smooth on an open neighbourhood of P.
Assume nu|c is an immersion at P. Let E be an integral curve through P,
distinct from c, and suppose dnu has generic rank at most one on E.
If an ambient regular function A has pullback

    nu^*A=u f^m

near P, where f is a local defining equation of c, u is a regular unit,
m>0, and m is nonzero in the ground field, these hypotheses contradict
one another.

Indeed, the zero-minor argument in the original proof works on the
integral E near P. Rank zero at P already contradicts immersion; if
rank one, its kernel has a regular line generator V near P on E.
Pairing the differential of the entire equality with V gives

    0=f^m du(V)+m u f^(m-1) df(V) in O_E.

Since E is distinct from c, f is nonzero in the domain O_E. Cancel
f^(m-1) in that domain, obtaining the regular equality

    f du(V)+m u df(V)=0 in O_E.

Now specialize at P. The first summand vanishes because f(P)=0;
m and u(P) are nonzero, so df(V)_P=0. Smoothness of c identifies
ker(df_P) with its tangent line, and the nonzero kernel line of dnu_P
is precisely this line. This contradicts the immersion of nu|c.

Here V need only be a section of T_S|E. Pairing differentials with V
defines a derivation from O_S to O_E with the usual Leibniz rule; no
vector-field extension off E and no intrinsic derivation of O_E are
needed. The unit need not be a pullback from the ambient space.
The argument does not claim df(V)=0 at every generic point: for a
nonconstant unit, its regular relation with du(V), followed by
specialization at P, is what proves the contradiction.

### Consequence for an arbitrary finite smooth normalization

Let nu:S->X subset P^N now be finite with S smooth projective, and put
H=nu^*O_X(1). Suppose an ambient form G of degree b>0 has the entire
pullback divisor

    div(nu^*G)=m c,

where c is smooth integral, m>0 is nonzero in the ground field, and
nu|c is an immersion. On an affine chart obtained by dividing by a
nonvanishing ambient hyperplane to degree b, the pulled-back form is
u f^m with u a regular unit: equality of Cartier divisors on the
regular local ring at P provides this factorization.

The divisor identity gives m c~bH. Since H is ample, c is ample as
well (an invertible sheaf is ample if a positive tensor power is).
Consequently c meets every integral curve E distinct from c. Applying
the local lemma at such an intersection shows that dnu has generic
rank two on every such E. This includes every conductor prime
distinct from c, without requiring c~H, Picard-group torsion-freeness,
a global section cutting out c, or a globally constant power factor.

### Exact boundaries of the strengthening

- The distinction E!=c is essential. If E=c, the restriction of f to
  E is zero and the cancellation in its domain is unavailable.
  Ampleness ensures intersections with other primes; it does not
  remove this exception.
- The entire local pullback divisor must be m c near the chosen P.
  If another component of div(nu^*G) passes through P, its factor is
  not a unit and the specialization need not force df(V)_P=0.
- Immersion of nu|c at P is a separate hypothesis. A single smooth
  inverse-image curve alone does not establish it.
- Only smoothness of S near the selected P is needed, but the argument
  gives no conclusion when that intersection lies in the singular
  locus of a normalization. The singular-normalization boundary
  therefore remains.
- Characteristic dividing m invalidates this proof. Characteristic
  zero makes the relevant multiplicity automatically invertible.

No new classification of nonnormal carriers follows solely from this
local strengthening. The earlier historical nongorenstein-scroll
boundary was subsequently closed by the separate
[complete scroll audit](2026-10-08-session-scroll-nongorenstein-independent-audit.md).
