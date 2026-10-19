# Independent audit: double-divisor Picard detection and nonreduced moving roots

Date: 2026-10-19. Reviewer: `spectral_nilpotent_audit`, independently
reconstructing the proposal received from the parent investigation.
The final review also checks the actual written proposal
[A doubled-divisor obstruction to nonreduced moving spectral roots](2026-10-19-spectral-nonreduced-root-obstruction.md),
including its component arithmetic, movement-two dichotomy, and integral
`(1,k)` component assertion.

Status: **PASS as a new, scope-limited mathematical argument.** This audit
is evidence for a proposal; it does not promote a canonical result or edit
an accepted result. No inherited theorem or certificate was rerun.

## 1. Exact claims reviewed and authority used

The auxiliary claim is over a field `k` of characteristic zero. Put
`S=P1_k x P1_k`. Let `D` be an effective Cartier divisor of bidegree
`(a,b)` with `a>0` and `b>0`. The divisor need not be smooth, integral,
or reduced. For integers `u,v`, the implication to review is

    O_S(u,v)|_(2D) = O_(2D)  =>  u=v=0.                 (A)

Here `2D` means the closed subscheme with ideal `I_D^2`, not a disjoint
union of two copies of `D`.

The spectral consequence is over an algebraically closed characteristic-zero
field, on the rational base `C=P1`, and uses the **full** finite flat root
divisor `Z` of [STCI-R-0008](../results/spectral_root_picard_criterion.md).
Assume `Z` has bidegree `(epsilon,r)`, `epsilon>0`, `r>=2`, and there is
an everywhere-coprime second relation in the quotient by the first, of
degree `s>r`. Then

    Z is reduced.                                      (B)

The accepted premise R-0008 is exactly the implication from that graded
second relation to

    O_Z(0,s) = pi^*O_P1(n) = O_Z(n,0)

for an integer `n`. Its criterion includes nilpotents and does not require
a global second polynomial line. I read the canonical R-0008 record and
its preserved independent spectral audit before using this premise.

I also read [STCI-R-0009](../results/moving_purepower_boundary.md) and its
second-relation audit for the comparison in Section 5. Those accepted
claims were treated as premises rather than independently re-proved.

## 2. Independent proof of the double-divisor claim

Write `Omega=Omega^1_(S/k)` and let `L=O_S(u,v)`.

**Infinitesimal triviality kills the restricted logarithmic Chern class.**
Choose a trivialization of `L|_(2D)`. Locally along `D`, lift the chosen
nowhere-zero local section to a local frame of `L`: a lift is again a
frame after shrinking, because its reduction modulo `I_D^2` is a frame.
Transition functions for these frames then have the form

    g_ij = 1+h_ij,              h_ij in I_D^2.

The Leibniz rule gives

    d(I_D^2) subset I_D Omega.

Consequently `(dg_ij)/g_ij` is zero in `Omega|_D`. The cocycle defining
the Hodge Chern class `c1^H(L)` therefore has zero restriction in
`H^1(D,Omega|_D)`.

This argument uses only the ideal-square condition and the smoothness of
the ambient surface. It does **not** require smoothness or reducedness
of `D`. The relevant target is the ambient restriction `Omega|_D`, not
`Omega_D`; replacing it by `Omega_D` would lose the needed information.

**The restriction map is injective.** Since `D` is effective Cartier and
`Omega` is locally free, its restriction sequence is exact:

    0 -> Omega(-D) -> Omega -> Omega|_D -> 0.

On the product surface,

    Omega(-D) = O_S(-a-2,-b) direct_sum O_S(-a,-b-2).

For `p<0` and `q<0`, the Kunneth formula gives

    H^1(S,O_S(p,q))
      = H^1(P1,O(p)) tensor H^0(P1,O(q))
        direct_sum H^0(P1,O(p)) tensor H^1(P1,O(q))
      = 0.

Both indices of both summands of `Omega(-D)` are strictly negative, so
`H^1(S,Omega(-D))=0`. The long exact sequence therefore makes

    H^1(S,Omega) -> H^1(D,Omega|_D)

injective. The previous paragraph implies `c1^H(L)=0` in
`H^1(S,Omega)`.

**The ambient class detects both integers.** The two ruling summands
identify `H^1(S,Omega)` with `k direct_sum k`. Under this identification,
the classes of `O_S(1,0)` and `O_S(0,1)` are the two basis vectors, up to
the common harmless choice of transition-sign convention. This can be
seen directly on each `P1`: the transition function of `O(1)` gives the
nonzero Cech differential `dz/z`, the generator of
`H^1(P1,Omega_P1)=k`. Additivity of `dlog` now gives

    c1^H(O_S(u,v)) = (u,v).

Characteristic zero makes the map `Z -> k` injective. Thus `u=v=0`,
proving (A).

