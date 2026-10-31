# Frobenius powers, lifting precision, and ramification

Fix \(C=[s^4:s^3t:st^3:t^4]\) with its integral embedding.
The [prime-to-p extraction theorem](PRIME_TO_P_POWER_EXTRACTION.md)
removes a power invertible in the residue field from an actual supported
lift. This note quantifies what happens to powers divisible by \(p\).
Finite-level statements impose the **strong** support containment below;
topological support on an Artin base is insufficient.

**Status, October 31, 2026:** independently reconstructed, reviewed
provisional results. No canonical promotion or unrestricted STCI conclusion.

## Strong lifts and the exact unramified precision shift

Let \(k\) be perfect of odd characteristic \(p\), and let
\((F_0,H_0)\), of degrees \((a,b)\), be a proper homogeneous pair
with sole geometric reduced support \(C_k\). Assume \(F_0\) is smooth
at the generic point of \(C\), and put \(r=ab/4\).
A **strong lift to precision \(N\)** is a flat complete-intersection
pair over \(W_N(k)\), reducing to the specified special pair, with
\[
 \mathcal I_C^{m}\subset(F,G)\subset\mathcal I_C,
\]
where \(m\) is its special transverse length. The curve is the same
fixed relative embedding throughout.

For \(n=p^e\), \(e\ge1\), and \(N>e\),
\[
 \boxed{
 (F_0,H_0^n)\text{ has a strong lift over }W_N(k)
 \iff
 (F_0,H_0)\text{ has a strong lift over }W_{N-e}(k).}
 \tag{1}
\]
All coefficients of both equations may vary. This is an equivalence of
existence, not a canonical correspondence of coefficient tuples. A factor
prime to \(p\) in the exponent can be extracted without precision loss,
so the shift for a general positive exponent \(n\) is \(v_p(n)\).

The special-pair and integral-kernel hypotheses are exactly those of the
extraction theorem. In particular, curve-containing coefficients lift
through every Witt reduction because the parametrization's restriction
kernel has an integral basis of differences of equal-image monomials.

## The local estimate with a loss of e digits

The generic normal-coordinate construction in the extraction proof gives,
for a strong powered lift, the augmented algebra
\[
 B=D_N[v]/(v^{nr}),
\]
where \(D_N\) is the generic-curve coefficient DVR modulo \(p^N\).
An image of a curve-containing lift of \(H_0\) has augmentation zero
and reduces to \(v^rU_0\), with \(U_0\) a unit.

For \(1\le k\le p^e\),
\[
 v_p\binom{p^e}{k}=e-v_p(k).
\]
For example, this follows from
\(\binom{p^e}{k}=(p^e/k)\binom{p^e-1}{k-1}\): the last factor
is a unit modulo \(p\), since the coefficients of
\((1+T)^{p^e-1}\) are \((-1)^j\) modulo \(p\).
For odd \(p\), \(s\ge1\), and \(k\ge2\),
\[
 ks-v_p(k)\ge s+1.
\]
Thus, in the truncated algebra, if \(x=v^rU+p^sA\),
\[
 x^{p^e}\equiv
 p^{e+s}v^{(p^e-1)r}U^{p^e-1}A
 \pmod{p^{e+s+1}B}. \tag{2}
\]
The term \((v^rU)^{p^e}\) vanishes exactly.

It follows successively that, for \(e+1\le j\le N\),
\[
 x^{p^e}\in p^jB
 \quad\Longrightarrow\quad
 x\in(v^r)+p^{j-e}B. \tag{3}
\]
Indeed, the linear term in (2) detects each coefficient outside \((v^r)\),
because multiplication by \(v^{(p^e-1)r}U_0^{p^e-1}\) is injective
on polynomials of degree below \(r\). Augmentation zero ensures that
the divided error at the next stage has order at least
\((p^e-1)r+1\), exactly the threshold of the global correction-space
identity in the extraction proof.

## Initial normalization and global correction

Take any curve-containing coefficient lift \(H\) of \(H_0\).
Equation (2), with \(s=1\), gives \(H^{p^e}\in p^{e+1}B\).
Modulo \(p^{e+1}\), this implies **global homogeneous** membership
\[
 H^{p^e}=cG+FL.
\]
To justify globalization, the Artin-base complete-intersection quotient
is Cohen–Macaulay, with the single associated prime
\((p,I_{C_k})\). Its homogeneous cone has no embedded vertex prime.
Vanishing at the generic point of \(C\), including after the faithful
formal completion used for \(B\), therefore implies membership in the
original homogeneous ideal. Degree gives a scalar \(c\); reduction and
coprimality of \(F_0,H_0\) give \(c\equiv1\pmod p\).
Rescale \(G\) by this unit and adjust its multiple of \(F\).
The case \(N=e+1\) needs only reduction to the original special pair;
for larger \(N\) this starts the congruence at precision \(e+1\).

