# Independent audit of the inseparable-root actual-CI bridge

Date: 2026-10-15. Reviewer: `new_logarithmic_review`.

Status: **PASS for the new arbitrary-characteristic actual-CI bridge,
under all literal hypotheses.** The proposed repair correctly replaces
the separable-root elimination argument with uncompleted local algebra
at the actual root prime. It proves the full global primitive structure,
the conormal splitting, actual Cartier lifts through the claimed stages,
and the conditional finite-gap consequence in arbitrary characteristic.

Reviewed source:
[inseparable-root blowup bridge](2026-10-15-generalization-inseparable-root-blowup-bridge.md).
The accepted characteristic-zero bridge and the
[characteristic-free formal/tower addendum](2026-10-15-generalization-smooth-root-characteristic-scope-addendum.md)
are premises. The separate
[generic local-algebra review](2026-10-15-generalization-inseparable-root-blowup-local-algebra-review.md)
passes the standard-basis and root-prime steps. This full new-scope
audit checks their use in the global extension, the new wild family,
and the obstruction/lift consequences. No accepted computation,
characteristic-zero proof, CAS calculation, or verifier was replayed.

## 1. The scope that must survive the extension

Let k be algebraically closed of any characteristic, X a smooth
threefold, and C a smooth connected curve. The actual complete
intersection Y=(F,G) has reduced support exactly C. The statement uses
all of the following:

- The actual first degree-r relation sheaf is a saturated line
  subbundle of Sym^r N_C^*.
- Both chosen actual equations have generic normal order r, and their
  degree-r coefficient sections generate this line at every point.
- The **full** generic ordinary initial ideal is the coprime binary
  complete intersection (f_r,g_s), with s>r and ell=s-r>=2.
- The actual Cartier divisor Z=(f_r) on E is smooth, including its
  scheme structure, not just its reduced support.

These hypotheses are stronger than a claim about two selected initial
forms. Joint leading base points, defective relation sheaves, vertical
fiber components, nonreduced roots, and noncoprime next relations have
not been removed by saturation or admitted by the new characteristic
scope. Components of the smooth Z can be handled separately.

## 2. The new generic replacement uses the actual local ideal

At eta_C, A=O_(X,eta_C) is a regular local ring of dimension two,
with maximal ideal m and residue field K=k(C). Its associated graded
ring is K[x,y]. The proposed choice P,H in I=(F,G)A is legitimate:
P is an original generator normalized by a lifted unit, and g_s in
the degree-s component of the full initial ideal is the symbol of an
actual H in I intersect m^s.

For J=(P,H), the inclusions of initial ideals force
in_m(J)=in_m(I). For each fixed n, repeated finite order reduction
puts every element of I into J+m^n. Krull intersection in the finite
module A/J then gives I=J in the uncompleted ring. There is no claim
that an infinite division series converges in A. Both pairs minimally
generate the height-two ideal, so their change matrix lies in GL_2(A).

Its pullback remains invertible on the localized blowup. Both original
strict equations were divided by u^r, and the valid transformed ideal
is therefore

    (F/u^r,G/u^r)=(P/u^r,H/u^r)
                  =(P/u^r,u^ell*(H/u^s)).               (A)

This keeps the second exceptional factor. Dividing the new H by u^s
instead would change the object. The proof correctly studies the
intersection of the original two strict divisors, rather than a
saturation or the strict transform of the supported intersection Y.

At a generic root prime xi, use either blowup chart as needed, so no
root at infinity is lost. On x=u,y=uv the regular local ring T has

    T/(u)=K[v]_(q), residue field K'=K[v]/(q),

