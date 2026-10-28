# Lower bounds on the genuine residual degree

Date: 2026-10-28. Continued on
`codex/intersections-containing-quartic-2026-10-27`. **Provisional
quantitative synthesis with separately reviewed source deductions; no
canonical promotion.** The question is how the containing-intersection
work constrains \(\deg R\), without presuming a nonzero residual for every
characteristic-zero pair.

The [independent integration audit](2026-10-28-residual-degree-integration-audit.md)
checks the source combination and its stated limitations in addition to
the separate proof audits linked below.

## 1. Exact objects and the answer furnished by this pass

For the main comparison work over \(\mathbf C\), with the fixed
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). The marked attachment
bound also holds in arbitrary characteristic, and the normalization source
separately states its algebraically closed characteristic-zero scope.
Let \(F_a,G_b\) be actual homogeneous forms with no
common surface component and both containing \(C\). Write

\[
[Y]=[V(F_a,G_b)]=m[C]+R,\qquad \delta=\deg R=ab-4m.
\]

Let \(T\) be the full \(C\)-primary component and \(Z\) the genuine
linked residual, so \([Z]=R\). The once-linked curve \(Y:C\) is a
different object, of cycle \((m-1)C+R\) and fixed degree \(ab-4\).
Its flatness and Hilbert polynomial do not force a lower bound on
\(\delta\) without further information about the supported part.

There are several usable lower bounds. Some were already hidden in the
repository's October 19 work; the new contributions connect the marked
attachment module to degree, extend carrier capacity through numerical
pullback and normalization, and identify the precise hypotheses under
which full attachment and genus become quantitative.

| Independently controlled input | Lower bound on \(\delta\) | Scope |
|---|---|---|
| Marked attachment \(A=\operatorname{length}(C\cap Z)\) | \(\lceil A/3\rceil\) | Every proper pair; nonreduced residual allowed; also valid in positive characteristic |
| Same \(A\), no residual component on the quadric \(Q\) | \(\lceil A/2\rceil\) | Location hypothesis applies to every weighted residual component |
| Integral normal degree-\(a\) carrier, \(t=C_{\rm num}^2\) | \(b(16-at)/(12-t)\) | No Q-Cartier or reduced-residual assumption |
| Integral carrier smooth along all of \(C\) | \(b(4a^2-14a+16)/(4a-2)\ge ab/3\) | Inherited smooth-capacity result, recovered by the new formula |
| Exact normal orders \(r,s\), \(K=16(as+br)-7ab-28rs\) | \(\max(0,\lceil K/5\rceil)\) | Inherited October 19 bound, no integral-carrier hypothesis |
| Same order data, no residual component on \(Q\) | \(\max(0,K)\) | Stronger inherited support-sensitive bound |

All scalar bounds must be rounded using \(\delta\equiv ab\pmod4\).
If both carriers are normal integral, apply the carrier formula in both
orientations and take the stronger result. Bounds can be combined when
their hypotheses hold simultaneously; none is universally the strongest.

Integral-carrier estimates also combine through factorization. If
\(F=\prod_i F_i^{u_i}\), each \(F_i\) is irreducible and the pair is
proper, cycle additivity gives

\[
\delta=\sum_{C\subset V(F_i)}u_i\deg R_i
       +b\sum_{C\not\subset V(F_i)}u_i\deg F_i.
\]

Here \(R_i\) is the genuine residual of \(V(F_i,G)\). Components
coinciding downstairs are still counted with their summed multiplicities.
Thus one may add the component estimates; factors missing \(C\) contribute
their entire intersection degree. In particular, if every integral factor
containing \(C\) is smooth all along \(C\), the inherited floor
\(\delta\ge ab/3\) also holds for this reducible or powered carrier.
This follows directly by intersecting each factor cycle with \(V(G)\);
properness excludes a common surface factor throughout.

## 2. A universal bridge from the attachment module

The [marked attachment proof](2026-10-28-residual-degree-attachment-detector.md)
and its [independent audit](2026-10-28-residual-degree-attachment-audit.md)
give a short scheme-theoretic argument. Choose a cubic through \(C\)
containing no component of \(Z\), using global generation of \(I_C(3)\).
It is a nonzerodivisor on the locally CM residual, and its zero scheme
there has length \(3\delta\). That finite scheme surjects onto
\(O_{C\cap Z}\), so \(A\le3\delta\). If \(q\) avoids all residual
components, use its degree two instead.

