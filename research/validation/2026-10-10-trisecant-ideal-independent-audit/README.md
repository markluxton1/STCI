# Independent trisecant ideal audit, 2026-10-10

Scope: the fixed smooth curve `C0=[s^4:s^3t:st^3:t^4]`, finite
trisecant parameter `a`, characteristic zero. This is a distinct audit
artifact. No canonical state file is changed.

Status: **PROVED**, with an exact Macaulay2 replay as additional evidence.

## Uniform ideal equality

Put `u=x0`, `v=x1`, `z=x2-a*x0`, `w=x3-a*x1`, and

```
q = u*w-v*z,
A = u^2*(z+a*u)-v^3,
B = u*(z+a*u)^2-v^2*(w+a*v),
D = (z+a*u)^3-v*(w+a*v)^2,
T = z^3+a*u*z^2-v*w^2 = D-2*a*B+a^2*A.
```

The curve ideal is `I=(q,A,B,D)` and the line ideal is `J=(z,w)`.
Then, for every finite `a`, including zero,

```
I intersect J^2 = (q*z,q*w,T).
```

Here is a proof uniform in the parameter; it does not infer special-fiber
intersection commutation from a generic computation. Let `E=(q*z,q*w,T)`.
The matrix

```
       [ w   -z*(z+a*u) ]
M =    [-z      v*w    ]
       [ 0       q     ]
```

has signed maximal minors `-q*z`, `-q*w`, `-T`. The quadric `q` is
irreducible and does not divide `T`: upon setting `w=0`, the specialized
polynomials are `-v*z` and `z^2*(z+a*u)`, and the latter is not divisible
by `v`. Thus the three generators have no common height-one prime,
and `E` has height two. Hilbert--Burch gives the exact resolution

```
0 -> R(-4) direct_sum R(-5) -> R(-3)^3 -> E -> 0.
```

Consequently `R/E` is unmixed of dimension two and has degree seven:
its Hilbert numerator is `1-3*t^3+t^4+t^5`. Both `q*z,q*w` and `T`
lie in `I intersect J^2`, so `E` is contained in that ideal `K`.
The union defined by `K` has degree `deg(C0)+deg(R/J^2)=4+3=7`.
This follows also from the exact sequence for an intersection of ideals;
the overlap is finite projectively. Hence `K/E` is a submodule of `R/E`
of dimension at most one. Unmixedness leaves no nonzero such submodule,
so `E=K`.

The original ideal generators are independently checked as the kernel
of the actual parametrization in `countercheck.m2`. The proof of the
intersection equality works over any field for which these displayed
curve-ideal and degree facts hold; the declared research scope is
characteristic zero.

## Degree four

The degree-four part is exactly

```
(I intersect J^2)_4 = q*J_2 direct_sum T*R_1.
```

Here `J_2` means the degree-two part of the line ideal `J`, with basis
`u*z,u*w,v*z,v*w,z^2,z*w,w^2`; it is not the degree-two part of `J^2`.
It has dimension seven. The second summand has basis `T*u,T*v,T*z,T*w`
and dimension four. If `q*h=T*l` with `h` quadratic and `l` linear,
primality of `q` and `q` not dividing `T` force `q` to divide `l`, hence
`l=0` and then `h=0`. Thus the sum is direct and has dimension eleven.
No coefficient or rank changes at `a=0`.

## Exact replay and preserved failures

Run:

```
/opt/homebrew/bin/M2 --script research/validation/2026-10-10-trisecant-ideal-independent-audit/countercheck.m2
```

Macaulay2 1.26.06 checked the universal equality over `QQ[a]`, the exact
parametrization kernel, and separate ideal intersections for
`a=0,1,-1,2,-2,3/2`. In each fiber it formed the eleven literal ambient
quartics, found coefficient rank eleven, and computed the independent
quotient Hilbert dimension `35-24=11`. `countercheck.out` records all
passes.

`attempt01-failure.txt` preserves an initial typed-module composability
failure while extracting polynomial forms from `basis(4,Ideal)`.
`diagnose-basis.m2` preserves the failed diagnostic attempt to call
`lift(Matrix,Module)`. Neither failed attempt supplied rank evidence.
The final script uses literal polynomial columns and quotient Hilbert
functions, so no generator-coordinate row is used as an ambient form.

The ruling classification was independently audited by a separate agent;
its distinct note is `ruling-classification.md`. Equivalence of all
nonendpoint lines is asserted over an algebraically closed field.
