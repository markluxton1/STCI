# Normal carrier Picard and local torsion: primary sources and new index audit

Date: 2026-10-14. Owner: `normal_torsion_primary`, child of `conductor_general`.

Scope: integral normal hypersurface surface `X` in projective three-space over an algebraically closed characteristic-zero field. The smooth rational quartic `C0` is fixed. Previously accepted exclusions of all mates of degree at most four are premises; no inherited verification was rerun. This note records new source checks and new numerical deductions only.

## 1. Picard torsion vanishes; Weil class torsion need not vanish

**KNOWN, primary theorem.** [Grothendieck, SGA 2, Expose XII, Corollary 3.5](https://wstein.org/sga/circle/SGA2.pdf), printed p.120, PDF page 128: for a projective scheme `V`, an ample invertible sheaf, and a regular section with zero scheme `Z`, the map of etale fundamental groups is surjective when the ambient depth at closed points is at least two. With depth at least three at closed points of `Z`, and purity at closed points outside `Z`, it is an isomorphism. Regular local rings give the required purity.

Apply this with `V=P3`, the ample sheaf `O(a)`, and the equation of `X`. The ambient local rings have depth three and are regular everywhere. Thus `pi_1^et(X)=pi_1^et(P3)=1`. The triviality for projective space can also be obtained by repeated applications of the same corollary starting with `P1`, whose connected finite etale covers are trivial by Riemann-Hurwitz.

**PROVED consequence.** [Stacks Project, Kummer theory, Lemma 59.28.1](https://stacks.math.columbia.edu/tag/03PK) applies to every positive integer in characteristic zero. Since the only global units on integral proper `X` are constants and the field is algebraically closed, Kummer gives

`Pic(X)[n] = H^1_et(X,mu_n) = Hom_cont(pi_1^et(X),mu_n) = 0`.

Therefore `Pic(X)` is torsion-free. This statement does **not** imply that `Cl(X)` is torsion-free.

**KNOWN, primary local-global sequence.** [Hartshorne--Polini, Divisors Class Groups of Singular Surfaces, Proposition 2.2(c)](https://arxiv.org/pdf/1301.3222), pp.2--3, gives the sequence of Picard, almost Picard, and local almost Picard groups. For a normal surface it specializes to

`0 -> Pic(X) -> Cl(X) -> direct_sum_{P in Sing(X)} Cl(O_X,P)`.

Exactness at `Cl(X)` is the required assertion; no surjectivity onto the direct sum is assumed. Picard torsion-freeness implies that localization is injective on the torsion subgroup of `Cl(X)`.

## 2. Exact local-index formula for the normal quartic carrier

Write `a=deg X`, `g=gcd(a,4)`, `mu=a/g`, `v=4/g`, and

`Delta0 = mu[C0] - v[H]`.

Assume `Delta0` has finite order `t`; this is the accepted normal-carrier mate criterion. The accepted exact progression of mate degrees gives `b_min=v*t`.

**PROVED HERE.** Let `r_P` be the algebraic local Cartier index of `C0` at `P in C0 intersect Sing(X)`. These indices are finite: the torsion relation makes `t*mu*C0` Cartier. Off `C0`, the local class of `Delta0` is zero. At a point on `C0` its local class is `mu[C0]_P`, hence its order is `r_P/gcd(r_P,mu)`. Injectivity of localization on global torsion gives

`t = lcm_P (r_P/gcd(r_P,mu))`.

Set `R=lcm_P r_P`, using `R=1` for the empty set. For each prime `ell`, the valuation on the preceding least common multiple is

`max_P max(v_ell(r_P)-v_ell(mu),0) = max(v_ell(R)-v_ell(mu),0)`.

Consequently

`t = R/gcd(R,mu)` and `b_min = (4/g)*R/gcd(R,a/g)`.

If `R` divides `a=g*mu`, the valuation formula gives `t` dividing `g`, so `b_min<=4`. The accepted low-degree exclusions therefore imply:

**Every normal carrier admitting a mate must have at least one singular point on `C0` whose local Cartier index does not divide the carrier degree.**

The special case `C0` disjoint from `Sing(X)` has `R=t=1` and is excluded. The same conclusion follows directly because then `C0` is Cartier everywhere, so `Delta0` is a torsion element of `Pic(X)` and must vanish.

## 3. Ordinary nodes and bounded local exponents

**KNOWN, primary local class computations.** [Brevik--Nollet, Local Picard Groups, Sections 4.1.1--4.1.3](https://arxiv.org/pdf/1110.1867), pp.8--9, give the completed rational-double-point class groups:

| Type | Completed local class group | Exponent |
|---|---|---|
| `A_n` | `Z/(n+1)` | `n+1` |
| `D_n`, `n` odd | `Z/4` | `4` |
| `D_n`, `n` even | `(Z/2)^2` | `2` |
| `E_6` | `Z/3` | `3` |
| `E_7` | `Z/2` | `2` |
| `E_8` | `0` | `1` |

Their Proposition 2.4 uses the injective map from the algebraic local class group to the completed class group. Its injectivity follows by faithful flat descent: if the completed rank-one reflexive module is free, the original module is free. In this normal excellent setting completion preserves the relevant rank-one reflexive module.

Source caution: the introductory summary at the beginning of their Section 4 reverses some `D_n` parity and `E_6/E_7` assignments. The detailed subsections and the introduction's explicit `D_n` discussion agree with the table above; use those precise locations.

**PROVED HERE, node corollary.** At an ordinary node, completion has exponent two, so `r_P` divides two. A smooth curve through a singular surface point cannot be Cartier: if its local ideal is `(f)`, the one-dimensional quotient is regular, giving embedding dimension of the surface local ring at most two, hence regularity. Thus a node on `C0` has `r_P=2`.

If all singularities on `C0` are ordinary nodes, `R` is one or two. For even `a`, `R` divides `a`; all these carriers are excluded. For odd `a`, the torsion formula alone requires a node on `C0`, and then `g=1`, `mu=a` odd, `R=t=2`, and `b_min=8`. The stronger Cartier-intersection constraint in Section 6 also excludes this odd-degree possibility. Thus the final result excludes all normal carriers with only ordinary nodes on `C0`, in every carrier degree covered by the accepted low-degree-carrier exclusions.

More generally, if every on-curve local class group has exponent dividing `L`, then `R` divides `L` and

`t divides L/gcd(L,mu)`, so `b_min <= (4/g)*L/gcd(L,a/g)`.

All new formulas and both node parity consequences passed an independent symbolic argument supplied to `conductor_general`. Algebraic local indices, not an unsupported equality between algebraic and analytic class groups, are used throughout.

## 4. Failure shield: normal hypersurface class groups can have torsion

**KNOWN construction plus explicit consequence.** [Elsenhans--Jahnel, Kummer Surfaces and the Computation of the Picard Group, Sections 4.2--4.3](https://arxiv.org/pdf/1109.4346), pp.6--7, describe a Kummer quartic `Q` with sixteen ordinary nodes, its abelian double cover, and the divisibility of the exceptional sum on the resolution `S`:

`2 alpha = E_1+...+E_16` in `Pic(S)`.

The exceptional curves are linearly independent over the rationals, as their intersection matrix is diagonal with entries `-2`. Under `Pic(S)=Cl(S) -> Cl(Q)`, the class of `alpha` has order two: its double is exceptionally supported, while `alpha` cannot be an integral combination of the `E_i`. Thus a normal quartic hypersurface has nonzero torsion in its Weil class group, although its Picard group is torsion-free.

This example defeats any unrestricted claim that normal projective hypersurfaces in `P3` have torsion-free `Cl`. It supplies no normal carrier for `C0` satisfying the required torsion relation; that is a separate problem.

## 5. Precise cyclic-cover source and its scope

[Ambro, Cyclic Covers and Toroidal Embeddings, Section 4, Lemmas 4.1--4.2](https://arxiv.org/pdf/1310.3951), pp.25--26, prove that a torsion Weil divisor of exact order `t`, with `t` prime to the characteristic, gives an irreducible normal cyclic cover of degree `t` by adjoining the root of a principal representative of `tD`. Lemma 3.5, p.22, gives the codimension-one ramification index `t/gcd(t,ord_E(phi))`; the proof of Lemma 3.6, p.23, gives etaleness on the regular locus when `D` is integral. Hence the torsion cover is quasi-etale, rather than necessarily etale at singular points.

Source caution: Theorem 0.1(a)'s introductory phrase about the entire etale locus, if read literally for non-Cartier integral `D`, is overbroad and conflicts with the stated flatness criterion. The precise later lemmas and the local Cartier argument are sufficient here. Do not use that introductory phrase to erase singular-point ramification.

No statement about the fundamental group of `X_reg` being trivial has been obtained or assumed. The Kummer example proves that such a general assertion is false. No universal bound on `t` across unbounded carrier degree is claimed.

## 6. New integral Cartier-intersection constraint and finite index families

Added on 2026-10-14 after the preceding source work. This is a new independent audit of the root's suggested strengthening, not a replay of an inherited computation.

**PROVED HERE.** Under the mate relation, `C0` is Q-Cartier. By the definition of each algebraic local index, `R*C0` is Cartier at every singular point on `C0`. It is automatically Cartier at regular points and, as a divisor, is zero locally outside `C0`. Therefore `R*C0` is globally Cartier.

If a mate gives `m*C0 ~ b*H`, intersection with `H` gives `4m=ab`, so `b/m=4/a`. The rational self-intersection is consequently

`C0^2 = (b/m)(H.C0) = 16/a`.

Equivalently, one can avoid treating the Q-Cartier self-intersection as a separate definition: restrict the line-bundle relation for `m*R*C0 ~ b*R*H` to `C0`, then take integer degrees and divide by `m`. Since `H|C0` has degree four, this gives

`deg(O_X(R*C0)|C0) = 4bR/m = 16R/a`.

The left side is the degree of an actual invertible sheaf on the smooth projective curve. It is an integer, hence

`a divides 16R`.

This argument would also work for an integral projective curve of degree `d`, giving `a divides d^2 R`, whenever the mate relation and actual local Cartier indices exist.

**PROVED finite arithmetic consequences.** Assume the accepted exclusion of normal carrier degrees at most four, so a surviving carrier has `a>=5`. If every local index divides a fixed integer `L`, enumerate only

`R|L`, `a|16R`, `g=gcd(a,4)`, `t=R/gcd(R,a/g)`, `b_min=(4/g)*t>4`.

An elementary integer divisor enumeration gives:

| Local index bound | Surviving `(a,R,t,b_min)` |
|---|---|
| `L=2` | none |
| `L=3` | none |
| `L=4` | none |
| `L=6` | none |
| `L=12` | `(6,12,4,8)` and `(8,12,6,6)` |

For `L=12`, the proper-divisor values `R=1,2,3,4,6` are already excluded by the preceding rows. For `R=12`, the carrier degrees to inspect are the divisors of `192` at least five: `6,8,12,16,24,32,48,64,96,192`. Substitution in the exact torsion formula leaves precisely `6` and `8`; the degree `12` case has mate degree four and the remaining cases have smaller mates. The enumeration was also checked with a short Python integer-divisor loop; this is elementary arithmetic verification, not a new CAS certificate or a rerun of an old verifier.

**Final node conclusion.** On-curve ordinary nodes give `R<=2`, so `a|32`. No odd carrier degree at least five divides `32`; the even degrees have already been excluded by `b_min<=4`. Hence all normal `C0` carriers whose on-curve singularities are ordinary nodes are excluded, assuming the accepted carrier-degree-at-most-four exclusions. Singularities away from `C0` are unrestricted in this statement.

The two `L=12` rows are only necessary arithmetic survivors. No existence statement, classification of actual on-curve ADE configurations, or global normal-carrier resolution follows from this table alone.
