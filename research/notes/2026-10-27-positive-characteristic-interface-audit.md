# Independent audit: the mu_q family and residual attachments

Date: 2026-10-27. Reviewer: formal-neighborhood/residual-visibility agent, independently reconstructing the positive-characteristic lane. Source: [construction interface](2026-10-27-positive-characteristic-construction-interface.md). **Outcome: the proposed family, cycle, and attachment-divisor assertions pass this review in their stated scopes.** This is review evidence for a provisional note, not canonical promotion or an unrestricted STCI conclusion.

## Scope and inherited authority

The fixed curve is C0=[s^4:s^3t:st^3:t^4] in P3 over an algebraically closed field. The proposed integral family has S=x0*x3^3-x2^4 and Gq=x1^q-x0^a*x2^b*x3^c, where q=3b+4c>0 and a=2b+3c. The exact allowable mate degrees on S and their prime minima are inherited from the [October 5 fixed-carrier note](2026-10-05-positive-quartic-carrier-optimality.md) and its recorded audit. This review uses them as premises; the present note accurately distinguishes that reviewed historical evidence from a canonical result record. The q=4 degeneration R-0021 remains narrower than the general family calculation. The conormal splitting R-0020 is an accepted premise, not reverified here.

## 1. Flatness and properness reconstructed

Over Z[x0,x3], first quotient the polynomial variable x2 by the monic equation x2^4-x0*x3^3, and then quotient x1 by the monic equation x1^q-x0^a*x2^b*x3^c. Successive monic division gives the claimed free basis x2^j*x1^i for j<4,i<q over Z[x0,x3]. This proves Z-flatness; the homogeneous localization and degree-zero pieces used in Proj remain Z-flat. No reduced-fiber assumption was used.

In every field both equations are a regular sequence: the first is monic in x2, and the second is monic in x1 after its imposition. Thus the projective fibers are pure Cohen–Macaulay CI curves of degree 4q. The complete-intersection genus formula gives 1+(4q)(4+q-4)/2=1+2q^2. This formula applies to the full scheme, not its reduced support.

## 2. Torus and endpoint completeness reconstructed

In the chart x0=1 with x2,x3 nonzero, put u=x3/x2. The surface relation gives x2=u^3,x3=u^4. Since 3b+4c=q, putting w=x1/u gives w^q=1. In characteristic p, writing q=p^e*m with p not dividing m yields w^q-1=(w^m-1)^(p^e). Therefore the m torus components are smooth at their generic points, each with scheme multiplicity p^e, and their closures are the stated diagonal transforms C_zeta of C0.

There is no unexamined projective boundary curve. If x0=0, S forces x2=0 and Gq then forces x1=0, leaving only [0:0:0:1]. If x3=0, S forces x2=0 and Gq forces x1=0, leaving only [1:0:0:0]. If x0*x3 is nonzero, S forces x2 nonzero and Gq forces x1 nonzero, so the torus description applies. The cone vertex [0:1:0:0] fails Gq=0. These observations independently confirm endpoint completeness; alternatively the total weighted degree of the displayed components is already 4q, exhausting the CI degree.

It follows that the cycle is p^e sum_(zeta^m=1)[C_zeta], with m_C=p^e and deg R=4(q-p^e). The two-generator CI has no embedded associated components. In characteristic not dividing q it is generically reduced on every component, hence reduced by the Cohen–Macaulay S1 property. Its reduced support is C0 exactly for p-powers q in positive characteristic. The word "p-power" here concerns the admissible q in <3,4>; it does not remove the semigroup condition or assert global minimal degrees over other carriers.

## 3. Attachment divisor and linkage reconstructed

Assume char(k) does not divide q. Then m_C=1 and the reduced linked residual is the union of the other components. At p0, the ambient coordinates u=x1, Y=x2-u^3, Z=x3-u^4 form a regular coordinate system. The linear normal terms of S and Gq are respectively

    (-4u^9)Y + (3u^8)Z,
    (-b u^(q-3))Y + (-c u^(q-4))Z.

