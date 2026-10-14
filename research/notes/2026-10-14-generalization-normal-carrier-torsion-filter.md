# All-degree torsion filter for normal carriers of fixed C0

Date: 2026-10-14. Owner: `global_structure`. Status: **NEW DIRECT
COROLLARY OF ACCEPTED PREMISES; independent review requested**.
No earlier verifier or proof was rerun.

## 1. Exact divisor-class criterion

Let `X subset P3` be a normal integral surface of degree `a` containing
the fixed smooth rational quartic `C0`, over an algebraically closed
field of characteristic zero. Let `H=O_X(1)` and let `c` be the
smooth Weil prime `C0` on `X`. Put

    h=gcd(a,4),    u=a/h,    v=4/h,
    Delta=u c-v H in Cl(X).

If a degree-`b` mate exists, its Cartier divisor is `m c` and
intersection with `H` gives `4m=ab`. Hence `m=u k,b=v k` and

    k Delta=0.

Conversely, if `Delta` is torsion of order `t`, its class relation
`t u c~t v H` supplies a global section of `O_X(tv)` with divisor
exactly `tu c`. Normality means no conductor descent remains. The
hypersurface restriction sequence lifts this section to an ambient
form of degree `tv`, giving a mate. Every normalized mate section is
unique up to scalar at its degree, because its specified divisor is
fixed and `X` is proper integral.

Therefore the complete normal-carrier criterion is:

    a mate exists iff Delta is torsion;
    if it does, its minimum mate degree is b_min=t*4/gcd(a,4).  (1)

This statement uses normality, not smoothness or Cartierness of `c`.
It covers arbitrary singularities and arbitrary carrier degree.

## 2. The accepted low-degree theorem forces nonzero torsion

The accepted fixed-C0 plane/quadric/cubic/quartic exclusions prohibit
any ambient mate of degree at most four, regardless of the other
carrier degree. If `Delta=0`, the converse construction above gives
a mate of degree `v`, which is one, two, or four. This is impossible.

Consequently every surviving normal carrier with a mate has

    Delta nonzero torsion,   t*v>=5.                         (2)

In particular **every normal carrier with torsion-free `Cl(X)` is
excluded for fixed C0 in every mate degree and every carrier degree**.
More generally, any normal carrier whose torsion subgroup does not
contain the required nonzero class order is excluded.

The congruence cases are:

| Carrier degree | `v` | Necessary class order and smallest possible mate degree |
|---|---:|---|
| `a` odd | 4 | `t>=2`, `b_min>=8` |
| `a=2 mod 4` | 2 | `t>=3`, `b_min>=6` |
| `a=0 mod 4` | 1 | `t>=5`, `b_min>=5` |

These are exact necessary class-order restrictions, not a theorem
that the indicated classes occur or that their divisor is the fixed
embedded curve.

## 3. Resolution formulation and a coverage warning

For a smooth projective resolution `M->X`, the class group can be
computed as the Picard group modulo the classes of exceptional primes.
The relevant torsion is therefore controlled by nonprimitive embeddings
of the exceptional lattice and, where present, Picard torsion.
Knowing that `Pic(M)` is torsion-free does not by itself show that
`Cl(X)` is torsion-free: a quotient by a nonprimitive exceptional
subgroup can acquire torsion. One must use the actual saturated
exceptional lattice, not silently discard this quotient torsion.

The accepted quartic/quintic lattice arguments already preserve this
distinction in their respective finite ADE types. The present result
does not classify exceptional lattices at arbitrary carrier degree.
It proves an all-degree exclusion for the torsion-free class-group
lane and leaves the required nonzero torsion classes as an explicit
global obstruction to be studied.

The Cartier-lift classification gives a different all-degree boundary:
a smooth rational degree-`d>=3` curve with a mate on a normal carrier
must be non-Cartier somewhere. The present torsion filter additionally
requires the particular primitive degree-zero divisor class `Delta`
to be nonzero torsion for fixed C0. Neither condition supplies a
uniform bound on all normal carriers.
