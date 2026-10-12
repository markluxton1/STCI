# Degree factors, cubic scope, and conditional MF6 closure

Date: 2026-10-11. Auditor: `oct11_quartic_assembly_audit/degree_factor_audit`.
Status: **PROVED elementary factor reduction; KNOWN cubic exclusion;
conditional consequences of the full integral-quartic assembly**.
No canonical frontier file is edited by this note. The complete quartic
assembly remains a separate proof obligation and is not certified here.

Throughout, k is algebraically closed of characteristic zero and

    C0 = [s^4:s^3t:st^3:t^4] subset P3_k.

The statements also hold after a projective change of these coordinates.
No assertion about every smooth rational quartic embedding is inferred
from the proposed fixed-C0 quartic theorem.

## 1. Every irreducible factor is itself a carrier with a mate

Suppose nonzero homogeneous forms F,G of positive degree satisfy

    V_P3(F,G) = C0

as sets. Factor them in k[x0,x1,x2,x3] into irreducible homogeneous
factors, with arbitrary positive multiplicities.

First, F and G have no common irreducible factor: any common factor
would put its entire projective surface in their intersection, contrary
to that intersection being the curve C0.

Let f be any irreducible factor of F and g any irreducible factor of G.
They are coprime. Their intersection is nonempty and pure of dimension
one in P3. One algebraic justification is that f,g form a regular
sequence in the four-variable polynomial ring. The quotient is
Cohen--Macaulay of dimension two, so its minimal homogeneous primes have
height two; none is the height-four irrelevant ideal. Equivalently,
the projective dimension theorem and the absence of a common surface
component give a projective curve intersection.

The containment

    V_P3(f,g) subset V_P3(F,G) = C0

now forces equality. A nonempty pure one-dimensional closed subset of
the integral curve C0 must be C0 itself. In particular each factor f
and each factor g vanishes on C0, and **every pair of factors, one from
each form, is itself an STCI presentation of C0**. The same conclusion
holds for f with the entire other form G, and for g with F.

This is stronger than the elementary prime-ideal observation that at
least one factor of F must vanish on C0. That observation alone does
not establish the conclusion for all factors; the projective
intersection argument does. Repeated factors cause no exception, since
they do not change any of these underlying zero sets.

## 2. The precise cubic theorem and the degrees below three

