# Socle budgets, source modules, and arithmetic comparisons

[Formal normal Framework](index.md) · [Original section addresses](normal_filtration_boundaries.md)

## Ordinary ideal powers and filtered equation modules are different source questions

In degrees \(d\ge3m\), the fixed quartic's ordinary ideal-power theorem identifies the complete ambient source \(H^0(I_C^m(d))\) with \((I_C^m)_d\), and gives \(H^1(I_C^m(d))=0\). This is a statement about ambient sections vanishing to a prescribed order. The comparison defect \(\Delta_n\) instead compares minimal generators of the **full initial ideal of an actual pair** with the filtered equation module \(J/I_CJ\). Neither assertion implies the other.

To pass from an ambient source to a specific normal symbol, the map to \(H^0(\operatorname{Sym}^m N_C^\vee(d))\) must be computed. To pass from compatible symbols to an actual supported complete intersection, one must also impose a common global lift, properness and degree exhaustion. See [the ideal-power proof](../../arguments/normal-geometry/formal-normal-intersection.md#12-ordinary-ideal-powers-on-a-smooth-quadric-complete-proof) and [the global-source treatment](../../arguments/normal-geometry/normal_boundary_weighted_initials.md#normal-boundary-strata-weighted-initials-and-lifting).


## Characteristic-two comparison and arithmetic scope

The fixed quartic pair in R-0021 is flat over the integers. Its characteristic-zero fiber contains four reduced quartics, whereas its characteristic-two fiber has sole reduced support C and generic transverse length four. The conormal extension changes splitting type (R-0020). In the special fiber, R-0031 identifies the cancellation-generated fourth initial equation with the filtered equation-module kernel O(-24); its comparison defect is zero.

R-0012 rules out a constrained flat embedded lift of this prescribed special scheme over Z_(2) or Z_2 with generic reduced support C. It does not contradict the integral family with four generic components or address arbitrary ramified bases. These are separate tests of normal structure, full initial equations, and global support.


## The shared duality mechanism and its limit

The boundary-repair catalecticant and the local-cohomology polynomial left dual are two concrete uses of duality on an actual source map. In the first, Serre duality changes a pole-repair problem into annihilation of a multiplication subspace; in the second, a row annihilating the complete tensor image separates a target class from the image. Both mechanisms work over any coefficient field where the displayed objects and maps are defined. They do not identify their obstruction spaces, and no theorem transfers a repair divisor from one problem to the other. The same global homogeneous source must remain fixed when several conditions are stacked. A separate divisor for each component or independently chosen normal jets would change the existence question.

The [complete endpoint owner](../../arguments/local-cohomology/degree_fifteen_obstruction.md#the-degree-fifteen-boundary-and-exact-duals) now assembles both rational target-u family exclusions with parameter coverage, all affine corrections, exact factor closure and actual tensor reconstruction. Its rational certificate scope is characteristic zero. The [positive-characteristic construction](../../arguments/arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) remains the global control: these duality mechanisms constrain specified sources; they do not exclude STCI in every characteristic.

A precise proposed cross-topic bridge is to compare the nonsaturated-first-relation/resultant defect of R0016 with the saturated quasiprimitive residual zero-cycle of R0019 **using the actual global equations and a proper auxiliary intersection**. The two constructions have different hypotheses and targets. A general divisor inequality has not been established. Any comparison must identify correction terms when ordinary normal flatness, generic curvilinearity, saturation or properness fails, rather than equate the two numerical defects or infer an extra curve from a vertical exceptional cycle.


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

