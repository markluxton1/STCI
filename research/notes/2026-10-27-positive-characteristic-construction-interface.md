# Positive characteristic as a construction and residual-geometry interface

Date: 2026-10-27. Curve throughout:

\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k.
\]

**Status:** independently reviewed provisional explanatory deductions with explicit proofs;
the [independent audit](2026-10-27-positive-characteristic-interface-audit.md)
reconstructs the claims below. No canonical promotion and no novelty claim. The
guiding question is what intersections containing C look like, including
residual curves. The characteristic-zero STCI question remains open.

## 1. What was already known, and what is being added

The positive-characteristic STCI assertion for this monomial curve is known
in every characteristic p>0. Moh's official abstract states the stronger
projective-monomial-curve theorem. The repository already has an exact
construction on one quartic carrier, including its allowable mate degrees:

- [Exact mate degrees on the fixed cuspidal quartic carrier](2026-10-05-positive-quartic-carrier-optimality.md).
- [Recorded independent reconstruction, sections 4 and 6](2026-10-05-foundational-frontier-audit.md).

Those are reviewed historical evidence, **not a canonical result record**.
Their fixed-carrier theorem is used as an inherited premise, not promoted or
re-proved here. In contrast, [R-0021](../results/quartic_mu4_degeneration.md)
is canonical and treats only the prescribed (4,4) family. The extension of
its finite-group-scheme explanation below is a new proposal in this note.

The useful additional interpretation is that an entire all-prime family
trades actual residual components for infinitesimal thickness according to
the connected and reduced parts of a finite diagonalizable group scheme.
For odd primes this happens while the conormal splitting remains unchanged.
The first-normal determinant records the residual attachment divisor when
the characteristic does not divide the group order.

## 2. An explicit family over the integers

Choose q in the numerical semigroup <3,4>, q>0. Choose b,c>=0 with
3b+4c=q and put a=2b+3c. Thus a+b+c=q and 4a+b=3q. Set

\[
S=x_0x_3^3-x_2^4,\qquad
G_q=x_1^q-x_0^a x_2^b x_3^c,\qquad Y_q=V(S,G_q).\tag{1}
\]

Both forms vanish on C. This is a **proper global homogeneous** pair of
degrees (4,q), with no coefficient-field substitution. Its graded
coordinate ring over Z is free over Z[x0,x3] on

\[
x_2^j x_1^i,\qquad 0\le j<4,\quad 0\le i<q.
\]

Indeed first impose the monic relation for x2^4, then the monic relation
for x1^q. This proves flatness over Z and the relative complete-intersection
degree 4q. In each field the same iterated monic construction gives a
finite free algebra over k[x0,x3]; the two equations form a regular
sequence, and the projective curve is Cohen--Macaulay and pure.

The inherited normalization description is

\[
\nu:\mathbf P(1,1,4)\longrightarrow V(S),\quad
[s:t:z]\longmapsto[s^4:z:st^3:t^4].
\]

Pulling back Gq gives z^q-(s^3t)^q. This normalization is finite and a
universal homeomorphism in every characteristic, as established in the
historical fixed-carrier note. One can also read the component structure
directly from the dense torus without relying on the normalization.

On x0=1 with x2,x3 nonzero, put u=x3/x2 and w=x1/u. Then S=0 gives
x2=u^3, x3=u^4, and

\[
Y_q\big|_{\rm torus}
 =\operatorname{Spec}k[u,u^{-1},w,w^{-1}]/(w^q-1)
 =\mathbf G_m\times\mu_q.\tag{2}
\]

## 3. Complete cycle description in every characteristic

Over an algebraically closed field of characteristic p>0 write
q=p^e m, with p not dividing m. In characteristic zero put e=0,m=q.
The reduced torus components have w=zeta with zeta^m=1, and their closures
are the smooth quartics

\[
C_\zeta=[s^4:\zeta s^3t:st^3:t^4].
\]

Each has generic multiplicity p^e in positive characteristic and one in
characteristic zero. Their total degree, with multiplicities, is 4q.
They exhaust the complete-intersection degree; purity excludes embedded
zero-dimensional components or other residual curves. Consequently

\[
[Y_q]=p^e\sum_{\zeta^m=1}[C_\zeta],\qquad
m_C=p^e,\qquad \deg R=4(q-p^e).\tag{3}
\]

In characteristic zero Yq is the **reduced** union of q quartics: purity
plus generic reducedness of all components gives reducedness. In positive
characteristic its reduced support is exactly C if and only if q is a
power of p. The full scheme is then generically k(C)[epsilon]/(epsilon^q).
The arithmetic genus of every fiber of this specific (4,q) family is

\[
p_a(Y_q)=1+2q^2.
\]

This genus belongs to the full complete intersection. It must not be
assigned to its reduced support in characteristic p.

For example the same integral (4,3) pair gives three actual quartic
components in characteristic zero and one generically triple structure in
characteristic three. The (4,25) pair has 25 quartics in characteristic
zero, one length-25 support in characteristic five, and 25 reduced quartics
in every other characteristic. The displayed (4,25) degrees are specific
to this fixed quartic carrier; a different repository construction gives
(3,20) in characteristic five.

