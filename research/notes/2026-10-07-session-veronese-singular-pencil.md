# Singular centers of Veronese projections: an exact classification

Status: **PROVED HERE**, independently of a classification citation. The proof
works over every algebraically closed field, including characteristic two.
This note concerns the singular-pencil stratum of projection centers. It does
not classify centers whose determinant polynomial is nonzero.

Let the Veronese surface in projective five-space be represented by rank-one
symmetric matrices `vv^T`, with coordinates
`[x^2:xy:y^2:xz:yz:z^2]`. A projection to projective three-space has a line as
its center. A basepoint-free projection has a center disjoint from the
Veronese surface, so that no nonzero matrix in its two-dimensional matrix
space has rank one.

Suppose the center is a symmetric pencil `M(s,t)=sA+tB` whose determinant
vanishes identically. Every member then has rank exactly two. The matrices
`A,B` are linearly independent, because they span a line in projective space.

## 1. The kernel map has degree one

Work in the unique factorization domain `R=k[s,t]`. Choose a nonzero column of
the adjugate matrix and divide its entries by their homogeneous greatest
common divisor. The resulting kernel vector `v` is primitive and homogeneous,
with all nonzero entries of the same degree `e`. Since the pencil has rank two
over the fraction field, every column of its adjugate is a rational multiple
of `v`. Such a multiple is polynomial: the denominator of a rational scalar
in lowest terms would divide every component of `v`, contradicting
primitivity. Thus `adj(M)=v p^T` for a polynomial vector `p`.

The adjugate is symmetric. Its symmetry gives `v_i p_j=v_j p_i`, so `p` is
a rational scalar multiple of `v`; the same primitive-vector argument makes
that scalar polynomial. Consequently

`adj(M)=h(s,t) v(s,t) v(s,t)^T`.

The entries of the adjugate have degree two, hence `deg(h)=2-2e`.
Primitivity of a homogeneous vector over `k[s,t]` means that its entries have
no common zero in projective one-space: a common zero would supply a common
linear factor. Since every member has rank two, the adjugate is nonzero at
every point of projective one-space. Therefore the homogeneous polynomial
`h` has no projective zero. Algebraic closedness forces `h` to be a nonzero
constant. It follows that `e=1`.

Write `v=s u+t w`. The vectors `u,w` are linearly independent, for otherwise
all entries of `v` would have a common linear factor. A constant change of
basis puts the kernel vector in the form `(s,t,0)^T`.

## 2. The complete matrix normal form

The identity `M(s,t)(s,t,0)^T=0` gives

`A e_1=0`, `B e_2=0`, and `A e_2+B e_1=0`.

Symmetry then forces

`M(s,t)=[[0,0,-b*t],[0,0,b*s],[-b*t,b*s,c*s+d*t]]`.

Here `b` is nonzero: otherwise every member would have rank at most one.
Rescaling and reparametrizing the pencil yields the normal form

`M(s,t)=[[0,0,t],[0,0,s],[t,s,alpha*s+beta*t]]`.                 (1)

This form is valid in every characteristic. In characteristic different
from two, replacing the third basis vector by itself plus a suitable linear
combination of the first two removes `alpha,beta`. Thus the usual singular
Kronecker pencil is the only congruence class in that characteristic.
In characteristic two the displayed diagonal terms need not be removable;
no assertion of a single congruence class is being made there.

For reference, the adjugate of (1) is

`-[s,-t,0]^T [s,-t,0]`,

and a nonzero `(s,t)` gives rank two. Both identities remain valid in
characteristic two, with the usual interpretation of the minus signs.

## 3. The projection has degree two and a quadric image

The line (1) in the six ambient Veronese coordinates is

`[0:0:0:t:s:alpha*s+beta*t]`.

Its four-dimensional annihilator therefore gives the projection

`[x:y:z] -> [x^2:xy:y^2:z^2-beta*x*z-alpha*y*z]`.              (2)

This map is basepoint-free. Its first three coordinates can vanish
simultaneously only when `x=y=0`, in which case the fourth is `z^2 != 0`.
The image satisfies the quadric equation `ac=b^2` in coordinates
`[a:b:c:d]`.

On `x != 0`, put `u=y/x` and `v=z/x`. Formula (2) becomes

`[1:u:u^2:w]`, where `w=v^2-(beta+alpha*u)*v`.

The induced extension `k(u,w) subset k(u,v)` has degree two. Indeed
`T^2-(beta+alpha*u)*T-w` is irreducible over `k(u,w)`: in
`k(u)[T,w]` it is linear and monic up to sign in `w`, its quotient is the
domain `k(u)[T]`, and Gauss's lemma applies when it is regarded as a primitive
polynomial over `k(u)[w]`. Thus the image is the entire quadric surface and
the generic degree is two.

The morphism is finite. The pullback of the hyperplane line bundle is
`O_P2(2)`, an ample line bundle, so no curve can be contracted. Alternatively,
the affine formula above is a monic quadratic finite map, and the analogous
`y != 0` chart together with the single preimage of the quadric vertex covers
all fibers.

In characteristic different from two, completing the square in the fourth
coordinate and adding a linear combination of the first three coordinates
reduces (2) to `[x^2:xy:y^2:z^2]`. In characteristic two, (2) is generically
separable if `(alpha,beta) != (0,0)`, and purely inseparable of degree two
otherwise. The image has degree two in either case.

**Consequence.** A basepoint-free projection of the Veronese surface whose
center is an identically singular symmetric pencil cannot have an integral
quartic surface as its image, and cannot realize the normalization map of
such a quartic surface. This disposes of the entire singular-pencil stratum;
it is not an argument about nonsingular determinant pencils.

## Reproduction

`research/computations/verify_session_veronese_singular_pencil.py` checks the
generic symbolic adjugate, the rank-two minors, the annihilator coordinates,
the target quadric equation, and the coordinate change in characteristic
different from two. The degree and exhaustiveness arguments above are
mathematical proofs, not consequences of a sampling computation.