For source verification of the standard constructions only, the
[Stacks discussion of logarithmic Hodge Chern classes](https://stacks.math.columbia.edu/tag/0FLE)
and [the field-base Kunneth formula](https://stacks.math.columbia.edu/tag/0BEC)
were checked. The needed calculation and ideal-square argument are
given explicitly above; no external nonreduced-root exclusion was used.

## 3. Scheme-theoretic audit of the spectral consequence

Set `L=O_S(-n,s)`. R-0008 gives `L|_Z=O_Z`.

**The positive descent degree remains valid on a nonreduced root.**
For any effective Cartier divisor `Z` of bidegree `(epsilon,r)` and
any integers `x,y`, the divisor sequence and
`chi(O_S(x,y))=(x+1)(y+1)` give

    chi(O_Z(x,y))-chi(O_Z) = r*x+epsilon*y.

This calculation works for singular, reducible, and nonreduced `Z`.
Applying it to the trivial bundle `L|_Z` gives

    -n*r+s*epsilon=0,
    n=s*epsilon/r > 0.                                  (1)

There is no use here of a degree formula valid only for smooth curves.
It also follows by taking the finite-flat norm, as in the accepted
R-0008 evidence.

**Every reduced component moves in both rulings.** Write the effective
divisor on the smooth surface as

    Z = sum_i m_i D_i,

where each `D_i` is a reduced irreducible component of bidegree
`(a_i,b_i)`. Finiteness of `pi:Z->P1` excludes vertical components:
`b_i>0`. More explicitly, an irreducible curve of bidegree `(a_i,0)`
would be a fiber of the projection to the first factor over the
algebraically closed field, and hence could not map finitely onto the
base. This is precisely where finite flatness of the **full** root
scheme is used, rather than merely a generic binary form.

Restricting `L|_Z=O_Z` further to `D_i` gives

    0 = deg(L|_D_i) = -n*b_i+s*a_i.

The degree formula is an intersection number on the smooth surface and
is valid for a singular integral `D_i`. Since `n>0`, `s>0`, and `b_i>0`,
it follows that `a_i>0` as well.

**A repeated component contains its full double.** If some `m_i>=2`,
then `Z-2D_i` is effective. The corresponding inclusion of divisor
ideals is

    I_Z subset I_(2D_i),

so `2D_i` is a closed subscheme of `Z`. Hence `L|_(2D_i)` is trivial.
Both bidegree entries of `D_i` are positive, and (A) applies with
`(u,v)=(-n,s)`. It would force `n=s=0`, contradicting `s>r>=2`.

Thus all multiplicities `m_i` equal one. Finally, an effective Cartier
divisor on the smooth surface has no embedded associated components;
equivalently, its local equations factor in the regular local UFDs
with exponents given by these divisor multiplicities. Multiplicity one
along every prime component therefore means the scheme `Z` is reduced.
This proves (B), including the exclusion of nilpotents supported only
at special points; there are no hidden embedded nilpotents left after
the multiplicity check.

The proof actually needs only `s>0` and a descent
`O_Z(0,s)=pi^*O(n)` with `epsilon>0`; the stronger `s>r>=2` is retained
because it is the accepted second-relation interface being applied.

## 4. Audit of the component bound and movement-two additions

I independently checked Section 5 of the written proposal, after the
double-divisor argument and its consequences had been reconstructed.

Put `g=gcd(epsilon,r)`, `epsilon0=epsilon/g`, and `r0=r/g`. Equations
`n*r=s*epsilon` and `s*a_i=n*b_i`, with `s>0`, give

    r*a_i=epsilon*b_i,
    r0*a_i=epsilon0*b_i.

Since `gcd(epsilon0,r0)=1`, `epsilon0` divides `a_i` and `r0` divides
`b_i`. Thus `(a_i,b_i)=t_i*(epsilon0,r0)` for a positive integer `t_i`.
The total bidegree and the already proved reducedness give

    sum_i t_i=g.

Consequently the number of components is at most `g`, and `g=1` forces
an integral full root. Positivity of both primitive entries uses
`epsilon>0` and `r>0`, already present in the finite-flat root setup.
No unrecorded irreducibility assumption enters this deduction.

For `epsilon=2`, either `g=1` or `g=2`. In the first case the root is
integral. In the second case, the partitions of `2` into positive
integers are only `(2)` and `(1,1)`. They give respectively an integral
divisor of class `(2,r)`, or two distinct reduced integral divisors of
class `(1,r/2)`; the second possibility requires even `r`. This is an
exhaustive necessary classification under spectral descent, rather than
a sufficient condition for descent or ambient realization.

For completeness, the smoothness assertion for an integral divisor
`D` of class `(1,k)` does not assume that `D` is already normal. Its
projection `q:D->P1_direction` has degree one because
`deg(q^*O(1))=1`. It is nonconstant, hence dominant. Every fiber is
zero-dimensional: a positive-dimensional closed fiber would contain
the whole integral curve. The proper map is therefore quasi-finite and
finite. Its generic degree one makes it birational. A finite birational
map from an integral curve to the normal curve `P1` is an isomorphism:
locally its finite algebra lies in the common function field and is
integral over an integrally closed target ring, so equals that ring.
Thus `D` is indeed smooth and rational, including when `k>1` and its
other projection has ramification.

Two distinct such components have no common curve component, and their
intersection product on the smooth surface is

    (1,k).(1,k)=2k=r.

Because the intersection is proper, this equals its scheme-theoretic
length, even if some intersections are tangent or concentrated at fewer
than `r` distinct points. The written proposal correctly retains this
gluing locus rather than replacing the root by a disjoint union.

All additions in Section 5 of the written source therefore **pass**.
The source's characteristic-zero restriction is also correct. The
explicit diagonal counterexample in the next section remains valid and
explains why this scope cannot be broadened by the displayed proof.

## 5. Adversarial checks and indispensable hypotheses

1. **Triviality on the reduced support is insufficient.** On the diagonal
   `D` of class `(1,1)`, `O_S(-1,1)|_D` is trivial, but (A) proves its
   restriction to `2D` is nontrivial. Thus the argument genuinely uses
   the full root scheme and cannot be replaced by numerical degree or
   reduced-support torsion.

2. **Positive bidegrees are essential for (A).** If `D` is a fiber of
   class `(1,0)`, the nontrivial ambient bundle `O_S(1,0)` is already
   trivial on `2D`: it is pulled back from a line bundle trivial on a
   neighborhood of that base point. The vanishing calculation correctly
   fails when one bidegree entry is zero.

3. **Characteristic zero is essential.** In characteristic `p>0`, take
   the diagonal `D` and `A=O_S(-1,1)`. Since `A|_D` is trivial, local
   adjusted transitions are `1+h` with `h in I_D`. Then
   `(1+h)^p=1+h^p=1 modulo I_D^2`, since `p>=2`. Consequently the
   nontrivial ambient bundle `A^p=O_S(-p,p)` is trivial on `2D`.
   The logarithmic class also correctly loses integer detection in
   characteristic `p`. No arbitrary-characteristic claim should be made.

4. **Constant roots must remain outside (B).** For `epsilon=0`, the
   first relation may be a fixed binary form with a repeated constant
   root and a fixed coprime second binary form. Its nonreduced root
   divisor has only constant components. Equation (1) then gives `n=0`,
   so the positive-bidegree reduction fails exactly as it should.

5. **Generic coprimality is weaker.** R-0008 supplies triviality on all
   of `Z` only from an everywhere-coprime quotient relation. A generator
   that degenerates or loses coprimality at a special base point need
   not yield a trivialization. Such presentations are not excluded.

6. **Reduced need not mean smooth or irreducible.** The conclusion leaves
   singular reduced roots and unions of distinct moving components open.
   It does not imply the hypotheses of the smooth-root actual-CI bridge
   STCI-R-0006.

## 6. Novelty, exact frontier impact, and verdict

Within the relevant canonical records and their linked evidence, R-0009
excludes everywhere-coprime second relations when the full root is a
pure multiple of one moving graph. The new consequence (B) includes
that rational-base case and additionally treats mixed roots with at
least one repeated component of any positive bidegree, even when the
reduced component is singular or has covering degree greater than one.
It needs no classification of those components and no higher-order
ambient obstruction calculation.

This is a genuine extension of the **rational-base graded exclusion**;
it does not supersede the whole R-0009 record. R-0009 also treats
arbitrary smooth projective base curves in characteristic zero and
quantifies the actual degeneration divisor and defect cost, while the
present argument proves neither of those assertions.

No claim of priority in the external mathematical literature is made.
The new claim should enter as a reviewed proposal with this audit as
evidence. It is not currently a promoted result merely because this
audit passes.

If promoted, the precise change to the rational-base R-0008 frontier is:
for `epsilon>0`, the full root underlying an everywhere-coprime graded
two-relation pattern must be reduced. Nonreduced full roots under that
interface are closed by this argument. Reduced singular roots, actual
ambient lifting, special-point failures of coprimality or saturation,
other initial-ideal patterns, and the unrestricted characteristic-zero
STCI problem remain open. In particular this is not a theorem excluding
every nonreduced root that may arise somewhere in an actual STCI.

**Verdict:** (A), (B), the primitive component bound, the movement-two
dichotomy, and the smoothness/rationality of integral `(1,k)` components
pass independent mathematical reconstruction against the written source.
All scheme inclusions, cohomology vanishings, characteristic assumptions,
and component-degree implications have explicit proofs above. No
unresolved computational step or mathematical dependency remains within
the stated graded scope; canonical promotion remains a separate reviewed
repository action.
