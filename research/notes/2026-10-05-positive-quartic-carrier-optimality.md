# Exact mate degrees on the fixed cuspidal quartic carrier

Date: 2026-10-05. Status: proved by the argument below and submitted to the
frontier-audit parent for an independent audit. This note was produced by
the positive-characteristic audit subagent and does not modify a shared
claim ledger. The finite checks at the end are corroboration, not the proof.

## Theorem and its scope

Let `k` be an algebraically closed field, let

\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k,
\qquad F=x_0x_3^3-x_2^4,
\qquad X=V(F).
\]

For an integer `N > 0`, a homogeneous form `G` of degree `N` satisfying
`V(F,G)_red = C_0` exists if and only if:

| Characteristic | Exact condition on `N` | Minimum `N` |
| --- | --- | --- |
| 0 | no positive integer qualifies | no mate |
| 2 | `4` divides `N` | 4 |
| 3 | `3` divides `N` | 3 |
| 5 | `25` divides `N` | 25 |
| prime `p >= 7` | `p` divides `N` | `p` |

These are exact minima and degree sets **on this particular quartic cone**.
They are not global minima among all carriers for `C_0`. In particular, the
characteristic-five `(4,25)` pair below does not improve the repository's
`(3,20)` presentation. In characteristic zero this carrier has no mate, but
the theorem does not exclude other carriers.

## Normalization and its fibers

Give `s,t,z` weights `1,1,4`. The map

\[
\nu:\mathbf P(1,1,4)\longrightarrow X,
\qquad[s:t:z]\longmapsto[s^4:z:st^3:t^4]
\]

comes from the graded inclusion

\[
A=k[s^4,st^3,t^4,z]\subset B=k[s,t,z].
\]

The plane subring `R=k[s^4,st^3,t^4]` has full kernel
`x_0 x_3^3-x_2^4`: this polynomial is irreducible (view it as a primitive
linear polynomial in `x_0`), and the image has dimension two. Thus `Proj A`
is exactly `X`, with the generators given ordinary degree one. Finiteness
follows from the monic equations `s^4=x_0`, `t^4=x_3`, and `z=x_1`.
Equivalently, pass to the fourth Veronese of `B` to obtain a finite map
between rings with ordinary grading. The weighted projective source is
normal because the polynomial ring, and hence its Veronese, is normal.

On `s != 0`, write `u=t/s` and `w=z/s^4`. The target rational coordinates
include `x_2/x_0=u^3`, `x_3/x_0=u^4`, and `x_1/x_0=w`, so `u` is recovered
as `(x_3/x_0)/(x_2/x_0)` on a dense open set. Therefore the map is
birational and is the finite normalization.

The plane normalization `[s:t] -> [s^4:st^3:t^4]` has a singleton fiber over
every geometric point in every characteristic. On `x_0 != 0`, a point is
given by `(u^3,u^4)`; nonzero `u` is recovered by their quotient and the
zero pair has only `u=0`. On `x_3 != 0`, `s/t=x_2/x_3` is recovered
directly. Away from the cone vertex, this unique normalized base point and
the fourth coordinate determine `z` up to weighted scaling. The vertex
`[0:1:0:0]` has the unique preimage `[0:0:1]`. Thus `nu` is finite,
surjective, and universally injective, and hence is a universal
homeomorphism. This argument includes characteristics two and three; no
separability assumption enters.

## The pullback forces a single power

The set-theoretic inverse image of `C_0` is

\[
D=V(\phi),\qquad\phi=z-s^3t.
\]

Indeed substituting `z=s^3t` gives exactly the parametrization of `C_0`.
The weighted vertex is not on `D`, consistently with the fact that the
cone vertex is not on `C_0`. The polynomial `phi` is irreducible and has
weighted degree four.

If `G` is a degree-`N` mate, its pullback is a nonzero polynomial
`g=G(s^4,z,st^3,t^4)` of weighted degree `4N`. Its projective zero set is
exactly `D`. The affine zero set is consequently `V(phi)` as well: both
cones contain the origin, and every other affine point has a weighted
projective image. Unique factorization in `k[s,t,z]` then implies

\[
g=c\phi^r\quad(c\in k^\times).
\]

