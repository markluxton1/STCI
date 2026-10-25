# Independent audit of the four-section surface and its arithmetic

Date: 2026-10-24. Reviewer: independent agent `audit_arithmetic`.
Status: **independent reconstruction and final-draft review completed;
reviewed provisional geometry, not canonical promotion**.

The reviewed objects are the particular surface and complete intersection
\[
 X=V(x_1^4-x_0^3x_3),\qquad
 D=V(x_1^4-x_0^3x_3,\ x_2^4-x_0x_3^3),
\]
the curves
\(C_\zeta=[s^4:s^3t:\zeta st^3:t^4]\), and the base
\(A=\mathbf Z_{(2)}\). Characteristic-zero geometric assertions use an
algebraically closed field. Put \(p_0=[1:0]\), \(p_\infty=[0:1]\).

The reviewer first reconstructed the cone, ruled bundle, endpoint rings,
conductor and orbit-image algebra independently, before the author drafts
were available. Findings were communicated to the authors during drafting.
The completed [surface note](2026-10-24-four-sheet-ruled-surface.md) and
[arithmetic note](2026-10-24-ruled-surfaces-arithmetic.md) were then read
in full and compared with those reconstructions. This audit records that
final comparison, rather than treating an agreement of draft summaries as
review. The repository index and contribution protocol were read first.

The accepted [STCI-R-0021](../results/quartic_mu4_degeneration.md) is used
only for its stated flatness and fiber description of these prescribed
equations; its accepted proof was not rerun. All additional normalization,
incidence and arithmetic claims below have their own arguments. No
carrier exclusion, arithmetic nonlifting theorem, or unrestricted STCI
claim enters the audit.

## 1. Ruled bundle and finite normalization are different objects

Fixing \([s:t]\) gives the line
\[
 [a s^4:a s^3t:b:a t^4].
\]
The common vertex is \([0:0:1:0]\). Projection away from that vertex
gives the plane quartic \([s^4:s^3t:t^4]\), whose normalization has
hyperplane bundle \(\mathcal O_{\mathbf P^1}(4)\). Consequently the
smooth incidence surface, in the lines convention, is
\[
 M=\mathbf P_{\mathbf P^1}(\mathcal O\oplus\mathcal O(-4))
   =\mathbb F_4.
\]
This determines the index independently of any expected answer. The
subbundle \(\mathcal O\) gives a section \(E\) with normal bundle
\(\operatorname{Hom}(\mathcal O,\mathcal O(-4))\), so
\[
 E^2=-4,\quad E f=1,\quad f^2=0,\qquad H=E+4f.
\]
The tautological \(H\) has degree one on a ruling fiber and degree zero
on \(E\). Its complete system has six sections and maps to
\(\mathbf P^5\); the four displayed coordinates give the map to \(X\).
Since \(E\) contracts, \(M\to X\) is not a finite normalization.

For an independent ring check write
\[
 B=A[s^4,s^3t,s^2t^2,st^3,t^4,b],\qquad
 R=A[s^4,s^3t,t^4,b].
\]
The missing degree-one generators are integral over \(R\) and belong
to its fraction field: they are respectively
\((s^3t)^2/s^4\) and \((s^3t)^3/(s^4)^2\). The full fourth
Veronese semigroup is saturated in its exponent lattice. Its semigroup
ring over the normal DVR \(A\), and over either residue field, is
normal. Thus \(\operatorname{Proj}B=\mathbf P_A(1,1,4)\) is the
finite normalization, and \(M\) is its ruled resolution. The same
argument works in characteristic two; the normalization of this
particular surface family commutes with its two fiber changes.

The notation \(\mathbf P(1,1,4)\) uses the fourth Veronese of the
weighted ring: the variables \(s,t,b\) have weights \(1,1,4\).
There is no claim that its resolution is an intermediate \(\mathbb F_3\).

## 2. The conductor, including the vertex

In the chart \(x_3=1\), set \(v=s/t\), \(b=x_2\). The ring map is
\[
 A[v^3,v^4,b]\subset A[v,b].
\]
The numerical semigroup \(\langle3,4\rangle\) has gaps \(1,2,5\)
and conductor six, giving the transverse cusp and conductor \(v^6\)
away from the vertex. This alone does not establish the global conductor.

