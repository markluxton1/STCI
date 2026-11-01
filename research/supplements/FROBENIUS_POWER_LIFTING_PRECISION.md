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

## A sufficient approximation radius at arbitrary ramification

The same extraction has a conditional extension without a bound on \(E\).
Keep an actual supported trait, \(n=p^e\), and \(\delta=eE\).
Suppose there is a curve-containing ambient degree-\(b\) lift \(H\)
of \(H_0\) whose image in the normal block satisfies
\[
 H\in I_C^rB+\pi^sB,
 \qquad s>\frac{E}{p-1}. \tag{6}
\]
Then \(cG=H_\infty^n+FL\) for a scalar unit \(c\) and an
ambient degree-\(b\) form \(H_\infty\) containing the fixed curve.

Indeed, write \(H=v^rU+\pi^sA\). The gap
\((k-1)s-Ev_p(k)>0\) for every \(k\ge2\) starts the global
congruence at precision \(\delta+s\). At every subsequent stage
\(j\ge\delta+s\), the correction to \(H\) has valuation
\(j-\delta\ge s\). The strict gap, divided-error order and exact
global correction space therefore persist, and the coefficient sequence
converges as before.

Condition (6) is independent of the normal generator: \((v)\) is
the image of the fixed curve ideal. It is equivalent to saying that
\((F,H)\), with the **same lifted first equation**, is already a
strong lower-multiplicity pair over \(R/\pi^s\). To see this, the
old equation on the formal carrier generates \((v^{nr})\), so its
contribution can be absorbed into \(v^r\). Thus \(H\) is a unit
times \(v^r\) modulo \(\pi^s\); conversely, strong containment
and the special order \(r\) force that form. The usual primary
membership argument globalizes the generic containment.

For the prescribed powered-quartic family, any remaining trait must
therefore fail this approximation condition for **every** eligible
degree-four lift. Ramified base change is not a way to obtain (6): for a
fixed \(H\), it multiplies both the achieved approximation order and
\(E\) by the same factor. Producing a better ambient \(H\) would
be additional geometric input. This radius criterion is a conditional
bridge to extraction, not a construction of that input.

## Root specialization and the remaining endpoint defects

There is also an all-ramification geometric criterion. Keep an actual
supported trait with special pair \((F_0,H_0^n)\), and write
\(X=V(F)\) and \(Z_0=V_{X_0}(H_0)\). No normality assumption
on the carrier is added. On \(X_K\), let \(D_K\) be the pure
\(r\)-fold structure on \(C_K\): its ideal is the contraction
of \((v^r)\) from the smooth generic point of the curve. This is
a coherent primary ideal. Let \(D\subset X\) be its schematic
closure. Its quotient has no \(R\)-torsion, hence is flat, and its
underlying support is the fixed \(C_R\).

At the generic point of \(C_0\), the relative carrier is smooth and
the curve is Cartier. The root closure therefore has ideal \((v^r)\).
Thus \(D_0\) and \(Z_0\) agree generically. Purity of the complete
intersection \(Z_0\) gives
\(I_{D_0}\subset I_{Z_0}\): the image of the first ideal in
\(\mathcal O_{Z_0}\) vanishes generically and so vanishes everywhere.
Consequently there is an exact sequence
\[
 \boxed{0\longrightarrow T\longrightarrow\mathcal O_{D_0}
 \longrightarrow\mathcal O_{Z_0}\longrightarrow0,
 \qquad T=I_{Z_0}/I_{D_0},\quad\dim\operatorname{Supp}T\le0.} \tag{7}
\]
The zero-dimensional sheaf \(T\) is precisely the embedded-point
part of this special fiber. Unlike \(Z_0\), \(D_0\) is not
assumed pure. At every point where \(X_0\) is smooth along the
curve, the same relative Cartier argument gives the local root ideal
\(I_{C_R}^r\), so \(T\) vanishes there.

If \(T=0\), then \(D_0=Z_0\) is Cartier on \(X_0\).
Flatness of \(D\) and \(X\) lifts Cartierness to a neighborhood
of the special fiber. The remaining non-Cartier locus is closed in the
proper \(X/R\); if nonempty its image would meet the closed point
of \(\operatorname{Spec}R\). Hence \(D\) is Cartier everywhere.

