# The section-parity defect behind a nonzero first moment

**Review.** Derived in the November 23 generalizations review and independently
reconstructed by the repeated-structure and algebraic-geometry reviewers.
This is a necessary-condition refinement of [sign-symmetric ACM
vanishing](chow_acm_parity_vanishing.md), not an obstruction to every CI limit.

## 1. The finite free section hull

Let \(k\) be algebraically closed of characteristic different from two.
Let \(E=k[z,w,x,y]/I\) be the saturated homogeneous coordinate algebra of
a pure projective curve with no embedded points and entire cycle
\(\sum n_i[C_{u_i,v_i}]\), and put \(Y=\operatorname{Proj}E\),
the actual possibly nonreduced curve. Assume the **ideal** is invariant under
\(\tau(z,w,x,y)=(z,w,-x,-y)\). Set \(B=k[z,w]\),
\(\mathfrak m=(z,w)\), and
\[
                  N=E^{**}_B,\qquad D=N/E.
\]
Then \(N\) is a finite graded free \(B\)-algebra and \(D\) has finite
length supported at \(\mathfrak m\). Multiplication by \(x,y\) and
\(\tau\) extend to \(N\), but \(N\) need not be generated as an algebra
by the original \(x,y\).

Indeed the projection center misses the support, so \(E\) is finite over
\(B\). Every associated component dominates the base; unmixedness implies
\(B\)-torsion-freeness. Away from the cone vertex its local rings are
locally Laurent-polynomial extensions of the locally Cohen–Macaulay
projective curve, hence Cohen–Macaulay. Finite Cohen–Macaulay modules over
the regular base are flat there. The reflexive hull agrees with \(E\)
off \(\mathfrak m\), and is graded free over the regular ring of dimension
two. Moreover, inside \(E\otimes_B k(z,w)\),
\[
                 N=\bigcap_{\operatorname{ht}\mathfrak p=1}E_{\mathfrak p}.
\]
Each term is an algebra. This justifies the algebra structure and extended
operators, rather than inferring them merely from freeness.

## 2. Opposite signs in the same degree

Choose a homogeneous \(\tau\)-eigenbasis of \(N\), of degrees \(d_i\)
and signs \(\epsilon_i\). The
[basis-independent matrix differential](chow_acm_parity_vanishing.md#2-a-basis-independent-matrix-differential)
still gives
\[
             \operatorname{Tr}(dX\wedge dY)=2M_1\,dz\wedge dw.
                                                               \tag{SD1}
\]
Only the same generic cycle is needed for that computation.
The paired entries \(X_{ij},Y_{ji}\) have degrees
\(e=d_j+1-d_i\) and \(2-e\). Unless both degrees equal one,
one entry is constant or zero and its differentiated pair vanishes.
Thus any surviving contribution requires
\[
                       d_i=d_j,\qquad\epsilon_i=-\epsilon_j.
                                                               \tag{SD2}
\]
The sign condition follows because \(x,y\) are odd and the base is fixed.
If \(M_1\ne0\), some generator degree therefore contains both signs.
In particular it contains a sign different from \((-1)^d\).

That nonstandard sign survives in the head of the finite defect. In the
right-exact sequence
\[
 E/\mathfrak mE\longrightarrow N/\mathfrak mN
       \longrightarrow D/\mathfrak mD\longrightarrow0,         \tag{SD3}
\]
the degree-\(d\) source has only sign \((-1)^d\), since it is generated
by degree-\(d\) polynomials in \(x,y\). The opposite-sign subspace
of the middle term injects into the last. Nonzero moment therefore forces
a nonstandard-parity class in \(D/\mathfrak mD\).

For saturated \(E\), this is the finite section/Rao defect:
\(N_d=H^0(\mathbf P^3,\mathcal O_Y(d))\) and the exact section sequence
identifies \(D_d\) with \(H^1(\mathcal I_Y(d))\). Indeed these section
modules agree with \(E\) off the cone vertex and are the depth-two hull.
This does not identify \(D\) with the unrestricted local-cohomology
or simultaneous-coregularity obstruction for the STCI ideal.

## 3. The single-quartic control and the remaining question

For the reduced \(C_{1,1}\),
\[
 E=k[s^4,s^3t,st^3,t^4],\qquad
 N=k[s^4,s^3t,s^2t^2,st^3,t^4].
\]
Over \(B=k[s^4,t^4]\), a basis is \((1,x,h,y)\), where
\(h=s^2t^2\) has degree one and positive sign. The defect is precisely
\(D=kh\): \(zh=x^2\), \(wh=y^2\), and there are no higher holes.
The extended multiplication relations include
\[
 x^2=zh,\quad xh=zy,\quad xy=zw,\quad
 y^2=wh,\quad yh=wx,\quad h^2=zw.
\]
The two paired linear matrix entries through \(h\), between \(x,h\)
and \(h,y\), each contribute \(dz\wedge dw\). Thus (SD1) is
\(2\,dz\wedge dw\), exactly as \(M_1=1\) requires.

Consequently a hypothetical characteristic-zero sole-supported CI must
have this kind of parity defect in **both** invariant pure hulls.
The defect is possible for invariant pure curves, as the control shows.
No proof here prevents its acquisition in a flat embedded CI limit,
and presence of a nonstandard sign is not a converse to nonzero moment.
The consequential next question concerns the constraints imposed on
(SD2–SD3) by the original two equations and their degeneration; arbitrary
free replacement discards exactly that information.