For the global check, a monomial \(s^a t^d\), with \(a+d\) a
multiple of four, belongs to the smaller base semigroup precisely when
\(a\ge 3j\), where \(j=d\bmod4\) lies in \(\{0,1,2,3\}\).
Using the congruence \(a+j=0\bmod4\), every such monomial with
\(a\ge6\) belongs, and remains in the smaller semigroup after adding
any exponent of the full Veronese. The only exponents below six that
can occur are \(0,3,4\); multiplying by an appropriate missing
degree-one monomial shows that none is in the conductor. It follows
that the full homogeneous conductor is
\[
 \mathfrak c=(s^6t^2,s^7t,s^8)=(x_1^2,x_0x_1,x_0^2)
             =(x_0,x_1)^2.
\]
Adjoining the independent vertex variable preserves this conductor
calculation, so it also checks the vertex. On \(M\), the common
factor of its generators is \(a^2s^6\); the remaining three monomials
\(s^2,st,t^2\) have no common zero. Therefore
\[
 \mathfrak c\mathcal O_M=\mathcal O_M(-2E-6f_\infty).
\]
The multiplicity two on the contracted section is part of the result.
The final surface draft has the complete conductor, rather than only
its reduced support.

## 3. Sections, endpoint ordering and full inverse images

On \(M\setminus E=\operatorname{Tot}(\mathcal O(4))\), use the fiber
coordinate \(q\). The graphs \(q=h\), for
\(h\in H^0(\mathcal O(4))\), are disjoint from \(E\), hence have
class \(H=E+4f\), square four and normal bundle \(\mathcal O(4)\).
The four strict lifts have \(h=\zeta st^3\). Their difference has
divisor
\[
 \operatorname{div}(st^3)=3p_0+p_\infty.
\]
An initial reviewer message reversed the endpoint labels; that message
was corrected immediately. The final author notes and this audit all
use the displayed ordering. The intersection length is four on \(M\).

Downstairs, on \(x_0=1\), the curve equations are
\(x_3=u^4,\ x_2=\zeta u^3\), giving length three at \(p_0\)
after adding the ideals of two distinct roots. On \(x_3=1\), they are
\(x_0=b^4,\ x_1=\zeta b^3\), giving length three at
\(p_\infty\). Thus the image intersection divisor is
\(3p_0+3p_\infty\), total length six. There is no common smooth
quadric on which these four different curves could be paired to infer
that number.

The additional full inverse-image assertion was checked directly. Set
\(c=\zeta^{-1}\), \(l=v-cb\), and
\(Q=v^2+cvb+c^2b^2\). Then
\[
 (v^4-b^4,v^3-\zeta b^3)=l\,(Q,b^3).
\]
Indeed the cubic factors as \(lQ\), and the cofactor of the quartic
is congruent to \(c^3b^3\) modulo \(Q\). Since \(c\) is a unit,
this gives the stated ideal equality. The quotient by \((Q,b^3)\)
has length six: it is free of rank two in \(v\) over
\(k[b]/(b^3)\). Thus the full inverse image consists of the reduced
section with an embedded correction of length six at the cusp point.
This verifies the author's distinction between full scheme inverse
image and strict or reduced lift. The calculation remains valid for
\(\zeta=1\) in characteristic two.

Three successive blowups of the common point above \(p_0\), followed
by one above \(p_\infty\), resolve the graph pencil. Locally
\(q=\zeta u^3\) becomes \(q_1=\zeta u^2\), then
\(q_2=\zeta u\), then \(q_3=\zeta\). The other endpoint already
has distinct tangent directions \(q=\zeta v\). These are exactly
the pencil's four basepoints, including infinitely near points, and
the final strict sections are disjoint with square \(4-3-1=0\).

## 4. Orbit images and the exceptional endpoint base change

The arithmetic graph divisor
\[
 D_M=V(q^4-h^4),\qquad h=st^3,
\]
has class \(4H\), avoids \(E\), and is finite flat of degree four
over \(\mathbf P^1_A\), by the monic basis \(1,q,q^2,q^3\).
The orbit map from \(\mu_4\times\mathbf P^1_A\) sends
\(q\) to \(\lambda h\). Reducing a possible kernel element to
degree at most three in \(q\) gives
\(\sum_{j=0}^3 a_jh^j\lambda^j\). The basis in powers of
\(\lambda\), and the fact that \(h\) is a nonzerodivisor, show
that its kernel is exactly \((q^4-h^4)\). This proof holds over
\(A\) and over \(k\), including the neighborhoods of both zeros
of \(h\). The orbit map is finite and is an isomorphism where
\(h\ne0\).

