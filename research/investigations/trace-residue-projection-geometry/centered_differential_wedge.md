# Centered differential wedge and endpoint divisibility

Exploratory calculation, pending independent review. Governing question is M_1 on the entire translated-cycle CI realization locus. No universal vanishing asserted. Inputs: [full endpoint response](full_endpoint_plane_response.md), [spectral Jacobian bridge](../../arguments/torus/spectral_jacobian_first_jet_bridge.md), [radical recovery](../../arguments/equations/jacobian_radical_support.md). Classical duality: adjunction for a projective CI, finite duality for the reduced immersion, and Rosenlicht's description of the dualizing sheaf of a reduced curve (see [Serre's exposition of regular differentials, discussed here](https://link.springer.com/article/10.1007/s11565-024-00495-8)). Work over algebraically closed characteristic-zero k.

Let E=k[z,x,y,w]/(F_a,G_b) for an actual proper translated-cycle CI with entire cycle sum n_i[C_(u_i,v_i)], m=sum n_i, ab=4m, q_i=u_i/v_i, M_1=sum n_i q_i, qbar=M_1/m. D_ij=F_i G_j-F_j G_i in ordered coordinates z,x,y,w. E is finite graded free over k[z,w]. Write d=a+b-2.

## Combining the two endpoint conditions

At infinity (w=1,z=0), Euler gives D03=-xD01-yD02=-xV+yU=2M_1 j, where j is the normalized socle of the endpoint Artinian CI. At zero (z=1,w=0), Euler gives D03=-xD13-yD23=xV-yU=2M_1 j. In both cases D12=ab j. Homogenization is exact in E/(z) and E/(w) by their freeness over k[w] and k[z], respectively. In particular
\[
 D_{03}-(\bar q/2)D_{12}\in zE\cap wE=zwE.
\]
The last equality follows from regularity of z,w (or graded freeness). Consequently there is a unique class K in E_(a+b-4) such that
\[
 D_{03}=(\bar q/2)D_{12}+zwK.
\]
Both minors belong to the annihilator of the nilradical by the generic mixed-minor/socle lemma and purity. Since zw is regular, K also belongs to it. The nonzero endpoint socle D12 shows that M_1=0 iff D03 is divisible by z, iff divisible by w, iff divisible by zw in E. The formula separates the mean spectral direction from its centered variation. Replacing the distinguished pencil coordinate by q-qbar depresses the spectrum, but is not a proof that its original geometrically marked coordinate is already centered. In particular it generally changes which member is marked zero.

## Interpretation as ordinary residue balance on the reduced arrangement

Let D=Y_red (all distinct translates). Finite duality for D->Y and CI adjunction give
\[
 \operatorname{Ann}_{O_Y}(I_{D/Y})\otimes O_Y(a+b-4)=\omega_D .
\]
Equivalently a socle section in degree a+b-4 represents a regular differential on D. To identify K's differential, use chart z=1, with finite projection w; relative residue identifies D12 with the weighted trace, or on each normalized reduced branch with n_i dw. The ratio D03/D12 on the generic socle of branch i is q_i/2 (not division by an invertible ring element). Thus K represents the tuple of differentials
\[
 \omega_i=2n_i(q_i-\bar q)\,dr/r
\]
on the normalizations, with r=t/s, and dw/w=4dr/r. Fix the adjunction sign using the indicated chart. The only poles are simple at the two shared endpoints. Rosenlicht regularity for simple poles is exactly cancellation of the residues at each point (all local regular functions have the same constant value on its branches). This is automatic for the centered tuple. The uncentered tuple 2n_i q_i dr/r is regular precisely if M_1=0. For a single component the centered differential is zero, as expected; this is a benchmark, not the subject of the investigation.

Thus the canonical centering identity is another exact expression of residue balance, not an independent restriction on the cycle. The actual CI content is the polynomial representative K in the specific socle module. The two mixed-minor tests have a parallel interpretation via double poles: at infinity in w=1, D02/z represents -3n_i dr/r^2 on branch r=s/t (since D02/D12=-dx/dz and relative residue identifies D12 with n_i dz). Vanishing of the Rosenlicht residue condition against a local function tests its common y-linear term, whose branch coefficients are q_i. At zero in z=1, D13/w represents -3n_i q_i dr/r^2 for r=t/s in the same relative convention, and the x-linear term tests M_1. Constant terms have zero residue and higher terms do not contribute. These tests recover the prior endpoint divisibilities without computing a plane algebra.

The lowest common normal factor of F,G divides the leading normal differential wedge, but may not determine the actual socle section: cancellation may move the first nonzero term to higher order. The current calculation has not shown that common normal factors enforce the uncentered balance. Future question: can the actual global normal forms force the distinguished projection component of the wedge to vanish at either endpoint section? Keep the full realization locus primary.