where q is irreducible over the actual K. Reducedness of Z is retained
under localization to K. Thus q has exponent one in f_r(1,v) over K,
even when q'=0 and K'/K is inseparable. For p=P/u^r, reduction gives
p=unit*q modulo u, so the maximal ideal of T is (u,p).
Coprimality makes H/u^s a unit at xi. Consequently (A) is exactly

    I_(Y',xi)=(p,u^ell).

The ring T/(p) is a regular local ring of dimension one, with uniformizer
u. Hence the length is ell. This is length at the actual prime with
residue field K', not a count of geometric roots or an assertion of
a K-compatible truncated coefficient-field model.

## 3. The actual global hypotheses give the local form everywhere

On E, the two original strict equations restrict to a f_r,b f_r.
The actual coefficient pair has no common zero, so this common zero
scheme is exactly Z. Off E the blowup is an isomorphism and Y has no
point away from C. Therefore Supp(Y')=Z. In particular no vertical
exceptional fiber is a component. The two strict divisors have no
common surface component; their intersection in the smooth threefold
is height two and Cohen--Macaulay, with no additional embedded or
isolated support. These conclusions use the original global equations,
not merely the generic generator change.

At every closed z in Z, choose an original strict equation h with unit
leading coefficient. Its restriction to E defines the actual smooth
Z. The full differential on E is nonzero; thus dh and du are
independent ambient cotangent vectors. This proves that S=(h) is
smooth and meets E transversely along Z, in any characteristic.
The differential in the base direction is retained when the fiber
derivative vanishes.

In the regular local surface ring R=O_(S,z), u is prime because
R/(u)=O_(Z,z) is a domain. The other strict equation has a nonzero
restriction h_2 with radical (u), by the support assertion. Unique
factorization in R gives h_2=epsilon*u^b, with epsilon a unit.
Localization at the generic point of the component identifies b
with the generic length ell already established. Lifting the unit
to the ambient local ring proves the exact uncompleted local ideal

    I_(Y',z)=(h,u^ell)                                  (B)

at every point. Neither geometric root splitting nor a coefficient
field is needed. The new inseparable generic calculation is therefore
sufficient to carry the global primitive structure across all closed
points, including purely inseparable projection points.

## 4. Conormal splitting and actual lifts are intrinsic

Let J=I_(Z/B). Since ell>=2, the image of I_Y' in J/J^2 is locally
the line generated by [h]; u^ell maps to zero. These lines glue as
the image of the global ideal map. Projection to N_(Z/E)^* is an
isomorphism on this line because h|E generates I_(Z/E). Thus they
split the actual sequence

    0 -> O_Z(-E) -> N_(Z/B)^* -> N_(Z/E)^* -> 0.

The quotient J/(J^2+I_Y') is exactly O_Z(-E), with no suppressed
point torsion. This gives the stated surviving ordinary conormal.
The full differential embedding N_(Z/E)^*->Omega_E|Z exists because
Z and E are smooth over k. Pulling back the ambient cotangent
extension gives this conormal sequence in every characteristic.
Its splitting therefore gives vanishing of the actual first
embedded-divisor obstruction. It does not transfer any
characteristic-zero formula or rational-denominator representative.

Equation (B) also gives I_E^ell subset I_Y' globally. On
V(I_E^ell), its quotient ideal is locally generated by h and is
invertible and embedded. For precision, the regular sequence is
(u,h); h is a nonzerodivisor modulo each u^n, since the successive
u-adic layers reduce this assertion to regularity modulo u. Thus
restriction preserves embedded Cartier ideals for every n<=ell.
Their equations and units glue because the ideal is the intrinsic
quotient of I_Y'. With E_m=V(I_E^(m+1)), the range supplied is

    m<ell.                                              (C)

No lift at the next stage is asserted. The condition ell>=2 is
substantive for the splitting and first-obstruction statement.

## 5. The wild family and the coefficient-field warning both pass

In characteristic p>0, put C=(x,y) in A3_(t,x,y), and choose

    F=y^p-t*x^p+x^(p+1),
    G=F+x^(p+ell), ell>=2.

The ideal is (F,x^(p+ell)), with radical (x,y), so it is an actual
height-two complete intersection supported exactly on C. Both chosen
equations have generic normal order p, and their leading coefficients
in the line generated by y^p-t*x^p are 1. That line is saturated:
the y^p coefficient is a unit at every base point.

For completeness, the claim about the **full** generic initial ideal
has an exact hand proof. Over K=k(t), the actual quotient by
x^(p+ell) is free of rank p over K[x]/(x^(p+ell)), because F is monic
of y-degree p. Its K-length is p*(p+ell). The coprime homogeneous
complete intersection (y^p-t*x^p,x^(p+ell)) has that same colength
and is contained in the actual initial ideal. Equality of these
finite colengths proves equality of the full initial ideals.

The root lies entirely in the x-chart and is v^p=t. It is smooth
as a total divisor, with full differential -dt, while its projection
is purely inseparable. Direct common division by u^p gives

    I_Y'=(v^p-t+u,u^ell).

This is a family satisfying the new bridge hypotheses, with exactly
the asserted primitive structure.

The containing generic DVR has u=t-v^p and residue field K'. If a
K-compatible embedding of K' existed, its element a with a^p=t
would satisfy (a-v)^p=u. That is impossible in a DVR, since its
valuation would require v_u(a-v)=1/p. Modulo u^ell the same failure
is already visible in the first layer: reduction forces a-v in (u),
so its p-th power lies in (u^p) subset (u^2), whereas u does not.
This works for every ell>=2, including ell<p.

The warning is specifically about compatibility with the original
K=k(t) embedding. Coefficient fields as k-fields are not excluded;
the natural k(v) coefficient field has t=v^p+u under the original
K-map. The example does not contradict Cohen coefficient fields.
Its base curve is affine, and it is not an example of an infinite
projective movement-two formal root excluded by the accepted theorem.

## 6. Consequence and acceptance boundary

Under the accepted characteristic-free smooth-root formal theorem and
tower, fix a balanced smooth rational embedding in P3 of degree e>=4
and a first normal order r. If K_N is its empty smooth-root stage,
the newly extended actual bridge supplies K_(ell-1) by (C).
Consequently

    ell=s-r<=N, equivalently s<=r+N.

At equality the actual pair supplies only stage N-1; that equality
is not excluded. Thus the positive-characteristic conditional
qualification in the earlier characteristic addendum is now met
for the literal actual-CI lane in Section 1. The bound remains
existential and does not exclude pairs introducing the second
relation before the empty stage.

This audit accepts the arbitrary-characteristic extension of that
lane, including the inseparable-root replacement and the field-model
failure shield. It does not infer a balanced normal bundle for the
literal C0 in an exceptional characteristic, cover defective or
nonreduced roots, or remove the full generic initial-ideal hypothesis.
No universal STCI or unrestricted C0 conclusion is drawn.

No commit, memory write, accepted verifier replay, or CAS computation
was performed.
