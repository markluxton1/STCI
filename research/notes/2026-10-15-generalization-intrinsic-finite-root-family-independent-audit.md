# Independent audit: intrinsic finite root families and nonsplit ruled numerics

Date: 2026-10-15. Reviewed: 2026-10-16.
Reviewer: `relative_scope_audit`.

**Verdict: PASS for the stated relative finite-family generalization,
bounded Hilbert-family construction, splitting-free intersection identities,
and conditional finite empty-stage consequence.** The completed
[owner note](2026-10-15-generalization-intrinsic-finite-root-family.md)
was read in full. The accepted embedded-Cartier lifting functor, its
noetherian stabilization argument, and the accepted intrinsic nef
formal-branch and plane-multiplicity theorems are premises. This audit
checks their new relative hypotheses and numerical inputs; it does not
replay those accepted proofs or any accepted computation. No CAS or
accepted verifier was run.

## 1. Relative negativity really yields a vector bundle over a nonreduced base

Write `q:mathcal Z -> S` for the proper smooth family with geometrically
connected one-dimensional fibers, and put

    mathcal L_m=N_(mathcal Z/(E x S)) tensor O_E(-mE)|mathcal Z.

The actual relative normal bundle in this definition is necessary: it
retains any universal coefficient line from the parameter space. Its
restriction to a geometric fiber has degree `A-m*nu`. Under
`nu>max(A,0)`, this is negative for every `m>=1`. A smooth geometrically
connected curve is geometrically integral, so negative degree gives
`H0=0`. Riemann--Roch then gives

    h1(Z_s,L_(m,s))=g-1-A+m*nu.

This numerical argument deliberately uses smooth, geometrically connected
fibers. Total negative degree would not imply the same vanishing on an
arbitrary reducible or nonreduced root.

