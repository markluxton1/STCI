# Independent audit of a finite normal-jet STCI criterion

Date: 2026-09-06. Role: bounded worker proof audit. Status: provisional contribution for lead evaluation; no canonical state changed.

## Verdict

The proposed criterion is correct under the stated assumptions. Coprimality is a consequence of the length equality with truncation exponent `M+1`; it need not be assumed. The exponent is uniformly sharp even among actual homogeneous global pairs. The matrix description needs a chosen coefficient-field splitting in the completed generic local ring; the identification with a polynomial jet algebra over `k(C)` is not canonical.

The proof is elementary once the usual projective degree formula for a complete intersection is available. Its scope is a fixed pair or fixed bidegree. It gives no upper bound on the bidegrees required to define a given curve set-theoretically, and it is not an assertion that arbitrary local jets extend to global equations.

## 1. Local truncation lemma

Let `(A,n)` be any Noetherian local ring, let `Q` be an ideal, and let `B>=1`. If

\[
t=\operatorname{length}_A A/(Q+\mathfrak n^{B+1})\leq B,
\]

then `A/Q` has finite length `t`. In particular, `n^t` is contained in `Q`.

Proof. Write `T=A/Q` and `q=nT`. The displayed length is

\[
\sum_{i=0}^{B}\operatorname{length}_A(\mathfrak q^i/\mathfrak q^{i+1}).
\]

There are `B+1` nonnegative integer summands. At least one is zero, so `q^i=q^(i+1)=q q^i` for some `i<=B`. The ideal `q^i` is a finite module over the Noetherian local ring `T`; Nakayama gives `q^i=0`. Consequently the truncated quotient already equals `T`. Finally, a finite local ring of length `t` has `q^t=0`: otherwise the first `t+1` filtration factors are all nonzero, again using Nakayama to rule out a gap followed by a nonzero power.

Regularity, dimension two, two generators, completeness, and an embedded residue field are unnecessary for this lemma.

The analogous implication at exponent `B` is false. For instance `K[[u,v]]/(u)` has infinite length but its quotient modulo `(u,v)^B` has length `B`. Even if finite colength is separately assumed, `J=(u,v^(B+1))` has length `B+1`, while the quotient modulo `J+(u,v)^B` has length `B`.

## 2. Integral-curve theorem, with the gcd step made explicit

Let `C` be an integral projective curve in `P^3_k`, with `k` algebraically closed and `d=deg C`. Let `F,G` be nonzero homogeneous elements of `I_C` of positive degrees `a,b`. Suppose `M=ab/d` is a positive integer. At the generic point `eta` put

\[
R=\mathcal O_{\mathbf P^3,\eta},\qquad
\mathfrak m=I_CR,\qquad J=(F,G)R.
\]

Here homogeneous sections are made into functions using any local trivializations. Then

\[
|V_+(F,G)|=|C|
\quad\Longleftrightarrow\quad
\operatorname{length}_R R/(J+\mathfrak m^{M+1})=M.
\]

**Forward direction.** Set-theoretic equality excludes a common homogeneous factor of positive degree, since its zero set would be a surface. Thus `F,G` are coprime. Their complete intersection has degree `ab`, and its sole curve component is `C`. Its coefficient along `C` is `length_R R/J`; hence this length is `ab/d=M`. Any local Artin quotient of length `M` is killed by `m^M`, so the displayed truncated length equals `M`.

**Reverse direction: finite local length.** The local lemma with `B=M` gives `length_R R/J=M`. In particular `J` is `m`-primary.

**Reverse direction: removal of all possible common factors.** Let `H=gcd(F,G)` in `k[x_0,x_1,x_2,x_3]`, put `e=deg H`, and write `F=HF'`, `G=HG'`, with `F',G'` coprime. If `H` belongs to `I_C`, then `J` is contained in the proper principal ideal `HR`. Since `R` is a regular local ring of dimension two and `H` is nonzero, `R/(H)` has dimension one. This contradicts finite length of `R/J`.

Thus `H` does not belong to the prime ideal `I_C`, and is a unit in `R`. Therefore

\[
(F',G')R=J,\qquad
F',G'\in I_C.
\]