This Cartier extension forces an actual degree-\(b\) equation.
Indeed, set
\[
 M=\mathcal O_X(D)\otimes\mathcal O_X(-b).
\]
Its special restriction is trivial, and the hypersurface sequence gives
\(H^1(X_0,\mathcal O_{X_0})=0\). The
[Picard exact sequence for square-zero thickenings](https://stacks.math.columbia.edu/tag/0C6Q)
therefore makes every map
\(\operatorname{Pic}(X_{N+1})\to\operatorname{Pic}(X_N)\)
injective. All restrictions of \(M\) are trivial. Since
\(H^0(X_N,\mathcal O_{X_N})=R/\pi^N\), their trivializations
can be made compatible. Proper formal full faithfulness over the complete
base gives \(M\simeq\mathcal O_X\).
[Grothendieck existence and full faithfulness](https://stacks.math.columbia.edu/tag/088C).

The canonical section of \(D\) is now a section of
\(\mathcal O_X(b)\). It lifts to an ambient form \(H\), because
\(H^1(\mathbf P^3_R,\mathcal O(b-a))=0\). Its zero scheme
on \(X\) is \(D\), so \((F_K,H_K)\) is a supported
degree-\((a,b)\) pair. The section also vanishes on the fixed
\(C_R\), since it does so generically and \(\mathcal O_{C_R}\)
is flat. This implication holds for every ramification index and every
\(n\); no division by \(p\) occurs.

For the prescribed powered-quartic family, the quartic exclusion thus
forces \(T\ne0\). The carrier \(F_p\) is smooth along \(C\)
away from its two parameter endpoints \(p_0,p_\infty\). Every
still-possible actual trait must therefore satisfy
\[
 \boxed{0<\operatorname{length}T,
 \qquad\operatorname{Supp}T\subset\{p_0,p_\infty\}.} \tag{8}
\]
Lengths here include residue-field degrees if the residue field is not
algebraically closed. Flat projectivity and (7) also give the exact genus
deficit
\[
 \boxed{p_a(D_K)=1+2p^2-\operatorname{length}T,} \tag{9}
\]
since the base \((p,4)\) complete intersection has arithmetic genus
\(1+2p^2\).

Thus the remaining issue is a nonzero endpoint defect in specialization
of the lower root, rather than an unaccounted deformation of a line bundle
already defined on \(X\). The powered equation supplies a Cartier
multiple; it does not make its lower root Cartier or its specialization
pure. Equations (8)–(9) neither exclude that defect nor construct a trait
realizing it. They connect the arithmetic question to the
[endpoint and saturation interfaces](../synthesis/fixed_surface_and_endpoint_algebras.md)
without identifying distinct defect modules from those interfaces.

## Torus-eigenform structure, \(\mu_p^{(1)}\)-orbit splitting in characteristic zero, and endpoint \(T\)-grading

*(Authored by Gemini on `evaluate_toric_integration_stci`; independently reviewed by Gemini subagent and verified in [`verify_toric_conductor_and_endpoint_defects.py`](../computations/verify_toric_conductor_and_endpoint_defects.py).)*

The prescribed powered-quartic family \((F_p, H_4^n)\) (\(p \ge 7\), \(3b + 4c = p\), \(a = p - b - c \ge 0\)) interacts directly with both the curve-preserving torus \(T = \mathbf G_m\) (centered weights \((-2,-1,1,2)\), uncentered \((0,1,3,4)\)) and the full ambient diagonal torus \(T_{\mathrm{amb}} = \mathbf G_m^3 \subset \operatorname{PGL}_4\):

1. **Binomial \(T\)-eigenform weights and VGIT locus:**
   Because \(3b + 4c = p\) and \(4a + b = 3p\), the carrier \(F_p = x_1^p - x_0^a x_2^b x_3^c\) is a binomial \(T\)-eigenform of degree \(p\), uncentered weight \(p\), and **centered weight \(-p\)**; the quartic mate \(H_4 = x_2^4 - x_0 x_3^3\) is a binomial \(T\)-eigenform of degree \(4\), uncentered weight \(12\), and **centered weight \(+4\)** (so \(H_4^n\) has centered weight \(+4n\)). Over \(\overline{\mathbf F}_p\), the special complete intersection \(J_0 = (F_p, H_4^n)\) is a \(T\)-fixed point in the unequal-degree VGIT bundle over \(\mathbf P(V_p)\) and lies in the intrinsic primary-power locus \(H_{pn}\) (\(I_C^{pn} \subset J_0 \subset I_C\)).

2. **Ambient \(\mu_p^{(1)}\)-symmetry and characteristic-zero vs. characteristic-\(p\) cycle decomposition:**
   Inside the ambient torus \(T_{\mathrm{amb}}\), consider the finite subgroup scheme
   \[
     \mu_p^{(1)} := \bigl\{[1 : \zeta : 1 : 1] : \zeta^p = 1\bigr\} \subset T_{\mathrm{amb}}, \qquad T \cap \mu_p^{(1)} = \{1\}.
   \]
   Because \(x_1\) enters \(F_p\) only through \(x_1^p\) and does not enter \(H_4\), the equations \(F_p\) and \(H_4\) are pointwise invariant under \(\mu_p^{(1)}\) over \(\mathbf Z\), and \(\mu_p^{(1)}\) commutes with the curve stabilizer \(T\):
   - **In characteristic zero:** \(\mu_p^{(1)}(\overline{\mathbf Q}) \cong \mathbf Z / p\mathbf Z\) is étale of order \(p\), and on the open chart \(x_0 = 1\) the equations \(x_2^4 = x_3^3\) (\((x_2,x_3) = (\tau^3,\tau^4)\)) and \(x_1^p = x_2^b x_3^c = \tau^{3b+4c} = \tau^p\) split \(V(F_p, H_4)\) into the \(p\) distinct \(T\)-invariant smooth rational quartics
     \[
       C^{(k)} := \bigl\{[s^4 : \zeta_p^k s^3 t : s t^3 : t^4]\bigr\} = [1 : \zeta_p^k : 1 : 1] \cdot C_0 \qquad (k = 0, 1, \dots, p-1),
     \]
     giving the exact cycle decomposition \([V(F_p, H_4)] = [C_0] + \sum_{k=1}^{p-1} [C^{(k)}]\) (generic multiplicity \(1\) along \(C_0\) and residual degree \(4(p-1)\)). All \(p\) branches pass through the two \(T\)-fixed endpoints \(p_0 = [1:0:0:0]\) and \(p_\infty = [0:0:0:1]\).
   - **In characteristic \(p\):** The group scheme \(\mu_p^{(1)} = \operatorname{Spec} k[\zeta]/(\zeta^p - 1)\) is connected and infinitesimal of length \(p\), so the \(p\) translates \(C^{(k)}\) coalesce scheme-theoretically into the sole-supported multiplicity-\(p\) intersection \(V(F_p, H_4)\) along \(C_0\).

3. **Endpoint \(T\)-grading of the specialization root defect \(T = I_{Z_0}/I_{D_0}\):**
   Because \(Z_0 = V_{X_0}(H_4)\) is \(T\)-invariant with singular locus along \(C_0\) restricted to \(\{p_0, p_\infty\}\), for any \(T\)-equivariant DVR trait specializing to \((F_p, H_4^n)\), the root closure \(D \subset X\) and its special fiber \(D_0\) are \(T\)-stable, and the zero-dimensional specialization defect module in (7)–(9) decomposes into opposite \(T\)-graded local endpoint modules:
   \[
     T = I_{Z_0}/I_{D_0} = T_{p_0} \oplus T_{p_\infty}, \qquad \operatorname{length} T_{p_0} + \operatorname{length} T_{p_\infty} = 1 + 2p^2 - p_a(D_K) > 0,
   \]
   parallel to the two local endpoint conductor quotients at \(p_0\) and \(p_\infty\) in the [tropical endpoint modification framework](../synthesis/tropical_thickenings_and_endpoint_duality.md).

Independent reconstruction checked both directions of the finite-precision
equivalence, global membership over Artin bases, scalar normalization and
containment-preserving coefficient lifts, the new lower-multiplicity pair,
the explicit family's exact global nilpotence index, the ramification gap,
the boundary counterexample, and the invariant approximation-radius criterion.
Two further reconstructions checked the root closure, its embedded-point
specialization sequence, Cartier extension, Picard rigidity and the endpoint
genus deficit, without assuming normality or pure special root fibers.
Finite-level heights here refer to strong
nilpotence, not merely to points of an incidence defined by field-valued
rank conditions. Every actual supported DVR trait has the requisite strong
nilpotence, so the resulting trait obstructions do apply.