The inherited **minimum mate degrees on this S** are:

| Characteristic | Minimum q | One Gq |
| --- | --- | --- |
| 2 | 4 | x1^4-x0^3*x3 |
| 3 | 3 | x1^3-x0^2*x2 |
| 5 | 25 | x1^25-x0^18*x2^3*x3^4 |
| p>=7 | p | choose 3b+4c=p and a=2b+3c |

These are not global minimum defining degrees over all carriers. The
all-degree criterion for arbitrary, possibly non-binomial mates on S is
the historical statement p^{v_p(N)} in <3,4>.

## 4. Where the residual curves attach, and what normal data sees

Assume char(k) does not divide q. The distinguished component C has
generic multiplicity one and R is the linked residual scheme
(S,Gq):I_C. Write
p0=[1:0:0:0] and pinfinity=[0:0:0:1]. We obtain the exact intersection
divisor on the smooth C:

\[
C\cap R=(q+5)p_0+(3q-3)p_\infty.\tag{4}
\]

Here the equality means the effective Cartier divisor on C defined by
restricting the residual ideal; it specifies attachment length and
concentration, not the entire singularity or gluing type of Yq.

To prove it, on x0=1 use u=x1, Y=x2-u^3, Z=x3-u^4. Modulo (Y,Z)^2 the
two equations have coefficient matrix

\[
\begin{pmatrix}
-4u^9&3u^8\\
-b u^{q-3}&-c u^{q-4}
\end{pmatrix},
\]

where a term with zero coefficient is omitted, so no negative exponent
is intended in the q=3 case. Its determinant is

\[
(4c+3b)u^{q+5}=q u^{q+5}.\tag{5}
\]

On x3=1 use v=x2, X=x0-v^4, Y=x1-v^3. The equations are S=X and
Gq=(v^3+Y)^q-(v^4+X)^a v^b; their first-normal determinant is
q v^{3q-3}. The two endpoint charts cover C, giving (4). Their lengths
sum to 4q+2, matching the degree of
det(N_C^*) tensor O_C(4+q), since deg(N_C^*)=-14.

For completeness, the local residual-ideal fact used here is elementary
complete-intersection linkage. In a regular local ambient ring, let
I_C=(Y,Z) and (S,Gq)=A*(Y,Z)^t be a regular sequence. Then
((S,Gq):I_C)=(S,Gq,det A). Restriction to C is therefore the principal
ideal generated by det(A)|C. For this specific family the determinant
calculation gives the displayed divisor, without asserting a
classification of residual schemes.

The formal neighborhood along C consequently sees these attachment germs.
At the generic point it sees only the identity component of mu_q; the
other components disappear after completing at w=1. At the endpoints the
completions retain the attached branches and their nontrivial gluing.
The generic formal neighborhood alone therefore misses the residual
curves, while completion along the whole C has more information. Recovering
the projective closure or abstract global geometry of R is a separate
problem; this example does not supply a universal reconstruction theorem.

A gluing warning is already visible at q=7. Every other component has
intersection length three with C at p0, so six separate pairwise lengths
sum to eighteen. Nevertheless C intersect the **union** of the residual
components has length twelve at p0 by (4). The total curve is not locally
planar there, and scheme-theoretic intersection with a union does not
distribute into the sum of those pairwise lengths. On the infinity chart
S is smooth and the corresponding planar sum is eighteen. This is an
exact example of why the residual scheme and its gluing contain information
beyond a component list and pairwise contacts.

When p divides q, (5) vanishes identically and the first-normal map drops
rank generically. The full higher equations recover multiplicity p^e;
reading only first symbols loses it. Thus residual attachment and thickness
are two regimes of one actual family, and changing characteristic changes
which regime occurs.

## 5. The toric and finite-group interpretation

On the three-dimensional projective torus the relation vectors are

\[
\ell_S=(0,-4,3),\qquad \ell_G=(q,-b,-c).
\]

Their cross product is q(1,3,4). The generated rank-two lattice therefore
has index q in the saturated relation lattice of C. Equivalently its
quotient character group has torsion Z/q. Over characteristic zero this
torsion yields q distinct geometric sheets. In characteristic p a
p-primary torsion group gives a connected infinitesimal mu_{p^e}; its
geometric support is one sheet. The semigroup condition is what makes the
relevant torus character extend to a projective homogeneous equation at
the boundary. Torus lattice calculations alone do not establish that
extension.

This is a concrete interface with diagonalizable group schemes and toric
semigroup descent. It overlaps the established literature on binomial
STCI and p-gluing, so it is an explanatory connection rather than a
claim of a new general principle.

For odd p, [R-0020](../results/quartic_conormal_characteristic_jump.md)
still gives N_C^*=O(-7)^2, exactly as in characteristic zero. The
existence of these odd-characteristic pairs therefore shows that the
characteristic-two splitting jump is **not necessary** for positive-
characteristic STCI constructions. The broader mechanism here is
inseparability together with descent across a nonnormal carrier.