The latter membership follows from primality, and also shows that both residual degrees are positive. The coprime pair `F',G'` defines a complete intersection of degree `(a-e)(b-e)` whose coefficient on `C` is still `M`. Positivity of all component degrees gives

\[
ab=dM\leq(a-e)(b-e).
\]

If `e>0`, the right side is strictly smaller than `ab`. Therefore `e=0` and the original pair is coprime.

**Reverse direction: exhaustion of support.** The complete intersection of `F,G` has degree `ab`, already exhausted by coefficient `M` on degree-`d` curve `C`. Every other curve component would contribute positive degree. There are no surface components by coprimality. There are no isolated support components either: in the polynomial ring every minimal prime over the two-generated ideal has height at most two, while coprimality forces height at least two. Every minimal prime therefore has height exactly two, so projective support is pure one-dimensional. Hence the support is exactly `C`.

The last height argument is sufficient for the set-theoretic claim. Complete-intersection unmixedness is another valid route. Merely saying that there are no embedded points is insufficient to exclude isolated components; those are distinct concepts. Embedded points on a retained curve would not change set-theoretic support in any event.

For reproducibility, the degree formula can be obtained from the elementary graded exact sequences for the regular sequence `F,G`:

\[
H_{S/(F,G)}(t)=\frac{(1-t^a)(1-t^b)}{(1-t)^4}
=\frac{(1+\cdots+t^{a-1})(1+\cdots+t^{b-1})}{(1-t)^2}.
\]

The numerator at `t=1` is `ab`, the projective degree. The component coefficient is the generic local length, and degree is the sum of coefficient times reduced-component degree. See the Stacks Project's [cycle associated to a coherent sheaf](https://stacks.math.columbia.edu/tag/02QV). Complete-intersection equidimensionality and Cohen–Macaulayness are also recorded in [local complete intersections](https://stacks.math.columbia.edu/tag/00S8).

## 3. Truncation sharpness, including global examples

**Without coprimality.** For every `M>=1`, let

\[
C=V_+(x,y)\subset\mathbf P^3_{[x:y:z:w]},\qquad
F=xz^{M-1},\quad G=x.
\]

Here `d=1`, `a=M`, `b=1`, and `ab/d=M`. At the generic point of the line, `z` is a unit and `J=(x)`. Thus

\[
\operatorname{length}_R R/(J+\mathfrak m^M)=M,
\]

but `V_+(F,G)=V_+(x)` is a plane. At exponent `M+1`, the quotient length is `M+1`, correctly rejecting the pair. Therefore the improvement to exponent `M` is impossible without some additional hypothesis, even with the degree budget imposed globally.

**With coprimality.** Coprimality gives `length_R R/J<=ab/d=M` by the degree formula. Hence `m^M` is already contained in `J`, and the criterion is equivalently

\[
\operatorname{length}_R R/(J+\mathfrak m^M)=M.
\]

This exponent is uniformly necessary for the equivalence. On the same line take `F=x`, `G=y^M`. The pair is coprime and defines the line set-theoretically; its local quotient is `K[[y]]/(y^M)`. Truncation at exponent `M-1` has length `M-1` when `M>=2`, so it fails to recognize this valid pair. For `M=1`, truncation at exponent zero is the zero quotient.

This does not say that every individual pair requires so many orders: any independently known smaller nilpotency bound gives a smaller sufficient truncation.

## 4. The finite matrix and its coordinate requirements

The residue field of `R` is `K=k(C)`, while `R` is a regular local ring of dimension two. Its completion admits a noncanonical coefficient-field section and an isomorphism

\[
\widehat R\cong K[[u,v]]
\]

