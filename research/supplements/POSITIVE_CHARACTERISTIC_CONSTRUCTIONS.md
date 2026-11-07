# Fixed-quartic positive-characteristic constructions and exact degree sets

This chapter owns the exact constructions and arbitrary-mate degree classification for the fixed embedded curve \(C_0=[s^4:s^3t:st^3:t^4]\), including the full exponent-compatible two-binomial component calculation. The [family-wide cubic construction](RATIONAL_QUARTICS_IN_POSITIVE_CHARACTERISTIC.md) applies to every smooth nondegenerate rational quartic and has different quantifiers. The [conormal and specialization proof](CONORMAL_SPECIALIZATION_AND_QUARTIC_SYMBOLS.md) owns the normal-bundle jump, prescribed \(\mu_4\) intersection and actual quartic symbols. These are inherited reviewed proofs. The characteristic-free geometric foundation is [here](../synthesis/global_equations_and_constructions.md).

The explicit binomial Frobenius construction for the fixed curve has direct primary-literature support in Barile–Morales–Thoma, *Set-theoretic complete intersections on binomials*, Theorem 5 and §3 Example 1, specialized to \(d=4\). Their characteristic-zero binomial statement does not address arbitrary pairs of forms. The linked repository argument for all smooth rational quartics has broader curve scope than that particular example; no novelty claim is inferred from the bounded literature check. [Publisher article](https://doi.org/10.1090/S0002-9939-01-06289-X).

<a id="every-positive-characteristic-quartic-carrier"></a>

## Every positive characteristic: a quartic carrier

For every prime \(p\), choose a power \(N=p^e>5\), so \(N\in\langle3,4\rangle\). Write \(N=3a+4b\) with \(a,b\ge0\). The literal homogeneous equations
\[
F=x_1^4-x_0^3x_3,\qquad
G=x_2^N-x_0^b x_1^a x_3^{2a+3b}
\]
cut out the fixed \(C_0\) set-theoretically in characteristic \(p\). On \(x_0=1\), they become \(x_3=x_1^4\) and \((x_2-x_1^3)^N=0\); on \(x_0=0\), they force \(x_1=x_2=0\). This includes every prime, with no separability assumption. For example \(N=4\) works in characteristic two, \(N=3\) in characteristic three, and \(N=25\) in characteristic five.

The full arbitrary-mate degree classification on this fixed cuspidal quartic, after reversing coordinates, is proved [below](#all-mate-degrees-on-a-fixed-cuspidal-quartic): exact least mate degrees are \(4,3,25,p\) for \(p=2,3,5,p\ge7\), respectively. The degree-25 assertion is stronger than minimality within one binomial ansatz. It is still a fixed-carrier minimum; a cubic carrier gives degree 20 in characteristic five.

Thus [the characteristic-zero quartic-carrier exclusion](../results/quartic_carrier_exclusion.md) cannot extend to any positive characteristic for this fixed embedding. The positive mechanism is Frobenius descent through a nonnormal carrier. The linked universal construction for every smooth rational quartic uses a cubic carrier and has different curve and degree quantifiers.

## Fixed-model cubic constructions (P-008): exact positive-characteristic presentations of the monomial quartic

Let

\[
C_0=[s^4:s^3t:st^3:t^4]
\]

and put

\[
\begin{aligned}
q&=x_0x_3-x_1x_2,\\
A&=x_1^3-x_0^2x_2,\\
B&=x_1^2x_3-x_0x_2^2,\\
D&=x_2^3-x_1x_3^2.
\end{aligned}
\]

Elimination on the two parameter charts, or the verified Hilbert--Burch
resolution, gives

\[
 I_{C_0}=(q,A,B,D).
\]

In characteristic three,

\[
 \sqrt{(A,\;x_0x_3^3-x_2^4)}=I_{C_0}.
\]

Indeed, on \(x_0=1\), the first equation gives \(x_2=x_1^3\), and the
second gives \((x_3-x_1^4)^3=0\); injectivity of Frobenius on a field gives
the affine parametrized curve.  At \(x_0=0\), the equations successively force
\(x_1=x_2=0\), leaving only the endpoint \([0:0:0:1]\).

There is also a uniform construction in every characteristic \(p>0\).  Choose
\(e=3\) for \(p=3\), and \(e=3p\) otherwise, and set \(N=4e/3\).  For
\(0\le j\le e\), put

\[
n_j=4(e-j),\qquad
b_j\equiv n_j\pmod 3,\quad 0\le b_j<3,
\]

\[
c_j=(n_j-b_j)/3,\qquad
a_j=N-b_j-c_j-j.
\]

The only negative exponent is \(a_1=-1\), but its coefficient
\(\binom e1=e\) vanishes in characteristic \(p\).  Therefore

\[
G_e=\sum_{\substack{0\le j\le e\\j\ne1}}
(-1)^{e-j}\binom ej
x_0^{a_j}x_1^{b_j}x_2^{c_j}x_3^j
\]

is a homogeneous form of degree \(N\).  Modulo \(A\), one has the exact
identity

\[
 q^e=x_0^{2e/3}G_e.
\]

On \(x_0=1\), this says \(G_e=(x_3-x_1^4)^e\).  On \(x_0=0\), the
\(j=0\) term becomes a nonzero scalar multiple of \(x_2^N\), so no boundary
line is introduced.  Consequently

\[
 \sqrt{(A,G_e)}=I_{C_0}.
\]

The degrees are \((3,4)\) in characteristic three and \((3,4p)\) otherwise.
The derivation is a proof; a separate exact-arithmetic script checked the
homogeneity, identity, boundary term, and power containments for
\(p=2,3,5,7\).  The computation also found the smaller characteristic-two
pair

\[
\sqrt{(x_1^4-x_0^3x_3,\;x_2^4-x_0x_3^3)}=I_{C_0}.
\]

## Conormal transition and the characteristic-three primitive triple

The [complete transition proof](CONORMAL_SPECIALIZATION_AND_QUARTIC_SYMBOLS.md) gives N=O(7)² for characteristic different from two and O(6)⊕O(8) in characteristic two. It also identifies the special characteristic-three (3,4) presentation as a globally primitive triple with graded pieces O,O(-7),O(-14).

## Every smooth rational quartic, constructibility and cusp minima

The [complete family-wide proof](RATIONAL_QUARTICS_IN_POSITIVE_CHARACTERISTIC.md) constructs an internal cuspidal projection and descends a degree-4p mate through radicial normalization. It also proves fixed-degree constructibility and the exact mate-degree semigroups on standard and nonclassical cubic cusp carriers. These quantifiers differ from the fixed-model quartic-carrier statements here.

## Fixed-model quartic construction (P-028): a degree-(4,p) pair for the monomial quartic in every prime characteristic p at least 7

Let the ground field be algebraically closed of prime characteristic \(p\ge7\).
Choose positive integers \(b,c\) with

\[
 3b+4c=p
\]

and put \(a=p-b-c=2b+3c\).  Such a choice always exists: if
\(p\equiv3\pmod4\), take \(b=1,\ c=(p-3)/4\); if
\(p\equiv1\pmod4\), take \(b=3,\ c=(p-9)/4\).  Define

\[
 F=x_0x_3^3-x_2^4,\qquad
 G=x_0^a x_2^b x_3^c-x_1^p.
\]

Both vanish on

\[
 C_0=[s^4:s^3t:st^3:t^4],
\]

because \(4a+b=3p\), which follows from \(a=2b+3c\) and
\(p=3b+4c\).

On the affine chart \(x_0=1\), the cusp equation \(F=0\) has normalization
\(x_2=v^3,\ x_3=v^4\).  The second equation becomes
\(v^{3b+4c}=x_1^p\), hence \(v^p=x_1^p\).  In characteristic \(p\) this is
\((v-x_1)^p=0\), so the reduced common zero set is the affine part of \(C_0\).
On the boundary \(x_0=0\), \(F=0\) forces \(x_2=0\), and then \(G=0\) forces
\(x_1=0\); the only projective point is \([0:0:0:1]\), the missing point of
\(C_0\).  Therefore

\[
 \sqrt{(F,G)^{\mathrm{sat}}}=I_{C_0}.
\]

This improves the second degree of the general Frobenius construction for
this explicit curve from \(4p\) to \(p\).  It is a positive-characteristic
result and supplies no specialization argument in characteristic zero.


## All mate degrees on a fixed cuspidal quartic

The following semigroup theorem applies to arbitrary homogeneous mates on the specified carrier. It is stronger than classifying one binomial ansatz. Its inherited independent foundational audit is unchanged; no general-carrier minimum is asserted.

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



## The prescribed mu4 intersection and actual quartic symbols

The [complete degeneration and symbol proof](CONORMAL_SPECIALIZATION_AND_QUARTIC_SYMBOLS.md#the-prescribed-mu4-intersection-and-actual-quartic-symbols) establishes the flat integral model, four components and3/3 endpoint contact in characteristic zero, characteristic-two sole support, full initial ideals and their failure of base change, and the exact actual quartic-symbol image.

## Exact two-binomial reduced support and endpoint contacts

## 1.2C Exact Frobenius-binomial criterion for a quartic first carrier

Let \(k\) be algebraically closed of characteristic \(p>0\), \(n=p^r\), and fix
\[
F=x_1^4-x_0^3x_3,\qquad
G=x_2^n-x_0^a x_1^b x_3^c.
\]
The second monomial has the same restriction as \(x_2^n\) on \(C_0=[s^4:s^3t:st^3:t^4]\) exactly when
\[
4a+3b=n,\qquad b+4c=3n.
\]
Thus \(a=(n-3b)/4,\ c=(3n-b)/4\), with \(a,b,c\) nonnegative integers. Equivalently, it suffices to choose
\[
0\le b\le\lfloor n/3\rfloor,\qquad b\equiv3n\pmod4.
\]
These conditions also imply \(a+b+c=n\), so \(G\) is homogeneous of degree \(n\).

**Claim (within this binomial family).** Every such choice gives \(\sqrt{(F,G)}=I_{C_0}\). On \(x_0=1\), the first equation gives \(x_3=x_1^4\), and the second becomes \(x_2^n=x_1^{3n}\). Since \(n\) is a power of the characteristic, this is \((x_2-x_1^3)^n=0\), so the reduced affine zero set is the parametrized quartic. On \(x_0=0\), \(F\) forces \(x_1=0\), and \(G\) forces \(x_2=0\), leaving only the endpoint \([0:0:0:1]\). The two forms have no extra projective component.

For odd \(n\), the smallest nonnegative admissible residue is \(b=1\) when \(n\equiv3\pmod4\), and \(b=3\) when \(n\equiv1\pmod4\). Hence every odd prime \(p\equiv3\pmod4\) works already with \(n=p\). For \(p\equiv1\pmod4\), \(n=p\) works exactly when \(p\ge9\), i.e. for primes \(p\ge13\); the exceptional prime \(p=5\) first works at \(n=25\). For \(p=2\), \(n=4\) gives \(b=0,a=1,c=3\). In particular the characteristic-five choice \(n=25,b=3,a=4,c=18\) gives
\[
G=x_2^{25}-x_0^4x_1^3x_3^{18},
\]
and characteristic seven gives \(n=7,b=1,a=1,c=5\).

The direct exponent calculation here proves minimality within the displayed quartic-plus-Frobenius-binomial ansatz. The separate [semigroup theorem](#all-mate-degrees-on-a-fixed-cuspidal-quartic) proves the stronger fixed-carrier result: in characteristic five every homogeneous mate on this quartic has degree divisible by 25. Neither result gives the minimum across other carriers; the cubic construction has a degree-20 mate.

## 1.2D Necessity of the Frobenius exponent and all reduced components

The power-of-characteristic condition in the preceding construction is **necessary**, not merely convenient, within the same two-binomial family. Let \(n\ge1\) be arbitrary and assume the nonnegative integers \(a,b,c\) satisfy the two exponent equations above. Write \(n=p^r m\), with \(p\nmid m\). On \(x_0=1\), the scheme is
\[
x_3=x_1^4,\qquad x_2^n=x_1^{3n}.
\]
Over an algebraically closed field, its reduced equation factors as
\[
\prod_{\zeta^m=1}(x_2-\zeta x_1^3)=0,
\]
since \(x_2^n-x_1^{3n}=(x_2^m-x_1^{3m})^{p^r}\). Thus the reduced projective support is the union of **exactly \(m\) distinct quartic curves**
\[
C_\zeta:\quad [s:t]\longmapsto[s^4:s^3t:\zeta st^3:t^4],\qquad \zeta^m=1.
\]
Indeed the \(x_0=0\) equations leave only the common endpoint, already contained in every \(C_\zeta\). Each affine component is irreducible and its projective closure is \(C_\zeta\). Consequently
\[
\sqrt{(F,G)}=I_{C_0}\quad\Longleftrightarrow\quad m=1
\quad\Longleftrightarrow\quad n\text{ is a power of }p,
\]
for exponent-compatible binomials of this precise shape. This is a complete **reduced-support classification of this family**, not a statement about arbitrary second equations.

The same calculation works over characteristic zero with \(m=n\), so no positive exponent \(n>1\) in this binomial family gives sole support there. In characteristic zero the \(n=1\) exponent congruence has no nonnegative solution (\(b\le0\) but \(b\equiv3\bmod4\)); hence the family produces **no characteristic-zero STCI at all**. This conclusion is limited to the displayed binomial ansatz.

## 1.2E Generic multiplicities and contacts among binomial components

The component classification above also determines the **fundamental one-cycle**, not just the reduced support. For \(n=p^r m\), \(p\nmid m\), the local complete intersection on \(x_0=1\) is
\[
(x_3-x_1^4,\ (x_2^m-x_1^{3m})^{p^r}).
\]
At the generic point of each \(C_\zeta\), the other \(m-1\) factors are units; the generic transverse length is exactly \(p^r\). Consequently, as an effective cycle,
\[
[V(F,G)]=p^r\sum_{\zeta^m=1}[C_\zeta].
\]
Each component has degree four, so the cycle degree is \(4p^rm=4n=\deg F\deg G\), as Bézout requires. In characteristic zero take \(p^r=1,m=n\).

The distinct components meet **only at the two endpoints**, but one must specify whether contact is measured on the original projective curves or on their ruled normalization model. Near \(p_0=[1:0:0:0]\), use \(t=x_1/x_0\); the branches are \((t,\zeta t^3,t^4)\). Their ideal sum imposes \(t^3=0\), giving length three for every distinct \(\zeta,\xi\).

Near \(p_\infty=[0:0:0:1]\), a common ambient coordinate is \(c=x_2/x_3\), not the parameter \(s/t\) separately on each curve. The equations of \(C_\zeta\) there are
\[
x_0/x_3=\zeta^{-4}c^4,\qquad x_1/x_3=\zeta^{-3}c^3.
\]
Therefore the local intersection length of distinct projective curves is
\[
\ell_{p_\infty}(C_\zeta\cap C_\xi)=
\begin{cases}
3,&\zeta^3\ne\xi^3,\\
4,&\zeta^3=\xi^3.
\end{cases}
\]
In the second case \(\zeta^4\ne\xi^4\), because equality of both powers would imply \(\zeta=\xi\). For the prescribed \(\mu_4\) pair all distinct fourth roots have different cubes, so the projective contact is **three at each endpoint**. This agrees with the arithmetic genus 33 of its reduced characteristic-zero complete intersection.

The contact divisor \(3p_0+p_\infty\) instead describes the distinct graph sections on the smooth ruled model \(\mathbf F_4\), before their finite map to the projective intersection. That map changes the infinity contact length from one upstairs to three downstairs in the \(\mu_4\) example. [The ruled arithmetic proof](../supplements/CUBIC_SCROLL_AND_RULED_SURFACES.md) keeps these two intersection problems distinct. Generic component multiplicity, contact on a resolution, and intersection length in \(\mathbf P^3\) are different invariants; none is determined by the total degree alone.