It is essential that the author now distinguishes the following two
operations. The fiber of the total scheme image at an endpoint is
\(\operatorname{Spec}A[q]/(q^4)\). The scheme image of the orbit
map of that endpoint point is the reduced fixed point \(q=0\).
Image formation does not commute with this endpoint base change.
In contrast, it does commute with the arithmetic specialization in
this example, since the nonzerodivisor argument survives modulo two.
This is a mathematical distinction, not a choice of terminology for
the word “orbit.”

The total divisor is reduced: it is flat over the parameter line and
over \(A\), and its generic polynomial has distinct roots over the
generic function field. A nilpotent vanishes generically and flatness
excludes the resulting torsion. Nevertheless its special fiber is
\(V((q-h)^4)=4C_1^M\), with just one reduced section. The special
group scheme \(\mu_4\) has length four and one geometric point;
the action retains its nilpotents.

The final added arithmetic intersection paragraph was also checked.
Over the explicitly changed base \(B=A[i]\), put \(\pi=1-i\).
Restricting the two graph ideals to one section gives the principal
ideal \(((\zeta-\eta)st^3)\). Its divisor on the regular arithmetic
surface \(\mathbf P^1_B\) is exactly
\[
 3[p_0]+[p_\infty]
   +v_\pi(\zeta-\eta)[\mathbf P^1_k].
\]
The differences of adjacent roots are associates of \(1-i\), and
the differences of opposite roots are associates of \(2\), with
\(v_\pi(2)=2\). Thus the claimed vertical multiplicities one and
two are correct. This verifies the total incidence specialization,
rather than retaining only the generic horizontal intersection
divisor. The base extension and root labels are stated explicitly.

## 5. Projective endpoint algebra and normalization of total space

The finite map from the ruled divisor to the projective intersection
is an isomorphism on \(x_0\ne0\). At \(x_3=1\) its rings are
\[
 A[y,q]/(y^4-q^{12})\longrightarrow A[v,q]/(v^4-q^4),
 \qquad y\longmapsto v^3.
\]
Here \(x_0=q^4\), \(x_1=y\), \(x_2=q\). Independently, the
images of the basis \(1,y,y^2,y^3\) are
\(1,v^3,q^4v^2,q^8v\) in the free module with basis
\(1,v,v^2,v^3\). This proves injectivity because \(q\) is a
nonzerodivisor. Finiteness follows from \(v^4=q^4\), and on the
dense chart \(q\ne0\) the inverse parameter is
\(v=y^3/q^8\). This verifies the stated scheme image and
componentwise birationality.

Modulo two the two rings are
\[
 k[y,q]/((y-q^3)^4),\qquad k[v,q]/((v-q)^4).
\]
Their reductions map isomorphically, while their embedded structures
at this endpoint differ. The final draft does not infer identical
endpoint algebra from identical reduced support or generic length.

Over \(A\), the total normalization of either reduced total curve
is
\[
 \mathbf P^1_A\sqcup\mathbf P^1_A\sqcup\mathbf P^1_{A[i]}.
\]
This follows from the factors \(q-h,q+h,q^2+h^2\), with integral
constant \(i\) on the quadratic factor. The source components are
normal and finite over the images, with the same component fraction
fields. Thus they give the full normalization. The intermediate orbit
parameter space \(\mu_4\times\mathbf P^1_A\) is reduced but not
normal; its constant ring normalizes to \(A\times A\times A[i]\).

The normalization's special fiber is
\[
 \mathbf P^1_k\sqcup\mathbf P^1_k\sqcup
 \mathbf P^1_{k[\epsilon]/(\epsilon^2)},
\]
because \(A[i]/2=k[i]/((i+1)^2)\). It is neither the normalization
of the reduced special curve nor even a reduced scheme. The latter
normalization is just one \(\mathbf P^1_k\). This proves the
claimed failure of normalization to commute with specialization for
the curve family, while retaining the different, positive answer for
the surface family in Section 1. After adjoining splitting roots the
normalization must be recomputed over that changed base; four
geometric generic components cannot silently replace the three
arithmetic components over \(A\).

## 6. The shared contact construction and its limits