after choosing regular parameters. This is the equal-characteristic regular case of the [Cohen structure theorem](https://stacks.math.columbia.edu/tag/032A), explicitly [Lemma 10.160.10](https://stacks.math.columbia.edu/tag/0C0S). Completion preserves all the finite quotients used here.

In this setup, with `N=M+1`, put

\[
A_N=K[u,v]/(u,v)^N,\qquad
D=\dim_K A_N=\frac{N(N+1)}2.
\]

Use the basis `u^i v^j`, `i+j<N`. Let `f_N,g_N` be the images of dehomogenized `F,G`. Form the multiplication map

\[
T_{F,G}:A_N\oplus A_N\longrightarrow A_N,
\qquad(h_1,h_2)\longmapsto h_1f_N+h_2g_N.
\]

It is a `D`-row, `2D`-column matrix over `K`, and

\[
\operatorname{length}_R R/(J+\mathfrak m^N)
=D-\operatorname{rank}_K T_{F,G}.
\]

Thus the theorem is the exact rank condition `rank T_(F,G)=D-M`. Columns that vanish by degree can be omitted. One must use the span of all monomial multiples, not just the two coefficient vectors of `f_N,g_N`.

Material implementation qualifications:

- There is no canonical inclusion `k(C)->R`; arbitrary lifts of residues need not form a field or give consistent multiplication. Choose a coefficient section in the completion or directly in the Artin quotient, and record how jets are calculated.
- A `k`-compatible section is available here. Since `k` is algebraically closed, `K/k` is separably generated. One concrete route chooses a separating transcendental element, lifts it, and Hensel-lifts a primitive element for the resulting finite separable field extension. This gives a coefficient field extending the original constants. In characteristic zero separability is automatic; in positive characteristic it should not be silently replaced by an arbitrary inseparable parameter choice.
- The regular parameters are two normal parameters at the generic point. An arbitrary pair of equations vanishing on `C` need not be a parameter system; check that their images form a basis of `m/m^2`.
- Dehomogenize in a chart meeting the generic point, or trivialize the two line bundles there. Changing the trivialization multiplies each equation by a unit and preserves the ideal and length.
- Changing normal parameters or the coefficient section alters the displayed matrix but not its rank defect. Only full jets through degree `N-1` are required, but leading normal forms alone do not determine these full jets.
- For a rational curve, `K=k(t)` is convenient. For a nonrational curve, retain a valid presentation of its function field, including algebraic relations. Do not replace it by `k(t)` without justification.
- When varying global forms, their unknown coefficients lie in `k`, not arbitrarily in `K`. A solution over `K` to a more freely parameterized jet problem need not correspond to any global degree-`a` and degree-`b` forms.
- Exact rank means rank over the function field. Numerical or finite-field samples are evidence unless the needed characteristic-zero or generic identities and nonidentities are certified.

For fixed bases of `H^0(I_C(a))` and `H^0(I_C(b))`, the matrix entries are linear in global scalar parameters, with coefficients in `K`. Rank equality is a finite constructible condition. A minor polynomial with coefficients in `K` vanishes identically precisely when its finitely many coefficients in a chosen finite-dimensional `k`-span vanish. This explains why the function-field condition can, in principle, be expressed using finitely many equations and inequations over `k`; it does not remove the computational cost or guarantee existence.

### Exact globalization trap supplied by the lead and independently checked

For `n>=2`, take the smooth rational curve

\[
C_n=(s^{n+1}:s^nt:st^n:t^{n+1}),\quad d=n+1,
\]

on `Q=xw-yz`. Put `S_n=yw^(n-1)-z^n`, `F=Q`, `G_1=yS_n`, and `G_2=wS_n`. The two `G_i` have degree `n+1` and vanish on `C_n`. On `w=1`, use the longitudinal parameter `tau=z` and normal parameters

\[
u=y-\tau^n,\qquad v=x-y\tau.
\]

Then `K=k(tau)`, `F=v`, `G_1=(tau^n+u)u`, and `G_2=u`. Allowing coefficients in this residue field gives

\[
G_1-\tau^nG_2=u^2,\qquad
\operatorname{length}K[[u,v]]/(v,u^2)=2.
\]

That equals the nominal budget `2(n+1)/(n+1)=2`. Yet for any nonzero constant pair `(alpha,beta) in k^2`,

\[
\alpha G_1+\beta G_2
=u(\alpha u+\alpha\tau^n+\beta),
\]

and the parenthesized factor has nonzero residue because `tau` is transcendental. Thus the actual generic intersection length is one for every nonzero constant pair in this pencil.

There cannot be a degree-`n+1` global equation outside the pencil that fixes the problem while keeping `F=Q`. In Segre coordinates `x=AC,y=AD,z=BC,w=BD`, the curve has equation `AD^n-BC^n=0`, of divisor class `(1,n)`, and

\[
S_n=B^{n-1}(AD^n-BC^n).
\]

A nonzero degree-`n+1` section restricted to `Q` has class `(n+1,n+1)`. Containing `2C_n` would require an effective remainder of class `(n-1,1-n)`, which is impossible. A section restricting to zero gives a common surface instead. Hence this is an exact false positive from permitting residue-field-valued surface coefficients.

Clearing the denominator changes the degree budget. The residue-field combination corresponds in homogeneous rational functions to

\[
G_1-(z/w)^nG_2=S_n^2/w^{n-1},
\]

whose polynomial numerator has degree `2n`, not `n+1`. Its intersection with `Q` also retains the residual line appearing in the factorization above. Finally, allowing coefficients in the existing residue field is not innocuous base change of the entire geometric problem: a genuine independent field extension would not identify its new scalar with the longitudinal coordinate in this way.

## 5. Reduced reducible curves

Let `C=union_(i=1)^r C_i` be a reduced pure projective curve with distinct integral components. Set `d_i=deg C_i`, `R_i=O_(P3,eta_i)`, `m_i=I_(C_i)R_i`, and `J_i=(F,G)R_i`. Continue to require nonzero homogeneous `F,G in I_C` of degrees `a,b`.

A formulation with prescribed multiplicities is:

\[
|V_+(F,G)|=|C|
\]

if and only if there exist positive integers `n_i` such that

\[
\sum_i d_i n_i=ab,\qquad
\operatorname{length}_{R_i}R_i/(J_i+\mathfrak m_i^{n_i+1})=n_i
\quad\text{for every }i.
\]

There is also a single predetermined test without enumerating a multiplicity vector. Define

\[
B_i=\left\lfloor\frac{ab}{d_i}\right\rfloor,\qquad
t_i=\operatorname{length}_{R_i}R_i/(J_i+\mathfrak m_i^{B_i+1}).
\]

Then

\[
|V_+(F,G)|=|C|
\quad\Longleftrightarrow\quad
\sum_i d_i t_i=ab.
\]

For the reverse implication, the weighted equality gives `t_i<=B_i` individually, so the local lemma identifies every `t_i` with actual finite local length. (If any `B_i=0`, the weighted equality is impossible because `t_i>=1`.) A common gcd cannot contain any `C_i`; otherwise the corresponding local quotient would have infinite length. It is consequently a unit at every generic point. Removing a nonconstant gcd would leave a coprime pair of strictly smaller product of degrees while preserving total weighted contribution `ab`, a contradiction. The final complete-intersection degree is exhausted by the listed components. The converse follows from its cycle decomposition and the same length bound.

If desired, use the sharper bound

\[
B_i'=\left\lfloor\frac{ab-\sum_{j\ne i}d_j}{d_i}\right\rfloor
\]

when all `B_i'>=1`; every other retained component has multiplicity at least one. The same proof works with exponent `B_i'+1`. If coprimality is separately assumed, exponents `B_i` (or the valid sharper `B_i'`) suffice.

A common value `ab/deg C` at every component is not a general reducible criterion: component multiplicities can differ. For example the coprime pair `F=z`, `G=x^2y` supports the union of two lines in the plane `z=0`, with generic multiplicities two and one, while the average is `3/2`.

## 6. Interpretation and remaining boundary

Established by this audit: the fixed-bidegree finite-jet criterion, the elimination of a separate coprimality hypothesis, sharpness examples, and the weighted reducible extension. The local and global proof steps have been checked independently; the examples are exact symbolic examples, not empirical probes.

This criterion combines local finite data with the global degree budget. Without that budget, local equality at one generic point cannot rule out residual components. It allows both equations to lie deeply in `I_C`; no first-order transversality or non-thick hypothesis has been introduced. Nevertheless, arbitrary bounded or unbounded degree searches, sufficient global jet realizability, and a uniform solution or obstruction for all projective curves remain separate questions. Lead integration should decide whether this reformulation changes the next feasible computation or only clarifies the existing boundary.