Weighted homogeneity gives `4r=4N`, so `r=N`. Conversely, if `phi^N` lies
in `A`, any homogeneous lift `G` has exactly the desired support by
surjectivity of `nu`. Therefore the mate problem on `X` is precisely

\[
\phi^N\in R[z].
\]

Adding an `F` multiple to a mate has no effect on this criterion.

## Exact semigroup and characteristic criteria

For any nonnegative integer `r`,

\[
s^{3r}t^r\in R
\quad\Longleftrightarrow\quad r\in\langle3,4\rangle.
\]

Indeed membership means there are nonnegative integers `a,b,c` with
`4a+b=3r` and `3b+4c=r`. The latter equation is necessary; if it holds,
then `a=2b+3c` supplies the former equation. The semigroup is

\[
\langle3,4\rangle=\{0,3,4,6,7,8,\ldots\},
\]

whose positive gaps are `1,2,5`.

In characteristic zero, the coefficient of `z^(N-1)` in `phi^N` is
`-N s^3 t`, which cannot belong to `R`. Hence there is no mate.

In characteristic `p > 0`, write `N=p^e M` where `p` does not divide `M`,
and set `r=p^e`. Frobenius gives

\[
\phi^N=(z^r-s^{3r}t^r)^M.
\]

The coefficient of `z^(N-r)` is `-M s^(3r)t^r` and is nonzero. This is
also the first nonzero non-leading binomial coefficient, as described by
Lucas's theorem. Thus descent necessarily requires `r in <3,4>`. If that
condition holds, every monomial coefficient in the last expansion belongs
to `R`, because its binary part is a power of `s^(3r)t^r`. Hence

\[
\boxed{\phi^N\in R[z]\iff p^{v_p(N)}\in\langle3,4\rangle.}
\]

Checking the three gaps `1,2,5` gives exactly the table in the theorem.
This proves necessity for arbitrary mates, including non-binomial ones;
the construction is not restricted to binomial equations.

## Explicit minimum-degree pairs

If `r=p^e` belongs to `<3,4>`, choose `b,c >= 0` with `3b+4c=r` and put
`a=2b+3c`. Then `a+b+c=r` and

\[
G=x_0^a x_2^b x_3^c-x_1^r
\]

pulls back to `-phi^r`. Together with the same fixed `F`, the smallest
pairs in characteristics two, three, and five are respectively:

\[
\begin{array}{c|c|c}
p&G&(\deg F,\deg G)\\\hline
2&x_0^3x_3-x_1^4&(4,4)\\
3&x_0^2x_2-x_1^3&(4,3)\\
5&x_0^{18}x_2^3x_3^4-x_1^{25}&(4,25).
\end{array}
\]

For `p >= 7`, use the choices in P-028: `b=1,c=(p-3)/4` when
`p=3 mod 4`, and `b=3,c=(p-9)/4` when `p=1 mod 4`. The latter has
`c >= 1` because the least applicable prime is thirteen. All these pairs
satisfy the unsaturated equality `sqrt((F,G))=I_C0`: equality of their
projective supports gives equality of their affine cones, including their
shared origin, and homogeneous Nullstellensatz applies.

## Exact finite corroboration

On 2026-10-05 the existing verifier
`research/computations/verify_positive_quartic_descent.py` passed under
`/private/tmp/stci-cas-venv/bin/python`. System and bundled Python lacked
SymPy and failed before running assertions; the temporary CAS environment
was already documented in the repository.

An additional read-only Python check enumerated the nonzero binomial
coefficients of `(z-s^3t)^N` modulo each prime and tested their semigroup
membership for every `1 <= N <=` the predicted minimum. It obtained the
minima `4,3,25,7,11,13,17,19,23,29,31` for primes
`2,3,5,7,11,13,17,19,23,29,31`, respectively. The exact check was:

```python
from math import comb

def belongs(r):
    return any(3*b + 4*c == r
               for b in range(r//3 + 1)
               for c in range(r//4 + 1))

def descends(n, p):
    return all(comb(n, j) % p == 0 or belongs(j)
               for j in range(n + 1))

for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
    predicted = {2: 4, 3: 3, 5: 25}.get(p, p)
    actual = next(n for n in range(1, predicted + 1) if descends(n, p))
    assert actual == predicted
```

The theorem's all-degree and all-prime conclusions follow from the proof,
not from the finite enumeration.