This explains failure of this particular binomial construction in
characteristic zero. It does not exclude a characteristic-zero pair with
different equations or carriers. Similarly [R-0012](../results/prescribed_z4_arithmetic_nonlifting.md)
concerns one prescribed embedded characteristic-two Z4 and two specified
unramified DVRs; it is not an obstruction to all characteristic-zero
STCI constructions.

## 6. Literature check and authority boundaries, 2026-10-27

1. **Moh (1985).** The [official AMS abstract](https://www.ams.org/proc/1985-094-02/S0002-9939-1985-0784166-1/)
   freshly confirms all projective monomial curves in positive
   characteristic are STCI. Its separate plane-projection criterion
   requires a center disjoint from the curve, birational image, and only
   cusps. We use only the first statement for this monomial C. The AMS PDF
   failed to open; theorem numbering and proof were not freshly inspected.
2. **Hartshorne (1979).** The [primary bibliographic record](https://www.jstor.org/stable/2373984)
   and [Singh--Walther's author-hosted paper, Example 3.5](https://www.math.utah.edu/~singh/publications/singh_walther_pure.pdf)
   identify the known positive-characteristic quartic result. The latter
   was opened and inspected. Hartshorne's original proof remains an access
   gap in this run. We do not assign him the exact equations of (1).
3. **Craighero (1981).** The [original NUMDAM scan](https://www.numdam.org/item/RSMUP_1981__65__177_0.pdf),
   printed pp. 178 and 190, explicitly includes the characteristic-three
   cubic/quartic example and credits Stagnaro (1980). This confirms the
   (3,4) case is classical. The OCR drops several characteristic exclusions;
   the hypotheses must be read with the scan and surrounding prose.
4. **Thoma (1989).** [Author-uploaded full text](https://www.researchgate.net/publication/243064039_Ideal_theoretic_complete_intersections_in),
   Theorem 2.2, states that a projective monomial space curve over an
   algebraically closed field of characteristic zero is STCI on two
   binomial surfaces exactly when it is already an ideal-theoretic CI.
   This is a binomial boundary, not a theorem about two arbitrary forms.
5. **Barile (2008).** The [journal PDF](https://www.mat.ucm.es/serv/revmat/vol21-1/vol21-1l.pdf)
   introduces the p-gluing connection and classifies characteristic sets
   for binomial STCI in simplicial codimension two. Its abstract and
   introduction were retrieved through indexed primary PDF text; a direct
   PDF retry returned HTTP 502. It is related toric context; the present
   specific calculation does not import that classification or assert
   that its hypotheses settle arbitrary hypersurface pairs.

The repository's [October 6 literature audit](2026-10-06-positive-characteristic-literature-audit.md)
and [October 10 refresh](2026-10-10-session-positive-characteristic-primary-refresh.md)
already preserve the affine/projective and cone-vertex boundaries.
Cowsik--Nori's affine-curve theorem does not replace the projective argument.
No current universal projective theorem is inferred from this bounded search.

## 7. Concrete construction-oriented continuation

1. Use Yq as a controlled residual laboratory: vary the mate by actual
   homogeneous forms on S and track which attachment divisors, generic
   multiplicities, and linked residual schemes occur. The fixed carrier's
   char0 no-mate theorem is an inherited constraint, so the purpose here
   is to learn residual dynamics and liftability, not to reopen that case.
2. On a **new higher-degree carrier**, seek a normalization with a graph
   divisor whose section descends in characteristic zero. The present
   model isolates the missing datum: a semigroup gap obstructs descent of
   the coefficient of z^{N-1}, while Frobenius removes precisely those
   offending coefficients. A constructive char0 analogue must solve that
   descent problem by different carrier geometry, rather than formally
   replacing a p-power by an ordinary power.
3. Compare the inseparable/connected-sheet regime with char0 degenerations
   that increase contact of residual sheets. Record the **full** linked
   scheme and conductor/attachment data as well as the cycle. A formal
   multiple structure or cancellation of a first-normal determinant does
   not itself yield two actual global equations.

## 8. Reproducible corroboration and review request

Run

```
python3 research/computations/verify_mu_q_residual_interface_2026_10_27.py
M2 --script research/computations/verify_mu_q_residual_linkage_2026_10_27.m2
```

The dependency-free verifier checks finite sparse two-chart expansions,
their determinant exponents, relation-lattice indices, and a finite
corroboration of the inherited prime minima. The universal statements
above rest on their proofs, not this finite enumeration. Independent
review should reconstruct flatness/purity, the mixed-characteristic cycle,
the colon-ideal use in (4), and the limits of the formal-neighborhood claim.

Execution on 2026-10-27 returned `PASS: 47 exact two-chart determinants and
relation-lattice indices` and `PASS: 11 inherited fixed-carrier prime minima
corroborated`. Repository whitespace validation passed at the same point.
The separate Macaulay2 computation forms the global colon ideal over QQ,
checks exact scheme union, and pulls the residual ideal back to C. For
q=3,4,7 it obtained residual degrees 8,12,24 and endpoint attachment lengths
(8,6), (9,9), (12,18), respectively. These finite examples independently
corroborate the linkage use, beyond the sparse first-symbol calculation.