Suppose now \(G-H^{p^e}-FL=p^jg\), \(e+1\le j<N\).
In \(B\), (3) and the divided form of (2) put \(\overline g\)
in the exact global space
\[
 H_0^{p^e-1}(I_C)_b+F_0S_{bp^e-a}.
\]
Write it as \(H_0^{p^e-1}h+F_0\ell\). Lifting \(h\) within
the fixed curve ideal, the updates
\[
 H\longmapsto H+p^{j-e}\widetilde h,
 \qquad L\longmapsto L+p^j\widetilde\ell
\]
advance the congruence by one digit. Flatness makes division by \(p^j\)
followed by reduction modulo \(p\) unambiguous.

At precision \(N\), (3) gives \(H\in(v^r)+p^{N-e}B\).
This also holds in the eliminated ambient power-series ring modulo
\(p^{N-e}\): a multiple of the old relation \(v^{nr}\) can be
absorbed into \(v^r\) without changing its unit coefficient.
Consequently the new pair \((F,H)\), by itself, has local quotient
\(D_{N-e}[v]/(v^r)\). Its special fiber is a proper complete
intersection, so it is flat. The same primary-ideal argument globalizes
its strong containment. This proves the forward implication of (1).

Conversely, lift a strong base pair from \(W_q(k)\) to \(W_{q+e}(k)\),
retaining containment of the fixed curve. On the lifted generic carrier,
\(H=v^rU+p^qA\). The same binomial estimate gives
\(H^{p^e}\equiv v^{rp^e}U^{p^e}\pmod{p^{q+e}}\).
The powered pair is strong locally, and hence globally by primary
membership. This proves the reverse implication.

## Exact obstruction level for the prescribed quartic construction

