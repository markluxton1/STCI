# Marked CI arrangements, forgetful reconstruction and compactifications

**Status:** exact open-locus calculation for reduced (4,4) arrangements; proposed compactification and general-degree program, not a proof of flat extension or an unrestricted STCI obstruction. Preserve all arrangement labels symmetrically; do not translate any marked component to the fixed quartic. Work over an algebraically closed field of characteristic zero.

## Established input and the visible-contour analogy

The [reduced-cycle realization criterion](../equations/chow_polytope_rigidity.md#realization-of-a-reduced-chow-matched-cycle) and [dual-line reformulation](arrangement_endpoint_delta.md) supply the actual eigenquartic generators. Kapranov, [*Chow quotients of Grassmannians I*](https://arxiv.org/abs/alg-geom/9210002), constructs visible contours by intersecting universal torus orbit closures with the sub-Grassmannian of planes containing a fixed vector. Keel–Tevelev, [*Geometry of Chow quotients of Grassmannians*](https://people.math.umass.edu/~tevelev/chow.pdf), §2.11, describes the flat family and Hilbert embedding. Hacking–Keel–Tevelev, [*Compactification of the moduli space of hyperplane arrangements*](https://arxiv.org/abs/math/0501227), supplies the stable-pair interpretation. This is a model for a construction, not a theorem that our incidence spaces are their Chow quotients.

The precise forgetful precedent is Schaffler–Tevelev, [*Compactifications of moduli of points and lines in the projective plane*](https://doi.org/10.1093/imrn/rnab200), Corollary 3.5: for the Grassmannian Chow quotients X(r,n), r>=2 and n>=r+2, the product of forgetful morphisms to X(r,I), |I|=r+2, is finite birational onto its image. For stable rational curves, cross ratios containing one fixed label already give a closed embedding (Aguirre–Felder–Veselov, [*Gaudin subalgebras and stable rational curves*](https://arxiv.org/abs/1004.3253), Theorem A.2, building on Gerritzen–Herrlich–van der Put). These are statements about recovering an object and compatible cross-ratio data; they do not imply that an arbitrary subvariety is cut out by the pullbacks of the images of its forgetful maps.

## 1. General configuration incidence

Let T=(G_m)^2 denote the transverse quotient torus with coordinates (u,v), and C_(u,v)=[s^4:s^3t:u st^3:v t^4]. For ordered distinct points Z in Conf_m(T), let A_Z be their reduced union, m=ab/4. Set S_d=H^0(P^3,O(d)), with weight spaces S_(d,w) for intrinsic coordinate weights (0,1,3,4). Each weight space restricts to a Laurent monomial system on T after removal of the common orbit-coordinate power. Evaluation on Z gives a matrix E_(d,w) and
K_d(Z)=H^0(I_(A_Z)(d))=direct sum_w ker E_(d,w).
On fixed-rank strata its row spaces and kernels define maps to Grassmannians equivariant under simultaneous translation of all parameters. Plücker supports may organize their degenerations, but no literal Kapranov visible contour or flat boundary family has been constructed.

For a<b a reduced CI arrangement necessarily has dim K_a=1, dim K_b=dim S_(b-a)+1, and its second generator is the unique line K_b/(F S_(b-a)); for a=b=d its defining pencil is K_d of dimension two. Conversely these dimension conditions plus coprimality give the CI by degree exhaustion. Thus there is a determinantal and open properness description on the distinct-configuration space. All labels remain symmetric under S_m. The reduced locus is special, not the complement of just the big diagonal.

## 2. The full ordered reduced (4,4) model, including constant-v carriers

Use the unique weight-four generator and weight-twelve generator of the pencil (up to scalar), as supplied by the existing eigenform theorem. After normalizing their nonzero coefficients, the dense quotient equations are
\[
 v=A+Bu,\quad u^4+euv^2+fv^3=0,
 \qquad A,f\ne0.
\]
Here B,e are arbitrary. A,B specify the carrier line, and e,f specify the mate; the four roots must be distinct. The absence of additional projective support and properness are the existing dual-line criterion. The carrier line is determined by any two arrangements since their u coordinates are distinct.

A useful **uniform** coordinate on the carrier is
\[
 q=u/v,\qquad u=Aq/(1-Bq),\qquad v=A/(1-Bq).
\]
It does not require B nonzero. The allowed marks satisfy q_i != 0 and 1-Bq_i !=0, and are distinct. The mate equation becomes the monic polynomial
\[
 P(q)=q^4+(e q+f)(1-Bq)/A.
\]
Writing e_j for the elementary symmetric polynomials in the four q_i, existence of the mate is exactly
\[
 \boxed{e_1=0,\qquad R:=e_2-B e_3+B^2 e_4=0.}
\]
Indeed comparing coefficients gives e/A=-e_3+B e_4 and f/A=e_4. The latter is nonzero since every q_i is nonzero. Conversely these formulas produce the unique mate. Thus the reduced ordered locus is explicitly the open subset of this two-equation family in coordinates (A,B,q_1,...,q_4), A nonzero, with all q_i, 1-Bq_i, q_i-q_j invertible. This includes B=0, where e_1=e_2=0. Its unreduced root polynomial completion, allowing repeated marks, still gives invariant CI pairs provided nonzero/boundary conditions hold (multiplicity partition retained).

On B nonzero introduce t=Bu/A and x=1/(1+t)=1-Bq=A/v. The three boundary marks in t are 0,-1,infinity; in x they are 1,infinity,0 respectively. The marked smooth carrier is a seven-pointed P^1. The two equations above become
\[
 \boxed{\sum_i x_i=4,\qquad \prod_i x_i=1.}
\]
Equivalently the monic t-root polynomial satisfies P_t(t) congruent to t^4 modulo (t+1)^2, i.e. P_t(-1)=1, P_t'(-1)=-4. The framed open space is the product (G_m)^2_(A,B) times the two-dimensional marked locus V_4 in M_(0,7), given by these equations on four distinct x_i in P^1 minus {0,1,infinity}. No arrangement mark is singled out. The B=0 chart has only two distinct boundary points; the three-point normalization is not valid there, whereas q and the uniform equations remain valid.

## 3. Forgetful maps and determination by their images

Let a labeled triple of q coordinates have elementary symmetric functions s,p,h (of degrees 1,2,3). The unique possible fourth mark is r=-s, from e_1=0. Substitution into R gives
\[
 \boxed{(1+Bs)(p-Bh)=s^2.}
\]
The admissible triple locus additionally requires r nonzero, 1-Br nonzero, and r distinct from the retained marks, as well as the original triple open conditions. This is exactly the image of forgetting any one label; the forgetful map is an isomorphism onto it, with regular inverse (A,B,q_i) -> (A,B,q_i,r). In original T coordinates the triple determines its carrier A,B, so no auxiliary framing choice is needed. The targets are **extendible triples of the (4,4) problem**, not (3,4) CI arrangements.

Stronger: on the ambient ordered distinct-point space, a quadruple is realizable if and only if its subtriples obtained by forgetting any TWO different labels are both extendible triples. The two triples overlap in two distinct points, so their unique affine carrier lines coincide. Work in the resulting common (A,B,q) coordinates. Let S=sum q_i and R above be calculated on the actual quadruple. For omitted label i, replacing q_i by q_i-S yields the only candidate completion, so its extendibility implies
\[
 R=S L_i,\qquad
 L_i=\sum_{k\ne i}q_k-B\sum_{k<l;\ k,l\ne i}q_kq_l+
 B^2\prod_{k\ne i}q_k.
\]
For i != j, the difference is
\[
 L_i-L_j=(q_j-q_i)\prod_{k\ne i,j}(1-B q_k),
\]
a unit on the distinct allowed carrier locus. Subtracting the two equations forces S=R=0. This also proves ideal equality on the carrier-coordinate open, since the differences are units. The converse follows by deleting any mark of a realized arrangement. Consequently the full symmetric family of four forgetful maps determines the locus; in fact any two pullbacks suffice (with the stated admissibility opens). On the normalized B nonzero chart this is especially simple: if a triple of x's has product P and sum S_3, its completion is 1/P and its extendibility equation is S_3+1/P=4. With all four x's present, write p_all=product x_i, s_all=sum x_i. The equation from omitting i is s_all-4+x_i(1/p_all-1)=0. Two different omissions give p_all=1 and s_all=4.

**Geometric proof and two-mark reconstruction.** There is a simpler
reason for the triple-image criterion that exposes its generalization
mechanism. The two weight-space embeddings are
\[
 T\longrightarrow\mathbf P^2,\quad (u,v)\mapsto[1:u:v],
 \qquad
 T\longrightarrow\mathbf P^2,\quad (u,v)\mapsto[1:v^2/u^3:v^3/u^4].
\]
The latter is injective on the torus since the character transformation
has determinant \(-1\). Two distinct arrangement marks therefore
determine a unique line in each plane, hence the two weight generators
up to scalar. If two overlapping triples admit proper reduced quartic
completions, their common two points force *the same* generators.
Their union is consequently contained in that same degree-16 complete
intersection, and exhausts its four components. This proves the
two-triple criterion directly, without the symmetric-polynomial
calculation. It also explains why the pair projection has two ordered
completions on its image: the two retained marks determine the entire
pencil and the unordered complementary pair. On the open coefficient
locus of proper eigenquartic pairs with four distinct quotient roots,
the ordered configuration space is the finite étale cover of all
orderings of the four roots. One candidate framed compactification is
the closure of its graph over
\(\mathbf P(S_{4,4})\times\mathbf P(S_{4,12})\cong\mathbf P^2\times\mathbf P^2\),
in combination with the stable marked carrier and Hilbert spaces.
The ability of two marks to determine the relevant hyperplanes, rather
than the specific quartic root formulas, is the potential general-degree
mechanism.

By contrast, on the normalized x chart forgetting two marks has dense image in the space of admissible ordered pairs: the remaining marks are the two roots of
\[
 z^2-(4-x_1-x_2)z+1/(x_1x_2)=0.
\]
For a general pair these roots are distinct, avoid 0,1 and are distinct from the retained marks, giving two ordered completions. (For example over Q take x_1=2,x_2=3.) Thus pair-image conditions cannot define the original surface as a closed locus on the distinct open; it is the triple compatibility that encodes the two constraints. This is not the same as saying cross ratios of the full configuration cannot recover it.

## 4. Three candidate compactifications and an established compactification result

* Ambient: for a smooth projective toric refinement S of the normalized orbit Chow quotient, Hilb^m(S) is a smooth projective compactification of the unordered distinct configurations with a universal finite flat scheme. After extending the finitely many weightwise monomial maps by toric refinement, the line bundles L_(d,w) give tautological evaluation maps S_(d,w) tensor O -> L_(d,w)^[m]. Their rank loci extend the evaluation conditions but may have extra boundary components. Take the closure of the actual coprime locus, not every component of the rank locus. The nested Hilbert scheme S^[m,m+1] is the blow-up of S^[m] x S along its universal length-m scheme (Ellingsrud–Strømme; see [Addington, §3.1](https://content.algebraicgeometry.nl/2016-2/2016-2-011.pdf)). This supplies an add-one-point correspondence, not a canonical deletion of an individual labeling at a collision.
* Ordered: [Fulton–MacPherson](https://annals.math.princeton.edu/1994/139-1/p06) S[m] retains labels and expanded fibers, with marking sections and forgetful morphisms. Compare with a universal marked carrier family and with the Hilbert scheme by closing the graph of the simultaneous data. No claim of a canonical morphism between these compactifications or of preserved flat CI fibers.
* Carrier-adapted: for a designated weight system, take the universal divisor curve D_F in S over its projective space of sections and the relative Hilbert scheme of length-m subschemes on it; impose the mate evaluation, properness and degree exhaustion on the appropriate open. For smooth carriers, ordered markings are sections of the pulled-back universal curve. This is the closest analog of visible contours; a canonical compactification with stable marked families or correct limiting equation spaces is the unresolved task.

For a concrete first compactification of the B nonzero **abstract** quartic marked locus, let W_4 be the scheme-theoretic closure of V_4 in the stable-curve space Mbar_(0,7). It is projective and inherits a stable seven-pointed universal curve with sections, with S_4 symmetry. Write W_(3,i) for the closure of the image of V_4 in Mbar_(0,6) under forgetting root i. Each deletion extends as a morphism W_4 -> W_(3,i).

In fact the product of these four extended maps is a **closed embedding**. By Aguirre–Felder–Veselov Thm A.2, the cross ratios containing any one fixed boundary label already embed Mbar_(0,7). Every such cross ratio uses at most three root labels, and hence factors through at least one of the four deletion maps. The product of deletions therefore embeds the ambient Mbar_(0,7), and restricts to an embedding of W_4 in the product of its forgetful images. This resolves the recovery question for this compactification using existing theory. It does **not** prove that W_4 equals the intersection of inverse images of W_(3,i) in Mbar_(0,7): extra boundary components may appear, and compatibility/closure equations are the next problem. The embedding also does not retain A,B or the embedded quotient torus; an additional framed compactification is required for the full realization locus and its blow-ups. One may take the graph closure of the simultaneous maps into marked-curve, framed carrier, Hilbert and equation spaces, then compare boundary fibers. The B=0 stratum must be included separately or via degeneration of the boundary markings; the normalized x model alone cannot be used as a compactification of the entire ordered realization space.

## 5. Second solved carrier, and general induction target

The [fixed quartic carrier theorem](fixed_carrier_chow_arrangements.md) provides another model: N nonzero roots on P^1 minus {0,infinity}, with e_1=e_2=e_5=0 (omit e_5 for N<5). For N=3,4 or N>=6, forgetting one root r gives r=-e_1(triple/general remaining multiset); the other constraints become e_2=e_1^2 and e_5=e_1 e_4 when applicable. Losev–Manin spaces (two heavy boundary marks and light root marks) offer a natural ordered compactification, retaining the overall scale separately. These are extendible (N-1)-point configurations, not CI arrangements in a lower bidegree. The degree-five obstruction follows from the e_5 equation and forbidden zero root.

The common direction is to characterize mate linear systems as constraints on finite divisors on moving quotient carriers, including boundary jets or conductor conditions where available, then analyze the images of each forgetful map and their compatibility. For general a,b the kernel maps supply exact incidence conditions, but neither smooth rational carriers nor unique reconstruction after deleting a point are automatic. The existing [trace-moment theorem](chow_arrangement_moments.md) excludes full coalescence in characteristic zero for the reduced CI closure, so the general non-invariant repeated-cycle STCI problem is outside this program's established coverage.

**Auxiliary quartic question:** determine the stable boundary of W_4 and whether its forgetful-image pullbacks introduce spurious components, if it helps illuminate the intrinsic arrangement compactification. It is not a prerequisite for the general-degree construction. The present note proves open reconstruction and compactified abstract recovery, not boundary-image sufficiency or a new STCI exclusion.



## 6. The quartic marked-root surface is a known mirror quartic K3 model

This is an **auxiliary model of the realization locus** on \(B\ne0\), not the ambient compactification of arrangements. In the coordinates \(\xi_i=1-Bq_i=A/v_i\), the normalized root equations read
\[
 \sum_{i=1}^4\xi_i=4,\qquad \prod_{i=1}^4\xi_i=1.
\]
Let \(\mathcal V_4\) be the open locus where \(\xi_i\) are distinct and avoid \(0,1,\infty\). Its projective model is
\[
 X:\quad (X_1+X_2+X_3+X_4)^4=256X_1X_2X_3X_4
 \quad\subset\mathbf P^3.
\]
Indeed normalize the nonzero sum to 4, giving the displayed affine equations. The precise open complement excludes the hyperplanes \(\sum X_i=0\), \(X_i=0\), \(4X_i=\sum X_j\) and \(X_i=X_j\).

This is the \(t=1\) quotient member of the Dwork mirror quartic pencil: the quotient of \(\sum Z_i^4=4t\prod Z_i\) by the product-one diagonal fourth-root group modulo scalar has equations \(\sum X_i=4t W\), \(\prod X_i=W^4\). See Heinrich Hartmann, [*Period- and mirror-maps for the quartic K3*](https://arxiv.org/abs/1101.4601), §4.1 and Proposition 4.1. Its six \(A_3\) points are the permutations of \([0:0:1:-1]\), and the additional \(A_1\) is \([1:1:1:1]\). Its minimal resolution is a K3 surface (adjunction, rational double points and \(H^1(\mathcal O_X)=0\)). Over \(\mathbb C\) the 19 exceptional classes and pullback of the hyperplane class are independent, hence its Picard number is 20. These are established K3 facts; the identification with our root equations is the application.

The three carrier-boundary labels and four arrangement labels play different roles. In particular the following maps are more intrinsic to the configuration problem than treating all seven marks symmetrically.

**Forget the boundary marks 0 and 1, retain infinity.** The four affine points are now considered modulo affine transformations. Write their centered homogeneous coordinates \(y_i\) with \(\sum y_i=0\); the distinct open in \(\mathbf P(\sum y_i=0)\cong\mathbf P^2\) is \(M_{0,5}\) with infinity the fifth label. Lift the configuration back by \(\xi_i=1+\ell y_i\), \(\ell\ne0\). The boundary label 1 is canonically the centroid, and the product constraint gives
\[
 e_4(y)\ell^2+e_3(y)\ell+e_2(y)=0.
\]
For a general configuration this has two admissible roots; the map from \(\mathcal V_4\) is generically degree two. Geometrically this is projection of \(X\) from its node. The discriminant is \(e_3(y)^2-4e_2(y)e_4(y)\). In the linear coordinates
\[
 (y_1,y_2,y_3,y_4)
 =(a+b+c,\ a-b-c,\ -a+b-c,\ -a-b+c)
\]
it equals
\[
 8(a^2-b^2-c^2)(b^2-a^2-c^2)(c^2-a^2-b^2).
\]
Thus a birational model is a double plane branched on three conics (not necessarily a smooth double plane; resolve its singularities). This uses characteristic zero. The double cover corresponds to possible positions of the forgotten boundary label 0 relative to the centered affine configuration, not to two possible CI pencils for a fixed framed arrangement.

**Forget all three boundary labels.** One cross ratio of the four arrangement points is
\[
 \lambda=\frac{(y_1-y_3)(y_2-y_4)}{(y_1-y_4)(y_2-y_3)}
        =\frac{a^2-c^2}{a^2-b^2}.
\]
For general \(\lambda\), the cross-ratio fiber in the plane is the smooth conic \((1-\lambda)a^2+\lambda b^2-c^2=0\). It meets each branch conic in four distinct points, with no common intersection between the three sets for general \(\lambda\): solve the two linear equations in \(a^2,b^2,c^2\), whose resulting ratios are all nonzero away from finitely many \(\lambda\); mutual branch intersections occur only at special values. The normalized projective fiber upstairs is therefore a double cover of a conic ramified at 12 points, hence genus five. This is a rational fibration of the K3 model, not a product with a fixed genus-five curve. Over the open marked configuration space the map is a genuine forgetful morphism; the fiber compactification statement is birational. The quotient by \(S_4\) is rational because the monic root polynomial has coefficients \((e_2,e_3)\) free away from its discriminant and the condition \(P(1)\ne0\).

**Important distinction about collisions.** The nodal point \([1:1:1:1]\) is collision with boundary label 1 in this normalized carrier chart. With \(A,B\) fixed nonzero it means \(q_i=0\), i.e. it leaves the quotient torus \(T\). It is not the deepest diagonal of the original arrangement space at an interior point \(z\in T\). The two framing parameters and their degeneration cannot be omitted when comparing collision strata. The trace-moment separator, not the K3 compactification, excludes \(m[C_z]\) from the reduced CI closure.

The \(\overline M_{0,7}\) graph and its cross-ratio embedding in §4 remain useful for this particular carrier model, but are **secondary**. The primary compactification should be independent of the defining degrees and of the choice of carrier, retain the entire configuration and its subconfigurations, and only then select the CI loci. The following all-subsets model is one such proposed construction.

## 7. Arrangement-first compactification

Let \(S\) be a projective compactification of \(T\) mapping to the orbit Chow closure, such as the normalized Chow quotient in
[the fan calculation](chow_quotient_fan_and_blowup_comparison.md). Close the graph of the map from \(T\) to
\(\operatorname{Hilb}_{4d+1}(\mathbf P^3)\) over \(S\), and allow a projective
equivariant refinement \(S'\). This gives a projective parameter surface
with a universal single-curve family
\(\mathscr C\subset\mathbf P^3\times S'\). It retains the chosen Hilbert
polynomial \(4d+1\) for individual curves; it does not make the embedded
unions of varying arrangements flat.

For a finite label set \(J\), take the reduced closure
\[
 \mathcal X_J=\overline{\{(\{z_i:i\in I\})_{\varnothing\ne I\subseteq J}:
 (z_i)\in\operatorname{Conf}_J(T)\}}
 \subseteq\prod_{\varnothing\ne I\subseteq J}
       \operatorname{Hilb}^{|I|}(S').
\]
The singleton factors retain ordered positions; the full-set and other
subset factors retain limiting collision schemes. Projections to factors
indexed by subsets of \(K\subseteq J\) extend deletion to proper surjective
forgetful maps \(\mathcal X_J\to\mathcal X_K\); relabeling acts by the
symmetric group. On the distinct locus this model is the original ordered
configuration space. It is projective, but is not claimed minimal, smooth,
or identical to a Fulton–MacPherson compactification.

Each subset factor has a universal finite flat scheme
\(\mathscr Z_I\subset S'\times\mathcal X_J\). Pulling back the universal
single-curve family gives
\[
 \mathscr D_I=\mathscr C\times_{S'}\mathscr Z_I
 \longrightarrow\mathcal X_J,
 \qquad \mathscr D_I\longrightarrow\mathbf P^3\times\mathcal X_J.
\]
The source family is flat and projective and maps compatibly with subset
inclusions, relabeling, and forgetting. Its embedded image need not be flat:
on collision the image can acquire scheme structure, and scheme-theoretic
image does not automatically commute with base change. Thus this constructs
a compactified family of **maps from arrangements**, not a universal flat
family of embedded unions. To obtain embedded flat families, take closures
inside a common endpoint-rank/Hilbert-polynomial stratum (and its relevant
Hilbert scheme); compatibility with relative Rees blow-ups must be checked.

On the locus where \(\mathscr Z_J\subset T\), restriction of degree-\(d\)
equations is represented by
\[
 H^0(\mathbf P^3,\mathcal O(d))\otimes\mathcal O_{\mathcal X_J}
 \longrightarrow
 H^0(\mathbf P^1,\mathcal O(4d))\otimes
       p_*\mathcal O_{\mathscr Z_J},
\]
where \(p:\mathscr Z_J\to\mathcal X_J\) is finite flat. On distinct fibers
its kernel is the space of equations containing the reduced arrangement.
At collisions it records equations vanishing on this family of curves over
the finite scheme; it does not parametrize every embedded non-invariant
thickening. Across the toric boundary, extend monomial-weight evaluation
maps on a suitable refinement or use the flat single-curve family with
relative cohomology and base change where applicable. Ranks may jump, so
use rank strata or graph closures rather than presuming a vector bundle of
kernels. The reduced complete-intersection locus is the open properness
part of this incidence; it remains distinct from arbitrary non-invariant
repeated-cycle equation incidence.

The full-set Hilbert–Chow map followed by addition of single-curve cycles
gives a projective cycle map to the Chow variety. In characteristic zero,
the [Chow trace-moment theorem](chow_arrangement_moments.md) shows that the
closure of the reduced arrangement CI locus misses every interior full
collision cycle \(|J|[C_z]\), since its first moment there is
\(|J|u/v\ne0\). The theorem's stated eigenform-covered repeated-cycle
cases share this exclusion. This closure argument does not cover an arbitrary non-invariant proper CI supported on a repeated cycle outside the reduced-locus closure; other proved repeated-cycle cases have their own hypotheses in the [first-moment proof boundary](universal_first_moment_proof_boundary.md). The later provisional [marked configuration boundary](marked_chow_configuration_boundary.md) supplies a different four-pencil log-surface model on a generic distinct-marking open, and the [endpoint incidence systems](marked_chow_endpoint_incidence.md) recover the opposite-plane rank strata. Neither identifies the all-subsets compactification here with the stable extension of those pairs or with flat embedded CI limits.
Keep simultaneous translations and label permutations on the arrangement
model; an ambient \(\operatorname{PGL}_4\) quotient is a separate operation
and need not preserve the fixed-coordinate slice.
