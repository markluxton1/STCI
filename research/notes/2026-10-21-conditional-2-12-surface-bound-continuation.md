# Conditional (2,12;6,16;2): strict-surface continuation and independent audit

Date: 2026-10-21. Author: `surface_bound` worker.

Status: **continuation of reviewed conditional proposals**. The normal
strict-sextic exclusion has independent review PASS in the linked audit.
The ampleness and nodal extension are independently reconstructed below.
No canonical result record is changed, and no global pair or emptiness
of the full residual incidence is asserted.

## 1. Saved work and exact authority

The pre-interruption contribution is
[the October 20 surface-bound proposal](2026-10-20-conditional-2-12-surface-bound.md).
It proves that an ACTUAL supported pair in the exact conditional
configuration cannot have a normal strict sextic `D` on
`B=Bl_C0(P3)`. Its proof was independently reconstructed by
`incidence_audit` in
[the October 21 audit, section 2](2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus.md).
The inherited mathematical inputs are promoted R-0010 and R-0011;
the finite singular-root bridge remains a separately reviewed,
unpromoted dependency. This continuation does not broaden those
promoted theorem statements.

For a normal strict sextic, the local Jacobian containment

    J_(A*p+t^10*U) subset (A,p,t^9)

gives total Milnor number at least `9*16=144`. It applies to all
multiplier multiplicities and all retained root types. A genus-six
general plane section of a resolution bounds its irregularity by six;
the resolution/contraction exact sequences give `b1(D),b3(D)<=12`.
Since a smoothing has Euler number 28, the isolated singularities have
total Milnor number at most 50. The contradiction `144>50` is the
reviewed normality obstruction. It needs no V5 model, discriminant
degree formula, or K3 singularity classification.

## 2. Independent audit: the strict mate is ample

Let `L=3H-E`. The seven cubic generators of `I_C0(3)` give a closed
graph embedding

    B -> P3 x P6.

Indeed the Rees algebra of the generated twisted ideal is a quotient
of its symmetric algebra, so its relative Proj embeds in the trivial
projective bundle. The restrictions of the two hyperplane bundles
are `H` and `L`. Consequently

    G' =16H-2E=10H+2L

is the restriction of the ample bundle `O(10,2)`.

If a projective curve `Gamma` is contained in `Sing(D)`, it must
intersect `G'`, unless it is contained in `G'`; in the latter case it
is already in the actual common support. The actual strict pair has
common support precisely `Z`. Thus every singular curve of `D`
meets `Z`. This is a consequence of the ACTUAL supported pair and
does not follow from the abstract root incidence alone.

**Independent verdict: PASS.** This replaces an unjustified global
normality assumption by a local analysis along the actual common root.

## 3. Independent audit: reduced div_Z(alpha) excludes every retained root

The retained root types are smooth integral genus one, integral nodal,
and two `(1,1)` components meeting in two nodes. Assume
`div_Z(alpha)` is reduced. Then `alpha` has simple base zeros, each
away from root nodes and branch values of the degree-two projection.
In particular every zero of `alpha|Z` is a smooth point of `Z`.

Along the entire exceptional surface:

* At a multiplier fiber away from `Z`, the base derivative of
  `alpha*f` is nonzero, so `D` is smooth.
* At a smooth root point with `alpha` a unit, the root derivative
  makes `D` smooth.
* At a zero of `alpha|Z`, the exact equation is `A*p+t^10*unit`
  in regular coordinates, hence an isolated `A9` singularity.
* At a retained node, `alpha` is a unit. The parameter-preserving
  Morse lemma writes the strict sextic as `xy+h(t)`, where `t=0`
  is the exceptional surface. It has a singular curve through the
  point only when `h=0`; then that curve is uniquely `x=y=0` and
  is smooth and transverse to `E`.

Thus no singular curve is contained in `E`. Any singular curve
`Gamma` not contained in `E` can meet `E` only at the at most two
nodes of `Z`, with local intersection multiplicity one. On its
normalization put

    d=H.Gamma>0,          e=E.Gamma<=2.