The [literature ledger](../LITERATURE_LEDGER.md), section
Craighero--Gattazzo 1989, agrees with a fresh inspection of the actual
[Numdam PDF](https://www.numdam.org/item/RSMUP_1989__81__171_0.pdf).
The abstract and introduction on printed pp.171--172 state the
exclusion for a smooth rational quartic, a cubic surface, and a mate
of arbitrary degree over an algebraically closed characteristic-zero
field. The notations on pp.172--173 explicitly define a cubic surface
to be reduced and irreducible. Thus the theorem directly applies to
every irreducible cubic factor supplied by section 1.

No descent from a complex-only formulation is needed for that primary
statement: its stated base field already has the required scope. A
reducible or nonreduced homogeneous cubic form is nonetheless excluded
as a possible defining form. Section 1 produces either an integral
cubic factor to which the theorem applies, or a factor of degree one
or two, to which the following elementary exclusions apply.

The curve C0 is not contained in a plane, since its four coordinate
binary quartics are linearly independent. Its unique quadric is

    q = x0*x3-x1*x2.

Indeed, restriction of the ten quadratic monomials to P1 gives nine
distinct powers of s,t, and the only repeated weight gives precisely
q. This quadric is smooth. Under its Segre identification with
P1 x P1, C0 has class (1,3), up to exchanging the factors.

If a homogeneous mate of degree b restricted to q cut out only C0,
its effective Cartier divisor would have class (b,b) and support C0.
It would therefore be m*C0 for some positive integer m, requiring

    (b,b) = m*(1,3),

which is impossible. A mate identically zero on q would instead
contain the whole quadric and also fails the required intersection.
Thus no integral carrier of degree one, two, or three can occur.

For completeness, a separate complex-only carrier exclusion could
be transported to this literal C0 by finite-coefficient descent.
Choose a finitely generated subfield K of k containing all coefficients
of a hypothetical pair and the finitely many membership witnesses
for its radical equality with the rational-coefficient ideal of C0.
Embed K into C. The witnesses persist under scalar extension, so the
same pair would be an STCI over C. Smoothness and the displayed
parametrization of C0 persist as well. This is a valid backup argument,
not an additional hypothesis imposed on the 1989 theorem.

## 3. Consequence if the full integral-quartic theorem is accepted

Assume the separately audited assembly proves:

> Every integral quartic surface containing fixed C0 admits no
> homogeneous mate cutting it set-theoretically to C0, in every
> positive mate degree.

Then every irreducible factor of both forms in an arbitrary STCI
presentation has degree at least five. In particular

    deg F >= 5 and deg G >= 5.

This applies to reducible, nonreduced, and entirely thick
presentations. It does not assert that either form is generically
regular along the curve. It also does not supply a theorem forcing
some defining form to have degree at most four.

Therefore a completed all-quartic assembly would be a strict
minimum-carrier-degree reduction, rather than a proof that C0 is not
an STCI in arbitrary degree.

## 4. Which actual MF6 mate branches that would close

The exact P-042 calculation in
[the research record](../RESEARCH_RECORD.md) gives

    5*deg L + deg D2 + deg D3 = -26,
    e = deg L + 7 in {0,1}.

After the already excluded primitive-triple type e=0,(d2,d3)=(0,9),
the seven necessary numerical types of an actual (4,6) presentation
are

| e | (d2,d3) |
|---:|---|
| 0 | (1,8), (2,7), (3,6), (4,5) |
| 1 | (0,4), (1,3), (2,2) |

The proposed full quartic theorem excludes **every one** of these
actual mate presentations at once. It includes the historically
retained regular-ratio e=0,(3,6) member, the principal e=1,(1,3)
carrier locus, and e=1,(2,2). The fifteen coarse nonregular pole
strata surviving the horizontal-degree bound likewise cannot support
an actual (4,6) pair. The BF types and pole strata encode different
necessary data; closure does not require an unproved bijection between
their lists.

The conclusion also covers any reducible quartic defining form by
section 1. It is not limited to generic-rank members, principal
charts, or to the stronger ancestor exclusions already proved in
particular defect strata.

More generally every actual (4,b) mate presentation is excluded,
including the e=2 larger-b early-defect profiles retained in section A
of the audited state. Their abstract local CI countermodels remain
valid models of the numerical constraints; a carrier theorem excludes
their realization by an actual quartic STCI pair rather than proving
those local models impossible. Early-defect problems for carriers of
degree at least five and ancestor incidence are separate.

## 5. What does not follow for common quartic ancestors

The finite local-cohomology problem asks for an ancestor alpha and
actual quartic multipliers satisfying

    F*alpha=u,   G*alpha=v.

Those equations do **not** assert V_P3(F,G)=C0. In the audited
finite-flat quadruple interpretation, F and G have nonzero socle
images; they vanish on its canonical triple, rather than on the
whole quadruple. In particular these equalities do not turn either
quartic into an STCI carrier with a mate supported only on C0.

The [retracted bridge](2026-10-07-session-localcoh-mf6-bridge.md)
records exactly why replacing the nonzero socle images by zero is
invalid. Its corrected simultaneous-target proof excludes particular
ancestor strata by their own target equations. The present carrier
factor reduction supplies no replacement for such a proof.

Consequently the common-quartic-ancestor incidence, the 22 retained
second-family parameter roots with their complete lower lift lines,
and surviving positive-D2 ancestor strata are not declared closed
merely by an all-quartic carrier theorem. A further bridge would have
to establish the missing support or a direct target obstruction.
The totally ramified split-sextic carrier boundary and higher minimum
carrier degrees likewise lie outside a quartic-carrier theorem.

The split boundary is genuinely a sextic-carrier problem. In the
[full ramified reduction](2026-10-06-split22-finite-reduction.md), the
surviving actual forms are

    F_tau = -B^2 + tau*q*K,  tau!=0,

with deg B=3, deg q=2 and deg K=4, hence deg F_tau=6. Its hypothesis
is the existence of a mate of any degree, retaining the integral
carrier, reduced/content-free split exceptional divisor, and no
vertical component assumptions of P-020. It is not the assumption
that this sextic has a quartic mate. The corresponding
[split-sextic note](2026-10-05-split-sextic.md) records the necessary
degree and branch-order scale k*(11,1,8), with k>0; in particular the
mate degree is 8k in this stratum. Thus an all-quartic theorem does
not close this surviving one-parameter family, its normalization or
conductor obligations, or arbitrary sextic carriers outside those
split hypotheses.

## 6. No circular use of the new assembly in the normal-carrier input

The prior normal-quartic theorem uses excluded compressed mate
degrees through five. Its
[nonreduced independent audit](2026-10-07-session-normal-nonreduced-independent-audit.md),
section 1, lists that dependency explicitly. The degree-five exclusion
is the already independently established P-040 no-(4,5) theorem in
the research record, proved from P-025's multiplicity-five structure
exclusion. It predates the present all-quartic assembly and does not
depend on it. Degrees one through three use the elementary and cubic
inputs above; degree four uses the separate classical CG1986
no-(4,4) theorem. Consequently this aspect of assembling the normal
carrier theorem into an all-quartic theorem introduces no circular
dependency. This observation does not re-audit every premise of the
prior normal-carrier classification or enumerations.

## 7. Audit boundary

This note certifies the factor argument, the elementary degree-one
and degree-two exclusions, and the exact scope of the inspected
1989 primary statement. Its all-quartic and MF6 closure consequences
are explicitly conditional on the separate full quartic assembly.
It gives neither an unrestricted negative theorem nor a novelty
certificate for the quartic assembly.