The passage to families is valid with all parameter nilpotents retained.
The morphism `q` is flat, proper, and of finite presentation, and
`mathcal L_m` is invertible and flat over `S`. The owner's cited
[Stacks Project, Lemma 36.30.1, tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
applies with the perfect object `mathcal L_m` and the flat sheaf
`O_mathcal Z`; its conclusion is perfect derived pushforward compatible
with arbitrary base change. Equivalently, one can apply the relative
perfect version,
[Stacks Project, Lemma 36.35.10, tag 0DJT](https://stacks.math.columbia.edu/tag/0DJT).

Locally represent this perfect complex in degrees zero and one. Its
differential is injective after every geometric residue-field pullback.
At each point, a maximal minor of this differential is a unit on some
neighborhood; elementary elimination makes it a split inclusion there.
The cokernel is consequently locally free even over a nonreduced local
ring. Thus, canonically in the derived category,

    Rq_*mathcal L_m=V_m[-1],
    rank V_m=g-1-A+m*nu.

After every `T -> S`, the pulled-back complex is `V_m|T[-1]`. This proves
the universal zero `H0` and the required base-change assertion for
`R1`, including nonflat maps from nonreduced parameter schemes. The
argument does not substitute a bare constant-dimension assertion for
perfect cohomology.

Properness here is a property of `q`; the parameter scheme need not be
proper. No global projectivity of the original intrinsic `X` is used
for this part of the statement.

## 2. The Cartier hypotheses supply the accepted lifting machinery

The root is an effective Cartier divisor and its quotient is flat over
`S`. It therefore remains Cartier after arbitrary base change, by
[Stacks Project, Lemma 31.19.1](https://stacks.math.columbia.edu/tag/056P).
Multiplication by its local equation is regular on every invertible
graded layer `J^i`. Lifting that equation to an exceptional thickening
preserves regularity by the finite nilpotent filtration. The resulting
quotient has layers `J^i|Z_T`, all flat over `T`, so its finite quotient
is flat over `T` as required.

These are the local regularity and quotient-flatness hypotheses used by
the accepted embedded-ideal torsor argument. Its difference sheaf is
precisely `mathcal L_m`, and the relative vanishing just proved applies
after every parameter base change. Therefore the accepted argument gives
the canonical obstruction section on the previous lifting locus, its
closed zero scheme, and uniqueness of the next embedded ideal. There is
no additional equation-unit parameter.

No global smoothness of `E` is silently required. The tower itself only
uses its Cartier embedding and the stated Cartier root. For a geometric
root where a smooth formal surface is needed later, smoothness of the
Cartier curve `Z subset E subset X` forces `E` to be smooth along `Z`:
locally `Z` is cut out in the regular three-dimensional ambient ring by
the two equations for `E` and for its Cartier root; smoothness of their
curve quotient makes their two cotangent classes independent. Thus the
resulting formal root surface has the required smooth transverse germ.

All stages lie over the same finite-type noetherian `S`. Hence the
accepted ideal-sheaf ascending-chain argument gives eventual
scheme-theoretic stabilization and the compatible formal Cartier ideal.
The note correctly retains the limitations: there is no numerical
cutoff, no inference from one adjacent equality, no algebraization
claim from the tower alone, and no assertion of flatness of an infinite
inverse-limit module.

## 3. The Hilbert construction is a bounded family with its scheme structure

For projective `E`, a chosen polarization and one Hilbert polynomial
give a projective finite-type Hilbert scheme with a flat universal
subscheme proper over the parameter space. The stated smooth,
geometrically connected, one-dimensional Cartier locus is open.

For the Cartier assertion, the ambient `E x Hilb` is flat and finitely
presented over `Hilb`, and the universal subscheme is flat and finitely
presented. The fiber criterion in
[Stacks Project, Lemma 31.19.9](https://stacks.math.columbia.edu/tag/056P)
identifies the relative Cartier property near every point where the
fiber has that property. Its complement is closed; properness of the
ambient projective family makes the image of that complement closed.
Restricting to the complementary parameter open gives Cartier fibers
everywhere and a relative effective Cartier universal divisor.

The locus where the entire proper flat fiber is smooth is open. After
restriction to nonempty smooth one-dimensional fibers, geometric
`h0(O_Z)` equals the number of connected components. The value-one
locus is open by upper semicontinuity, since this number is at least
one. These constructions restrict the existing Hilbert scheme; they
do not replace it by a reduced parameter scheme.

For a relative line bundle `M` on this proper smooth family,

    deg M_s=chi(M_s)-chi(O_(Z_s))

is locally constant. Applying this to the actual relative normal bundle
and the fixed exceptional line bundle gives the claimed local
constancy of `A` and `nu`; genus is also locally constant. A finite-type
scheme has finitely many connected components, so the desired numerical
loci are finite unions of open-and-closed strata. Each such stratum is
a legitimate finite-type `S`, even though it generally is not proper.

The distinction in the note is necessary and correct: on a general
surface, fixing only `g,A,nu` is not by itself a boundedness theorem,
and fixing a Hilbert polynomial does not automatically fix every
intersection invariant. The explicit numerical stratification supplies
the needed fixed-invariant families. An infinite union over Hilbert
polynomials supplies no single finite-type parameter scheme or uniform
stabilization integer.

## 4. The nonsplit blowup identities have consistent signs

Let `n=deg N_(C/P3)=4e+2gamma-2`. With the explicit line convention
`E=P_lines(N)` and `eta=c1 O_E(E)`, one has

    eta.f=-1,                     eta^2=-n.

This is equivalently the quotient convention `P_quot(N^*)`; the
duality matters. A numerical divisor of fiber degree `r` has the form

    Z == -r*eta+p^*D.

Intersecting with `eta` gives `deg D=rn-nu`; squaring gives

    A=Z^2=r^2*n-2r*nu.

Independently, the blowup canonical class and adjunction give

    K_E=(-4H+2E)|E,
    2g_Z-2=A-4er+2nu,
    A=2g_Z-2+4er-2nu.

Consequently

    2g_Z-2=n*r^2-4er-2(r-1)*nu.

The signs, the factor `r` in the quadratic formula, and the factor
`r-1` in the last identity are correct. At `r=1` the last formula
recovers `g_Z=gamma`. These calculations use only the actual ruled
bundle, not a splitting or product replacement.

The displayed equivalent uniqueness tests also follow exactly:

    nu>max(A,0)
    iff nu>0 and (2r+1)*nu>n*r^2
    iff nu>0 and 3nu>2g_Z-2+4er.

For the fixed ruled exceptional divisor, `(r,nu)` fixes the numerical
divisor class. It therefore fixes its degree in every chosen ample
polarization, and the adjunction identity fixes its genus. All smooth
connected roots of that fixed class lie in one fixed Hilbert scheme,
with polynomial `(Q.Z)t+1-g_Z`. The `r` and `nu` functions are degrees
of fixed relative line bundles and hence give an open-and-closed
stratum there.

A positive `r` excludes a vertical integral curve. Its proper
nonconstant map to `C` is finite, and a finite map between smooth
integral curves is flat. The optional family assertion in the note is
also valid: `mathcal Z -> C x S` is proper with finite geometric fibers,
thus finite; flatness follows from `S`-flatness and the fiberwise flatness
criterion. Its rank is the fixed degree `r`.

## 5. Numerical incompatibility implies an empty stable scheme and finite order

For a smooth formal root in the blowup, the accepted transverse-branch
construction has normal degree `nu` and hyperplane degree `h=er`.
Under `nu>4g_Z+5`, the imported nef formal-branch and plane-multiplicity
arguments apply with exactly the proposed inputs. They require an
integer `d>=1` such that

    d<=M(h,nu),
    M(h,nu)=max_(a integer,a>=1)(2ah-nu*a^2),
    (d-1)(d-2)>=er(r-1).

The maximum is finite and integral because `nu>0`; replacing it by the
real quadratic maximum would weaken the stated test. Since
`P(d)=(d-1)(d-2)` is nondecreasing on positive integers, with
`P(1)=P(2)=0`, absence of such an integer `d` is equivalent to

    M<1, or M>=1 and (M-1)(M-2)<er(r-1).

This handles the degree-one and degree-two boundaries, including
`r=1`. The note correctly presents this as an emptiness criterion
under the high-normal-degree and all-order uniqueness hypotheses.

If every geometric root in the family is numerically forbidden, the
stable closed scheme has no geometric point. A nonempty finite-type
scheme over an algebraically closed field has a geometric point, so
the stable scheme is empty, with all its possible nilpotents. Eventual
scheme-theoretic stabilization then gives one finite empty stage for
the chosen whole family. No explicit value for that stage has been
deduced from the numerical argument.

## 6. The actual-CI application keeps its bridge condition and strict indexing

This audit accepts the actual-CI bridge only when its full independent
hypotheses hold. If it supplies the strict local ideal
`(h,u^(s-r))`, its first principal relation survives through exceptional
stage `m` precisely in the asserted range `m<s-r`. Thus an empty stage
`K_N` forces `s-r<=N`. At equality only stage `N-1` is provided, so
there is no off-by-one strengthening.

This is a necessary bound on the generic normal-order gap in that
bridge lane. It is not a projective hypersurface-degree bound and
does not make formal compatibility sufficient for an actual complete
intersection. Singular and nonreduced roots remain outside this
intrinsic negative-degree proof. The unrestricted characteristic-zero
`C0` question and the universal STCI question remain open.

The review produced only this audit file. It changed no accepted
verifier, canonical record, index, commit, or memory.