At all these contacts `alpha` is a unit, so one may take the first
finite-bridge generator to be `F'` itself. Then

    G'=C*F'+t^10*unit.

Since `F'` vanishes on `Gamma`, restriction gives order exactly
ten times the order of `E` at each contact. There are no other
zeros of `G'|Gamma`, by actual sole common support `Z`. Hence

    G'.Gamma=10e.

The divisor class of `G'` also gives

    16d-2e=10e,          e=4d/3.

Integral positive `d,e` then imply `e>=4`, contradicting `e<=2`.
There is no singular curve, so the Cohen--Macaulay hypersurface
`D` is regular in codimension one and normal. Section 1 excludes it.

**Independent verdict: PASS.** Therefore every actual pair in the
exact configuration must have a NONREDUCED divisor `div_Z(alpha)`.
The proof retains singular nodes; it does not add a smooth-root
assumption. In coefficient terms the reviewed exceptional condition
is currently

    Disc_8(Ncomp(tau))*Res_(8,4)(Ncomp(tau),Delta)=0,

of total degree 52 in the nine root coefficients, with
`Delta=b^2-4ac`, `tau=f(-z/2,1)`, and the actual norm multiplier.
The earlier full root discriminant factor is unnecessary.

## 4. Conductor budget: a useful identity, not yet an exclusion

For an integral nonnormal strict sextic let `nu:Y->D` normalize it.
The finite-duality identity gives

    omega_Y = I_conductor tensor nu^*omega_D,
    omega_D=O_D(Q'),          Q'=2H-E.

Let `Cbar` be the conductor scheme on `Y`. If a general `L` section
meets all its components properly, normalizes the corresponding
section curve, and avoids the finitely many normalization singular
points, ordinary curve conductor duality gives

    L.Cbar=2*(6-g_L)<=12.

Here `g_L` is the geometric genus of that section curve. The identity
records the arithmetic-genus-six budget for a general `L` section;
it cannot be used when that section does not separate components or
meets a contracted conductor component improperly without checking
the stated conditions. In particular it is not a bound on the
length of the whole Jacobian scheme.

The normal plane class `H` has degree zero on exceptional vertical
fibers, whereas `L` has degree one there, so `L` can detect conductor
on such fibers. The initial budget of twelve alone nevertheless
allows several generic ordinary-double fibers and supplies no
contradiction by itself. High contact does not force their generic
transverse singularity to be `z^m+t^10`: the permitted formal model

    F'=p*(z^2+t^2)+t^10

is generically an ordinary double point along the fiber `z=t=0`.
Its conductor cost cannot be estimated by silently omitting the
`t^2` term in `A`.

## 5. Local nonnormal escape models and the global degree boundary

At a smooth ramification point a simple BASE multiplier can still
give a nonreduced pulled-back divisor. The exact formal model

    A=z, p=z-w^2-2t^5,
    F'=A*p+t^10=(z-t^5)^2-z*w^2

has smooth root `z=w^2` on `E`, simple base multiplier `z`, and a
singular curve `w=0,z=t^5`. Thus squarefreeness on the base alone
does not establish local normality. This model is not a global
sextic in the permitted coefficient space.

At a node with a simple base multiplier there are further local
escapes. Put

    R=(z-t)^2*(z-t^8),
    F'=z*w^2-R,
    p=(F'-t^10)/z.

The last expression is regular because `R(0,t)=-t^10`. Then
`F'=z*p+t^10`, the exceptional root is `w^2-z^2=0`, and the
singular curve `w=0,z=t` leaves `E`. This verifies why the case
where a base multiplier vanishes at a node needs its own analysis.

None of these formal constructions supplies actual global
`k`-coefficients of `F6,G16`, and the original literal normal-degree
budget of the sextic is still binding. They are countermodels to
missing local hypotheses, not counterexamples to the global
conditional exclusion sought by the user.

The separate conductor-ramification note develops a stronger route
through a Gorenstein surface with trivial dualizing sheaf. Applying
it here requires an independently justified contraction to such a
surface; the bare local bridge does not supply that contraction.
Until that bridge and the local conductor arguments are reviewed,
section 3 is the exact independently checked global exclusion.
