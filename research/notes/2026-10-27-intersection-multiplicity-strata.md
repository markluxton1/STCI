# Fixed-degree strata of intersections containing the quartic

Date: 2026-10-27. Author: coordinating agent. Status: **provisional deduction and organizing framework**; no claim of literature novelty or canonical promotion. The finite-jet argument below is an application of the already archived fixed-degree criterion, not a new solution of STCI.

## Exact question and inputs

Let \(k\) be algebraically closed, in any characteristic, and fix

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k.
\]

For positive integers \(a,b\), put \(V_d=H^0(\mathcal I_C(d))\). Work on the open locus

\[
U_{a,b}\subset\mathbf P(V_a)\times\mathbf P(V_b)
\]

of pairs with no common surface factor. Empty source spaces simply give an empty locus. Equal-degree pairs can instead be described by pencils on the appropriate Grassmannian; all the assertions below are invariant under change of generators of a pencil. This is a parameter space of **actual homogeneous equations with coefficients in \(k\)**.

For \(Y=V(F,G)\), set

\[
m_C(Y)=\operatorname{length}_{\mathcal O_{\mathbf P^3,\eta_C}}
\mathcal O_{\mathbf P^3,\eta_C}/(F,G),\qquad
[Y]=m_C(Y)[C]+R.
\]

Purity and the complete-intersection degree formula imply

\[
1\le m_C(Y)\le B:=\lfloor ab/4\rfloor,
\qquad \deg R=ab-4m_C(Y).                         \tag{1}
\]

The source for the finite truncation used below is [VI-011](../archive/space-curves-2026-10-19/space-curves-vi/state/artifacts/integrated/ARTIFACT-20260906-011-finite-normal-jet-certificate.md), §§1–3. That archived result has donor review evidence but is not a promoted canonical result in this repository. For this reason the short local argument is given explicitly rather than citing the archive as canonical authority. It is not a rerun of a historical computation.

## Multiplicity strata are closed within the proper-pair locus

**Proposition.** For every \(1\le r\le B\), the set

\[
U_{a,b}^{\ge r}=\{(F,G)\in U_{a,b}:m_C(Y)\ge r\}
\]

is relatively Zariski closed. Consequently the exact-multiplicity strata are locally closed, and the residual degree can only decrease under specialization that remains in \(U_{a,b}\).

**Proof.** On \(x_0\ne0\), write

\[
x_1=u,\quad x_2=u^3+X,\quad x_3=u^4+Y.
\]

At the generic point of \(C\), the completed transverse ring is \(K[[X,Y]]\), \(K=k\(u\)\). Let

\[
A=K[X,Y]/(X,Y)^{B+1},\quad D=\dim_K A=(B+1)(B+2)/2.
\]

A local Artin algebra of length \(m\le B\) has its maximal ideal annihilated by its \(m\)-th power: otherwise its first \(m+1\) successive nonzero quotients would give length at least \(m+1\). Thus the truncation recovers the actual generic length for every proper pair in this degree range. For the multiplication matrix

\[
T_{F,G}:A\oplus A\longrightarrow A,\qquad (h,k)\longmapsto hF+kG,
\]

one therefore has

\[
m_C(Y)=D-\operatorname{rank}_{K}T_{F,G}.           \tag{2}
\]

All truncated monomial multiples of **both** equations are columns; their two coefficient vectors alone do not generate the truncated ideal as a vector space. In the chosen chart, matrix entries are polynomials in \(u\), linear in the actual global coefficient parameters. Rank at most \(D-r\) means the relevant minors vanish identically as polynomials in \(u\). Their finitely many coefficients give finitely many polynomial equations over \(k\). The condition descends across the ordinary projective coefficient charts. This proves closedness. Formula (1) proves the specialization assertion. The empty case \(B=0\) needs no construction. ∎

Here specialization means specialization in the closure of a point or of a family, not comparison of unrelated closed points. No flatness of an independently chosen residual scheme is being asserted.

## STCI is a possible terminal stratum

If \(4\nmid ab\), there is no supported endpoint in these degrees. If \(4\mid ab\), put \(M=ab/4\). On \(U_{a,b}\),

\[
\operatorname{Supp}(Y)=C
\quad\Longleftrightarrow\quad
m_C(Y)=M
\quad\Longleftrightarrow\quad
(F,G)\in U_{a,b}^{\ge M}.                       \tag{3}
\]

Indeed, (1) leaves zero degree for any other curve, and a proper complete intersection has no isolated support components. Thus supported intersections form a **closed, possibly empty** locus inside the proper-pair parameter space. The ambient parameter space includes common-factor degenerations outside \(U_{a,b}\), where this interpretation cannot be used.

This provides a construction-oriented question: which components and specializations of the actual pair space raise \(m_C\), and can one reach the terminal stratum while keeping properness? It does not show that every intermediate stratum exists, that adjacent strata meet, or that a terminal stratum is nonempty. Residual degree zero remains a legitimate sought-for endpoint. There is no need to posit its impossibility as the organizing question.

## Residual absorption requires changes beyond a fixed boundary divisor