The [reviewed October 27 module identity](2026-10-27-absorption-attachment-module.md)
writes

\[
A=\tau+\eta,
\]

where \(\tau\) is torsion length in \(I_T/I_CI_T\) and \(\eta\)
is the zero-divisor degree of the actual equation determinant after
passing to its torsion-free quotient. Thus

\[
\boxed{\deg R\ge\lceil(\tau+\eta)/3\rceil,}
\]

with denominator two under the no-quadric-component hypothesis.
An independently controlled positive module contribution gives a genuine
positive residual bound, including when \(T\) is non-lci. Positivity of
that contribution for every possible pair has not been proved.

The factor three is attained by actual pairs on the smooth quadric:
\(Y=sC+B\), where \(B\) consists of \(2s\) trisecant rulings. Then
\(\delta=2s\), \(A=6s\), but the **full** attachment is
\(\operatorname{length}(T\cap Z)=6s^2\). This also proves that substituting
full attachment into the marked inequality would be false.

The preceding every-divisor construction can also concentrate the entire
marked attachment at one point while retaining a smooth integral residual
of the same degree. Thus attachment position or concentration alone does
not force a larger bound through this argument. The total length or
additional normal/valuation data must enter.

## 3. A new quantitative bound on normal carriers

The [normal-carrier source](2026-10-28-residual-degree-singular-carriers.md)
and [independent audit](2026-10-28-residual-degree-singular-audit.md)
make the smooth-carrier argument work when \(C\) is not Cartier. On a
resolution principalizing the actual curve ideal, write
\(I_C O_X=O_X(-Z_C)\), and \(H\) for the hyperplane pullback. Then
\(L=3H-Z_C\) is globally generated and nef.

Mumford's numerical pullback of the effective Weil residual is effective,
even without a Cartier multiple. Write \(M=C^{\rm num}\), \(t=M^2\).
Since \(R^{\rm num}=bH-mM\) and \(Z_C-M\) is exceptional,

\[
0\le L\cdot R^{\rm num}=b(3a-4)-m(12-t).
\]

Hodge index gives \(t\le16/a<12\), so division is legitimate:

\[
\boxed{\delta\ge b\frac{16-at}{12-t},\qquad
\delta\ge ab-4\left\lfloor\frac{b(3a-4)}{12-t}\right\rfloor.}
\]

This is a necessary quantitative condition. It is positive when the
normal Hodge gap \(16/a-t\) is positive, and gives zero on the numerical
proportionality boundary. The older October 17 proposal's pending
endpoint-sufficiency statement is not an input and is not promoted here.

For the actual marked singularity \(ty-z^q=0\), \(C=(y,z)\), the
resolution calculation gives

\[
t=15-4a-1/q.
\]

Hence **every proper mate** on a carrier smooth along \(C\) except for
this one marked A-type point obeys

\[
\delta\ge b\frac{4a^2-15a+16+a/q}{4a-3+1/q}.
\]

For \(a\ge4\), this implies the convenient coarse floor
\(\delta\ge5ab/13\). These are the carriers constructed in the preceding
work, for sufficiently large degree depending on the prescribed index.
Large local index by itself does not remove their residual capacity.
For a general marked singularity, the relevant correction depends on
discrepancies and where the strict curve meets the exceptional matrix;
the local index alone does not determine it.

## 4. Normalization and first-normal data broaden the usable input

The [normalization extension](2026-10-28-residual-degree-normalization.md)
and its [audit](2026-10-28-residual-degree-normalization-audit.md) allow a
nonnormal integral carrier. If its normalization has one divisorial inverse
\(\Gamma\) of \(C\), let \(f=\deg(\Gamma\to C)\),
\(e=\operatorname{ord}_\Gamma I_C\), and
\(\sigma=(\Gamma^{\rm num})^2\). Then

\[
\boxed{\delta\ge
\frac{be(16f^2-a\sigma)}{12f-e\sigma}.}
\]

The exact normal order of the carrier is \(ef\); the denominator is
positive, and an integer form also uses \(\delta\equiv ab\pmod{4f}\).
Isolated inverse points are retained in the principalization. This is
not a conductor-descent criterion. With several inverse curves, the source
gives explicit linear inequalities for their actual valuation vector,
rather than selecting one branch and discarding the others.

There is also an accessible input when the carrier has generic order one.
Let \(d_F\) be the binary-form gcd degree of its two first-normal
coefficients; these each have degree \(4a-7\). The inherited normal-sheaf
comparison bounds \(\sigma\le14-4a+d_F\). Substitution gives the
one-carrier corollary

