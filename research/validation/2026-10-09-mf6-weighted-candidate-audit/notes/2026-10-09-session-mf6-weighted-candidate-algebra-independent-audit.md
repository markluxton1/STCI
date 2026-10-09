# Independent algebra and Bezout audit of the principal MF6 candidate

Date: 2026-10-09. Auditor: `verification`. Status: **PROVED HERE / independently accepted necessary finite reduction**, on the explicitly retained principal contact open. The finite zero list, exact nonnormal locus, and all-mate exclusion at those zeros remain unresolved by this reduction.

## 1. Accepted statement and its scope

Use weighted parameters (p,r,b) of weights (2,1,1), and the integral weighted sextic H from the [owner proof](2026-10-09-session-mf6-principal-weighted-candidate.md). Put

    d=p-rb,
    P=2p+12r^2+16rb+9b^2,
    T=2p-4r^2-4rb-b^2,
    U=p P d (2r-b) T.

On H=0,U!=0, the accepted complete contact-rank audit gives a one-dimensional space of containing quartics for the principal e=1,d2=1 triple. The checked first polynomial generator G0 either spans that space or vanishes at a parameter. Its actual first-normal binary octic, multiplied by d, defines a fixed 14-by-14 binary-gradient Sylvester determinant Delta. This audit accepts:

* Delta is a completely specified homogeneous polynomial of weighted degree 210, by its preserved actual matrix.
* Delta is nonzero on the geometrically integral weighted curve H.
* Every nonnormal carrier with an STCI mate for C0 on this contact open lies in Delta=0, using the separately accepted geometric multiple-zero necessity.
* There are at most 630 distinct principal weighted parameter points in this necessary locus.

Zero chosen-generator fibers and zero first-normal vectors remain in the candidate locus. The result is not a description of the exact nonnormal locus, a factorization or enumeration of Delta's zeros, or an exclusion of every mate there. Contact-frame complement fibers retain their independent boundary proofs.

## 2. Exact source and input binding

Owner source SHA256 is `78ed372321bb99c81003892e30ca48a253b56702d0a00e05c5347e7a93e17370`. Its three exact inputs are:

| Input | SHA256 |
| --- | --- |
| `derive-mf6-principal-weighted-kernel-2026-10-08.json` | `0da6eff927a635a81179ce631468e9d4f3fc89a1c78af1c7a6a8cd6cc81fe85d` |
| `mf6-principal-weighted-kernel-2026-10-08.json` | `4889f20b60fa094cde47992342701ebdf29a98413fc216b20f971550331cd9db` |
| `session-mf6-e1-principal-contact-2026-10-08.json` | `bc32db62b6d87e15300168a47f50d6bf3cd952d0d19b60ad52fc5ae8cdfa9818` |

The last is the contact reconstruction already bound by the [complete principal audit](2026-10-08-session-principal-e1-d1-independent-completeness-audit.md). All three inputs give exactly the same eighteen literal ambient quartic forms. The owner verifier proves each vanishes on actual C0, proves their ambient coefficient rank eighteen, and checks the thirty-five quartic monomials restrict to all z-degrees 0 through 16. Thus the full degree-four ideal kernel has dimension 35-17=18, and these forms constitute the complete space; this is not a generator-coordinate substitute for ambient forms.

The full 23-by-18 contact matrix specializes at b=1 to the accepted eleven first-contact rows and twelve second-contact rows. Its row offsets are exactly 1 through 11, then 10 through 21; its column offsets are exactly 1,0,2,3,4,5,6,1,3,4,5,6,7,7,8,9,9,10. Homogeneous polynomial extension of a fixed offset is uniquely determined by its b=1 specialization: a monomial p^i r^j has the unique possible b-exponent w-2i-j. The owner checks these entry weights, each coordinate of the three degrees 9,9,10 generators, and all sixty-nine contact identities modulo H.

The root separately performed the fresh isolated complete owner replay, exit zero in 25.463 seconds. This audit inspected that source and performed the smaller independent coefficient/matrix reconstruction described below; it did not duplicate the three large contact-syzygy calculations. Completeness of the kernel module over the entire parameter scheme is not needed for the candidate argument. The accepted pointwise rank-one conclusion on U!=0 and one actual checked polynomial syzygy suffice.

## 3. Independent actual normal-coefficient reconstruction

The new self-contained bounded audit source is [audit_session_mf6_weighted_candidate_2026_10_09.py](../computations/audit_session_mf6_weighted_candidate_2026_10_09.py), SHA256 `a513320aeeed37260151d209cd2d232ac321edb892d647b22395a06cb45a1ac8`. It asserts the three input hashes above, the frozen owner source hash, and the binding of the owner saved result.

It independently differentiates the eighteen actual forms and contracts the first polynomial generator to produce F_U and F_V along C0, in the balanced frame

    U=-r m/d+(1+rz)y,
    V=-p m/d+(b+pz)y.

With A=1+rz and B=b+pz, it verifies the full polynomial identities modulo H

    A F_U+B F_V=0,
    hhat=-r F_U-p F_V,
    d F_U=B hhat, d F_V=-A hhat.

It reconstructs all nine coefficients h_j of hhat, checks their exact equality with the saved vector, and checks that no coefficient of degree greater than eight survives modulo H. The two latter frame identities also explain why hhat is the actual common first-normal binary octic: F_U=B h and F_V=-A h, with hhat=d h and d a unit on the declared open. The homogeneous linear direction A,B is basepoint free when d!=0. This controls both curve charts rather than only an affine derivative chosen in a frame with a zero.

