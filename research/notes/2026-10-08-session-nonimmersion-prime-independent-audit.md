# Independent audit: the generic nonimmersion-prime obstruction

Date: 2026-10-08. Auditor: `verification`. Status: **PROVED HERE**, independently audited from the full power identity. This note does not classify all nonnormal quartic surfaces.

## Exact statement

Let k be algebraically closed, let S be a smooth projective surface, and let nu:S -> X subset P^N be finite and birational. Write H=nu^*O_X(1). Suppose a smooth integral curve c on S satisfies c~H, there is f in H^0(S,O_S(H)) with divisor c, and an ambient homogeneous polynomial G of positive degree n satisfies

    nu^*G=lambda f^n, lambda in k^*.

Suppose that nu|c is an immersion into P^N. Assume n is nonzero in k; in particular the statement applies in characteristic zero. If E is any integral curve distinct from c with H.E>0, then dnu has generic rank two along E.

Neither smoothness of E nor a conductor hypothesis on E is required. A finite normalization of a smooth rational quartic scroll has H ample, so every actual conductor prime satisfies the positive-intersection hypothesis. The previously audited full-support mate reduction supplies exactly c, f, and the power identity in that application.

## Proof, including singular E and the point f=0

Because c.E=H.E>0 and E is distinct from c, choose a closed point P in c intersect E. Suppose that dnu has generic rank at most one along E. On any local chart, every two-by-two minor of its derivative matrix vanishes in k(E). The entries are regular and E is integral, so those minors vanish modulo the prime ideal of E. Hence the rank of dnu at P is at most one. Rank zero would already contradict immersion of c; its rank is therefore exactly one.

Choose an ambient hyperplane section h nonzero at nu(P). Its pullback trivializes H near P, and the target is in the affine chart h!=0. Trivialize the smooth source tangent bundle near P. Let q_1,...,q_N be the pulled-back affine target coordinates, and write a derivative row as (a,b), with at least one entry a unit at P. The regular vector field

    V=(-b,a)

in this tangent frame is nonzero at P. It kills that row identically. Its pairing with every other derivative row is a two-by-two minor, up to sign, so

    V(q_i)=0 modulo I_E for every i.

This is the required kernel construction. It works over the singular ring O_E: a unit pivot and vanishing minors suffice. There is no need to regard E as a smooth curve, to extend an a priori kernel line bundle, or to assume a global involution.

Put g=f/(nu^*h) and A=G/h^n. These are respectively a source regular function and a target affine regular function, with

    nu^*A=lambda g^n.

The chain rule gives V(nu^*A)=0 modulo I_E, and differentiation gives

    n lambda g^(n-1) V(g)=0 in O_E.

The image of g in the local domain O_E is nonzero: its divisor on S is c, distinct from E. Cancel its nonzero power in that domain, using n lambda!=0, to obtain V(g)=0 in O_E. The resulting equality is regular at P, so dg_P(V(P))=0. This cancellation takes place before specializing at g(P)=0; it does not divide by g(P).

Since c is smooth, dg_P is nonzero and its kernel is the one-dimensional tangent line T_Pc. The nonzero vector V(P) both lies in that tangent line and is killed by dnu_P. This contradicts immersion of nu|c. Thus the assumed generic rank deficiency is impossible.

## A local-unit variant and exact limits

The same cancellation argument even permits a local identity nu^*A=u g^n for a regular unit u, provided that A is an ambient function. Differentiation modulo I_E gives

    g^(n-1) (n u V(g)+g V(u))=0.

After cancelling in O_E and evaluating at P, where g(P)=0, one again obtains V(g)(P)=0. The global constant-power identity available in the scroll application is stronger than needed for this local argument.

The proof does not apply to an isolated rank-drop point on a prime which is generically immersive. It does not infer rank deficiency merely from an upstairs conductor multiplicity. A claim that a concrete conductor branch is excluded must establish its generic derivative rank from the actual normalization morphism or from a valid transverse singularity argument. In characteristic dividing n, the derivative of g^n loses the necessary information.

## Relation to the current frontier

This independently agrees with the separate [normal-global audit](2026-10-08-session-normalization-differential-independent-audit.md), whose proof uses the equivalent constant-rank kernel over O_E. Agreement is not the proof: the unit-pivot argument above independently establishes the extension across singular E and across c intersect E.

For an integral quartic with smooth rational quartic-scroll normalization, any mate of the fixed smooth rational quartic C0 must therefore leave the normalization generically immersive along every actual conductor prime. The generic Artin classification or geometric transverse branch classification still has to establish which conductor possibilities have that property; the obstruction alone is not a closure of that carrier class.

No canonical frontier file was changed by this audit.
