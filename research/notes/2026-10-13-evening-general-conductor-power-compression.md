# A degree-independent conductor power-compression theorem

Date: 2026-10-13. Root continuation. Status: **NEW WRITTEN THEOREM;
independent mathematical review pending**. Existing audited conductor and
quartic results are accepted as premises at the user's direction. This
note generalizes the single-field phase mechanism used in the quintic
Jbar-zero lane. It is not an assertion that its hypotheses hold on all
carriers, and no novelty claim is made.

## 1. Full Artinian descent, without bounding nilpotent length

Let A -> B be an injective finite map of commutative Artinian local rings
of characteristic zero. Put K=A_red and E=B_red. Assume K is a field
containing every root of unity and E is a field of finite degree r over K.
If u is a unit of B and u^n belongs to A for some n>0, then

    u^m belongs to A, where m=[K(bar u):K] <= r.

Moreover m divides n. Consequently u^N belongs to A for
N=lcm(1,2,...,r). There is no bound on the lengths of A and B, and the
conclusion is membership in the actual nonreduced ring A.

Proof. Write alpha=bar u. Since alpha^n belongs to K and K contains all
n-th roots of unity, K(alpha)/K is the splitting field of the minimal
polynomial of alpha: all its roots lie among zeta*alpha and hence in
K(alpha). In characteristic zero it is a cyclic Galois extension, with
Galois group a subgroup of mu_n. Its order m divides n and alpha^m
belongs to K. Set s=n/m and w=u^n in A. The polynomial V^s-w over A
has the simple nonzero residual root beta=alpha^m in K; its derivative
s*beta^(s-1) is nonzero. The Artinian local ring A is Henselian, so it
has a unique root v in A with residue beta. Its image in B and u^m
have that same residual root and satisfy the same equation. Uniqueness
in B gives v=u^m. This proves membership in A, including every
nilpotent layer.

This proof can also be given by finite Newton iteration along the
nilradical. The only general reference consulted here is the simple-root
lifting property in [Stacks, Henselian local rings, tag 04GE](https://stacks.math.columbia.edu/tag/04GE).

## 2. Global surface theorem

Let X be an integral Cohen--Macaulay projective surface over an
algebraically closed characteristic-zero field, with finite normalization
nu:S->X. Let L be a line bundle on X and Q a nonzero section of nu^*L.
Assume:

1. The zero divisor of Q contains no prime of the upstairs conductor.
   Thus Q is a unit at every generic conductor point in a local frame
   pulled back from X.
2. At every generic prime eta of the downstairs conductor, the reduced
   upstairs conductor algebra is a single field E_eta over k(eta), of
   degree at most a fixed r. All full nilpotent conductor structures
   are retained.
3. Q^n descends to a section of L^n for some n>0.

Then Q^N descends to a section of L^N, where N=lcm(1,...,r).

Proof. Let I be the full conductor. At eta the actual quotients
A_eta=O_X,eta/I_eta and B_eta=(nu_*O_S)_eta/I_eta are Artinian, and
the second hypothesis makes B_eta local. The first hypothesis makes
the local representative of Q a unit; apply section 1, since k(eta)
contains all roots of unity. The image of Q^N lies in A_eta for every
eta. Membership modulo I is equivalent to actual membership in
O_X,eta, because I is the same ideal on both sides of the conductor
square.

The sheaf T=nu_*O_S/O_X has no associated closed points. At a closed
point x of X, both O_X,x and (nu_*O_S)_x have depth at least two: the
first by Cohen--Macaulayness, the second by normality at the finitely
many points of S over x and finiteness. The depth lemma gives depth
T_x>=1 whenever T_x is nonzero. Therefore a section of T tensor L^N
that vanishes at every generic support point vanishes everywhere.
Apply this to the image of Q^N. This argument preserves pointwise
noninvertibility of the conductor; it does not discard it or assume
that the downstairs conductor is Cartier.

The depth facts can be expressed using [Stacks, Depth, tag 00LE](https://stacks.math.columbia.edu/tag/00LE)
and [coherent depth and associated points, tag 0340](https://stacks.math.columbia.edu/tag/0340).

## 3. All-mate-degree consequence on a hypersurface

Suppose X is an integral degree-a surface in P3, L=O_X(d) with d>0,
and the reduced zero support of Q is precisely nu^(-1)(C). If any
power Q^n is an actual mate section, the theorem gives one of degree

    b <= d*lcm(1,...,r).

Indeed Q^N descends, has exactly the same zero support, and lifts to
an ambient homogeneous form of degree Nd by the hypersurface sequence
and H1(P3,O(Nd-a))=0. Thus this entire class of unbounded mate degrees
reduces to one bounded degree. For r=1 it descends already; for r=2
it suffices to test Q squared; for r=3, exponent six suffices.

The section Q and its divisor ray are part of the hypotheses. A mate
with several independently varying lifted multiplicities does not
automatically supply a fixed Q of bounded degree. Producing such a Q
uses a separate Cartier/Picard or exceptional-lattice argument.

## 4. Essential failure shields and the general research target

The single-field hypothesis is essential. For the diagonal subring
A=k in B=k x k and u=(1,zeta), with zeta of arbitrarily large finite
order n, u^n descends and no smaller positive power does. The sum of
residual field degrees is always two. Consequently neither the total
conductor degree nor a bound on Artinian length yields a uniform
phase exponent on split conductor algebras. The geometric exclusion
of split branches in existing proofs is doing real work.

In characteristic p, the derivative used above can vanish; nilpotent
depth can then require further p-powers. This is consistent with the
repository's Frobenius constructions. The characteristic-zero
hypothesis cannot be removed from this argument.

The useful degree-independent program is therefore:

* compress the lifted divisor ray to a primitive Cartier section Q;
* prove a geometric bound on residual field degrees on the actual
  conductor, and rule out uncontrolled split phases;
* apply full-ring power compression, then a ribbon/socle obstruction
  at the resulting bounded degree.

This avoids treating each mate exponent independently. The remaining
global bottlenecks are the primitive section degree, split conductor
phases, and coverage of entirely thick or generically nonregular
minimum carriers. None is assumed solved here.