Each h_j is homogeneous of parameter weight 11+j. The independently rebuilt fixed matrix agrees entry by entry with the saved matrix. Its first seven row weights are 18 through 24; its other seven row weights are 19 through 25; its column weights are 0 through 13. Every determinant term therefore has weight

    sum(18,...,24)+sum(19,...,25)-sum(0,...,13)=210.

No leading coefficient is cancelled. A control octic s times the product of seven distinct (t-j s) has a simple infinity root and nonzero gradient determinant. A control octic s^2 times the product of six distinct (t-j s) has a double infinity root and zero determinant. A zero nine-coefficient vector gives the zero fixed matrix and zero determinant. These exact controls confirm the intended behavior of the fixed degree-seven padding.

## 4. Characteristic-zero nonvanishing from the exact modular witness

The independently reconstructed sample at (p,r,b)=(4,2,1) modulo 101 has

    H=0, U=16!=0,
    (h_0,...,h_8)=(26,6,34,38,38,31,17,81,16),
    det(fixed Sylvester matrix)=22!=0.

The sample octic has degree eight and is coprime to its derivative. The modular determinant is exact finite-field arithmetic, and the sample is on H and in the declared contact open.

The audit proves H is a primitive integer polynomial, with leading coefficient 8 in p, and checks that every rational coefficient in the actual determinant matrix has denominator a power of two. Consequently Delta lies in Z[1/2][p,r,b]. If Delta vanished identically on the irreducible characteristic-zero H, H would divide Delta over Q. Clear only a power of two to make an integer polynomial; the primitive polynomial H then divides it in Z[p,r,b] by Gauss's lemma. Reducing that identity modulo 101 is legitimate. Since 101 does not divide the cleared power of two and the sample lies on H, it would force the sample determinant to be zero, contrary to 22. Thus Delta is nonzero on H in characteristic zero.

Geometric integrality of H is an accepted preceding theorem, not inferred from the single modular point. Its explicit certificate in `verify_mf6_e1_d1_principal_curve_2026_10_08.py` rules out a root of the cubic H(p,r,1) over the algebraic closure's rational function field: integrality makes a rational root polynomial in r, leading-degree comparison bounds its degree by two, and the coefficient equations for p=a r^2+c r+d have Groebner ideal (1). A cubic with no such root is absolutely irreducible. Homogenization introduces no b factor, since H contains 8p^3. The prior genus-one model is compatible with this stronger irreducibility argument but is not needed for Bezout.

## 5. Specialization and exceptional-generator qualification

At a point of U!=0 where G0 is nonzero, it lies in the complete contact kernel and hence is a nonzero scalar multiple of the unique actual quartic. That scalar and d do not change first-normal root multiplicities. The geometric necessity proved by the [separate audit](2026-10-09-session-mf6-weighted-candidate-geometric-audit.md) forces a multiple projective root, so Delta vanishes.

If G0 specializes to zero, its first-normal vector specializes to zero, and Delta vanishes automatically. If G0 remains nonzero but its entire first-normal vector is zero, the same conclusion holds. No exceptional parameter was removed by dividing by a coefficient of G0, by a leading coefficient h_8, or by a rational scalar chosen on a smaller chart. The basepoint-free and contact units are the explicit U factors; parameters outside that open are handled separately, not silently added to this candidate theorem.

## 6. Ordinary-plane cover and the 630 bound

The map

    pi:P2 -> P(2,1,1), [a:r:b] -> [a^2:r:b]

is the finite quotient by a -> -a; equivalently its invariant graded ring is k[a^2,r,b], with generator degrees 2,1,1. Pullback gives ordinary homogeneous equations of degrees six and 210. Even if the lifted sextic splits, each of its irreducible curve components maps onto the integral H: finiteness prevents a curve from being contracted, and the only dimension-one closed image in H is H itself. Since Delta is nonzero on H, none of these components is contained in the pulled-back Delta. The two plane curves therefore have no common component.

Bezout bounds their scheme intersection length by 6*210=1260. A principal point has p!=0. On H it cannot have r=b=0 because H would then be 8p^3. It consequently has two distinct plane lifts [a:r:b] and [-a:r:b]: scaling would have to fix a nonzero r or b and hence be one, while a!=0 and characteristic zero forbid identifying the signs. Thus every distinct principal candidate consumes at least two distinct intersection points, proving at most 1260/2=630 candidates. Intersection multiplicities can only strengthen this upper bound; no reducedness of the intersection or irreducibility of its lift is assumed.

The bound concerns distinct weighted parameter points in the necessary locus, not 630 constructed quartics or 630 proven nonnormal fibers. Normal carriers, singularities away from C0, and generator base fibers may all occur among zeros; the exact zero list remains uncomputed here.

## 7. Durable execution record

The bounded independent source completed in isolation with exit zero, wall time 7.909 seconds. Its log and result hash is `061217ff3b5ecc72aeec7bd5aa0791a3b7299ac43a8865f35f2f1529b1743ce2`. The original sources and all four input/result artifacts were unchanged. Full snapshots, source hashes, accepted-input hashes, exact sample coefficients, matrix agreement, and the infinity controls are preserved under `research/validation/2026-10-09-mf6-weighted-candidate-audit/`.

This is one new bounded countercheck execution in addition to the central owner replay. It does not change the status of the universal STCI question and does not edit canonical frontier files.
