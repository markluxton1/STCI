# Marked deformations and residual absorption

Let \(C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\). A proper
intersection \(Y=V(F_a,G_b)\) containing \(C\) has cycle
\([Y]=m[C]+R\), where \(ab=4m+\deg R\). This chapter concerns actual
families in which \(m\) increases and residual degree moves onto the fixed
embedded curve. Such partial absorption occurs in characteristic zero.
The unrestricted question whether \(R\) can vanish remains open.

These are independently reviewed deductions. Consolidation review reconstructed the proofs, the
normal-carrier endpoint criterion, the explicit ribbon-quotient boundary,
the rational-curve extension, and the characteristic statements. Inputs are cited at their exact uses. No computation is needed for these
proofs.

## Geometric orientation: incidence, specialization, and the marked curve

The organizing object is the incidence space of complete intersections
together with an embedded multiple structure on the fixed curve C.
Residual absorption is specialization of cycles within a flat family:
the total intersection degree stays fixed, while multiplicity along C
increases and the residual cycle loses degree.

Three geometric questions must be distinguished. Can a lower multiple
structure move in a bounded neighborhood of C? Can an abstract family
be embedded while C stays marked? Can actual global hypersurfaces of
prescribed degrees contain that moving structure? These are different
deformation problems, with different obstructions. In particular, the
full primary component need not vary flatly during absorption; a
persistent lower thickening is often the appropriate marked witness.

The torus preserving C acts on these incidence spaces. Its fixed
Hilbert limits can organize possible boundaries, but they need not
remain complete intersections. Weight decompositions can refine
deformation calculations without replacing the global equation test.

### Fixed-degree multiplicity strata of actual pairs

Over an algebraically closed field, let \(U_{a,b}\) be the open set of
proper pairs in
\(\mathbf P H^0(I_C(a))\times\mathbf P H^0(I_C(b))\), with \(C=C_0\)
fixed. Write \(B=\lfloor ab/4\rfloor\). On the chart \(x_0=1\), put
\(x_1=u,\ x_2=u^3+X,\ x_3=u^4+Y\), and let
\[
 A=k(u)[X,Y]/(X,Y)^{B+1},\qquad D=\dim_{k(u)} A.
\]
Each generic transverse quotient on \(U_{a,b}\) has length
\(m_C\le B\) by the cycle degree identity. Its maximal ideal has
\(m_C\)-th power zero by the successive-factor length argument, so
\[
 m_C=D-\operatorname{rank}_{k(u)}\bigl(A^2\longrightarrow A,
            \ (h,j)\longmapsto hF+jG\bigr).
\]
Use all truncated monomial multiples of both equations as columns.
Entries are polynomials in \(u\) with coefficients in the actual scalar
equation parameters on affine coefficient charts. The coefficients in
\(u\) of the minors for rank at most \(D-r\) cut out the closed
condition \(m_C\ge r\) in each chart. Rescaling either equation preserves
the rank. For equal degrees, changing the basis of the pencil also
preserves it, so the loci descend via local bases to the proper open
set of the Grassmannian. Along a specialization in the proper locus,
\(m_C\) can increase and the residual degree can drop. When \(4\mid ab\),
sole support is the terminal stratum \(m_C=ab/4\) by degree exhaustion
and purity. The strata can be empty.

