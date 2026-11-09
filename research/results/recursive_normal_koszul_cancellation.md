---
id: STCI-R-0066
type: result
title: Recursive transverse complete intersections with prescribed normal Koszul cancellation
scope: "#scope"
statement: "#statement"
proofs:
  - name: full initial ideal, strict shifted resolution, and integral perturbation
    at: "research/arguments/normal_koszul_cancellation.md#the-recursive-family-and-its-cancellation-page"
    using: [STCI-R-0030, STCI-R-0065]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---

# Recursive transverse complete intersections with prescribed normal Koszul cancellation

## Scope

Let \(L\) be any field, \(n\ge2\), \(q\ge3\), \(R=L[[x,y]]\), and \(I=(x,y)\).
All weights are total normal order in \(x,y\). The integral-carrier
construction uses the same parameters over \(L\), with an extra variable
\(t\) along a marked affine line. The projective statement concerns the
closures in \(\mathbf P^3_L\) and the local calculation on the affine part of
that line.

## Statement

Define
\[
D_0=1,\qquad D_1=x,\qquad D_j=xD_{j-1}-y^qD_{j-2},\qquad
h_i=y^{qi}D_{n-i}\quad(0\le i\le n).
\]
The ideal \(J=(h_0,h_1)=(D_n,y^qD_{n-1})\) is an \(I\)-primary complete
intersection of colength \(qn(n+1)/2\). With \(S=L[X,Y]\), the full normal
initial ideals are
\[
H=\operatorname{in}_I J=(X,Y^q)^n,\qquad
T=\operatorname{in}_I(IJ)=S_+H+(X^{n-i}Y^{qi}\mid 2\le i\le n).
\]
Put \(a_i=n+(q-1)i\) for \(0\le i\le n\) and \(b_i=a_i+1\) for \(1\le i\le n\).
The defect of [R-0030](local_filtration_comparison_defect.md) is
\[
\Delta=T/S_+H=\bigoplus_{i=2}^n L(-a_i).
\]
The [normal Koszul spectral sequence](normal_koszul_comparison_defect.md)
has bases \(e_0,\ldots,e_n\) in homological degree one of weights \(a_i\),
and \(u_1,\ldots,u_n\) in homological degree two of weights \(b_i\), supplied
by a strict filtered resolution. Its only nonzero higher differential is
\[
d_{q-2}(u_i)=e_{i+1}\quad(1\le i<n),\qquad d_{q-2}(u_n)=0 .
\]
Thus \(n-1\) defect classes are canceled on the same page, with surviving
Tor-one weights \(a_0,a_1\) and Tor-two weight \(b_n=qn+1\). Both the
number and degrees of the defect classes are unbounded, and every page
\(r\ge1\) occurs by taking \(q=r+2\).

### Integral affine carriers

For \(N\ge qn+1\) in \(\mathbf A^3_{t,x,y}\), set
\[
F=D_n+t\,y^N,\qquad G=y^qD_{n-1}+t(x^N+y^N).
\]
These define integral hypersurfaces, with the same completed ideal as \(J\)
along the affine line \(x=y=0\). The local calculation therefore gives the
displayed cancellation and generic defect over the transverse field
\(L(t)\) of this line.

### Projective scope

Ordinary homogenization gives integral projective carriers of the marked
line. Their completed intersection along its affine part has the local
behavior just described.

[Complete proof in A-0009](../arguments/normal_koszul_cancellation.md#the-recursive-family-and-its-cancellation-page)

## Limitations

The calculation uses \(q>2\) to separate the weights in the lifted matrix.
The unperturbed recursive equations need not define integral hypersurfaces.
The projective construction permits residual components. The calculation
controls the completion along the affine part of the marked line. The point
at infinity and the fixed quartic are outside this calculation. The generic
defect here is nonzero, so this example lies outside the
[punctual sole-support question](../FRONTIER.md#punctual-relative-defect-under-sole-support).
The general comparison with
the extended Rees torsion filtration also remains open.

## Review

The Phase 5 nonauthor reviewer accepted this route using R-0030 and R-0065.
The reviewer reconstructed the resultant and full initial ideals, the
graded Hilbert–Burch resolution, the strict lifts in the complete shifted
modules, and the two graded augmentations that compare the Tor models
from \(E_1\) onward. As a separate check of the page, rank and sign, the
reviewer lifted the graded socle basis by \(s_i=y^{qi-1}D_{n-i}\) and found
that \(s_i(e_x\wedge e_y)\) has differential \(s_{i+1}e_y\) in \(R/J\)
for \(i<n\), and zero for \(i=n\). In weight \(a_{i+1}\) the target has
connecting class \(\operatorname{in}_I(h_{i+1})\). The reviewer also checked
the coprimality proof in arbitrary characteristic, the generator change
along the affine line, and the separate projective scope. The reviewer
inspected the verifier assertions and based the decision on the proofs.

The October 24 review records two independent reconstructions of the
recurrence, the full initial ideal by resultant and colength, the defect
degrees, and the integral perturbation. It checks the difference between the
lifted and graded Hilbert–Burch matrices, the \(q-2\) gap for \(q\ge3\), and
the scope along the marked line.
[October 24 recursive-family review](https://github.com/markluxton1/STCI/blob/737bfe4eacb93dfc1273228773695e1b55c72028/research/notes/2026-10-24-delta-singular-locus-review.md#L57)

The historical primary agent inspected and replayed the two scripts. The
separate independent executable check sampled the punctual family for three
thickness parameters. The batch 4 replays and their scope are described with
the proof.
[Historical computation scope](https://github.com/markluxton1/STCI/blob/737bfe4eacb93dfc1273228773695e1b55c72028/research/notes/2026-10-24-delta-singular-locus-review.md#L75)
