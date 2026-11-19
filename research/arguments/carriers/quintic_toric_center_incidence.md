# Toric quintic centers: full inverse support and exclusion

<a id="toric-quintic-centers-full-inverse-support-and-the-remaining-incidence"></a>

Fix the embedded rational quartic
`C0=[u^4:u^3v:uv^3:v^4]` over an algebraically closed field of
characteristic zero. Every admissible projection of a marked toric
quintic normalization has an extra inverse point over C0. Consequently
no integral quintic with toric normalization can carry a mate for C0.
The argument leaves the unrestricted STCI question open.

## 1. Geometric object and scope

Assume an integral quintic S has toric normalization and a hypothetical
sole-supported mate for C0. The [polarized-source classification](quintic_non_gorenstein_toric_sources.md#41-this-is-the-only-remaining-polarized-toric-normalization)
gives the full reduced inverse of C0 as a single smooth degree-four
curve. The [marked-curve classification](quintic_non_gorenstein_toric_sources.md#42-the-marked-curve-is-unique-up-to-a-source-automorphism)
identifies the normalization and that curve, up to polarized isomorphism,
with the following pair in P4:

    X: BD-C^2 = AEC-D^3 = ABE-CD^2 = 0,
    c(t)=(t,t^3(t+1),t^2(t+1),t(t+1),(t+1)^2).

The marked curve includes its projective point at infinity. The
normalization morphism is projection from a point outside X and maps c
isomorphically to C0. An extra point of X outside c mapping into C0
contradicts the full reduced inverse support forced by a mate of any
degree. Equivalently, every pulled-back mate would be a nonzero scalar
times a positive power of the [section with divisor `5c`](quintic_non_gorenstein_toric_sources.md#5-the-quartic-root-exists-on-the-normalization),
which is nonzero at the extra point. This is the necessary support part
of the [fixed-carrier criterion](../../results/fixed_carrier_conductor_criterion.md).

Restriction identifies `H0(X,H)` with `H0(P1,O(4))` because the five
coordinates of c form a basis. In the binary monomial basis the target
embedding C0 uses the subsystem `span(u^4,u^3v,uv^3,v^4)`. Since any
isomorphism from c to C0 differs from the displayed parametrization
by a PGL2 change on P1, the four-dimensional subsystem on c is a
PGL2 translate of that subsystem. Its annihilator gives the center,
so the centers form the PGL2 orbit of coefficient extraction at
`u^2v^2`, restricted to points outside X.

In coordinates, apply the functional `f -> [u^2v^2] f(U,V)` for
an invertible substitution `(U,V)=(a_0*u+b_0*v,c_0*u+d_0*v)`.
Scaling either column of this substitution scales the functional by
the square of that factor, and exchanging the columns preserves it.
Thus it suffices to use the unordered pairs of distinct points
`[a_0:c_0],[b_0:d_0]` of P1. For a finite pair choose
`(U,V)=(u+v,q*u+r*v)`. For one point at infinity choose
`(U,V)=(u,r*u+v)`. These are the two charts of §§2–3. Coincident
columns would give a functional proportional to evaluation at the
common column point, which is a point of c itself and cannot be a
center.

If `(p0,p1,p2,p3,p4)` are the extracted coefficients for
`(U^4,U^3V,U^2V^2,UV^3,V^4)`, the coefficients in the marked source
coordinates are `(p3,p0+p1,p1+p2,p2+p3,p2+2*p3+p4)` by the
homogeneous parametrization (6) of the marked source. Substituting
the two chart matrices yields the center formulas below. Each such
center outside X yields the required image on c. The projection of X
is finite because its pullback of O(1) is ample. Its image spans P3,
so the degree product five also forces this projection to be
birational onto an integral quintic.

## 2. Finite-pair chart and certified exclusions

For distinct finite r,q put `m=r+q`, `n=rq`, `Delta=m^2-4n !=0`.
The source center `P=(a,b,c,d,e)` is

    a=3mn, b=3(m+2), c=m^2+2n+3m,
    d=m^2+2n+3mn, e=m^2+2n+6mn+6n^2.

Here c in this coordinate list is a scalar, not the marked curve. Set

    K=bd-c^2=-Delta*K0,   K0=m^2-n+3m+3,
    h(t)=dt^2-2ct+b,      D(t)=t(t+1)h(t).

On the fiber line `c(t)+lambda P`, the quadric equation is
`lambda(D+lambda K)=0`. For K nonzero the nonmarked branch is
`lambda=-D/K`. The residual polynomial W is preserved by its six exact
coefficients in the [finite-center input](../../computations/quintic_toric_finite_centers.json),
produced by the [finite-center certificate](../../computations/quintic_toric_finite_centers.py).
It satisfies

    W_5=d*N, W(0)=K0*U0, W(-1)=-K0*V1*V2,
    Res_t(W,h)=Delta^4*d^2*K0^3*M,   R(P)=-Delta*N,

where

    N=m^4+6m^3n+9m^2n^2+m^2n+9mn^3-6mn^2-2n^2,
    U0=m^4+4m^2n+4n^2+3m^3+6mn+3m^2-12n,
    V1=m^2+2n+6m+6,
    V2=m^2+2n+6mn+6n^2,
    M=11m^4+15m^3n+36m^3+21m^2n^2+8m^2n+39m^2
      +9mn^3+30mn^2-45mn+27m+6n^3+8n^2-30n+18.

The geometric meaning of a root of W outside `D=0` is an actual extra
inverse point: the resulting lambda is nonzero and all three equations
of X vanish. Thus `d*N*U0*V1*V2*M !=0` excludes full inverse support.
The factor M is essential; an earlier diagnostic omitted it and was
corrected before acceptance.

The following boundary arguments are also certified.

| Parameter locus | Actual reason for exclusion |
| --- | --- |
| `K=0` | `n=m^2+3m+3`. For `m != -1,-2`, take `t=1/(m+1)` and `lambda=-t^2(t+1)/c`; the resulting point has B=C=D=0 and lies on X outside c. The diagonal case m=-2 is inadmissible. At `(m,n)=(-1,1)`, take t=0 and lambda=-1/3, obtaining `[1:-1:0:0:0]`. |
| `K !=0, d !=0, N=0` | At the marked point at infinity, `Q=lambda(d+lambda K)` and `R=lambda^3 R(P)`. The nonzero root `lambda=-d/K` also satisfies T by the toric syzygy, giving an extra point. |
| `K !=0, d=0` | Substitute `n=-m^2/(3m+2)`. W has degree four on the retained locus. Full support would require `W | D^5`. The remainder-coefficient numerator gcd is `243(m+2)^5`, whose only root is diagonal. All denominator zeros are outside the retained locus. |

After these tests, the initially certified remaining finite locus is

    Delta*K0*d*N !=0,   U0*V1*V2*M=0.                 (1)

## 3. The entire one-infinity boundary is excluded

Here

    P(r)=(3r,0,1,1+3r,1+6r+6r^2), K=-1,
    h=(1+3r)t^2-2t, D=t(t+1)h.

The [boundary certificate](../../computations/quintic_toric_boundary_centers.py)
uses exact identities on `lambda=D`:

    (R/lambda)=t(t+1)W_b[1-(3r+1)t],
    (T/lambda)=-t^2(t+1)W_b.

The polynomial W_b has constant coefficient one, leading coefficient
`(3r+1)(9r^3+9r^2+6r+1)`, value
`W_b(-1)=-(6r^2+6r+1)`, and resultant with h equal to
`(3r+1)^2(9r^3+21r^2+15r+11)`. Away from these four parameter factors,
any root supplies an extra point. The complete exceptional tests give:

| Parameter factor | Degree of W_b | Degree of gcd(W_b,D^5) |
| --- | ---: | ---: |
| `3r+1` | 4 | 0 |
| `9r^3+9r^2+6r+1` | 4 | 0 |
| `6r^2+6r+1` | 5 | 1 |
| `9r^3+21r^2+15r+11` | 5 | 1 |

Each factor is irreducible over Q and the factors are pairwise coprime;
the exact number-field computations therefore cover every conjugate
parameter in characteristic zero. The strict degree inequality supplies
an extra root in every case. The support test uses D^5 rather than D,
so repeated roots are retained.

The projective marked endpoint was separately checked with fiber coordinates
`(3rz,1,z,(1+3r)z,(1+6r+6r^2)z)`. It has an extra point when
`9r^3+9r^2+6r+1=0`; at r=-1/3 the fiber is a double point supported
on c. The limiting center r=infinity is `[0:0:0:0:1]` on X and is
inadmissible. These endpoint checks do not replace the finite-t argument.

<a id="4-three-exceptional-curves-and-the-uncompleted-locus"></a>

## 4. Exceptional finite loci and complete exclusion

For nonzero W in characteristic zero, the exact elementary criterion is

    Supp V(W) subset Supp V(D)  iff  W divides D*W'.     (2)

At a root of multiplicity e, W' has order e-1. This explains both
necessity and sufficiency and why characteristic zero matters; it is
not a characteristic-independent support certificate.

The [three-curve calculation](https://github.com/markluxton1/STCI/blob/719e47f452b5286a794731637df5c086b068bad5/research/computations/quintic_toric_exception_centers.py)
uses (2) on U0, V1 and V2. The independent source closeout review **passes**:
all three curves are excluded on `Delta*K0*d*N !=0`. It supplies the
[separate specialization audit](https://github.com/markluxton1/STCI/blob/719e47f452b5286a794731637df5c086b068bad5/research/computations/quintic_toric_exception_audit.py)
and the following complete evidence, rather than inferring coverage from a
generic remainder.

Write the source equations on the fiber line as R and T, distinguishing
the coordinate D of P4 from the polynomial D(t). The exact identities are

    K^2 (R/lambda)|_(lambda=-D/K) = -Delta*t(t+1)*W*(dt-c),
    K^2 (T/lambda)|_(lambda=-D/K) = -Delta*t(t+1)*W*(ct-b).

The two linear cofactors have resultant `c^2-bd=-K !=0`. Thus the
specialized residual gcd after the universal endpoint factors is exactly
W up to a unit at every retained point, not only generically.

The parameterizations and numerator-gcd tests are:

| Curve | Parameterization | Gcd of numerator coefficients of rem(D W',W) |
| --- | --- | --- |
| V1 | `m=k, n=-(k^2+6k+6)/2` | `81(k+2)^4` |
| V2, m nonzero | `m=-2k/q, n=km`, `q=6k^2+6k+1` | `81(2k+1)^4(10k^2+6k+1)` |
| U0, m nonzero | `m=-12(k+3)/p`, `x=6+(k-3)m/2`, `n=(x-m^2)/2`, `p=k^2+27` | `139968(k-3)^3(k+3)(k^2-12k+63)` |

Every root of these gcds has Delta=0 or K0=0. The V1 graph is complete.
For V2 with m nonzero, k=n/m gives `mq+2k=0`; q=0 would also force k=0,
so its poles give no affine center. The m=0 points are `(0,0)`, excluded
by Delta, and `(0,-1/3)`, whose separately computed remainder has
coefficient-numerator gcd 800 and is nonzero. For U0 put
`x=m^2+2n`, `y=2x+3m-6`; then
`y^2+27m^2+36m-36=4U0`. With m nonzero, `k=(y-6)/m` gives
`pm+12(k+3)=0`. Its poles again give no finite center. The two m=0
points are `(0,3)` with K0=0 and `(0,0)` with Delta=0.

For explicit denominator coverage, define

    A1=k^2+4k+2,
    B1=k^6+14k^5+78k^4+212k^3+276k^2+144k+8,
    A0=k^3-3k^2+99k+135,
    B0=k^9+3k^8+144k^7+648k^6+15066k^5-30618k^4
       +577368k^3-1714608k^2-6528195k+27497151.

| Curve | Leading coefficient of W (dN) | Common denominator of canceled remainder coefficients, up to rational units |
| --- | --- | --- |
| V1 | `27(k+2)^2 A1 B1/16` | `8 A1 B1^3` |
| V2 | `1728 k^10(2k+1)^2/q^6` | `k^3 q^8` |
| U0 | `5038848(k-3)^2 A0 B0/p^10` | `p^10 A0 B0^3` |

All additional denominator zeros lie on dN=0, on an excluded Delta=0
point, or at parameter poles with no affine center. W therefore has
degree five throughout the retained open set, division commutes with
specialization there, and no degree-drop point was silently omitted.

The remaining finite incidence is consequently

    M=0, Delta*K0*d*N*U0*V1*V2 !=0,
    W divides h*W'.                                      (3)

The omitted t(t+1) factor in (3) is invertible on Supp(W), by the
nonzero U0,V1,V2 conditions. The infinity fiber is already controlled
by N nonzero. The quadratic h has two distinct roots, since its
discriminant is `4(c^2-bd)=-4K !=0`. Thus (3) is equivalently

    W=gamma*(t-alpha)^j*(t-beta)^(5-j), j=0,...,5,

where alpha,beta are those two roots and gamma is nonzero. Up to their
exchange there are three multiplicity patterns, 5+0, 4+1 and 3+2.
Geometrically all five residual-polynomial roots would have to coalesce
at the two parameters where the nonmarked branch returns to the marked
point. The following calculation excludes all three multiplicity patterns
at once.

### Exact elimination on M=0

Write `W=sum_i w_i t^i` and set `w_-1=w_6=0`. On (3) we have
`w_5=dN !=0`. If W divides `h W'`, comparing the two highest
coefficients forces the quotient to be `5dt-10c-d*w_4/w_5`.
After clearing `w_5`, the coefficient of `t^i` in the difference is

    E_i = w_5*((i-6)*d*w_(i-1) - 2ci*w_i + b*(i+1)*w_(i+1))
          + (10c*w_5+d*w_4)*w_i.

The coefficients at degrees six and five vanish identically. Thus (3)
requires `M=E_0=...=E_4=0`. For each i from 0 to 4 compute
`R_i(m)=Res_n(M,E_i)` over Q[m] using the degrees before specializing m.
For every pair `(m_*,n_*)` in the ground field satisfying these six
equations, evaluation at `n_*` annihilates the image of each Sylvester
map specialized at `m_*`. Evaluation is a nonzero linear functional, so
all five resultants vanish at `m_*` even if some input degrees drop. The
[exact elimination](../../computations/quintic_toric_remaining_centers.py)
gives the monic squarefree part of `gcd(R_0,...,R_4)` as
`p_1*p_2*p_3*p_4/24`, where

    p_1 = m+2,
    p_2 = 3m+2,
    p_3 = m^3+4m^2+4m+8,
    p_4 = 8m^5+32m^4+42m^3+31m^2+16m+4.

These four irreducible factors give the necessary projection locus.
For each factor p, let a be the class of m in the number field
`Q[m]/(p)`. Reduce the coefficients of M and every E_i modulo p, then
take their monic common gcd as polynomials in n over that field.
The degrees of `(M,E_0,E_1,E_2,E_3,E_4)` over Q(m) are
`(3,8,8,9,9,9)`. The table gives the exact specialized degrees and gcds.

| Factor | Specialized degrees in n | Monic common gcd in n | Consequence on (3) |
| --- | --- | --- | --- |
| `p_1` | `(3,8,8,9,9,8)` | `(n-1)^2` | At `a=-2, n=1`, the gate factor `Delta=a^2-4n` vanishes. |
| `p_2` | `(2,7,7,8,8,7)` | `1` | The specialized equations have no common root. |
| `p_3` | `(3,8,8,9,9,9)` | `n-a^2/4` | The gate factor `Delta=a^2-4n` vanishes. |
| `p_4` | `(3,8,8,9,9,9)` | `n+a^2/(3a+2)` | The gate factor `d=a^2+(3a+2)n` vanishes. |

In the last row `3a+2` is nonzero because `p_4` is coprime to `p_2`.
Each embedding of `Q[m]/(p)` into the algebraically closed
characteristic-zero ground field transports the gcd and its Bézout
identity, so the same computation covers every conjugate of a.
The specialized gcds use the actual input degrees, including the drops
in the first two rows. The quotient calculation in t requires degree
five only on (3), where `w_5=dN` is nonzero; the finite cases with
`dN=0` were already treated in §2. The verifier checks that the
squarefree part of each specialized gcd divides the specialized gate
`Delta*K0*d*N*U0*V1*V2`. An independent replay checked the signs,
projection and specialized exclusions. This closes the last finite-center
incidence. Together with the one-infinity boundary in §3, it excludes
full inverse support for every admissible toric center.

## 5. Exact computational evidence and scope

The [finite-center program](../../computations/quintic_toric_finite_centers.py), [coefficient input](../../computations/quintic_toric_finite_centers.json), and [one-infinity boundary program](../../computations/quintic_toric_boundary_centers.py) record the exact polynomial calculations. The [three-curve specialization certificate](https://github.com/markluxton1/STCI/blob/719e47f452b5286a794731637df5c086b068bad5/research/computations/quintic_toric_exception_centers.py) and [independent specialization audit](https://github.com/markluxton1/STCI/blob/719e47f452b5286a794731637df5c086b068bad5/research/computations/quintic_toric_exception_audit.py) establish the stated exclusions under \(\Delta K_0dN\ne0\). Their exact source versions were previously checked; these files have not been rerun in this consolidation.

The JSON preserves the coefficients and the intermediate four-curve
necessary gate. Section 4 tests all four curves and completes the
exclusion. The obstruction is an actual extra point in the inverse of C0,
so it applies to every power of the upstairs section and every mate degree.
The marked-source classification covers toric normalizations. The
non-toric, non-Gorenstein case and unrestricted characteristic-zero STCI
remain open.

## Related quintic incidence developments

The following independent mathematical developments are preserved in their complete focused Arguments, rather than repeated here as historical heading stubs:

- [Nonendpoint single-root incidence and actual quotient fibers](extracted_nonendpoint_single_root_incidence.md): regular L1 and L2 geometric bridges, conductor-root and exceptional-locus conditions.
- [Quintic h=2 necessary incidence and unresolved degree-five boundary](extracted_quintic_h2_incidence_and_localcoh_frontier.md): correct logarithmic ODE and failure of proposed eliminations.
- [Monic h=2 ODE and open incidence](extracted_quintic_h2_monic_ode_and_open_incidence.md): automatic high-coefficient open, denominator-free equations, and exact assembly.
- [Global h=2 rank and saturation frontier](quintic_h2_rank_incidence_and_ode.md): the seventeen-equation necessary model and its uncompleted saturation.

None of these necessary-incidence calculations by itself establishes a quintic mate or excludes the remaining global h=2 locus.