Terms with zero coefficient are omitted; this avoids spurious negative exponents at q=3. The determinant is (4c+3b)u^(q+5)=q*u^(q+5). On x3=1, the coordinates v=x2, X=x0-v^4, Y=x1-v^3 give S=X and first-normal determinant q*v^(3q-3). These endpoint charts cover C. Since q is invertible, both local determinant ideals have the asserted exact vanishing orders.

The colon step is valid even where both original surfaces are singular. In a regular local ambient ring A, let I=(Y,Z), J=(f,g) be two regular-sequence ideals with J subset I, and write (f,g)^t=M*(Y,Z)^t. Adjugation puts det(M) in J:I. Conversely the comparison of the two Koszul resolutions, followed by complete-intersection duality, identifies

    Ext_A^2(A/I,A)=Hom_(A/J)(A/I,A/J)

and sends its generator to det(M) modulo J. The right side is precisely (J:I)/J. Hence J:I=(J,det M). Restricting to C kills J and leaves the determinant ideal. This reconstructs the formula used in the source, rather than inferring an attachment scheme from a determinant without a linkage argument.

Therefore the exact Cartier divisor on C is (q+5)p0+(3q-3)pinfinity. Its total length 4q+2 agrees with det(N_C^*) tensor O_C(4+q), but the local calculation establishes the stronger endpoint concentration. The assertion remains valid in positive characteristics not dividing q, including characteristic two with q odd.

The q=7 gluing warning is also correct. On a component C_zeta at p0, the two generators of I_C restrict to (1-zeta^3)t^3 and (1-zeta^4)t^4. For a nonidentity seventh root, the former coefficient is nonzero, so each pairwise intersection has length three. Six pairwise lengths sum to eighteen, whereas the residual union has attachment length twelve. At infinity S is smooth and the individual order-three contacts add to eighteen. Thus the union attachment cannot be replaced by the sum of pairwise intersections.

## 4. Finite verifiers independently executed

The newly proposed dependency-free Python verifier and the newly proposed Macaulay2 linkage verifier were both run in this review. They reported:

- 47 exact two-chart determinant and lattice-index checks;
- the script's 11 finite inherited-minimum corroborations;
- global colon residual degrees 8,12,24 for q=3,4,7;
- exact union-ideal equalities and attachment divisors (8,6), (9,9), (12,18) for those examples.

The Python script tests sparse expansions modulo normal degree two; it does not compute full residual ideals. The separate M2 computation does compute those ideals in the three stated characteristic-zero examples. Universal flatness and cycle assertions rest on the preceding proofs, not finite enumeration. The inherited-minimum block is not used to elevate the historical theorem's status.

Commands:

```
python3 research/computations/verify_mu_q_residual_interface_2026_10_27.py
/opt/homebrew/bin/M2 --script research/computations/verify_mu_q_residual_linkage_2026_10_27.m2
```

SHA-256 values of the reviewed verifier sources:

```
80b65ae5c0aca2f17c3438d57097a9e834cf5c2628fec67858d8ee913d31e7fc  verify_mu_q_residual_interface_2026_10_27.py
ff04f55ba17f76969a6f9ef745a6e66929fb8694bfa067176a18bb9ae92ead06  verify_mu_q_residual_linkage_2026_10_27.m2
```

## 5. Interpretation and remaining limits

The finite-group-scheme interpretation is exact: the cross product of the two torus relation rows is q*(1,3,4), so the lattice index is q. Its prime-to-p part gives distinct reduced sheets and its p-primary part gives infinitesimal thickness. The same marked conormal bundle outside characteristic two coexists with positive-characteristic STCI pairs for every odd p, so the characteristic-two splitting jump cannot be a necessary mechanism for positive-characteristic existence.

This explains this fixed binomial construction's characteristic dependence and does not rule out non-binomial characteristic-zero constructions on other carriers. In the non-pure-p-power case, the generic completion at the marked C retains only its p-primary thickness; completions at endpoint attachments retain other residual germs. The source correctly avoids claiming that this alone reconstructs all global geometry of R. The [formal-visibility note](2026-10-27-formal-neighborhood-residual-visibility.md) adds the separate G3 distinction for full globally glued formal sections in prescribed twists.

No literature access gap was silently closed by this audit. The source's claim-by-claim literature descriptions retain their stated original-PDF and historical-evidence boundaries. The new family calculations can be used independently of the broad external classification statements.
