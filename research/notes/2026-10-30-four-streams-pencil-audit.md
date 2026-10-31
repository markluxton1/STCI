# Independent audit: the full-ideal pencil control family

Date: 2026-10-30. Reviewer: independent `pencil_audit` agent.

**Outcome:** the proposition in [the pencil proposal](2026-10-30-four-streams-pencil.md), §§1–4, passes independent reconstruction on its stated hypotheses. No material mathematical defect was found. This is reviewed provisional evidence, not a canonical promotion and not a construction for the fixed quartic.

## Scope and evidence

The tested setting is an algebraically closed field of characteristic zero, integers \(d\ge2,e\ge1\), \(n=d(e+1)\), and the actual homogeneous equations
\[
G=Y^n+X^d(Z^{de}-W^{de}),\qquad F=G+X^n.
\]
The support is the line \(L=V(X,Y)\). I read `research/INDEX.md` and `research/MAP.md` before the proposal and checked the precise structural dependency in [the October 19 Rees audit, §§2–4](2026-10-19-rees-residual-independent-audit.md). Its no-vertical-divisor and coefficient statements apply to this codimension-two regular immersion. They are independently audited evidence, not promoted canonical records. The argument below also reconstructs the relevant structural steps. No computational experiment or inherited proof execution was needed; the literature discussion was not independently re-audited.

## Algebra, support, and the actual blowup

Both carrier irreducibility arguments work. The factors \(Z-\zeta W\) of \(Z^{de}-W^{de}\) are distinct and do not divide \(X\), so Eisenstein in \(Y\) applies to \(G\). For \(F\), the polynomial \(H=X^{de}+Z^{de}-W^{de}\) is squarefree: a repeated irreducible factor would divide all three partial derivatives, whose common divisorial gcd is one. Also \(X\nmid H\). Any prime factor of \(H\) therefore has valuation exactly one in the constant term \(X^dH\), again giving Eisenstein. Primitivity in \(Y\) supplies the required Gauss-lemma passage to the full polynomial ring.

The equality \((F,G)=(X^n,G)\) proves sole reduced support \(L\), and \(X^n,G\) is a regular sequence. Both surfaces have all first derivatives zero along \(L\), since their normal orders are at least \(d\ge2\). At the generic point of \(L\), the quotient by \((x^n,y^n+A(t)x^d)\) has the \(n^2\) standard monomials stated in the proposal. These facts give a proper entirely-thick supported complete intersection, with generic multiplicity \(n^2\).

Regular immersion gives
\[
E=\mathbf P_{Y_0}(\mathcal I_{Y_0}/\mathcal I_{Y_0}^2),\qquad
E_{\rm red}=\mathbf P_L(\mathcal O_L(-n)^{\oplus2})\simeq L\times\mathbf P^1.
\]
The generator change from \((F,G)\) to \((X^n,G)\) is an invertible constant change of pencil coordinates. Thus the product's second coordinate really is the specified equal-degree pencil.

## The finite local normalization and its global consequence

Let \(K=k(t)\), \(A(t)=t^{de}-1\), and let \(R\) be the local ring at \((x,y)\) of the actual chart
\[
K[x,y,\lambda]/(\lambda x^n-y^n-A(t)x^d).
\]
The regular-sequence Rees presentation justifies this chart; its residue field at that prime is \(K(\lambda)\). In its fraction field set \(\beta=y^{e+1}/x\). Then
\[
\beta^d=\lambda x^{de}-A(t),\qquad x\beta=y^{e+1}.
\]
Consequently \(S=R[\beta]\) is finite and birational over \(R\). The polynomial \(B^d+A(t)\) is Eisenstein at \(t-1\), and remains irreducible over \(K(\lambda)\). Therefore
\[
S/(x,y)S=K(\lambda)[B]/(B^d+A(t))
\]
is a field. Finiteness and integrality over the local ring imply that \(S\) has exactly this one maximal ideal. The element \(\beta\) is a unit, because its \(d\)-th power is a unit of \(R\). Hence \(x=y^{e+1}/\beta\), and the maximal ideal of \(S\) is \((y)\). The one-dimensional Noetherian local domain \(S\) is a DVR. Being finite birational and integrally closed, it is the full normalization of \(R\), not merely an intermediate integral extension.

This proves precisely one normalized divisor over the generic point of \(E_{\rm red}\), with residue field \(k(D)(\lambda)\), where \(k(D)=k(t)(\beta)\) and \(\beta^d=1-t^{de}\). To pass globally, normalization of the three-dimensional blowup is finite. Every divisor above the center has a two-dimensional image under that finite map. Its image must therefore be the irreducible surface \(E_{\rm red}\); a one-dimensional blowup fiber over a closed point of \(L\) cannot receive such a divisor. Thus no hidden additional exceptional prime appears at a branch point or at infinity. There is exactly one exceptional prime \(T\).

The valuation has \(v(y)=1\), \(v(x)=e+1\), and \(v(G)=v(x^n)=n(e+1)\), because \(\lambda\) is a unit at the generic exceptional point. Accordingly
\[
\nu^*E=n(e+1)T,\qquad [k(T):k(E_{\rm red})]=d,
\qquad n(e+1)d=n^2.
\]
This checks the coefficient/finite-degree identity with the actual transverse length.

The global product conclusion uses more than birational ruledness. The map \(T^\nu\to E_{\rm red}\) is finite, and its field extension over the specified base is exactly \(K(\lambda)\subset k(D)(\lambda)\). The smooth product \(D\times\mathbf P^1\) is also finite and normal over \(L\times\mathbf P^1\), with this same field inclusion. Uniqueness of integral closure therefore identifies it with \(T^\nu\) over the base. This resolves the potential generic-to-global gap. It does not prove that the divisor \(T\) itself is normal.

## Branch behavior, controls, and geometric limits

Each of the \(de\) simple zeros of \(1-t^{de}\) is totally ramified with index \(d\). At infinity, \(s=1/t\) and \(\gamma=\beta s^e\) give \(\gamma^d=s^{de}-1\). The special fiber has \(d\) distinct nonzero roots, so infinity is unramified. There is no other ramification. Riemann–Hurwitz gives
\[
g(D)=\frac{(d-1)(de-2)}2.
\]
For \((d,e)=(2,1)\), the quartic pair has a rational double cover branched at two points, exceptional coefficient eight, and multiplicity sixteen. For \((2,2)\), the sextic pair has an elliptic double cover branched at four points, coefficient eighteen, and multiplicity thirty-six. These are exact specializations, not numerical tests.

Geometrically, normalization separates transverse root directions over the support into a connected cyclic cover. Its branch fibers are entire pencil-direction curves in the exceptional surface; they create no extra support curve in \(\mathbf P^3\). The smooth exceptional normalization has irregularity \(g(D)\), unbounded already for \(d=2\). Varying \(d\) also makes the local ramification index unbounded.

Two formulation limits should remain explicit. First, the degree is \(n=d(e+1)\): the family exists in arbitrarily large equal degrees, including every even \(n\ge4\), but does not claim a construction in every integer degree. Second, the changed “field of constants over the support” means the relative algebraic closure of \(k(L)\) in \(k(T)\), namely \(k(D)\); the absolute constant field remains \(k\).

The control refutes universal rationality, unramifiedness, and genus bounds based only on rational support, integral entirely-thick carriers, and an actual two-generator complete intersection. It establishes no realization for \(C_0\), no compatibility with its normal bundle or equation spaces, and no quartic-specific obstruction. The unrestricted characteristic-zero STCI question for \(C_0\) remains open. No source, canonical record, or navigation file was changed by this audit.
