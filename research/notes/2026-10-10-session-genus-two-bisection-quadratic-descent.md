# Genus-two bisections: quadratic compression and split-conductor descent

Date: 2026-10-10. Owner: `oct10_conic_bundle_mate`.
Status: **PROVED HERE, supplied for independent audit**. The second-pencil
and four-blowup inputs below are independently proved in the
[second-pencil audit](2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md).
The conductor and blowup model are the actual entire schemes, not a
generic or reduced substitute. This note does not exclude all bisection
mates and edits no canonical frontier file.

Work over an algebraically closed field of characteristic zero, for the
fixed smooth rational quartic

    C0=[s^4:s^3t:st^3:t^4].

Let `X` be an integral nonnormal quartic with normalization sectional genus
two and let `S`, `M`, `H`, `L`, `f`, `c`, and `Z` have their accepted
meanings. Assume a mate and the bisection stratum

    c^2=0, K_M.c=-2, f.c=2, Z=L-c,
    Z>=0, Z supported on vertical exceptional (-2)-curves.

## 1. Independently audited second-pencil input

The complete `|c|` is a basepoint-free connected rational pencil, and
`(f,c):M -> P1 x P1` has degree two. Its normal Stein cover `W` is a
flat double cover with branch class `(2,2)` and is an ADE del Pezzo
surface of degree four. If `V -> W` is its crepant minimal resolution,
`M -> V` consists of exactly four point blowups, including any infinitely
near centers. Write the effective integral relative canonical divisor as
`R`. There is an actual equality of rational divisors

    Z+R=sum_t (k_t/2) F_t,
    sum_t k_t=4,

where `F_t` is the entire fiber and `k_t` counts the four centers over
that fiber. In particular

    2Z=sum_t k_t F_t - 2R

is an integral exceptional divisor. The support can consist of up to
four fibers; a proposed two-fiber bound was false and is not used here.
The audited remaining blowup partitions are `[3,1]`, `[2,1,1]`, and
`[1,1,1,1]`. No local fiber classification is claimed by this count.

Pushing the integral divisor identity down to `S` gives the actual Weil
equivalence

    2c_S ~ 2H.

Thus `2c_S` is effective Cartier, with a section
`Q in H0(S,O_S(2H))` having entire divisor `2c_S`. Every mate degree is
even. If its degree is `b=2n`, its pullback to `S` is a scalar multiple
of `Q^n`, since both sections have entire divisor `2n c_S` and `S` is
normal projective integral. This is compression on the normalization;
`Q` has not yet descended to an ambient quadric.

## 2. The extra quadratic section and its entire conductor restriction

The [entire-conductor audit](2026-10-10-session-genus-two-entire-conductor-independent-audit.md)
gives the actual reduced conductor line `Gamma` and the exact sequence

    0 -> O_X -> nu_*O_S -> O_Gamma(-2) -> 0.

Twisting by two and using the hypersurface restriction sequence gives

    h0(S,2H)=11,
    H0(S,2H)/H0(X,O_X(2))=k.

The ten sections of `O_X(2)` are precisely ambient quadrics. On the entire
upstairs conductor `D`, the canonical trace splitting is

    p_*O_D=O_Gamma (+) O_Gamma(-2),
    w^2=delta, delta in H0(Gamma,O_Gamma(4)).

Here `w` denotes the local trace-zero generator, with its global twist.
After twisting by `2H`, every section restricts in the form

    Q|D=m+a w,
    m in H0(Gamma,O_Gamma(2)), a in k.

The coefficient `a` is zero exactly when the section is ambient. This
follows either from the normalization sequence above or directly from
the exact common-conductor square: a section descends if and only if its
entire restriction to `D` comes from `Gamma`. The trace-zero part of the
normalization quotient is the displayed `O_Gamma(-2)`.

For our `Q`, one must have `a!=0`. Otherwise `Q` would give a quadric
mate for `C0`. Every ambient quadric containing `C0` is a scalar multiple
of the unique smooth quadric

    q=x0 x3 - x1 x2.

On `q=P1 x P1`, the curve has class `(1,3)`, while an integral quartic
carrier cuts class `(4,4)`. A divisor supported only on `C0` would have
class `j(1,3)`, and no positive `j` gives `(4,4)`. Hence this quadric
cannot be a mate. Normalize `Q` so that

    Q|D=m+w.

The restriction is a nonzerodivisor on the CM curve `D`: the divisor of
`Q` has support only `c_S`, and `c_S` cannot be a component of `D`, whose
entire `H`-degree is two rather than four.

## 3. The trace-zero alternative is excluded by the known (4,4) theorem

If `m=0`, then

    Q^2|D=delta

