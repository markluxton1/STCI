# Filtration calculations and exact computational sources

[Formal normal Framework](index.md) · [Original section addresses](normal_filtration_boundaries.md)

## Retired exact computational sources: filtration and principal direction

The following preserve the mathematical statements of four historical checkers, **not** claims of actual mates or unconditional STCI exclusions.

### BF e=1, d2=1 annihilator

For `xi=c1 z^-1+c2 z^-2+c3 z^-3` in `H1(O(-4))`, a linear `delta=d0+d1 z` annihilates `xi` after twisting to `H1(O(-3))` exactly when
```
[c1 c2; c2 c3] [d0;d1]=0,  c1*c3-c2^2=0,
c1=-b1(2a0*b1+12a1^2+16a1*b0+9b0^2),
c2=-(2a1+b0)(8a0*b1+12a1^2+4a1*b0+3b0^2),
c3=-2a0(2a0*b1+36a1^2+16a1*b0+3b0^2).
```
For `Delta=a0*b1-a1*b0`, `det=-3Delta^2 Q`. A reduced cover polynomial is `Qred=16x^2+(72+64r+24r^2)x+36+72r+52r^2+16r^3+3r^4`; its discriminant is `64(r+2)^2(6r^2+8r+24)`, with nonsquare last factor over `QQ(r)`. Sample tuples `(a0,a1,b0,b1)` and their annihilators are `(-8,-3,2,-3):(4,-1)`, `(-8,-2,-4,-4):(2,-1)`, `(-8,-1,-2,-4):(2,-1)`. These test the obstruction-side condition, not ambient equations.

### Principal e=1, d2=1 weighted curve

With weights `wt(p,r,b)=(2,1,1)`, the exact weighted equation is
```
H=8p^3-(64r^2+128rb+16b^2)p^2
 +(96r^4+512r^3b+592r^2b^2+128rb^3+6b^4)p
 -(576r^6+960r^5b+880r^4b^2+544r^3b^3
   +220r^2b^4+60rb^5+9b^6).
```
Its discriminant in `p` is `-1728(2r-b)^2(2r+b)^4 S6` with `S6=93b^6+676b^5r+1996b^4r^2+3552b^3r^3+7984br^4+10816r^5b+5952r^6`. On `b=1` the affine singular ideal is `(8p+24r^3+12r^2-38r-3,(2r-1)(2r+1)^3)`, yielding a node at `(2,1/2)` and a tacnode at `(-2,-1/2)`. The historical exact computation finds an absolutely irreducible genus-one normalization with `Y_E^2=X_E^3+96X_E-448`, `j=2048/3`. Its birational chart uses `x=r+1/2, W=(p+2-4x)/x^2, Y=(A(W)x-C(W))/W` with `A(W)=-W^3+8W^2-12W+72`, `C(W)=2(W^2-6W+36)`; inverse `x=(C+WY)/A,r=x-1/2,p=-2+4x+Wx^2`. Exceptional denominators require separate charts.

In the principal frame `A=1+rz,B=1+pz`, the cocycle is `-(2A+zB)(12A^2+3z^2B^2+4z^2(A'B-AB'))/(8z^5)`. Its negative Laurent coefficients satisfy `H=64(c1*c3-c2^2)` on `b=1`. For `delta=-8c2+8c1z` and the corresponding correction `Gamma`, the computed resultant is `Res_z(delta,Gamma)=p^4(2p+12r^2+16r+9)^4/8`. This establishes a flatness test on the stated open, not the remaining ambient quartic/cubic incidence.

### First-normal octic discriminant candidate

The historical principal-weighted construction used 18 independent quartic source forms, a 23-by-18 contact matrix and three polynomial kernel columns of weighted degrees `9,9,10`. For the first generator, `hhat=(p-rb)*coefficient_m(F)` in the actual balanced frame is a binary octic. The candidate equation is the *fixed* 14-by-14 Sylvester determinant `Res(partial_s hhat,partial_t hhat)` for two degree-seven binary gradients, retaining infinity roots. Its weighted degree is 210. A nonzero modular check on `H=0` at `(p,r,b)=(4,2,1)` modulo 101 shows it is not identically zero on the principal curve. The stated double-cover Bézout argument bounds distinct candidate points by 630; this is only a **necessary** candidate set, not mate existence or exclusion.

### CI(5,8) multiplicity-ten necessary filtration degrees

For `l=-7,-6,-5`, put `T=-38-9l` and defect sequence `(0,0,a,b,c,T-c,T-b,T-a,T,T)`. Nonnegativity, symmetry and superadditivity reduce, in the enumerated range, to
`0<=a<=b<=c; 2a<=c; 2c<=T; a+b+c<=T; 3b<=T`.
The Euler check is `10+45l+sum(defects)=-180`. After the separate P-010 primitive-triple exclusion for `l=-7,a=0`, the respective counts are `198,97,13` (total 308). This is a numerical census, not an embedded-structure classification.

These four historical scripts supplied exact polynomial checks; their distinct formulas, hypotheses, limitations and algorithms are retained here without preserving generated artifacts.


## Related proof developments

- [Primitive e=2 quartic incidence and obstructions](../../arguments/normal-geometry/e2_primitive_quartic_incidence.md)
- [Ideal filtrations and the filtered quartic exclusion](../../arguments/normal-geometry/ideal_filtrations_quartic_exclusion.md)
- [Principal multiplicity-six candidate loci](../../arguments/normal-geometry/mf6_principal_candidate_loci.md)
- [Normal boundary strata, weighted initials, and lifting](../../arguments/normal-geometry/normal_boundary_weighted_initials.md)
- [Entirely thick equality cases, socle, and filtrations](../../arguments/normal-geometry/thick_equality_socle.md)
- [Normal filtrations and actual equation modules](../../arguments/normal-geometry/actual_equation_filtration.md)
- [Multiplicity-six models and nonnormal structures](../../arguments/normal-geometry/mf6_and_nonnormal_structures.md)