In characteristic zero, the first thickness increase for sextic pencils
has a smaller presentation. For \(V=H^0(I_C(6))\), the map
\[
 \Phi:\bigwedge^2 V\longrightarrow
 H^0(C,\det N_C^*\otimes O_C(12))=H^0(\mathbf P^1,O(34))
\]
takes the wedge of the two first-normal symbols. It is surjective by
[attachment-map dominance](residual_global_models.md#3-new-deduction-attachment-map-dominance-for-all-abge4):
the image of the surjective differential of the affine wedge map is
contained in \(\operatorname{im}\Phi\). The quotient has length one
exactly when the two first symbols span the generic conormal space,
by Nakayama. Thus the \(m_C\ge2\) locus in the proper open subset of
\(\operatorname{Gr}(2,V)\) is its intersection with
\(\mathbf P(\ker\Phi)\) in Plücker space. The 35 ambient linear equations
are independent. With \(\dim V=59\), every component of the projective
linear section has dimension at least \(114-35=79\).
The equations' independence gives no transversality on the Grassmannian.

For \(q=x_0x_3-x_1x_2\) and \(f=x_0^2x_2-x_1^3\), the pencil
\((qx_0^4,f^2)\) is proper. In the displayed chart its completed
transverse ideal is \((Y-uX,X^2)\), so it has exact length two and
residual degree 28. This gives a nonempty first-thickness stratum.
Imposing the full-jet rank threshold for \(m_C\ge3\) on its components
remains a separate incidence problem. The \(m_C=9\) endpoint still
requires a proper pencil.

The [source proof](https://github.com/markluxton1/STCI/blob/b271fc5bf20a6920b1540cabd57f095139d8d7a5/research/notes/2026-10-27-intersection-multiplicity-strata.md)
and [independent review](https://github.com/markluxton1/STCI/blob/b271fc5bf20a6920b1540cabd57f095139d8d7a5/research/notes/2026-10-27-intersections-integration-audit.md)
record the fixed-degree rank calculation, descent by scalar coefficient
equations, endpoint equivalence, and the sextic wedge calculation and
proper witness. The review also fixes the genus distinction between
full residual removal and the [once-link family](residual_liaison.md#21-the-once-linked-curve-is-flat-through-multiplicity-jumps).


## 1. Three different deformation problems

A proposal to absorb residual curves can involve three distinct objects:

| Object being moved | Local/global compatibility | What success does not establish |
|---|---|---|
| An embedded lower thickening \(T\) above fixed \(C\) | A marked Quot deformation; tangent \(\operatorname{Hom}(J/I^N,I/J)\) | Existence of containing equations in chosen degrees |
| A given abstract family with central embedding | Marked map lifting; obstruction sheaf \(i^*T_{\mathbf P^3}\otimes I_{C/T}\) | Generation by two ambient equations |
| Actual homogeneous forms through a moving thickening | Connecting classes in \(H^1(J(a))\oplus H^1(J(b))\) | Removal of residual support |

Here \(I=I_C\), \(J=I_T\). These tasks share a lifting mechanism: local
solutions differ by sections of a coherent sheaf, and their differences
must glue. Their obstruction groups belong to different deformation
functors; no identification between them is asserted. Sections 2–3 give
positive constructions, §4 computes the actual-equation interface, and
§5 extends abstract ribbon deformations while preserving this embedding.

### 1.1. The full primary component is not a flat witness at absorption

If a pure curve \(T\) has sole reduced support \(C\) and generic length
\(m\), then \(\deg T=m\deg C\). A flat projective family with fixed
Hilbert polynomial fixes this degree. Consequently a family of *full*
\(C\)-primary components cannot remain flat when \(m\) increases. One
can instead keep a flat **lower witness** \(T\subset Y_t\), which need
not be the full primary component at the special parameter.

An explicit control, over any field, marks \(L=(x,y)\subset\mathbf P^3\):
\[
Y_\lambda=V\bigl(x,y^m(y-\lambda z)\bigr),\qquad m\ge1.
\tag{1}
\]
After imposing \(x=0\), the relation is monic of degree \(m+1\) in \(y\).
The graded quotient is free over \(k[\lambda,z,w]\) on
\(1,y,\ldots,y^m\), proving flatness. At \(\lambda\ne0\) its components
are \(mL\) and the distinct line \(L_\lambda=(x,y-\lambda z)\);
these lines meet at \([0:0:0:1]\). At zero the entire scheme is
\((m+1)L\). The full primary ideals are therefore \((x,y^m)\) and
\((x,y^{m+1})\), respectively. Their degrees jump, although the fixed
lower witness \(mL\) remains contained in every fiber. This is a line
control, not a construction for \(C_0\).

Even a flat family of pure thickenings can change its generic algebra and
number of generators. Locally
\[
J_\lambda=(x^2-\lambda y,xy,y^2)\subset k[\lambda,t,x,y]
\tag{2}
\]
has quotient free on \(1,x,y\) over \(k[\lambda,t]\). For
\(\lambda\ne0\) its normal algebra is curvilinear of length three;
for \(\lambda=0\) it is \(k(t)[x,y]/(x,y)^2\), requiring three ideal
generators. Flatness alone does not preserve a rank-two equation module.

The full attachment invariant, its non-lci correction, and the distinction
between full and once-linked residuals belong to
[the full-primary attachment theorem](residual_capacity_and_constructions.md#full-primary-equation-module-and-exact-attachment-divisor).
In particular the non-lci example there has a **unit** torsion-free
determinant and nevertheless real attachment of length two. A deformation
must retain the full equation module; a determinant alone is insufficient.

## 2. Absorption as specialization in a linear system on a carrier

The basic geometric operation is a pencil of Cartier divisors on a
surface containing C. At a special parameter, its order along C
increases, so the residual divisor acquires a multiple of C.
The positivity hypotheses below make this a construction by actual
homogeneous hypersurfaces, rather than only a formal specialization.



The essential positive operation is interpolation between sections with
different orders along one fixed divisor. The quartic is only needed to
make its positivity threshold explicit.

### 2.1. General Cartier interpolation

Let \(S=V(F_a)\subset\mathbf P^3_k\) be a smooth integral surface over an
algebraically closed field of arbitrary characteristic. Let \(C\subset S\)
be any smooth connected curve such that \(I_C(\delta)\) is globally
generated, and let \(H=O_S(1)\). Fix \(1\le m<n\) and
\(b\ge\delta n+1\). There are actual homogeneous forms \(G_m,G_n\) of
degree \(b\) for which every finite pair
\[
Y_t=V(F_a,G_n+tG_m)
\tag{3}
\]
is proper, has exact generic \(C\)-multiplicity \(m\) for every \(t\ne0\),
and has multiplicity \(n\) at zero. The residual after removing the fixed
lower divisor \(mC\) forms a flat Cartier family whose special fiber is
\[
(n-m)C+D_n.
\tag{4}
\]
Here \(D_n\) is smooth integral and does not contain \(C\); for general
nonzero \(t\), the residual is also smooth integral. Thus
\((n-m)\deg C\) units of residual cycle degree are absorbed.

**Proof.** Since \(C\) is Cartier, the restriction of \(I_C(\delta)\)
surjects onto \(O_S(\delta H-C)\); call this globally generated bundle
\(M\). For \(r=m,n\),
\[
bH-rC=rM+(b-\delta r)H
\]
is very ample. Indeed a very ample bundle tensored with a generated
bundle is very ample: take the graph of the associated morphism together
with the closed immersion given by the first bundle, then the Segre
embedding. The very ample system defines a closed immersion, so smooth Bertini
and geometric irreducibility of general hyperplane sections apply in
every characteristic. In particular Bertini supplies sections \(\tau_r\) of these
bundles with smooth integral divisors \(D_r\) and not vanishing identically
on \(C\). Avoiding \(C\) as a component is a nonempty open condition.

With \(s_C\) the canonical section of \(O_S(C)\), put
\[
\sigma_r=s_C^r\tau_r,\qquad
\sigma_n+t\sigma_m=s_C^m(s_C^{n-m}\tau_n+t\tau_m).
\tag{5}
\]
Different exact orders along \(C\) make \(\sigma_m,\sigma_n\)
independent, so every finite section is nonzero. For \(t\ne0\) the
bracket restricts to \(t\tau_m|_C\ne0\); its exact order is \(m\).
The zero member has exact order \(n\). Both the total divisor family and
the bracket family have nonzerodivisor equations on every fiber of
\(S\times\mathbf A^1\), so the fiberwise Cartier criterion proves
flatness. At zero the bracket has the product ideal giving (4), not
merely the same cycle. Extend the residual pencil to \(\mathbf P^1\).
Its infinity member is \(D_m\), so openness of smoothness and geometric
integrality gives the asserted general finite members.

Finally the hypersurface sequence
\[
0\to O_{\mathbf P^3}(b-a)\xrightarrow{F_a}O_{\mathbf P^3}(b)
\to O_S(bH)\to0
\tag{6}
\]
and \(H^1(\mathbf P^3,O(b-a))=0\) lift the two sections to forms over
\(k\). Their pencil lifts simultaneously. Since no restriction vanishes
identically on integral \(S\), no pair has a common surface component.
This proves every assertion. The standard facts used are
[Bertini smoothness](https://stacks.math.columbia.edu/tag/0FD4),
[Bertini irreducibility](https://stacks.math.columbia.edu/tag/0G4C),
[projective-space cohomology](https://stacks.math.columbia.edu/tag/01XS),
and [relative Cartier divisors](https://stacks.math.columbia.edu/tag/062Y).

### 2.2. Application to the fixed quartic

The unique containing quadric \(Q\) is smooth and \(C\) has bidegree
\((1,3)\), up to swapping rulings. Thus
\[
0\to O_{\mathbf P^3}(1)\xrightarrow{q}I_C(3)
\to O_Q(2,0)\to0.
\tag{7}
\]
The last bundle and first bundle are globally generated, and
\(H^1(O_{\mathbf P^3}(1))=0\) lifts the sections generating the quotient.
Hence \(I_C(3)\) is globally generated. Proposition 2.1 applies with
\(\delta=3\), giving \(b\ge3n+1\) and absorbed degree \(4(n-m)\).
It uses no STCI exclusion or balanced normal-bundle hypothesis.

The same nef bundle \(3H-C\) bounds how far this carrier geometry can go.
On any integral degree-\(a\) surface smooth **along all of \(C\)**,
\(C^2=14-4a\). Thus for \(bH=mC+D\),
\[
0\le(3H-C)\cdot D=b(3a-4)-m(4a-2),
\quad
m\le\frac{b(3a-4)}{4a-2},\quad\deg D\ge ab/3.
\tag{8}
\]
The full proof, exact hypotheses, general-curve form and sharp example
are owned by [the smooth-along-C capacity theorem](normalization_residual_capacity.md#4-a-uniform-residual-floor-when-a-carrier-is-smooth-along-c).
This is a capacity limit for carriers smooth along \(C\), including
ones singular elsewhere; it is not an arbitrary-carrier bound. In
particular the positive construction does not approach a supported
endpoint merely by increasing \(b\).

### 2.3. Normal carriers: two levels of extension

Let \(S\subset\mathbf P^3\) instead be a specified normal integral
hypersurface over an algebraically closed field of arbitrary characteristic.
If \(hC\) is Cartier for \(h>0\), it is effective Cartier: nonnegative
codimension-one valuations make local Cartier equations regular on a
normal scheme. Choose \(\delta\) with \(\delta H-hC\) globally generated.
For \(1\le u<v\), \(b\ge\delta v+1\), the preceding proof applied to
\(hC\) gives multiplicities \(hu,hv\) and the Cartier special residual
\((hv-hu)C+D_{hv}\). General residual divisors avoid the finite singular
locus and are smooth integral by Bertini on its smooth complement.
There is no uniform \(\delta\) across carriers, nor a construction of
carriers with prescribed index in this statement.

Without any Cartier multiple, there is a weaker operation in **every
characteristic**. On a specified normal integral \(S\), the coherent
divisorial ideals \(\mathcal J_r=O_S(-rC)\subset O_S\) are globally
generated after sufficiently large common twists, for \(r=m,n\).
At \(\eta_C\) they are \((\pi^r)\) in a DVR. At least one generating
global section has exact valuation \(r\), since otherwise the generators
would lie in \((\pi^{r+1})\). Choose \(\sigma_m,\sigma_n\) with these
orders. The pencil \(\sigma_n+t\sigma_m\) again has exact orders
\(m,n\), has no zero member, lifts by (6), and cuts a flat proper CI
family by the fiberwise Cartier argument. No smooth-residual assertion,
uniform degree threshold, product-ideal residual gluing, or commuting
primary extraction follows in this non-Cartier setting.

The distinction between partial transfer and its endpoint is exact on a
normal carrier:
\[
\text{a mate with sole support }C
\iff \exists n,b>0:\ nC\sim bH\text{ as Weil divisors on }S.
\tag{9}
\]
For the forward implication the mate's Cartier divisor is \(nC\).
For the converse the relation makes \(nC\) an effective Cartier divisor
in \(O_S(bH)\); its canonical section lifts by (6). Its restriction is
nonzero, so the resulting pair is proper with exactly that support.
In particular a non-\(\mathbf Q\)-Cartier \(C\) cannot reach the endpoint
on this fixed normal carrier. Serre generation supplies finite orders,
not the positive class relation (9). For nonnormal carriers the correct
replacement includes full-conductor descent, addressed in the
[normalization and conductor chapter](normalization_conductor_projection.md).

## 3. Characteristic and Cartier descent through finite modifications

On a singular carrier, reaching sole support requires the appropriate
multiple of C to descend as a Cartier divisor. The conductor records
a finite gluing problem on the modification; its principal-unit
obstruction behaves differently in characteristic zero and positive
characteristic. Solving a finite-level descent problem is not the same
as producing one compatible solution at every level.



Here is a local control for all orders, independent of the quartic.
Let \(B=K[[z]]\), \(A_N=K+z^NB\), \(N\ge2\), and \(u=1+z\). Its
conductor is \(z^NB\): this ideal is a conductor, whereas an element
of \(A_N\) with nonzero constant term leaves \(A_N\) when multiplied
by \(z\). The normalization is finite; indeed this is
\(K[[z^N,\ldots,z^{2N-1}]]\subset K[[z]]\).
In characteristic \(p>0\), writing \(r=p^eM\), \(p\nmid M\), gives
\[
u^r=(1+z^{p^e})^M=1+Mz^{p^e}+\text{higher terms}.
\]
Consequently
\[
u^r\in A_N\iff p^{v_p(r)}\ge N.
\tag{10}
\]
The least descending exponent is the least \(p\)-power at least \(N\).
In characteristic zero the coefficient \(r\) of \(z\) never vanishes,
so no positive power descends. At each finite truncation a suitable
\(p\)-power kills \(u\), but no one exponent kills it at every level.
Thus \(\forall N\,\exists r_N\) cannot be replaced by
\(\exists r\,\forall N\). A finite generic conductor algebra uses
one finite level; an entire formal neighborhood is a different object.

The finite integral datum \(\mathbf Z\subset\mathbf Z[z]/(z^N)\)
with unit \(1+z\) gives eventual descent in every positive-characteristic
fiber and none over \(\mathbf Q\). The descending exponents can depend
on the characteristic; such witnesses alone do not transfer a descending
power to characteristic zero.

The mechanism is the principal-unit formal law \(X+Y+XY\).
In characteristic zero its finite nilpotent logarithm turns raising
to the \(r\)-th power into multiplication by \(r\), which cannot kill
a nonzero logarithmic defect. In characteristic \(p\), the \(p^e\)-series
is \(X^{p^e}\), annihilated by a sufficiently high **finite** nilpotence
order. No direct-product decomposition of higher principal units is
needed. The full global criterion remains
[R-0003](../results/fixed_carrier_conductor_criterion.md), with its
specified carrier, full inverse support and conductor hypotheses.

There are characteristic-zero alternatives to Frobenius. A finite-order
semi-invariant has an invariant power with exactly the image zero support;
the [finite-quotient proof and corrected-square twisted-cubic benchmark](../supplements/TORSION_CONSTRUCTIONS_AND_PINCHING_LIMITS.md#a-corrected-homogeneous-square-on-the-twisted-cubic)
show why this can produce an actual characteristic-zero supported pair.
Its projective use needs linearization, the correct ambient twist and
an actual carrier. The
[full positive-relation-cone cancellation mechanism](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md#constructive-use-of-the-descent-lattice)
can instead cancel opposite logarithmic defects in distinct compatible
global divisor directions. Neither mechanism supplies a quartic carrier
here. The [nodal pinching control](../supplements/TORSION_CONSTRUCTIONS_AND_PINCHING_LIMITS.md#nodal-pinching-can-destroy-the-marked-support-requirement)
shows why local phase choices must also preserve the marked inverse support.

## 4. The marked Quot space and its equation incidence

An embedded lower thickening is a point of a marked Quot space of a
bounded infinitesimal neighborhood of C. Containing hypersurfaces
are additional incidence data over that space. Deforming the
thickening and lifting its defining global sections are therefore
separate steps. The tangent and connecting maps below quantify
this distinction; neither first-order compatibility nor abstract
deformability automatically supplies a supported complete intersection.



Let \(X=\mathbf P^3\), and let \(T\subset X\) be a pure CM thickening
with support \(C\), ideal \(J\subset I=I_C\), and generic length \(m\).
No lci, curvilinearity or normal-flatness hypothesis is imposed.

### 4.1. A finite marked Quot model and its tangent

One has \(I^m\subset J\subset I\). At \(\eta_C\), the maximal ideal
of an Artinian algebra of length \(m\) has \(m\)-th power zero: every
nonzero successive power gives a strict step in its length filtration.
The image of \(I^m\) in \(O_T\) therefore vanishes generically and has
finite support. Purity excludes such a nonzero submodule, proving the
inclusion everywhere.

For any \(N\) with \(I^N\subset J\), put \(B_N=I/I^N\). Marked
thickenings between the two fixed outer schemes correspond to quotients
\(B_N\twoheadrightarrow I/J\) with fixed Hilbert polynomial. An
\(O_X\)-submodule of \(I/I^N\) is an ideal modulo \(I^N\). Moreover
\[
0\to I/J\to O_T\to O_C\to0
\]
makes quotient flatness equivalent to flatness of \(T\) over a parameter
base. The appropriate pure CM locus may be imposed separately. This gives
a finite neighborhood for one thickening, not a uniform Euler-characteristic
or degree bound across all thickenings.

The tangent space is
\[
V_T=\operatorname{Hom}_X(J/I^N,I/J).
\tag{11}
\]
Indeed, under the graph convention
\(J_\xi=\{j+\epsilon h:h\bmod J=\xi(j)\}\),
\(O_X\)-linearity makes an ideal flat over \(k[\epsilon]/\epsilon^2\).
Requiring \(J_\xi\subset I[\epsilon]\) puts its image in \(I/J\);
requiring \(I^N[\epsilon]\subset J_\xi\) kills \(I^N\).
Conversely these conditions give every such first-order ideal. Since
\(J\) annihilates \(I/J\), the source also factors through
\(J/(I^N+J^2)\). This is not the equation module \(J/IJ\).
Standard quotient deformations distinguish this Hom space from their
possible [Ext obstruction](https://stacks.math.columbia.edu/tag/0CZU)
and [torsor of lifts](https://stacks.math.columbia.edu/tag/0CZV).

### 4.2. Exact first-order compatibility for the pair

Fix actual forms \(F\in H^0(J(a))\), \(G\in H^0(J(b))\). Use affine
coefficient spaces. For \(d=a,b\), let
\[
\delta_d:H^0((I/J)(d))\longrightarrow H^1(J(d))
\]
be the connecting map for \(0\to J(d)\to I(d)\to(I/J)(d)\to0\).
A tangent \(\xi\in V_T\) lifts together with the actual pair iff
\[
\operatorname{Ob}_{F,G}(\xi)
=(\delta_a(\xi(F)),\delta_b(\xi(G)))=0.
\tag{12}
\]
For the incidence space of thickenings and pairs the exact tangent sequence
is
\[
0\to H^0(J(a))\oplus H^0(J(b))
\to T_{(T,F,G)}\operatorname{Inc}_N
\to\ker\operatorname{Ob}_{F,G}\to0.
\tag{13}
\]
To prove this, write \(F_\epsilon=F+\epsilon\dot F\). The graph ideal
condition is \(\dot F\bmod J=\xi(F)\). Its right side lies in \(I/J\),
so the allowed global lift is necessarily an actual form in \(H^0(I(a))\).
The exact sequence gives precisely the first class in (12). Differences
of two lifts lie in \(H^0(J(a))\); do the same for \(G\). This proves
both the criterion and (13). Projectivizing removes scaling directions
but does not change compatibility. A nonzero class rejects this specified
motion and degrees, not every motion or every higher degree.

### 4.3. Artin steps and the distinct fixed-source problem

Suppose \(B'\twoheadrightarrow B\) is a small extension with kernel \(A\)
killed by its maximal ideal, and a flat marked \(T_B\) has **already**
been lifted to \(T_{B'}\). Flatness of its structure sheaf makes its
ambient ideal flat as well, and base change gives
\[
0\to J(d)\otimes_k A\to J_{B'}(d)\to J_B(d)\to0.
\tag{14}
\]
The connecting class of a chosen \(F_B\) in \(H^1(J(a))\otimes A\)
vanishes exactly when it lifts through this chosen ideal lift. Choices
form a torsor under \(H^0(J(a))\otimes A\), independently for \(G\).
Lifting the quotient itself is an earlier, separate deformation problem.
A successful compatible tower gives fixed-degree formal coefficient
series; it does not by itself give an algebraic parameter curve.

Prescribing classes in the fixed equation module \(D_T=J/IJ\) instead
uses
\[
0\to IJ(d)\to J(d)\to D_T(d)\to0,
\tag{15}
\]
whose obstruction lies in \(H^1(IJ(d))\), not \(H^1(J(d))\).
In a bounded family sufficiently large twists, with cohomology and base
change, remove section-lifting obstructions and make incidence a vector
bundle over the chosen ideal family. They do not ensure that two sections
generate the ideal or eliminate residual curves.

### 4.4. A motion that exists as ribbons but fails with a quadric equation

In any characteristic take \(T=2C\) on the unique smooth quadric
\(Q=V(q)\), so \(J=(q)+I^2\). The conormal sequence is
\[
0\to K=O_{\mathbf P^1}(-8)\to E=I/I^2
\to L=O_{\mathbf P^1}(-6)\to0
\tag{16}
\]
by [R-0020](../results/quartic_conormal_characteristic_jump.md).
The \(N=2\) flag tangent is
\(\operatorname{Hom}_C(K,L)=H^0(O(2))\), of dimension three.
These directions actually integrate. In characteristic different from two,
\(E=O(-7)^2\), and its surjections to \(L\) are basepoint-free pairs of
binary linear forms modulo scalar, an open subset of \(\mathbf P^3\).
In characteristic two, \(E=O(-8)\oplus O(-6)\); a map to \(L\) consists
of a quadratic and a scalar. Surjectivity requires that scalar to be
nonzero, since a quadratic alone has a zero. After scalar normalization
these maps form affine three-space. In either case the inverse-image
ideals locally have form \((x,y^2)\), hence define pure embedded ribbons. The relevant
vanishing is \(\operatorname{Ext}^1_C(K,L)=H^1(O(2))=0\).
It is not ambient \(\operatorname{Ext}^1_X(i_*K,i_*L)\), which has
normal-direction terms and dimension twenty here.

Uniqueness of the quadric gives \(H^0(I(2))=H^0(J(2))=kq\), with zero
image in \(H^0(L(2))=H^0(O(2))\). Quadratic monomial restriction covers
all nine monomials of \(H^0(O_{\mathbf P^1}(8))\), so \(H^1(I(2))=0\).
The connecting map \(\delta_2\) is therefore an isomorphism. Since
\(q\) trivializes \(K(2)\), evaluation \(\xi\mapsto\xi(q)\) is also
an isomorphism. Every nonzero ribbon tangent consequently has a nonzero
actual-quadric lifting class in (12).

For a proper actual pair take \(F=q\), \(G=f^2\),
\(f=x_0^2x_2-x_1^3\). In Segre coordinates
\((x_0,x_1,x_2,x_3)=(su,sv,tu,tv)\),
\(f=s^2(tu^3-sv^3)\), so its divisor on \(Q\) is \(C+2\ell\).
The pair has full primary component \(2C\) and residual \(4\ell\).
Since \(G\in I^2\), every permitted tangent kills \(G\); only the
first coordinate of (12) obstructs. This exact control refutes the
inference that integrable thickening motion automatically carries the
chosen-degree equations with it.

## 5. Embedding abstract deformations with the quartic marked

An abstract ribbon family does not come with a deformation of its
map into projective space. The geometric issue is extending the
embedding while fixing its restriction to C. The obstruction
calculation below concerns that marked map problem; it does not
establish that the embedded family has two global equations.



### 5.1. A marked embedding criterion with algebraization

Let \(S\) be locally Noetherian over an algebraically closed field,
\(s\in S(k)\), and \(\mathcal X\to S\) proper, flat, finitely presented.
Assume a flat closed mark \(C\times S\hookrightarrow\mathcal X\), and
central embeddings \(i:W=\mathcal X_s\hookrightarrow\mathbf P^3\),
\(j=i|_C\). Put \(J=I_{C/W}\). If
\[
H^1(W,i^*T_{\mathbf P^3}\otimes J)=0,
\tag{17}
\]
then after an étale neighborhood of \(s\), \(i\) extends to a closed
immersion of \(\mathcal X\) into \(\mathbf P^3_S\), equal to the fixed
\(j\) on \(C\times S\). Neither reducedness nor lci is required of \(W\).
The same result holds for a fixed smooth separated finite-type target.

**Proof.** Write \(\mathcal J=I_{C\times S/\mathcal X}\), which is
\(S\)-flat by the ideal sequence. For a small extension \(A'\to A\)
with kernel \(K\) killed by the maximal ideal, the closed union
\(D=\mathcal X_A\cup C_{A'}\) in \(\mathcal X_{A'}\) has ideal
\[
(KO_{\mathcal X_{A'}})\cap\mathcal J_{A'}
=K\mathcal J_{A'}=K\otimes_k J.
\tag{18}
\]
The first equality uses flatness of the distinguished quotient; the last
uses flatness of its ideal. A lifted map over \(A\) and the fixed map on
\(C_{A'}\) agree on \(C_A\), so give a map on \(D\). Smoothness of the
target gives local lifts; differences form a Čech cocycle in
\(i^*T_{\mathbf P^3}\otimes J\otimes K\). Condition (17) kills its
class and glues a lift through every small extension. This is the
[map deformation mechanism](https://stacks.math.columbia.edu/tag/08U8).

To algebraize, take the fiber over \(j_S\) of the restriction map
\[
\operatorname{Mor}_S(\mathcal X,\mathbf P^3_S)
\longrightarrow\operatorname{Mor}_S(C\times S,\mathbf P^3_S).
\]
These Mor spaces are algebraic and locally of finite presentation by
[Stacks 0D1C](https://stacks.math.columbia.edu/tag/0D1C); the marked fiber
has the same property. The preceding Artin lifting criterion, also after
residue-field extension, makes it smooth at \([i]\) by
[0APN](https://stacks.math.columbia.edu/tag/0APN). An étale scheme chart
and smooth local coordinates give a section through the specified point
after an étale base neighborhood. Its universal map extends \(i\).
The [closed-immersion locus](https://stacks.math.columbia.edu/tag/05XA)
is open; shrink to retain it. This produces an actual algebraic family,
not an asserted convergence of a formal arc.

### 5.2. Every prescribed embedded ribbon in the vanishing range

Over \(\mathbf C\), let \(W\subset\mathbf P^3\) be **any given** ribbon
with reduction the specified embedded \(C_0\), with conormal ideal
\(J=O_{\mathbf P^1}(-d)\), \(0\le d\le6\). Then \(W\) is the special
fiber of an embedded algebraic flat family whose noncentral members are
\(C\cup C_t\), with \(C\) fixed pointwise, \(C_t\) a distinct smooth
rational quartic, and \(C\cap C_t\) consisting of \(d\) transverse
reduced points (empty for \(d=0\)).

**Proof.** The parametrizing sections have syzygy columns
\[
(t,-s,0,0),\quad(0,t^2,-s^2,0),\quad(0,0,t,-s).
\]
They are independent at every point and have degrees \(1,2,1\).
Their maximal minors are the parametrizing monomials, up to sign.
The pulled-back dual Euler sequence consequently gives
\[
T_{\mathbf P^3}|_C=O(5)^2\oplus O(6).
\tag{19}
\]
Because \(J^2=0\), the sheaf in (17) is the pushforward from \(C\)
of this bundle tensored with \(O(-d)\), and
\[
h^1(W,i^*T_{\mathbf P^3}\otimes J)
=2\max(d-6,0)+\max(d-7,0)=0.
\tag{20}
\]

For \(1\le d\le6\), choose a reduced divisor \(\Delta\) of degree \(d\)
on \(\mathbf P^1\). Drézet's
[Proposition 3.2.6 and Theorem 3.2.7(ii)](https://arxiv.org/html/1409.4175v3#S3.SS2)
give a global maximal reducible deformation of the abstract ribbon with
conormal \(O(-\Delta)\). Definition 2.3.1 specifies closed total-space
components, each flat with scheme-theoretic special fiber the reduced
\(C\); general components are smooth and meet transversely in \(d\)
points. One component becomes \(\mathbf P^1\times S\) étale locally,
with prescribed central identification: \(H^1(T_{\mathbf P^1})=0\)
lifts its isomorphism through Artin extensions, and the relative Isom
space and smooth local section algebraize it. It supplies exactly the
flat closed mark required in §5.1, so (20) extends the given embedding.

For \(d=0\), the abstract ribbon splits because its gluing class lies
in \(H^1(T_{\mathbf P^1})=0\). Use instead the explicit proper flat
family
\(\mathbf P^1\times\operatorname{Spec}\mathbf C[z,t]/(z(z-t))\),
marked by \(z=0\), and apply the same lemma. The extended polarization
has degree four on each smooth component, by flatness and its central
restriction. The closed immersion preserves the stated intersections.
The total genus \(d-1\) also follows from
\(0\to O(-d)\to O_W\to O_C\to0\), agreeing with the reducible fiber.

The cited theorem supplies an abstract ribbon deformation, not this
projective embedding. The latter is a repository deduction from (17).
Only its reduced-divisor global theorem is used; the broader local
criterion and higher-multiplicity discussion supply no iteration theorem.

### 5.3. Actual proper pairs absorb four residual degrees into that ribbon

After shrinking this pointed smooth base, choose sufficiently large
**fixed** \(a,b\). Relative Serre vanishing and generation make the
ideal sections commute with base change and lift central forms through
the whole embedded family. Choose \(F_0,G_0\) in the central ideal
generally so that they are proper and generate the ribbon ideal at
\(\eta_C\). These conditions are simultaneously nonempty open:
generation supplies independent generic conormal classes, and the
ideal system has no surface base component. Lift them to forms \(F,G\).

The central ribbon is lci. The fiberwise lci criterion and openness,
followed by properness and a base shrink, make the embedded family a
regular codimension-two immersion; see
[Stacks §37.62](https://stacks.math.columbia.edu/tag/068E).
The determinant of the two equation classes in its conormal bundle is
nonzero on a central open. Restricted to either smooth component family,
its nonvanishing locus maps openly to the base and meets the special
point. Shrinking makes it nonempty on every nearby component fiber.
The pair therefore generates the family ideal at both generic points
away from zero, and the ribbon ideal generically at zero. Properness
of the pair persists by projective fiber-dimension semicontinuity.
The fiberwise regular sequences give a flat CI family with cycles
\[
[Y_0]=2[C]+R_0,\qquad [Y_t]=[C]+[C_t]+R_t,\quad
\deg R_0=\deg R_t=ab-8.
\tag{21}
\]
No \(R_t\) contains the displayed components.

The full \(C\)-primary component of \(Y_0\) is precisely the **given**
\(W\), not just some length-two thickening. Its ideal is pure with sole
prime support, hence is the contraction of its localization at
\(\eta_C\); generic equality of the two ideals proves the claim.
Relative to the fixed \(C\), the full residual degree is \(ab-4\)
away from zero and \(ab-8\) at zero. Exactly four units are absorbed.
The residual after full-primary extraction need not be flat. The flat
once-linked family and its precise hypotheses belong to the
[relative residual construction](residual_liaison.md#21-the-once-linked-curve-is-flat-through-multiplicity-jumps).
The \(d\) points describe \(C\cap C_t\), not attachment to the entire
CI residual, which also includes \(R_t\). No smoothness of \(R_t\) or
optimal numerical degree threshold is asserted.

The same existence conclusion holds over every algebraically closed
characteristic-zero field \(k\). Descend the specified ribbon and its
embedding to a finitely generated subfield \(k_0\subset k\), embed
\(k_0\) in \(\mathbf C\), and construct the complex witness. All the
family, marks, embeddings, central identifications and chosen forms
use finitely many coefficients; descend them to a finite-type
\(k_0\)-subalgebra by
[finite-presentation descent](https://stacks.math.columbia.edu/tag/01ZM).
Shrink its spectrum to retain flatness, the smooth pointed curve,
closed immersions, properness and transverse noncentral fibers; these
properties descend by [Stacks §32.8](https://stacks.math.columbia.edu/tag/081C).
A closed point has residue field finite over \(k_0\), hence embeds over
\(k_0\) in algebraically closed \(k\). Specialization and base change
retain the original central ribbon. No embedding of the whole field
\(k\) in \(\mathbf C\) is assumed.

### 5.4. What the threshold means, and a general rational-curve form

The interval \(0\le d\le6\) is a **sufficient marked-lifting range**.
It is not the range of all embedded ribbons. In characteristic zero an
embedded ribbon on \(C_0\) is equivalent to a line-bundle quotient
\(I/I^2\twoheadrightarrow O(-d)\), whose inverse-image ideal locally
is \((x,y^2)\). By R-0020 its source is \(O(-7)^2\). For nonnegative
\(d\), such quotients exist exactly when \(d\le7\): use a basepoint-free
pair of degree-\((7-d)\) binary forms when \(d<7\), or any nonzero
constant pair when \(d=7\); for \(d>7\) every Hom vanishes. At \(d=7\),
(20) equals two. This proves failure of the vanishing shortcut, not
failure of every marked deformation.

This quotient classification also shows the exact positive-characteristic
change. In odd characteristic the balanced conormal and the same proof
give \(0\le d\le7\). In characteristic two the conormal is
\(O(-6)\oplus O(-8)\). For nonnegative \(d\), quotients to \(O(-d)\)
exist for \(d\le6\) (choose a basepoint-free pair of degrees \(6-d,8-d\))
and for \(d=8\) (use the scalar map from \(O(-8)\)). They do not exist
for \(d=7\), where the only possible nonzero map is a linear form from
\(O(-8)\), which vanishes somewhere, nor for \(d>8\), where all maps
are zero. This is a classification of possible line-bundle quotients,
not a reducible-deformation theorem in positive characteristic.

More generally, over an algebraically closed characteristic-zero field,
let a specified smooth rational curve embedded in \(\mathbf P^3\) have
\(T_{\mathbf P^3}|_C=\bigoplus_iO(e_i)\). For any given embedded
ribbon with conormal \(O(-d)\), \(d\ge0\), the same Drézet-plus-marked-map
proof works whenever
\[
d\le1+\min_i e_i.
\tag{22}
\]
Indeed \(H^1(O(e_i-d))=0\) exactly in that range, and its abstract
reduced components are rational and become trivial étale locally.
The general component has the original curve's degree by flatness.
This is the actual general mechanism; the special quartic contributes
its tangent splitting (19), not a separate deformation theorem.

## 6. The sufficient vanishing is unavailable at a hypothetical endpoint

Suppose conditionally that \(Z=V(F_a,G_b)\) has sole support \(C_0\)
in characteristic zero, with \(a,b\ge5\), as required by the accepted
low-degree boundary. Put \(c=a+b-4\), \(E=T_{\mathbf P^3}|_Z\),
\(J=I_{C/Z}\), and \(R=k[x_0,x_1,x_2,x_3]/(F,G)\). Then
\[
\boxed{h^1(E\otimes J)=19+ab(3c/2-4)>0.}
\tag{23}
\]

**Proof.** The CI is ACM and Gorenstein, with \(\omega_Z=O_Z(c)\).
For \(n\ge0\), \(h^0(O_Z(n))=H_R(n)\). In the restricted Euler
sequence
\[
0\to O_Z\to O_Z(1)^4\to E\to0,
\]
Serre duality identifies the dual of
\(H^1(O_Z)\to H^1(O_Z(1))^4\) with coordinate multiplication
\(R_{c-1}^4\to R_c\). Standard grading makes this surjective for
\(c\ge1\). Since \(h^0(O_Z)=1\), \(h^0(O_Z(1))=4\), it follows that
\[
h^0(E)=15,\qquad h^1(E)=4H_R(c-1)-H_R(c).
\]
All fifteen sections are ambient projective vector fields. Their
restriction to \(C\) is injective: a matrix vanishing projectively at
every curve point has every curve line as an eigenline; irreducibility
puts the curve in one eigenspace, and nondegeneracy makes that the whole
space, so the matrix is scalar. By (19), \(h^0(E|_C)=19\),
\(h^1(E|_C)=0\). The exact sequence
\(0\to E\otimes J\to E\to E|_C\to0\) gives
\(h^1(E\otimes J)=4+h^1(E)\). Finally
\(\chi(O_Z(n))=abn-ab c/2\), so
\(\chi(E)=ab(4-3c/2)\). Substituting \(h^0(E)=15\) proves (23).
Here \(c\ge6\), so positivity is immediate.

For any nondegenerate smooth rational degree-\(e\) marked curve in such
a CI, the same argument replaces 19 by \(4e+3\), since its restricted
Euler sequence gives \(h^0(T_{\mathbf P^3}|_C)=4e+3\), \(h^1=0\).
No classification of multiple structures enters.

Equation (23) is the dimension of a space **which can contain** marked
map-lifting obstructions. It exhibits no obstruction class for a
particular deformation and proves neither singularity of the marked
Hom space nor impossibility of the endpoint. It says exactly that the
sufficient vanishing (17) cannot certify it.

The calculation itself uses no characteristic-zero input: for
\(a,b\ge2\), \(c=a+b-4\ge1\), the same identity (23) holds in every
characteristic. The assumption \(a,b\ge5\) comes only from the
characteristic-zero carrier exclusion and must not be transferred to
positive characteristic. Indeed the actual
[positive-characteristic quartic-carrier endpoints](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md)
of degrees \((4,N)\), with \(N=p^e>5\), have the positive obstruction-space
dimension \(19+4N(3N/2-4)\) and nevertheless exist. They are a direct
control of why a nonzero space is not a nonzero obstruction class.

## 7. Partial absorption and the missing passage to sole support

Two genuine positive operations survive: arbitrary finite order increases
on specified normal carriers after sufficiently large twists, and
absorption of a moving quartic into **any prescribed** ribbon in the
marked-lifting range, with actual proper equation pairs. The former fixes
a carrier and prescribes orders; the latter fixes embedded ribbon data.
Neither operation deforms every starting residual configuration.

Their shared useful mechanism is solvability of a gluing problem in an
actual finite-dimensional source. Ample twisting repairs section lifting;
marked tangent vanishing repairs extension of a prescribed embedding;
Cartier or divisorial ideals encode orders. These are proved implications.
Their analogy with conductor-unit descent is that local candidate data
need global compatibility; their cohomology groups and unit quotients
are not thereby the same invariant.

An iteration to STCI would require a new theorem giving compatible higher
thickenings or curves, their marked embeddings, and actual pairs with
properness and generic generation retained, while **all** remaining
residual degree disappears at a final parameter. Increasing degrees alone
does not achieve this: the prescribed-ribbon operation always absorbs
four degrees, while its remaining degree is \(ab-8\). On a normal fixed
carrier an endpoint requires (9); on a nonnormal carrier it additionally
requires the actual full-conductor conditions. The full attachment
module, including its non-lci torsion and normal nilpotent gluing, must be
tracked fiberwise rather than assumed flat across primary jumps.

These are concrete open interfaces. The existence of partial absorption,
vanishing of selected tangent classes, nonvanishing of an obstruction
**space**, and separate finite characteristic-\(p\) repairs decide none
of them and do not decide the characteristic-zero STCI question.


## 8. Exact characteristic boundary

The fixed curve remains \(C_0\) throughout; none of these assertions is
about all rational quartic embeddings. The
[quartic-carrier construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md)
proves that this \(C_0\) is an STCI in **every** positive characteristic.
This is compatible with the characteristic-free partial-transfer and
lifting mechanisms above. It contradicts any attempt to extend the
characteristic-zero quartic-carrier exclusion to characteristic \(p\).

| Mechanism | Positive-characteristic reach | Boundary used in this chapter |
|---|---|---|
| Cartier interpolation and normal Cartier-index extension (§2) | Full statements, including general smooth integral residuals, hold over algebraically closed fields in every characteristic | The systems are very ample and define immersions; arbitrary inseparable basepoint-free systems would not justify smooth Bertini |
| Weak divisorial interpolation and normal endpoint equivalence (§2.3) | Both are characteristic-free | Exact finite orders do not supply the positive global divisor relation |
| Smooth-along-\(C\) residual floor (§2.2) | Characteristic-free under the same smooth-on-\(C\) hypotheses | A positive-characteristic supported quartic carrier lies outside this smooth-on-\(C\) carrier class |
| Marked Quot, graph tangent, Artin actual-equation lifting (§4) | The statements and proofs are characteristic-free | The curve-specific conormal parameterization changes at two, as stated in §4.4; an Artin lift is not an algebraic arc |
| Marked map-lifting and tangent syzygies (§5.1–5.2) | The marked embedding lemma, splitting (19), and vanishing calculation (20) work in every characteristic | They extend an **already given** abstract family; they do not produce Drézet's required abstract family in characteristic \(p\) |
| Prescribed-ribbon reducible family and its actual-pair corollary (§5.2–5.4) | No blanket extension claimed here | The abstract existence theorem is over \(\mathbf C\), then spreads in characteristic zero; no positive-characteristic abstract existence theorem is supplied |
| Endpoint cohomology (§6) | The identity holds for \(a,b\ge2\), \(a+b-4\ge1\) in every characteristic | Characteristic-zero degree exclusions do not transfer; actual characteristic-\(p\) endpoints have nonzero obstruction spaces |
| Nilpotent conductor powering (§3) | Finite nilpotent defects can be killed by a sufficiently large \(p\)-power | Characteristic-zero logarithmic rigidity fails, while the infinite-level quantifier warning remains |

In particular, the characteristic-free map criterion and the existence of
characteristic-\(p\) STCI pairs are established facts with different inputs.
They do not prove that every prescribed positive-characteristic ribbon
has the reducible family of §5.2. This is the exact unproved extension,
not a presumed impossibility of positive-characteristic absorption.

## 9. What supported semiregularity and coefficient estimates can detect

The obstruction space in §6 invites a sharper question: can a known
annihilator of deformation obstructions retain information that the space
itself does not? The following uniform vanishing closes one specified
supported detector. It does not compute a marked obstruction class.
This addition preserves the independently reviewed continuation through
`427f3d4`; its complete proof and primary-source applications also passed
independent consolidation review.

### 9.1. A characteristic-free supported vanishing

Let \(C\subset X=\mathbf P^n_k\), \(n\ge2\), be any smooth projective
curve over an algebraically closed field. Rationality, nondegeneracy,
normal splitting and equations are unnecessary. Then
\[
H_C^n(X,\Omega_X^{n-2})=0,
\qquad
\mathbb H_C^{2n-2}(X,\Omega_X^{<n-1})=0.
\tag{24}
\]
The truncated complex has \(\Omega_X^p\) in degrees \(0\le p\le n-2\).
Both assertions hold in every characteristic.

**Proof.** Put \(C_m=V(I_C^m)\). For a locally free sheaf \(V\),
the coherent supported-cohomology formula and Serre duality give
\[
H_C^q(X,V)=\varinjlim_m\operatorname{Ext}_X^q(O_{C_m},V),
\quad
\operatorname{Ext}_X^q(O_{C_m},V)
=H^{n-q}(C_m,V^\vee\otimes\omega_X|_{C_m})^\vee.
\tag{25}
\]
These are global Ext groups. The colimit uses coherent coefficients on
the Noetherian scheme; it is not an arbitrary-sheaf assertion.
The duality is [coherent Serre duality](https://stacks.math.columbia.edu/tag/0FVZ),
with the locally free twist moved across Ext; \(O_{C_m}\) need not be
locally free. In particular these groups vanish for \(q>n\).

For \(V=\Omega_X^{n-2}\), exterior-power duality identifies
\(V^\vee\otimes\omega_X=\Omega_X^2\). The regular embedding gives
\(I_C^r/I_C^{r+1}=\operatorname{Sym}^rN_{C/X}^\vee\).
The conormal and Euler sequences are locally split bundle injections
\[
N_{C/X}^\vee\hookrightarrow\Omega_X^1|_C
\hookrightarrow O_C(-1)^{n+1}.
\]
Taking symmetric and exterior powers, then tensoring, yields
\[
\Omega_X^2|_C\otimes\operatorname{Sym}^rN_{C/X}^\vee
\hookrightarrow O_C(-r-2)^{M_r}
\tag{26}
\]
for a finite \(M_r\). Local splitting makes these injections valid even
in positive characteristic. Negativity kills global sections on every
connected component. The finite normal filtration then gives
\(H^0(C_m,\Omega_X^2|_{C_m})=0\) for every \(m\). Equation (25)
proves the first assertion of (24).

For the second, use the supported hypercohomology spectral sequence
\(E_1^{p,q}=H_C^q(X,\Omega_X^p)\). On \(p+q=2n-2\), all terms
have \(q>n\) except \((p,q)=(n-2,n)\), which also vanishes.
The spectral sequence is for sheaves of \(k\)-vector spaces: the de Rham
differential need not be \(O_X\)-linear. At \(n=2\) the truncated
complex is just \(O_X\), so the same proof applies. Nonproper curves
and singular reduced supports have not been included by this argument.

### 9.2. Which obstruction comparison this eliminates

[Iacono–Manetti, Theorem 11.1 and its proof](https://arxiv.org/pdf/1112.0425)
annihilate embedded Hilbert obstructions already in
\(\mathbb H_Z^{2p}(X,\Omega_X^{<p})\), under their characteristic-zero
setup: a codimension-\(p\) lci is the regular zero locus of a section of
a rank-\(p\) vector bundle on a Zariski open neighborhood.
A global complete intersection meets that setup.
[Support cohomology](https://stacks.math.columbia.edu/tag/0A39) depends
only on the closed topological support. For thickenings of a smooth curve,
\(p=n-1\), this target and its precursor
\(H_Z^{p+1}(X,\Omega_X^{p-1})\) are the two zero groups (24).
In \(\mathbf P^3\) the supported truncated target is
\(\mathbb H_C^4(\mathbf P^3,[O\to\Omega^1])=0\).

The ordinary ambient trace components in
[Pridham, Corollary 2.22 and Remarks 2.27–2.29](https://webhomes.maths.ed.ac.uk/~jpridham/semireg2.pdf)
also vanish here: \(H^{q+2}(\mathbf P^3,\Omega^q)=0\).
Neither a zero target nor annihilation in it shows that an original
obstruction is zero or nonzero. Other relative or marked complexes
have not thereby been examined. The geometric reason for (24) is that
**every finite normal neighborhood lacks ambient two-form sections**;
it does not depend on the amount of thickness or equation degrees.

There is also a direct reason that ordinary embedded CI deformations
are a different problem from prescribed marked abstract deformations.
Let an existing global CI \(Z=V(F_a,G_b)\subset\mathbf P^3\) contain
the fixed \(C\).
Its ACM ideal gives \(H^1(I_Z(a))=H^1(I_Z(b))=0\).
Across Artin extensions, ideal flatness and these vanishings lift its
generators to global equations. For a deformation still containing
\(C\), these equations lie in the fixed coefficient spaces
\(H^0(I_C(a))\) and \(H^0(I_C(b))\), where their coefficients lift
freely. Their special-fiber regular sequence makes the lifted CI flat;
Nakayama identifies it with the specified embedded deformation at the
previous stage. Thus this embedded deformation functor is unobstructed.
It does not follow that an independently prescribed abstract marked
family has that embedding or is induced by these equation motions.
The nonzero marked-map obstruction space in §6 is consistent with both
facts, including the actual positive-characteristic endpoints.

### 9.3. Local valuation completeness does not control global coefficients

[Herrera Govantes–Mahboub–Olalla–Spivakovsky, Theorem 6.2 and Remark 3.34](https://arxiv.org/pdf/1406.0657)
concern a simple transcendental extension of valued fields with rank-one
base valuation. Their complete key polynomials attain each polynomial's
value through suitable truncated valuations; coefficients in the valued
field are allowed. The order-type bound is not a bound on the sum of
coefficient poles over all places of the curve in terms of the original
homogeneous degrees. Rescaling to be integral at one place can introduce
poles elsewhere. This is a scope limit, not a defect in valuation
completeness and not an obstruction to a specified bounded use of it.

A global estimate can become useful after actual functions and their
boundary are controlled. In characteristic zero let \(u,v\) be
\(S\)-units on a smooth complete genus-\(g\) curve, not both constant,
with \(z=1+u+v\notin\{0,1,u,v\}\). Put
\(\chi=2g-2+|S|\), \(\widetilde H=H(1:u:v)\),
\(H^*=\widetilde H+\chi+|S|\), and \(S_z=S\cup z^{-1}(0)\).
[Corvaja–Zannier, Theorem 1.1](https://www.numdam.org/article/BSMF_2011__139_4_437_0.pdf)
gives
\[
|S_z\setminus S|\ge
\widetilde H-15\chi-6(H^*)^{2/3}\chi^{1/3}
\]
for multiplicatively independent \(u,v\) modulo constants. For a
primitive dependence \(u^r=\lambda v^s\), it instead gives
\[
|S_z\setminus S|\ge
\widetilde H\left(1-\frac1{\max(|r|,|s|)}\right)-15\chi.
\]
Their Theorem 1.1* also bounds height from absolute support bounds;
a small support-to-height ratio is one sufficient mechanism, not a
necessary prerequisite. Independence is not an absolute gate.

To apply such bounds to successive normal cancellations of an arbitrary
pair, one must produce the actual relation, control **zeros and poles**
of its coefficients, and compare its counted points with normal contact
or genuine residual support. Enlarging \(S\) records new divisors but
does not bound their cost. No checked theorem supplies these missing
comparisons automatically. Function-field coefficient points and vertical
normal defects are not automatically extra curves downstairs.

Consequently these bare detector applications stop at a precise boundary.
The supported semiregularity target is zero; valuation completeness alone
supplies no global coefficient-cost bound. A future bounded test can use
a different relative target or an actual coefficient relation with a
specified independent support bound and geometric comparison. None of
this reverses the positive prescribed-ribbon construction or settles
characteristic-zero STCI. The vanishing (24) is characteristic-free;
Iacono–Manetti's application and the quoted height estimates retain their
characteristic-zero hypotheses, with no blanket extension to characteristic
\(p\) asserted.


## 10. Elementary modifications and the projective endpoint-gluing gap

The [quadric elementary modification](quadric_modification_and_global_corrections.md)
constructs an actual rank-two bundle with \(c_1=10,c_2=28\), and its
complete lift space consists of \(F=c_0^2+qH_4\),
\(G=c_2^2+qK_4\) with both quartic corrections arbitrary. A supported
section in this prescribed lift space would have cycle \(7C\) and produce a CI with cycle \(9C\).
The full source nevertheless has residual degree at least four. Its
first cancellation either fails, or requires a common binary quartic;
for a nonzero quartic the next correction misses the middle section
\(4s^{11}t^{11}\) even after enlarging the allowed correction space to
all degree-ten binary forms at either endpoint. The zero-quartic branch
uses the actual-pair residual inequality.

This is a concrete positive construction input with a complete bounded
negative test. Its full proof preserves all correction quartics, bundle
and cycle data, and the exact characteristic boundary. It neither
classifies all elementary modifications nor excludes arbitrary sextic
pairs, and does not select a higher-power continuation. The companion
[arithmetic incidence account](../supplements/ARITHMETIC_EQUATIONS_AND_JET_GAPS.md)
retains the distinct ramified-trait and support-preserving algebraization
questions; a fixed-carrier jet failure is not a result about the full
simultaneous-pair incidence.


## Consolidated historical source: `research/supplements/OCT7_THICK_CARRIERS_AND_MARKED_GEOMETRY.md`

Original mathematical content and qualifications retained verbatim. Historical relative links may require repair.

# Historical mathematical source compilation

This compilation retains the mathematical hypotheses, failed arguments, qualifications, and unresolved cases. It supplies no new independent audit.

---

## Source: 2026-10-07-thick-apic-conductor-bridge.md

# Entirely-thick branch: normalization, conductor, and almost-Cartier reformulation

Date: 2026-10-07
Status: LITERATURE CONNECTION + EXACT REFORMULATION TARGET / NO NEW EXCLUSION YET

## 1. Audit of the existing conductor theorem

The normalization/conductor theorem says the following for an integral carrier X with finite normalization nu:S->X and full reduced inverse image
    W=(nu^{-1}(C))_red.

If C has an STCI mate on X, then W must support an effective Cartier divisor on S. If all nonnormality of X is supported on C, then existence of some mate is equivalent to existence of such an effective Cartier divisor A with
    O_S(A)=O_S(bH)
for some b>0; after taking a power, conductor descent is automatic.

Therefore, in the clean-conductor case, conductor descent itself cannot supply a further asymptotic obstruction. The remaining obstruction is the existence/class of A.

## 2. Literature connection not presently recorded in main

Hartshorne and Polini, "Divisor class groups of singular surfaces", Trans. AMS 367 (2015), develop exact sequences relating Pic(X), APic(X), Pic(S), and local data along the singular/conductor locus. The paper explicitly applies this framework to restrictions on set-theoretic complete-intersection curves in P3.

This is more directly aligned with the present thick-carrier problem than generic conductor language alone.

No novelty claim is made for the APic framework.

## 3. Correct reformulation

For an integral hypersurface carrier X, C is an almost-Cartier divisor under the usual codimension-one hypotheses. If a mate of degree b cuts C set-theoretically, the corresponding principal/hyperplane divisor has support C with some generic multiplicity m. Thus the class of the resulting thick divisor lies in the hyperplane subgroup of APic(X).

After normalization this condition has two parts:

1. the pullback divisor class on S must lie in the subgroup generated by H;
2. the local almost-Cartier/conductor class must satisfy the compatibility needed to descend.

The existing clean-conductor theorem shows that after a suitable power the second condition disappears once the required effective Cartier support upstairs exists. Hence the difficult invariant is the class of the full inverse-image divisor in Pic(S), together with local APic data when extra nonnormality is present.

## 4. Relation to the entirely-thick valuation data

The generic transverse cluster and its Rees valuations measure multiplicity of the pair ideal along divisorial valuations over C. On a fixed carrier X, the normalization records branches above C as curve components
    Gamma_j subset S
mapping finitely to C.

A mate pulls back to an effective Cartier divisor
    A=sum_j n_j Gamma_j
(possibly impossible if the full inverse image also has isolated points).

The valuation of the mate along Gamma_j is exactly n_j. Thus the generator-sensitive valuation data has a natural normalization interpretation: it determines the coefficient vector (n_j) of the candidate Cartier divisor upstairs.

This gives the first credible bridge between the relative-cluster lane and the conductor lane:
    relative valuations -> coefficient vector on branches above C -> Pic(S)/<H> and local APic class.

The bridge is conceptual at present; the exact identification for the first-blowup section coefficients c_i has not been proved.

## 5. What would produce an obstruction

For a fixed integral carrier X, compute the subgroup
    K_X = { (n_j)>0 : sum n_j Gamma_j is Cartier and linearly equivalent to bH for some b>0 }.

If K_X is empty, X admits no mate.

If the entirely-thick Rees/cluster data restricts the possible coefficient vectors to a set V_X, then it is enough to prove
    V_X intersect K_X = empty.

This is a finite-lattice/class-group problem whenever the number of branches Gamma_j is finite and Pic(S) or its relevant quotient is computable.

## 6. Why this can couple generic and special data

The coefficient vector n_j is generic along the normalization branches, while the APic/local-conductor terms record compatibility at special singular points. Unlike the failed inequalities c_i >= Phi(M_i), an exact sequence for APic(X) genuinely relates these two strata.

Thus APic is the appropriate place to seek a theorem coupling:
- generic multiplicities along horizontal branches;
- special pinch/triple/conductor points;
- global hyperplane linear equivalence.

## 7. Next concrete target

Do not attempt this first for an arbitrary thick carrier.

Choose the simplest surviving integral nonnormal carrier class already represented in the repository, compute:
1. its normalization S;
2. the full inverse image of C and branch curves Gamma_j;
3. their classes in Pic(S);
4. the hyperplane class H;
5. the local APic/conductor contribution at special points.

Then solve the positive integer relation
    sum n_j [Gamma_j] = b[H]
in Pic(S), with the local APic compatibility.

This can either exclude that carrier class or produce an explicit finite family of admissible coefficient vectors for comparison with the thick valuation tree.

## 8. Boundary of the claim

Nothing here excludes the entirely-thick branch globally. The new contribution is identification of a standard literature framework that precisely packages the missing generic-to-special coupling, and a concrete lattice formulation for the next carrier-specific calculation.


---

## Source: 2026-10-07-thick-boundary-carrier-rigidity.md

# Entirely-thick (3,4) boundary: rigidity of the degree-3p carrier

Date: 2026-10-07
Status: PROVED equality rigidity on Q / OPEN ambient lifting problem

Let C be the smooth rational quartic on its unique smooth quadric Q, with C=(1,3). Let F have degree a=3p and exact generic normal order p along C.

## 1. Exact order after restriction to Q

The standard restriction calculation gives
\[
F|_Q=h^pR_F,\qquad R_F\in H^0(Q,O_Q(2p,0)).
\]

In earlier notes a general warning was retained: a residual section R_F can sometimes itself be divisible by h, so the order of F|Q along C may exceed the ambient generic normal order.

On the equality a=3p this cannot happen. Indeed h has class (1,3), whereas R_F has class (2p,0). If h divided R_F, the quotient would have class (2p-1,-3), which has no nonzero sections.

Therefore:
\[
\operatorname{ord}_C(F|_Q)=p
\]
exactly.

This is an equality-case rigidity statement for the individual carrier, independent of the mate.

## 2. Pure ruling residual divisor

Every effective divisor in |O_Q(2p,0)| is pulled back from a degree-2p divisor on the ruling base. Hence
\[
R_F=\lambda\prod_i \ell_i^{M_i},
\qquad \sum_iM_i=2p,
\]
where the \ell_i cut ruling fibers.

Thus on Q the degree-3p carrier has the exact form
\[
F|_Q=h^p\prod_i\ell_i^{M_i}.
\]

In the STCI equality pair a=3p,b=4q, the previous exceptional-cycle argument further bounds the number r of distinct fibers by
\[
r\le\min(p,q).
\]

So the boundary carrier is not merely high-contact with C: its entire residual intersection with Q is a repeated union of trisecant ruling fibers.

## 3. Ambient lifting formulation

Let q_Q be the quadratic equation of Q. Choose any ambient degree-3p lift H_p of
\[
h^pR_F\in H^0(Q,O_Q(3p,3p)).
\]
Then every ambient carrier with this restriction has
\[
F=H_p+q_QK,\qquad \deg K=3p-2.
\]

The condition that F have ambient normal order at least p is
\[
F\in I_C^p.
\]
Consequently the boundary classification problem becomes:

> Classify the lifts of the special section h^pR_F through
> \[
> H^0(P^3,I_C^p(3p))\to H^0(Q,O_Q(3p,3p))
> \]
> and determine the possible correction terms K modulo the q_Q-kernel.

This is naturally a Rees/associated-graded problem for I_C.

## 4. Why this may be more useful than normalization at this stage

Normalization depends on the actual ambient lift F, not merely F|Q. The equality boundary does not yet force F to be nonnormal or to have a prescribed normalization.

But it does force the image of F in the restriction to Q into an extremely small nonlinear locus:
\[
h^p\cdot\{\text{binary forms of degree }2p\text{ with at most }\min(p,q)\text{ roots}\}.
\]

Thus before applying APic one should classify or constrain the ambient lifts in I_C^p(3p).

## 5. Associated-graded target

The first symbol of F lies in
\[
H^0(C,\operatorname{Sym}^p N_C^*(3p)).
\]
Since N_C^*=O(-7)\oplus O(-7),
\[
\operatorname{Sym}^p N_C^*(3p)
\simeq O_C(12p-7p)^{\oplus(p+1)}
=O_C(5p)^{\oplus(p+1)}.
\]

The quadric direction supplies one distinguished linear factor in the conormal bundle. Restricting the first symbol to that direction recovers R_F|_C. Equality a=3p therefore fixes a highly special slice of the first symbol but does not a priori determine the other p normal-direction coefficients.

The next exact calculation should determine the image and kernel of
\[
H^0(I_C^p(3p))\to
H^0(I_C^p/I_C^{p+1}(3p))
\]
together with restriction to the quadric direction.

If this map has small kernel or a forced factorization at degree 3p, then the equality boundary may classify the carrier itself. If the kernel is large, normalization cannot yet be forced from boundary numerics.

## 6. Boundary of the claim

No claim is made that F is a p-th power, reducible, nonnormal, or generated by a quadric and cubic. Those would require the ambient lifting calculation.

The proved statement is only the exact restriction rigidity:
\[
F|_Q=h^pR_F,\quad R_F\in H^0(O_Q(2p,0)),
\]
with exact h-order p and, for an STCI equality pair, at most min(p,q) distinct ruling factors.


---

## Source: 2026-10-07-thick-degree-3p-quotient.md

# Entirely-thick boundary: exact degree-3p quotient modulo the quadric

Date: 2026-10-07
Status: PROVED

Let C=[s^4:s^3t:st^3:t^4] be the smooth rational quartic, Q its unique smooth quadric, and I=I_C.

## 1. Cartier restriction on Q

On Q=P1xP1, C has class (1,3), so
\[
I_C^p O_Q=O_Q(-p,-3p).
\]
After twisting by 3p,
\[
I_C^pO_Q(3p)=O_Q(2p,0).
\]

Thus restriction gives
\[
(I^p)_{3p}\longrightarrow H^0(Q,O_Q(2p,0)).
\]

The target has dimension 2p+1.

## 2. Surjectivity from cubic equations

For p=1,
\[
\dim I_3=20-h^0(C,O_C(3))=20-13=7.
\]
The unique quadric Q times linear forms contributes a 4-dimensional subspace. Therefore
\[
I_3/(Q S_1)
\]
has dimension 3, matching
\[
H^0(Q,O_Q(2,0)).
\]
The restriction map is therefore an isomorphism on this quotient.

Choose cubic equations A_0,A_1,A_2 whose restrictions form a basis of H^0(P1,O(2)) in the ruling-base coordinate.

For arbitrary p, products of p such cubics lie in (I^p)_{3p}. Their restrictions are products of p binary quadratics. The multiplication map
\[
\operatorname{Sym}^p H^0(P^1,O(2))
\to H^0(P^1,O(2p))
\]
is surjective (equivalently every binary monomial of degree 2p is a product, or linear combination of products, of p binary quadratics).

Hence
\[
(I^p)_{3p}\twoheadrightarrow H^0(Q,O_Q(2p,0))
\]
is surjective for every p>=1.

Consequently
\[
(I^p)_{3p}/\big((I^p)_{3p}\cap(Q)\big)
\cong H^0(Q,O_Q(2p,0)),
\]
and this quotient has dimension exactly
\[
2p+1.
\]

## 3. Interpretation

Every possible equality-boundary restriction
\[
F|_Q=h^pR,\qquad R\in H^0(O_Q(2p,0))
\]
already has a lift obtained from products/linear combinations of p cubic equations of C.

Thus the non-Q-divisible part of the degree-3p boundary contains no hidden higher-Rees obstruction.

The STCI equality condition restricts R to the nonlinear repeated-root locus with at most min(p,q) distinct roots, but every such R still lifts to I^p in degree 3p.

## 4. Where ambient freedom remains

The fiber over a fixed residual binary form is an affine translate of
\[
K_p=(I^p)_{3p}\cap(Q).
\]
Equivalently
\[
K_p=Q\,(I^p:Q)_{3p-2}.
\]

No claim is made here that
\[
(I^p:Q)=I^{p-1}.
\]
That colon identity would require a separate associated-graded/Rees argument.

Hence the remaining ambient classification problem is exactly the kernel/colon problem, not the boundary restriction problem.

## 5. Strategic consequence

The equality a=3p is rigid on Q but flexible enough that every allowed binary residual divisor lifts. Therefore one cannot exclude the (3,4) boundary from the F-side restriction alone.

Any further obstruction must use at least one of:
- the Q-divisible kernel K_p;
- compatibility with the mate G;
- singularity/normalization properties of the chosen lift;
- or higher pair/valuation data.

This sharply separates the solved quotient problem from the unresolved ambient problem.


---

## Source: 2026-10-07-thick-first-blowup-marked-coupling.md

# Entirely-thick boundary: first-blowup marked-point coupling audit

Date: 2026-10-07
Status: STRUCTURAL AUDIT / NO c_T-versus-M_T INEQUALITY FROM SEMICONTINUITY

Fix a horizontal component T of the first exceptional intersection cycle on
\[
B=\operatorname{Bl}_C P^3,
\qquad E=P(N_{C/P^3}),
\]
and let P=T cap S_Q be the marked point where T meets the quadric-direction section.

The goal is to put the generic coefficient c_T and the special repeated-root multiplicity M_T into one local model.

## 1. Blowup coordinates

Locally on C choose a parameter t and transverse parameters y,z with
\[
I_C=(y,z),\qquad Q=(z=0).
\]

On the blowup, the exceptional divisor is locally the projective normal-direction bundle with homogeneous coordinates
\[
[Y:Z]=[y:z].
\]

The strict transform of Q meets E in the section
\[
S_Q=[1:0].
\]

If F and G have exact generic orders p and q along C, write their initial normal forms as homogeneous binary forms
\[
f_p(t;Y,Z),\qquad g_q(t;Y,Z).
\]
Their common zero scheme on E is the first exceptional intersection W.

A horizontal component T corresponds generically to a common linear factor
\[
L_T(t;Y,Z)
\]
of these two binary forms over k(C). Its coefficient c_T in W is the generic intersection multiplicity of the two transformed divisors along T; equivalently it is determined in the completed two-dimensional local ring at the generic point of T.

## 2. The marked root multiplicity is a section-intersection phenomenon

The equality-boundary repeated-root multiplicity M_T is detected where T meets S_Q.

It is not obtained by taking a finite flat family of zero-dimensional complete intersections parameterized by T and then specializing its length. Rather, it records the order with which the restriction of the F-symbol to the distinguished section S_Q vanishes at the point
\[
P=T\cap S_Q.
\]

Thus c_T and M_T are two measurements of the same first-blowup geometry but in different directions:

- c_T: generic transverse intersection of D and D' along T;
- M_T: tangency/vanishing of the F-symbol along S_Q at T cap S_Q.

Ordinary upper semicontinuity of fiber length does not compare them.

## 3. Why a naive local trivialization is misleading

In a local trivialization of E over an open subset of C, write a section as
\[
[1:\lambda(t)].
\]
Then S_Q is [1:0]. A different constant graph [1:\lambda_0] with nonzero constant lambda_0 does not meet S_Q inside that trivializing open set.

The actual intersection T cap S_Q therefore depends on the global ruled-surface geometry and on transition functions. It cannot be modeled correctly by declaring both T and S_Q to be coordinate axes in one product chart over all of C.

This is precisely why modifications concentrated at P can alter M_T without altering the generic germ along T and hence without altering c_T.

## 4. No semicontinuity inequality

There is therefore no legitimate argument of the form
\[
M_T\le c_T
\]
or
\[
c_T\ge\Phi(M_T)
\]
coming merely from upper semicontinuity of local complete-intersection length.

Such an inequality would require an additional global divisor/line-bundle relation controlling how T approaches S_Q.

This strengthens the earlier root-budget separation result: even after placing both invariants on the first blowup, they are not fibers of one finite flat length function.

## 5. The correct coupling datum

The first place a genuine relation can occur is the divisor theory of the ruled surface E itself.

One should compute:
1. the divisor classes of T and S_Q in Pic(E);
2. their intersection number T.S_Q;
3. the divisor of the restriction of the first normal form f_p to S_Q;
4. how the common-factor divisor sum c_j T_j sits relative to S_Q;
5. whether the equality u=0 forces a relation among local intersection multiplicities
   \[
   I_P(T_j,S_Q),
   \]
   the root multiplicities M_j, and the section coefficients c_j.

This is a global ruled-surface calculation, not a local semicontinuity calculation.

## 6. Immediate next target

Use the known identifications
\[
E\simeq P^1\times P^1,\qquad
H|_E=O_E(4,0),\qquad
E|_E=O_E(7,-1)
\]
to identify the exact classes of:
- constant horizontal sections T_j;
- the quadric-direction section S_Q.

Then compute T_j.S_Q and the restriction of D|_E and D'|_E to S_Q.

This should determine whether the repeated-root multiplicities are already encoded by the intersection divisor
\[
W|_{S_Q}
\]
and, crucially, whether the coefficients c_j enter that divisor or disappear after restriction.


---

## Source: 2026-10-07-thick-generic-normalization-filter.md

# Entirely-thick branch: generic normalization valuation filter

Date: 2026-10-07
Status: EXACT LOCAL NECESSARY CONDITION / NO GLOBAL EXCLUSION

## 1. Why no carrier-specific APic computation was made

The current frontier does not contain a surviving explicit integral nonnormal carrier with normalization data sufficient for a Pic/APic lattice computation.

The retained cubic pinch-surface normalization is a control example already excluded because the full inverse image of C contains an isolated point. The normal quartic B1/B2/B3/D frontier has trivial normalization and is a different problem.

Therefore introducing an ad hoc nonnormal carrier would not advance the audited STCI frontier.

## 2. Generic local setup

Let X be an integral surface carrier containing C and let
    nu:S -> X
be its normalization. At the generic point eta of C, let Gamma_1,...,Gamma_t be the height-one points of S lying over eta. Their DVR valuations are v_1,...,v_t.

For a mate g whose reduced common zero set with X is C, the pullback of g to S has divisor along the branches
    div_S(g) = sum_j n_j Gamma_j + B,
where n_j=v_j(g)>0 and B has no component mapping dominantly to C.

If the mate has no additional common curve on X, any component of B relevant over the carrier must be excluded by the global support condition. In the clean situation the divisor supported over C is therefore
    A_g=sum_j n_j Gamma_j.

This is an effective Cartier divisor because it is locally principal, cut by the pulled-back mate.

## 3. Hyperplane relation

If g has ambient degree b, then on S
    O_S(div(g)) = O_S(bH).
Hence whenever the full zero divisor on the carrier is supported over C,
    sum_j n_j [Gamma_j] = b[H]
in Pic(S), or in the appropriate divisor class group if S is not smooth.

Thus the branch valuation vector
    n(g)=(v_1(g),...,v_t(g))
must lie in the positive integral kernel of the quotient map
    Z^t -> Pic(S)/<H>,
    e_j |-> [Gamma_j].

This is the generic normalization valuation filter.

## 4. Relation to Rees data

The Rees valuations of the pair ideal (f,g) in the ambient transverse two-dimensional regular local ring are not automatically the same as the branch valuations v_j on the normalization of the single carrier X=(f=0).

However, once a carrier f is fixed, the valuations v_j(g) are generator-sensitive data naturally visible in any resolution/normalized blowup dominating the normalization of X.

Therefore the correct bridge is not
    section coefficient c_i = branch coefficient n_j,
which has not been proved,
but rather:
    resolve the fixed carrier -> identify divisors/branches dominating C -> read v_j(g) -> impose the Pic/APic lattice relation.

## 5. Local APic contribution

When X is nonnormal along C, the class of a divisor supported on C is more naturally an almost-Cartier class. Hartshorne-Polini's normalization framework relates APic(X) to Pic(S) and local data along the conductor/singular locus.

Accordingly the full filter has two layers:

1. global normalization condition:
       sum n_j[Gamma_j] belongs to <H> in Pic(S);
2. local gluing condition:
       the associated local APic/conductor class is compatible with descent.

In the special case where all nonnormality is supported on C and only existence of some mate degree is sought, the repository's conductor-power theorem shows that sufficiently high powers remove the separate descent obstruction once the required Cartier support and hyperplane relation upstairs exist.

## 6. Immediate corollaries

For a fixed carrier:

- If no positive vector n has sum n_j Gamma_j proportional to H, the carrier is excluded for every mate degree.
- If the solution cone is one-dimensional, all mate branch multiplicities have a fixed rational ratio.
- If the solution monoid is finitely generated, comparison with possible valuation vectors becomes a finite semigroup problem.
- An isolated point in the full inverse image remains an immediate exclusion before this lattice calculation.

## 7. What this says about the entirely-thick program

The generic Rees/cluster invariant becomes useful only after fixing enough geometry of one carrier to map its valuations to normalization branches.

Thus there is no carrier-independent APic inequality analogous to the first-blowup inequality presently justified.

The next effective use of APic should occur when an explicit nonnormal carrier survivor emerges from the split/thick classification. At that point the normalization lattice test should be applied immediately rather than after a long local jet analysis.

## 8. Literature boundary

Hartshorne and Polini's divisor-class-group work already provides the general APic-via-normalization framework and applies it to STCI questions. The generic valuation filter above is a direct specialization/repackaging of standard divisor pullback plus the repository's conductor criterion; no novelty is claimed.

The project-specific open problem is to identify the coefficient vectors forced by the entirely-thick carrier geometry and show that they miss the admissible Pic/APic lattice for a nontrivial carrier family.


---

## Source: 2026-10-07-thick-local-pair-marked-trisecant.md

# Entirely-thick boundary: local pair model at a marked trisecant point

Date: 2026-10-07
Status: NEGATIVE LOCAL RESULT

Let L be a repeated trisecant ruling component of the residual divisor R_F on Q, and let P be one point of the degree-three divisor Z_L=C cap L.

This note asks whether retaining simultaneously
- the multiplicity M of L in R_F,
- the marked point P,
- the mate restriction on L,
- and the ambient Q-transverse coefficient
creates a local compatibility condition not visible in the earlier reduced-line analysis.

It does not, from reduced support alone.

## 1. Correct transverse local coordinates on Q

Since L and C meet transversely at a reduced point P in the generic trisecant case, choose regular parameters (u,y) on Q at P such that
\[
L=(u=0),\qquad C=(y=0).
\]

If L occurs with multiplicity M in R_F, then after removing units and residual factors not passing through P,
\[
F|_Q=y^p u^M\cdot \text{unit}.
\]

Write
\[
G|_Q=y^q R_G(u,y).
\]

## 2. What the support condition says

Along the reduced line L, the residual mate is
\[
R_G|_L=R_G(0,y).
\]

Suppose the exponent assigned to P in the divisor of R_G|_L is e. Locally the STCI support condition says only
\[
R_G(0,y)=y^e v(y),
\qquad v(0)\ne0.
\]

Globally on L, the three exponents e_1,e_2,e_3 at the points of C cap L satisfy
\[
e_1+e_2+e_3=q.
\]

Locally at P there is no further condition on the expansion
\[
R_G(u,y)
=
y^e v(y)
+uA_1(y)+u^2A_2(y)+\cdots.
\]

Thus all derivatives normal to L inside Q remain free, exactly as in the previous thickened-fiber countermodel.

## 3. Adding the ambient normal direction

Choose an ambient parameter z with Q=(z=0). Then locally one may write
\[
F=y^p u^M U + zA,
\]
and
\[
G=y^qR_G(u,y)+zB
\]
after choosing representatives, with U a unit in the displayed leading term.

The coefficient A is the transverse smoothing datum supplied globally by the Q-divisible kernel in the degree-3p recursion. Away from C it need not vanish along L.

The reduced common-support condition does not impose a relation between A and the coefficients A_j(y) in the u-expansion of R_G. If F is transversely smooth because A is a unit, the equation F=0 can locally eliminate z; substituting into G changes higher-order terms but does not alter the basic fact that extra reduced common points on L are governed by R_G(0,y).

Hence the ambient transverse coefficient does not rescue a local marked-point jet obstruction.

## 4. Three marked points do not change the local conclusion

For a generic trisecant
\[
C\cap L=P_1+P_2+P_3.
\]
The only global coupling visible on the reduced line is the degree condition
\[
e_1+e_2+e_3=q.
\]

For any fixed exponent triple, the earlier ruling interpolation audit proves that such reduced restrictions can be prescribed independently on all relevant distinct ruling fibers. The local expansions normal to each L remain unconstrained by reduced support.

Therefore keeping all three marked points still does not produce a new local compatibility equation.

## 5. Consequence

The smallest model containing
- repeated-root multiplicity M,
- the three marked points,
- mate zero allocation (e_1,e_2,e_3),
- and the Q-transverse smoothing coefficient of F
still has arbitrary higher local coefficients compatible with the reduced STCI support condition.

So the obstruction cannot be purely local at one trisecant line if it uses only reduced support.

## 6. What information is still missing

A surviving obstruction must import scheme-theoretic information that reduced support forgets. The candidates are now sharply narrowed to:

1. the actual complete-intersection multiplicity/Noether cluster of (F,G) over C;
2. variation and proximity of that cluster as the point of C moves;
3. a global divisor relation on successive exceptional surfaces;
4. normalization/conductor data of an actual carrier;
5. a relation imposed by the fact that F and G are global homogeneous equations, beyond their separately flexible restrictions.

The first item is the most immediate: compute the local pair ideal at P after the first blowup, retaining simultaneously the horizontal section T corresponding to L and the special point Ptilde=T cap S_Q. This is the first place where generic-along-T multiplicity and marked-point degeneration coexist in one two-dimensional family.


---

## Source: 2026-10-07-thick-marked-point-jets.md

# Entirely-thick (3,4) boundary: marked-point jets versus section budgets

Date: 2026-10-07
Status: PROVED separation of invariants / OPEN coupling problem

## 1. Two different invariants

On the first exceptional surface E, fix a constant common section T and let P=T intersect S_Q, where S_Q is the quadric-direction section.

Let r=ord_T(D|E). This is a divisorial multiplicity: it records whether the entire section T is a component of the first exceptional divisor and with what multiplicity.

Let M_T be the multiplicity at the corresponding ruling root of the residual binary form R_F. Equivalently, M_T is a vanishing order at the marked point P of the restriction of the p-th normal form to S_Q.

These are different kinds of data:
- r is generic along T;
- M_T is a jet order at one point P on the transverse moving section S_Q.

There is no formal inequality r >= M_T.

## 2. Local countermodel to naive coupling

Use regular local coordinates (x,z) on E near P with S_Q=(z=0) and T transverse to S_Q. A function
    A=z+x^M
has restriction
    A|S_Q=x^M,
so its marked-point restriction has order M, while A is not divisible by a local equation of T for a suitable transverse choice of T.

Thus arbitrarily high marked-point vanishing can occur without high divisorial multiplicity along T.

Therefore the hoped-for route
    M_T large => r large => c_T large
is invalid without additional global structure.

## 3. Consequence for the repeated-root argument

The audited repeated-root theorem remains useful, but only as a marked-point jet constraint:
    sum_T M_T = 2p,
with at most min(p,q) marked points.

It cannot by itself be inserted into the sectionwise Noether budget
    sum_T c_T = 2pq.

Any inequality c_T >= Phi(M_T,...) must use information beyond local smooth-surface intersection theory.

## 4. Where coupling can come from

The quadric Q supplies extra global structure. The marked point P is not arbitrary: it is the intersection of T with S_Q, and the residual ruling line associated to P is globally contained in V(F). The STCI condition then forces all zeros of G on that ruling line back onto C.

Hence the promising object is not M_T alone, but the restriction of G (and possibly higher transforms of F,G) to the corresponding ruling line L_T subset Q.

For a root of multiplicity M_T in R_F, F|Q contains L_T with multiplicity M_T in the residual factor. Meanwhile
    G|L_T = (h|L_T)^q (R_G|L_T)
and R_G|L_T is a degree-q section whose zeros must all lie at L_T intersect C. Since that intersection is a single point with multiplicity three for the trisecant ruling convention, the support condition forces R_G|L_T to be supported at that same point.

This converts the earlier existence-of-a-zero argument into a stronger one-variable restriction problem.

## 5. Next exact question

Determine the possible section R_G|L_T in H^0(L_T,O(q)) under the condition that every zero is supported at P=L_T intersect C.

Over an algebraically closed field this forces
    R_G|L_T = lambda * ell_P^q
for some nonzero scalar lambda,
unless R_G|L_T is identically zero.

Thus on every ruling component L_T of R_F, the mate residual restricts to a pure q-th power at the distinguished point.

This is a substantial sharpening of the existing repeated-root statement.

## 6. New target

Exploit the simultaneous conditions
    R_F = product_i L_i^{M_i},  sum M_i=2p,
and
    R_G|L_i = lambda_i ell_{P_i}^q  or 0
for at most min(p,q) distinct ruling lines L_i.

Since R_G has bidegree (3q,q), these pure-power restrictions are interpolation conditions on a single global section of O_Q(3q,q).

The next calculation is therefore finite-dimensional and global on Q:
compute the codimension/rank of the restriction map from H^0(O_Q(3q,q)) to the jets on the selected ruling lines, allowing the zero restriction case, and compare it with the freedom in choosing the roots of R_F.

This reconnects the entirely-thick branch to the project's jet-condition/discrepancy framework.


---

## Source: 2026-10-07-thick-quadric-section-divisor.md

# Entirely-thick boundary: quadric section and exceptional intersection divisor

Date: 2026-10-07
Status: PROVED CLASS CALCULATION / IDENTIFICATION ISSUE FLAGGED

On the first blowup B=Bl_C P3 let E be the exceptional surface. Use the established convention
\[
E\simeq P^1\times P^1,\qquad
H|_E=O_E(4,0),\qquad
E|_E=O_E(7,-1).
\]

## 1. Class of the quadric-direction section

The strict transform of the unique quadric is
\[
\widetilde Q=2H-E.
\]
Hence its intersection with E is
\[
S_Q=\widetilde Q|_E=(2H-E)|_E.
\]
Therefore
\[
[S_Q]=(8,0)-(7,-1)=(1,1).
\]

So
\[
\boxed{S_Q=(1,1).}
\]

At the (3,4) boundary the horizontal components T_j of W have class
\[
[T_j]=(0,1).
\]
Using the P1xP1 intersection form,
\[
T_j.S_Q=(0,1).(1,1)=1.
\]
Thus every T_j meets S_Q in one reduced point when the intersection is transverse, and in total intersection multiplicity one in all cases.

## 2. Restriction of W to S_Q

At the boundary
\[
W=D.D'=\sum_jc_jT_j,
\qquad
\sum_jc_j=2pq.
\]
Therefore as an intersection divisor on S_Q,
\[
W|_{S_Q}=\sum_j c_jP_j,
\qquad P_j=T_j\cap S_Q,
\]
and
\[
\deg(W|_{S_Q})=2pq.
\]

This is the first natural divisor on the marked section that retains the sectionwise coefficients c_j.

## 3. Restricting the two exceptional divisors

At the boundary
\[
D|_E=(5p,p),\qquad D'|_E=(9q,q).
\]
Since S_Q=(1,1), their degrees on S_Q are
\[
D.S_Q=5p+p=6p,
\qquad
D'.S_Q=9q+q=10q.
\]

These degrees are not the residual-root degrees 2p and the mate fiber degree q. They include the full first-normal divisors on E, not merely their restrictions after removing the contribution associated with C on Q.

Thus one must not identify D|S_Q directly with R_F or D'|S_Q directly with R_G without accounting for the relevant line-bundle identifications and fixed factors.

## 4. Important coordinate issue

A root of
\[
R_F\in H^0(Q,O_Q(2p,0))
\]
selects a trisecant ruling fiber L in Q. That fiber meets C in a degree-three divisor.

By contrast a horizontal exceptional section T_j meets S_Q in one point P_j.

Therefore the statement “a ruling root corresponds to P_j” requires an explicit map between:
- the ruling-base P1 parameterizing trisecant fibers of Q;
- the base C=P1 of the exceptional bundle E;
- and the graph S_Q=(1,1).

For C=(1,3), the projection from C to the trisecant-ruling base has degree three. Hence a generic ruling root has three preimages on C.

This must be reconciled with the one-point intersection T_j cap S_Q before comparing
\[
\sum c_jP_j
\]
with the repeated-root divisor of R_F.

## 5. Consequence

The divisor W|S_Q is well-defined and retains the c_j coefficients, but a direct coefficient comparison c_j versus M_j is not yet justified.

The next calculation must write the explicit Segre parametrization
\[
C=[s^4:s^3t:st^3:t^4]
\]
as a (1,3)-curve on Q, identify both ruling projections, and identify the exceptional P1xP1 coordinates used in
\[
H|_E=(4,0),\qquad E|_E=(7,-1).
\]

Only after this coordinate dictionary is fixed can one decide whether a root of R_F gives one horizontal section, three marked points, or a ramified combination in W|S_Q.

This is a potentially important consistency check on the existing equality-root argument.

