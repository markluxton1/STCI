# Sign symmetry and first-moment vanishing for ACM arrangements

**Review status.** The generalizations reviewer derived this extension during
the November 23, 2026 synthesis. A distinct repeated-structure investigator
independently reconstructed the matrix, parity and repeated-component proof.
The algebraic-geometry reviewer separately reconstructed the argument,
including its characteristic-different-from-two scope. No CI or Gorenstein
hypothesis is used.

## 1. The finite-flat sign-symmetry theorem

Let \(k\) be algebraically closed of characteristic different from two.
Put \(B=k[z,w]\), with all four coordinates \(z,w,x,y\) of degree one.
Let
\[
 E=k[z,w,x,y]/I
\]
be a finite flat graded \(B\)-algebra, for a standard-homogeneous ideal
\(I\) invariant under
\[
 \tau:(z,w,x,y)\longmapsto(z,w,-x,-y).
\]
Suppose its entire projective cycle is
\[
 \sum_i n_i[C_{u_i,v_i}],\qquad
 [z:x:y:w]=[s^4:s^3t:u_i st^3:v_i t^4],\qquad u_i,v_i\ne0.
\]
Then
\[
                         \sum_i n_i u_i/v_i=0.                 \tag{AP1}
\]
The multiplicities are interpreted in \(k\). In particular, the theorem
applies to every \(\tau\)-invariant arithmetically Cohen–Macaulay curve
with that entire cycle. Full intrinsic-torus invariance is sufficient,
because its element \(-1\) is \(\tau\).

## 2. A basis-independent matrix differential

In any \(B\)-basis of \(E\), let \(X,Y\) denote multiplication by
\(x,y\), and set
\[
              \lambda_E=\operatorname{Tr}(X\,dY),\qquad
              \Omega_E=d\lambda_E=\operatorname{Tr}(dX\wedge dY).
                                                               \tag{AP2}
\]
These expressions are independent of a parameter-dependent basis change.
Indeed, for \(X'=P^{-1}XP\), \(Y'=P^{-1}YP\), and
\(A=dP\,P^{-1}\),
\[
 \operatorname{Tr}(X'dY')
 =\operatorname{Tr}(X(dY+[Y,A]))
 =\operatorname{Tr}(XdY)+\operatorname{Tr}([X,Y]A)
 =\operatorname{Tr}(XdY).
\]
Thus the same holds for the exterior derivative. No choice of residue
functional or complete-intersection presentation enters (AP2).

Over \(K=k(z,w)\), make the finite separable extension splitting the
quartets \(x^4=z^3w/v_i\). Separability uses \(4\ne0\). The commuting
matrices \(X,Y\), whose characteristic polynomials now split, can be
simultaneously upper triangularized, even when their joint algebra is
nonreduced. Gauge independence allows this rational change of basis.
If \((x_j,y_j)\) are the diagonal characters, repeated with their local
Artin lengths, then
\[
 \lambda_E=\sum_j x_j\,dy_j,\qquad
 \Omega_E=\sum_j dx_j\wedge dy_j.                              \tag{AP3}
\]
For a translated component, each of its four compatible conjugate roots is
\[
 x=v_i^{-1/4}z^{3/4}w^{1/4},\qquad
 y=u_i v_i^{-3/4}z^{1/4}w^{3/4},
\]
and contributes
\(dx\wedge dy=(u_i/(2v_i))\,dz\wedge dw\). Consequently
\[
                    \Omega_E=2M_1\,dz\wedge dw.              \tag{AP4}
\]
The equality descends from the separable splitting field: differential
forms inject under that extension. Repeated multiplicities contribute
their Artin lengths in the trace, not independently labeled moving
nilpotent points.

## 3. Homogeneous parity forces the differential to vanish

Choose a homogeneous basis of \(E/(z,w)E\) and lift it to a homogeneous
\(B\)-basis of \(E\). Graded Nakayama and flatness justify freeness:
the regular sequence \(z,w\) gives the Hilbert series of the free lift,
so the resulting graded surjection has zero kernel. Since \(2\ne0\),
the lifts can be averaged to \(\tau\)-eigenvectors.

On the central fiber, a degree-\(d\) vector is represented by a
homogeneous polynomial in \(x,y\), and has sign \((-1)^d\).
Thus a basis element \(e_i\) of degree \(d_i\) has that sign after
lifting. A nonzero entry \(X_{ij}\) has base degree
\(d_j+1-d_i\). Since multiplication by \(x\) reverses the sign,
\(d_i-d_j\) is odd, so this entry degree is even. The same holds for
\(Y\).

In \(dX_{ij}\wedge dY_{ji}\), the degrees before differentiation are
nonnegative even integers summing to two. One is therefore zero, and
its derivative vanishes. Every summand in \(\Omega_E\) is zero.
Combining with (AP4) and canceling two proves (AP1). \(\square\)

For the ACM consequence, the disjoint projection center gives a finite
graded \(B\)-module. Cohen–Macaulayness makes \(z,w\) a regular
sequence, and the same basis-lifting argument makes the module free.
Thus the finite-flat hypotheses hold. No specified Hilbert numerator,
reducedness, CI decomposition or central Gorenstein condition is required.

## 4. Consequences for full torus limits

If an intrinsic-torus-invariant pure hull of a flat embedded limit has the
same entire translated cycle and is ACM, its moment vanishes regardless
of its Hilbert numerator. In characteristic zero this rules out an ACM
pure hull for **either** opposite intrinsic limit of a hypothetical
sole-supported CI, since its cycle still has \(M_1=m u/v\ne0\).
Pure-hull formation preserves that fundamental cycle and torus invariance.

This removes the need for the special effective-CI-cycle decomposition
previously used to infer vanishing on certain invariant ACM hulls. Such
decompositions retain their independent structure where established.
The theorem does not prove that any arbitrary full limit has an ACM hull.

The actual sign symmetry is essential to this proof. Invariance of the
cycle alone does not imply \(\tau\)-invariance of the ideal, nor the
parity constraint on its multiplication matrices. Likewise, a finite
projection of a non-ACM curve need not be flat at the base origin; replacing
its algebra by an abstract free algebra would discard the embedding being
tested. The reduced single quartic is non-ACM and has nonzero moment,
consistently with this boundary.

The matrix differential is the classical commuting-matrix expression of
the Hilbert-scheme form, and (AP4) extends the
[CI residue interpretation](chow_hilbert_symplectic_form.md#1-an-exact-pullback-formula)
without relying on that construction in positive characteristic.
The contribution is the graded sign-symmetry vanishing criterion and its
application to actual translated arrangements and invariant pure hulls.
It is not universal vanishing for non-invariant CI ideals.