comes from `Gamma`, on the entire conductor including every nilpotent
stratum. The common-conductor square therefore descends `Q^2` to a
section of `O_X(4)`. The hypersurface restriction sequence lifts it to
an ambient quartic. Its pullback has divisor `4c_S`, so its zero set on
`X` is precisely `C0`; finiteness and surjectivity of normalization
justify that full-support conclusion. This gives a `(4,4)` STCI.

Craighero--Gattazzo's 1986 theorem excludes exactly this degree pair for
the literal Cremona quartic over an algebraically closed field of
characteristic different from `2,3`, hence in characteristic zero.
The primary PDF was checked live on 2026-10-10: its abstract on printed
page 177 states the characteristic hypotheses, and Proposition 4 on
printed page 187 is the two-quartic exclusion. See
[the primary paper](https://www.numdam.org/item/RSMUP_1986__76__177_0.pdf).
This use is only a `(4,4)` exclusion, not an unrestricted non-STCI
theorem. Consequently `m!=0`.

## 4. Every remaining bisection mate has a reduced split conductor

Apply the independently audited
[quadratic power-descent criterion](2026-10-09-session-quadratic-conductor-power-descent-independent-audit.md)
to the actual nonzerodivisor `m+w`. Since `m!=0` and the trace-zero
coefficient is one, descent of a positive power forces

    m^2=rho delta,
    rho=((1+zeta)/(1-zeta))^2,

where `zeta` is a root of unity different from `1` and `-1`.
The equality is an equality of global quartic sections, including all
special fibers. In particular `delta` is a nonzero square.

Write `delta=r^2` after choosing a constant square root, with
`r in H0(O_Gamma(2))`, and `m=alpha r`. Then `D` is reduced with two
components mapping isomorphically to `Gamma`; they meet at the zero
scheme of `r`. The conductor sections are

    Q_+=(alpha+1)r, Q_-=(alpha-1)r.

Nonzerodivisorship gives `alpha!=1,-1`; the excluded trace-zero case
gives `alpha!=0`. The remaining condition for a power to descend is

    ((alpha+1)/(alpha-1))^n=1.

Conversely this equality implies descent on the entire reduced `D`,
since equality on its two generic components implies equality of the
sections on a reduced scheme. No unbounded root-of-unity order has been
replaced by a finite search. If the ratio has order `n`, the compressed
mate degree is `2n`, with `n>=3`.

Thus this branch now requires a **reduced split genus-one conductor**
and a constant root-of-unity ratio. The nonreduced `delta=0` branch and
all nonsplit quadratic-cover branches are excluded for a bisection
mate; they were retained through the reduction rather than assumed
away at the start.

## 5. A proposed additional contact identification, for separate audit

The following local deduction is supplied separately and should not be
used before its audit.

The entire support of `Z` is a union of connected exceptional fibers.
Indeed for a prime outside its support,

    Z.E=-c.E<=0,

while effectivity and distinct-curve intersections give `Z.E>=0`.
Hence no outside exceptional prime is adjacent to its support. The
horizontal coefficients are zero, so every singular point met by `c_S`
has only (-2)-curves in its exceptional fiber and is ADE. In particular
`S` is Gorenstein near `c_S`, and its actual conductor ideal, identified
with `omega_S`, is invertible there. Thus `D` is Cartier near every zero
of `Q|D`.

The Cartier divisor cut by `Q` is a CM double structure on the smooth
embedded curve `c_S`. Its nilradical is a line bundle on `c_S`: it has
generic rank one, no finite-support torsion, and square zero because
the square is generically zero and the CM double curve has no nonzero
finite-support subsheaf. It is therefore a ribbon. Intersecting this
ribbon with a Cartier divisor that meets its reduction properly doubles
the local intersection length. On the other hand the split conductor
and the formulas for `Q_+`, `Q_-` give

    length(O_D/(Q)) at P = 2 ord_P(r).

Since the conductor ideal on `X` is the ambient ideal of `Gamma`, its
restriction to `c_S~=C0` defines the actual scheme `Gamma intersect C0`.
The local ribbon calculation would therefore identify

    div_Gamma(r)=Gamma intersect C0

as degree-two schemes. For an ordinary bisecant both roots are simple;
at either contact `S` would have to be singular, since a smooth surface
would make `c_S` Cartier and give even vanishing order on each smooth
conductor branch, whereas `Q_+`, `Q_-` have order one. A tangent secant
retains a double root and is not excluded by that argument.

## 6. Unresolved obligations

The root-of-unity ratio in section 4 has not been constrained enough
to exclude every remaining split conductor. The literal secant line
and the two rational conductor components must still be tied to the
specific missing-middle-coordinate embedding of `C0`. The four-blowup
partitions have not been classified geometrically, and singular conic
fibers and infinitely near centers remain essential.

The section/trisecant branch is separate. No claim here excludes the
genus-two quartic lane, the unrestricted `C0` question, or the universal
STCI question.