The contact formulas were independently reconstructed from polynomial
coefficients. The middle coefficient of
\((t-us)^3(t-vs)\) is \(3u(u+v)\); away from the endpoints the
residual osculating relation closes to \(v=-u\). The corresponding
coefficient of \(((t-us)(t-vs))^2\) is
\(u^2+4uv+v^2\). Thus the bitangent multiplier scheme is
\[
 T_B=\operatorname{Spec}A[\lambda]/(\lambda^2+4\lambda+1).
\]
It is a finite flat subscheme of the endpoint torus, rather than a
subgroup over \(A\). Its reduction is \(\mu_{2,k}\).

The author's global comparison map
\[
 (p,\lambda)\longmapsto(p,q=\lambda^3st^3)
\]
is an actual family of graph sections. It is defined by the
weight-three action on the specified section of \(\mathcal O(4)\),
so it extends over both endpoints. This is stronger than comparing
supports of unrelated characteristic-two degenerations. On \(T_B\),
\[
 \lambda^3=15\lambda+4,\qquad
 \eta=\lambda^3\quad\Longrightarrow\quad
 \eta^2+52\eta+1=0.
\]
Since fifteen is a unit in \(A\), this cubing map is an isomorphism
onto the stated multiplier scheme. The same monic-basis argument as
in Section 4 verifies the image divisor
\(q^2+52hq+h^2=0\), including its endpoint neighborhoods.
On the special fiber it is \(2C_1^M\), embedded in the
\(4C_1^M\) orbit divisor; the multiplier inclusion is exactly
\(\mu_2\subset\mu_4\). No such inclusion holds on the generic
fiber. The osculating multiplier \(-1\) gives the single graph
section \(q=-h\), and specializes with multiplicity one. Its
residual graph must not be replaced by the whole special \(\mu_2\).

The base action \((u,q)\mapsto(\lambda u,\lambda^3q)\), which
preserves the distinguished graph, is different from fiber scaling,
which fixes \(u\) and permutes the four graph sections. The final
arithmetic draft explicitly retains this distinction. The comparison
depends on the marked coordinates, chosen \(F\), and weight-three
section. It is not a proved coordinate-free identification for an
unordered endpoint pair. That broader formulation remains open in
the author's stated questions.

## 7. Final outcome and remaining scope

No mathematical discrepancy remains in the reviewed final central
identifications, conductor, divisor classes, endpoint schemes,
normalization assertions, or marked weight-three specialization
construction. The initial endpoint-label reversal in a reviewer
message was corrected; the distinction between total orbit image and
individual endpoint orbit was requested during review and is present
in the final draft. The global conductor and embedded inverse-image
correction were independently checked rather than inferred from the
normalization's reduced support.

The four elementary transformations in the surface note's final
quadric bridge were also checked: with \(C:A=u^3\) on
\(\mathbb F_0\), the first three centers on the evolving negative
section lie on \(C\), while the fourth does not. Its squares are
\(6,5,4,3,4\), and its classes become \(E_j+3f\) for
\(0\le j\le3\), then \(E_4+4f\). This verifies the marked bridge
without identifying projective hyperplane classes or pretending it
is invariant under exchanging endpoints.

This audit certifies only the arguments for the specified geometric
and arithmetic configurations. It is not a novelty assessment,
canonical theorem promotion, or change to the STCI frontier.

## 8. Final synthesis comparison

The final [package synthesis](2026-10-24-p4-ruled-surfaces-synthesis.md),
Section 3's row for \(X=V(F)\) and Section 6's four-section and
arithmetic comparison, was read against the reviewed source notes.
The \(\mathbb F_4\) model, hyperplane and curve classes, conductor,
full inverse-image correction, endpoint intersections, orbit-image
distinction and weight-three comparison agree with the audited
arguments above. One wording correction was requested and then
confirmed in the revised Section 6: the special fiber of the total
normalization is now displayed explicitly as two reduced projective
lines and one projective line over \(k[\epsilon]/(\epsilon^2)\).
The text correctly distinguishes its three reduced support components
from the nonreduced third connected component. The added splitting-DVR
intersection formula was also reread and agrees with Section 4 of this
audit, including the stated adjacent and opposite root valuations and
the need to retain the vertical component. No discrepancy remains in
these revised synthesis passages. The review does not assert an
additional audit of the synthesis's separate cubic-scroll arithmetic
paragraph.