For \(p\ge7\), use
\[
 F_p=X^p-x_0^aY^bZ^c,\qquad H_4=Y^4-x_0Z^3,
 \quad 3b+4c=p,\quad a=p-b-c,
\]
with positive \(b,c\) and \((X,Y,Z)=(x_1,x_2,x_3)\).
The base pair exists in characteristic \(p\), and the
[reviewed trace obstruction](MIXED_CHARACTERISTIC_TRACE_OBSTRUCTION.md#a-stronger-infinitesimal-statement-with-explicit-support-hypotheses)
excludes every strong \(W_2\) lift of it. Formula (1) therefore proves
\[
 \boxed{
 \text{maximum unramified strong precision for }(F_p,H_4^n)
 =1+v_p(n).} \tag{4}
\]
This bound applies to arbitrary lifted coefficients in both forms, not
only to a chosen integral representative.

It gives an exact degree-versus-precision tradeoff in this family. For
\(N\ge2\), a strong \(W_N\) lift requires \(p^{N-1}\mid n\),
and \(n=p^{N-1}\) attains the requirement. Thus the minimum larger
defining degree among these strong lifts is
\[
 \boxed{\min\max(p,4n)=4p^{N-1}\quad(N\ge2).} \tag{5}
\]
At \(N=1\), it is \(p\). The minimum ranges over lifts of the
prescribed powered-quartic special pairs, not all STCIs over
\(\overline{\mathbb F}_p\).

The naive integral forms exhibit the bound explicitly. Put \(n=p^e\)
and \(m=p^{e+1}\). On \(x_0=1\), fix \(X=t\), set
\(Y=t^3+v\), and solve \(F_p\) for \(Z\). The integer \(c\)
is a unit modulo \(p\), so this is an integral formal elimination.
At \(v=0\),
\[
 Z'(0)=-\frac bc\,t,\qquad
 H_4'(0)=\frac pc\,t^9.
\]
Since \(H_4\) has exact order \(p\) modulo \(p\), its literal
Taylor decomposition is
\[
 H_4=v^pU+pA,\quad U\text{ a unit},\quad
 A\in vD[v],\quad\deg A<p,\quad A'(0)=t^9/c.
\]
Thus \(A\) has exact order one modulo \(p\). Expanding gives
\[
 H_4^{p^e}\equiv v^mU^{p^e}
   +p^{e+1}v^{m-p}U^{p^e-1}A
 \pmod{p^{e+2}}.
\]
The terms beyond the linear correction vanish at this precision, including
when \(e=0\), when there are no such terms.

At precision \(e+2\), the quotient therefore has relation
\[
 v^m=-p^{e+1}v^{m-p+1}V(v),\qquad V(0)\text{ a unit}.
\]
Its Weierstrass basis is \(1,v,\ldots,v^{m-1}\). It follows that
\[
 v^{m+p-2}\ne0,\qquad v^{m+p-1}=0.
\]
The first expression is a nonzero unit multiple of
\(p^{e+1}v^{m-1}\); the second vanishes after a second substitution.
Purity globalizes the upper containment, while generic nonvanishing gives
minimality. Hence this naive pair has **global curve-ideal nilpotence
index \(m+p-1\)** at the first failed level, instead of the required
\(m\). Here the generic point is the point of \(C\) on the Artin
fiber, not the characteristic-zero generic fiber.

For every requested finite precision one can therefore construct such a
strong lift by increasing \(e\), and hence the degrees \((p,4p^e)\).
These are not compatible lifts of one fixed-degree presentation. The naive
characteristic-zero pair retains residual support, and (4) excludes any
unramified strong continuation beyond the stated level.

## Extraction when the absolute ramification index is below p minus one

Let \(R\) now be a complete mixed-characteristic DVR with
\(E=v_\pi(p)<p-1\), and suppose an actual supported trait reduces
to \((F_0,H_0^{p^e})\). Put \(\delta=eE\).
For \(s\ge1\), the valuation gap between the \(k\)-th binomial
term and the linear term is at least
\[
 (k-1)s-Ev_p(k)\ge1\qquad(k\ge2).
\]
If \(p\nmid k\), this follows from \(k-1\ge1\); otherwise use
\(k-1\ge(p-1)v_p(k)\) and \(E\le p-2\).
The preceding proof thus works with a loss of \(\delta\) powers of
\(\pi\): start at \(\pi^{\delta+1}\) and correct the root at
stage \(j\) by \(\pi^j h/p^e\), which is integral and tends to zero.
Tracking the initial scalar normalization gives
\[
 cG=H^{p^e}+FL,\qquad c\in R^\times.
\]
No root of \(c\) is needed; the generic pair \((F,H)\) has the
required lower degrees and sole support.

Applied to the prescribed powered-quartic pairs, the characteristic-zero
quartic exclusion proves that **any still-possible supported trait must
have \(E\ge p-1\)**. Exponents prime to \(p\) were already excluded
for every \(E\); this is a necessary ramification bound for the remaining
\(p\)-divisible powers. It is not a degree bound for arbitrary STCIs.

The inequality is essential to this proof. At \(E=p-1\), take
\(R=\mathbb Z_p[\pi]/(\pi^{p-1}-p)\),
\(B=R[v]/(v^{pr})\), \(r\ge2\), and \(x=v^r+\pi v\).
Then \(x^p\in\pi^pB\), but
\[
 \frac{x^p}{\pi^p}\bmod\pi
 =v^p+v^{(p-1)r+1}.
\]
Its order is \(p\), below the correction-space threshold
\((p-1)r+1\). This is a counterexample to extending the local Newton
estimate at the boundary. It is not an actual global supported trait.
The existence or exclusion of such traits at \(E\ge p-1\), and for
other special presentations, remains unresolved.

Combining this with prime-to-\(p\) extraction, any actual supported
characteristic-zero trait reducing to the prescribed
\((F_p,H_4^n)\) must satisfy
\[
 \boxed{p\mid n,\qquad\deg G=4n\ge4p,\qquad v_\pi(p)\ge p-1.}
\]
These are growing necessary bounds for **liftability in this specified
family**, not for every positive-characteristic STCI presentation of \(C\).

Independent reconstruction checked both directions of the finite-precision
equivalence, global membership over Artin bases, scalar normalization and
containment-preserving coefficient lifts, the new lower-multiplicity pair,
the explicit family's exact global nilpotence index, the ramification gap,
and the boundary counterexample. Finite-level heights here refer to strong
nilpotence, not merely to points of an incidence defined by field-valued
rank conditions. Every actual supported DVR trait has the requisite strong
nilpotence, so the resulting trait obstructions do apply.