\[
\delta\ge b\frac{4a^2-14a+16-a d_F}{4a-2-d_F},
\]

positive if \(d_F<4a-14+16/a\).
Its denominator is always at least five, since \(d_F\le4a-7\).
More strongly, if \(s\) is the mate's actual normal order, the graph's
existing root-slope refinement applies automatically to the saturated
normal direction of degree \(h=4a-7-d_F\). It gives

\[
\boxed{\delta\ge
\frac{b(4a^2-14a+16-a d_F)+4s d_F}{4a-2-d_F}.}
\]

If no residual component lies on \(Q\), replace the denominator by
\(4a-6-d_F\), also positive. Exact numerical self-intersection can
improve on this using finer singularity data. These comparisons matter:
the gcd corollary is an accessible application of retrieved machinery,
not a new uniformly stronger inequality than the October 19 results.

## 5. What the Fano and liaison descriptions do, and their limits

The [graph analysis](2026-10-28-residual-degree-blowup-bounds.md) and
[audit](2026-10-28-residual-degree-blowup-audit.md) recover the earlier
order-dependent bounds and identify their slack. With \(L=3H-E\), the
graph's nef cone is exactly spanned by \(H,L\). Therefore the new
\(V_5\) presentation gives no automatic extra linear nef inequality.
The universal coefficient five is attained by weighted trisecant residuals;
the no-quadric coefficient one is attained by general cubic-generated pairs.
For example \((a,b;r,s)=(6,6;2,2)\) forces \(\delta\ge4\), strengthened
to \(20\) if all residual components avoid \(Q\). This is a specified-order
statement, not a lower bound for all sextic pairs.

The [liaison budget](2026-10-28-residual-degree-liaison-budgets.md) and
[audit](2026-10-28-residual-degree-liaison-audit.md) use

\[
B=\operatorname{length}(T\cap Z)
=(a+b-4)\delta-2p_a(Z)+2.
\]

If \(Z\) is reduced, \(\delta\ge\lceil B/(a+b-2)\rceil\). If
\(H^0(O_Z)=k\), \(\delta\ge\lceil(B-2)/(a+b-4)\rceil\).
Nonreduced double lines show why arbitrary negative genus invalidates
an unqualified genus-only argument. Actual equations nevertheless give
a bounded full attachment for a degree-two genuine residual, and hence
an exact small-degree exclusion test. No matching degree/genus or Rao
module alone guarantees the proposed residual occurs.

These bounds are useful from an independently controlled lower estimate
\(B\ge B_0\) or a proposed family of primary structures. Once a full
primary decomposition and its degree have actually been computed,
\(m\) and \(\delta\) are already known; the bound is then a consistency
check rather than a computational shortcut.

## 6. What would make the residual small?

The normal-carrier inequality can be inverted. If one wants
\(\delta/(ab)\le\epsilon<1\), it is necessary that

\[
t\ge\frac{16/a-12\epsilon}{1-\epsilon}.
\]

Thus small residual degree requires the actual numerical curve class to
approach the hyperplane ray. In the marked-resolution description, the
adjunction correction must grow enough to approach that boundary. In a
generic-order-one equation, the first-normal common-zero divisor must be
large enough. Meanwhile the marked attachment module must satisfy
\(\tau+\eta\le3\delta\), so its contribution must also become small.

These are compatible quantitative targets for construction, not a proof
that the targets cannot be met. The next useful test is to compute the
marked correction or first-normal divisor in an actual carrier family,
combine the applicable bounds, and follow how those quantities change
in the flat once-linked family. At zero numerical gap, full inverse
support, conductor descent and actual equation presentation remain
essential. Nothing here gives a universal positive bound depending only
on arbitrary degrees when \(ab\) is divisible by four.

## Evidence and authority

The promoted conormal splitting R-0020 and inherited reviewed ideal-
generation, numerical-comparison and attachment-module inputs are used
with their exact scopes. October 19 residual inequalities remain reviewed
provisional evidence. New quantitative deductions have separate independent
audits linked above; they are not canonical records. Primary surface,
ribbon and Cartier-intersection references were checked live, with precise
sources in the individual notes. No literature novelty is claimed.

The [validation record](../validation/2026-10-28-residual-degree/README.md)
records review, local links and metadata checks. Proofs establish these
bounds; no inherited certificate rerun or finite sample is substituted for
a universal statement.
