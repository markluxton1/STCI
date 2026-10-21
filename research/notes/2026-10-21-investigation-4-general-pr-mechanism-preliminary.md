# Investigation 4: universal divided-power arithmetic and geometric limits (preliminary)

**Status:** preliminary mathematical analysis from the 2026-10-21 conversation. Not independently audited, not promoted, and not a canonical divided-Frobenius identification.

## 1. Arithmetic theorem

Let \(p\) be prime, \(r\ge1\), and \(0<j<p^r\). Then
\[
v_p\binom{p^r}{j}=r-v_p(j).
\]
Proof: \(j\binom{p^r}{j}=p^r\binom{p^r-1}{j-1}\), and Lucas's theorem gives \(\binom{p^r-1}{j-1}\not\equiv0\pmod p\), because the digits of \(p^r-1\) are all \(p-1\).

Define the integral polynomial
\[
\Delta_{p^r}(a,b)=\frac{(a+b)^{p^r}-a^{p^r}-b^{p^r}}p.
\]
The only terms surviving modulo \(p\) have exponent \(j=kp^{r-1}\), \(1\le k<p\). Their coefficients satisfy
\[
\frac1p\binom{p^r}{kp^{r-1}}\equiv \frac{(-1)^{k-1}}{k}\pmod p,
\]
so
\[
\Delta_{p^r}(a,b)\equiv
\sum_{k=1}^{p-1}\frac{(-1)^{k-1}}{k}
a^{(p-k)p^{r-1}}b^{kp^{r-1}}
=\Delta_p(a^{p^{r-1}},b^{p^{r-1}})\pmod p.
\]
For \(p=2,r=2\), this is \(a^2b^2\); for \(p=2,r=3\), \(a^4b^4\); for \(p=3,r=2\), \(a^6b^3+a^3b^6\).

## 2. Relative obstruction framework (conditional)

For an unramified DVR \(R\) with uniformizer \(p\), suppose a flat parameter space of marked embedded conormal quotients carries a locally free relative Ext obstruction bundle \(\mathcal H\), with a canonical obstruction section \(o\) vanishing on the special fiber. Over the appropriate flat first-order congruence space, the reduction \(o\bmod p^2\) is divisible by \(p\), yielding a leading section \(\lambda\) via \(p\mathcal H/p^2\mathcal H\simeq\mathcal H/p\mathcal H\). If its restriction to the first-order lift torsor is affine-linear, the difference map \(D:T\to H_k\) is linear and the image of \(\lambda\) in \(\operatorname{coker}D\) is lift-independent. Nonvanishing then obstructs every lift in the *specified marked family*. Flatness, base change, the comparison of special-fiber obstruction spaces, and affine linearity must be proved in each example. This does not construct a divided-Frobenius map into the cokernel.

## 3. Counterexample to automatic nonvanishing

Let \(C_R\) be a smooth curve and take a split rank-two conormal bundle \(E=M\oplus L\). The zero section of the corresponding vector bundle has local normal coordinates \(x,y\) and admits globally compatible primitive thickenings \(J_n=(x,y^n)\), using the splitting. The ribbon-to-triple Yoneda obstruction vanishes. Yet the universal polynomial \(\Delta_{p^r}\bmod p\) is nonzero. Therefore universal arithmetic nonzero cross-effects do **not** force nonzero geometric obstruction classes.

## 4. Normal-order observation and limits

If \(a\) is a unit along \(C\) and \(b\in I_C\) is a normal parameter, the least normal degree of \(\Delta_{p^r}(a,b)\bmod p\) is \(p^{r-1}\). Thus this *particular leading cross-effect* appears in a quadratic normal neighborhood only when \(p^{r-1}\le2\). This does not exclude other contributions or establish a universal thickening stage. In particular, the quartic \(p=2,r=2\) case has the suggestive quadratic term \(a^2b^2\), but a canonical comparison to the Yoneda obstruction has not been constructed.

The cross-effect satisfies the additive polynomial 2-cocycle identity; for \(r=1\), its negative is the usual carry polynomial in length-two \(p\)-typical Witt addition. Such an arithmetic cocycle is **not automatically** a Čech cocycle of embedded thickenings.

## 5. Open mathematical problem

Construct a natural, coordinate-independent comparison from a divided-power/Frobenius/Witt operation into an appropriate relative embedded obstruction cokernel, with precise marking and base-change hypotheses; alternatively, show why no such map exists generally. Separate (a) universal arithmetic identities, (b) intrinsic deformation-theoretic construction, and (c) nonvanishing in a specific embedded example.

**No new script or independent audit accompanies Investigation 4.**