When a family stays in one exact-\(m_C\) stratum, its residual cycle **degree** stays fixed, while component structure, normalization genera, singularities, attachment, and gluing may change. The once-linked curve defined by \((F,G):I_C\) has fixed degree \(ab-4\) and arithmetic genus \((a+b-4)(ab-8)/2\), even after it retains some thickness on \(C\); at \(m_C=1\) it is the entire residual away from \(C\). Do not conflate this linked curve with removing the whole \(C\)-primary component. Moving the attachment divisor in the \(m_C=1\) locus does not by itself move toward STCI. When \(m_C\) jumps, the residual degree drops by positive multiples of four; one must recompute the supported primary component and linked residual scheme. Holding the Hilbert polynomial of the residual after removing the whole C-primary component fixed throughout such a jump would impose the wrong moduli problem; the once-linked curve legitimately has a fixed Hilbert polynomial.

There are three separate boundary phenomena worth recording in a family:

1. residual components acquire singularities or change gluing at fixed \(m_C\);
2. residual cycle mass transfers onto \(C\), raising \(m_C\), while the pair stays proper;
3. the equations acquire a common surface factor and leave \(U_{a,b}\).

Only the second moves toward the supported endpoint within the original problem. A construction search must distinguish all three.

The characteristic comparison supplies actual instances of mass transfer in arithmetic fibers: [R-0021](../results/quartic_mu4_degeneration.md) already proves the prescribed four-component family becomes a characteristic-two quadruple. The [new all-μ_q interface](2026-10-27-positive-characteristic-construction-interface.md) extends this organizing calculation provisionally. It does not provide a characteristic-zero path to the supported endpoint.

## What a useful computation would retain

For a chosen actual family of pairs, first remove the common-factor locus, then keep the multiplication matrix (2), its coefficient equations for each rank threshold, and the residual colon/saturation data on surviving components. Do not replace coefficient parameters in \(k\) with arbitrary elements of \(k(u)\). Use full homogeneous ideals to distinguish a genuine residual curve from vertical exceptional geometry. Compute at least one complete component or exact family; a few rank samples do not establish emptiness or a generic rank statement.

For characteristic zero, [R-0001](../results/quartic_carrier_exclusion.md) supplies the accepted closed low-degree boundary: a hypothetical supported pair must have both degrees at least five. This does not limit the utility of lower-degree residual examples as models. The first equal degree divisible-by-four degree product above that boundary is \((6,6)\); mixed degrees \((5,8)\) also pass this elementary divisibility test, whereas \((5,5)\) cannot be supported because \(25\not\equiv0\pmod4\). A \((5,5)\) family remains useful for understanding residual deformation, not for finding a supported endpoint in those fixed degrees.

## An explicit first construction locus in degree (6,6)

In characteristic zero put \(V=V_6\), so \(\dim V=59\) and \(\dim\operatorname{Gr}(2,V)=114\). The first-normal wedge is a linear map

\[
\Phi:\bigwedge^2 V\longrightarrow
H^0(C,\det N_C^*\otimes\mathcal O_C(12))
=H^0(\mathbf P^1,\mathcal O(34)).
\]

The [all-degree attachment calculation](2026-10-27-global-containing-intersections.md), §3, implies that \(\Phi\) is surjective: a surjective differential of the wedge map has image contained in the image of \(\Phi\). Thus its 35 coordinate equations are independent linear equations in the ambient Plücker space. For a proper pair the generic intersection length is one exactly when its two first-normal classes are independent. Consequently the **first increase of thickness** is the explicit linear section

\[
\{m_C\ge2\}=
U_{6,6}\cap\operatorname{Gr}(2,V)\cap\mathbf P(\ker\Phi).       \tag{4}
\]

This is not a statement that the intersection is transverse or has codimension exactly 35 on the Grassmannian. The projective dimension theorem gives only that every component of the projective linear section has dimension **at least \(114-35=79\)**. Its intersection with the proper locus is nonempty. For example set

\[
q=x_0x_3-x_1x_2,\qquad A=x_0^2x_2-x_1^3,\qquad
F_6=q\,x_0^4,\quad G_6=A^2.
\]

The factors \(q,x_0,A\) share no surface factor across \(F_6,G_6\). On \(x_0=1\), with \(x_1=u,\ x_2=u^3+X,\ x_3=u^4+Y\), one has

\[
A=X,\qquad q=Y-uX,
\]

so the generic transverse quotient by \((F_6,G_6)\) is \(K[[X]]/(X^2)\). This gives an actual proper point of **exact multiplicity two**, residual cycle degree \(36-8=28\). This elementary reducible-pair control is not claimed as a new construction in the literature. It fixes a nonempty starting locus for subsequent deformation.

A useful bounded next computation is to study components of (4), then impose the next full-jet rank condition \(m_C\ge3\), recording when equations become reducible, remain proper, or acquire a common surface factor. The terminal sextic condition would be \(m_C=9\). None of (4), its dimension lower bound, or the displayed multiplicity-two witness establishes that this terminal stratum exists or can be reached from that witness.

## Independent review and limits

Independent review is recorded in the [integration audit](2026-10-27-intersections-integration-audit.md). No finite rank matrix for an unresolved global endpoint has been eliminated in this note. Equations (2)–(3) define exact fixed-degree tests; they provide neither a uniform degree bound nor an unrestricted existence/nonexistence conclusion. The new contribution is the residual-inclusive use of the stratification to select construction problems and to distinguish meaningful specialization from degeneration out of properness.
