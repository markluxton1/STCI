# Independent review of the canonical conductor contact budget

Date: 2026-10-14. Reviewer: `projection_global_continue`. Scope: the new proofs in
[the conductor--Jacobian bridge](2026-10-14-generalization-projection-conductor-jacobian-bridge.md)
and [the conductor contact budget](2026-10-14-generalization-projection-conductor-contact-budget.md).
Status: **PASS under the stated Gorenstein, smooth Cartier-lift, full-support,
and generic-regularity hypotheses**. The accepted Cartier-lift classification,
normal splitting, projective contact criterion, and fiber-degree bound are
premises. Their computations were not rerun.

## 1. Actual conductor and the local first-symbol identity

For a finite birational extension `A subset B` with common fraction field,
every `A`-linear map `B->A` is multiplication by a fraction. Consequently
`Hom_A(B,A)` is the actual conductor `{q:q B subset A}`, not merely its
reflexive hull or its divisorial support. Since `A` is Gorenstein and `B`
is Cohen--Macaulay, finite canonical duality gives

    omega_B = Hom_A(B,A) tensor_A omega_A.

On a Gorenstein normalization the two canonical modules are invertible. The
conductor is therefore an invertible ideal on the normalization. In the
projective hypersurface setting this proves

    conductor O_S=O_S(-B),  B~(a-4)H-K_S.

The new local bridge was independently reconstructed in completed regular
coordinates. Take source coordinates `(t,u)`, with `c=(u=0)`, and ambient
coordinates `(x,y,z)` with `C=(y=z=0)` and `nu*x=t`. Write `nu=(t,Y,Z)`.
If `h` generates the actual conductor and `eta=dx wedge dy/F_z` generates
the hypersurface dualizing module, then `h nu*eta` is a generator of
`omega_S`. Hence there is one common unit `epsilon` satisfying

    F_z composed with nu=epsilon h Y_u,
    F_y composed with nu=-epsilon h Z_u.

At least one of these rational residue expressions is available generically:
the map is birational and is an isomorphism at the generic point of the
hypersurface. The equalities extend in the regular local ring. Restriction
to `u=0` gives the exact DVR-ideal equality

    (F_y|C,F_z|C)=(h|c)(Y_u|c,Z_u|c).

Taking orders proves the entire divisor identity

    Z(F_1)=B|c+A.

This argument uses the actual invertible conductor before restricting to
`c`; it avoids the possible codimension-two error in restricting only a
Weil-divisor or reflexive-hull identity. It also keeps isolated zeros of
the transverse differential. Smoothness along `c` follows from the accepted
smooth Cartier-curve lemma. The quadric cone is Gorenstein and its smooth
Cartier conic avoids the vertex, so that model satisfies the hypotheses.

## 2. Integer conductor budget

Generic regularity along `C` ensures `c` is not a component of the effective
conductor divisor. With `B=sum m_i D_i`, ampleness and Cartierness of `c`
give positive integers `c.D_i`. Adjunction then gives the exact equality

    sum_i m_i(c.D_i)=B.c=d(a-4)+c^2-(2g-2)=N.

This bounds the number of prime conductor components, all positive
conductor multiplicities, and the total weighted branch contact with `c`.
The assertion includes the singular branches of each `D_i`: pulling the
Cartier section defining `c` to the normalization of `D_i` has divisor
whose total degree is exactly `c.D_i`.

For the smooth-quadric and quadric-cone models, `B=10c` and `N=20`; for
the plane model, `B=51h` and `N=51`. These are canonical intersection
computations, independent of a putative mate degree.

## 3. Ordered pair curves and the factor of two

Let `Delta` be a generic image conductor curve, `K=k(Delta)`, and
`E=product E_i` its reduced normalization residue algebra. For fixed first
branch `E_i`, the algebra `E_i tensor_K E` is finite etale over `E_i` in
characteristic zero, of rank `d_Delta=sum_j [E_j:K]`. Its diagonal factor
has rank one, including when `E_i/K` has nontrivial conjugates. The sum of
the first-projection degrees of all remaining factors is therefore exactly
`d_Delta-1`, not the number of field factors and not twice that number.

Using the accepted `d_Delta<=a` bound, and pulling back the Cartier contact
divisor to each normalized pair curve, gives

    sum_T deg(p_1*c)
      =sum_i(d_(image D_i)-1)(c.D_i)
      <=(a-1)sum_i c.D_i
      <=(a-1)N.

This counts integral components of the ordered off-diagonal fiber product.
An exchange-invariant integral component is counted once; exchange may act
nontrivially on its function field. Thus the displayed formula has neither
a missing conjugate-pair factor nor an unjustified factor of two. Every
summand is a positive integer, since the projected curve meets the ample
`c`. The bounds 140 and 765 on pair-contact data follow.

## 4. Mathematical consequence and scope

The result supplies a uniform finite amount of integer contact data for
all mate degrees on any one of the three fixed normalized models. It also
shows that the full conductor contact is recovered from the carrier first
symbol *and* the actual normalization differential, under the explicit
duality hypotheses. Neither first symbol alone nor a reduced common-root
support substitutes for this identity.

The theorem leaves the scalar phases unbounded and retains the entire
nilpotent conductor defect. Finite weighted graph types do not give finitely
many projection coefficients or a finite list of phase values. The
non-Gorenstein, non-Cartier, multiple-inverse-branch, and generically thick
boundaries remain outside its scope. This is an accepted structural
reduction, not an exclusion of all nonnormal carriers or a solution of the
universal STCI question.
