-- Exact checks accompanying ARTIFACT-20260906-011 and -012.
-- Run: M2 --script scripts/finite_normal_jet_certificate.m2
-- These examples validate the certificate, not universal nonexistence of STCI pairs.

jetLength = (f,g,N) -> (
    R := ring f;
    degree(R/(ideal(f,g)+(ideal gens R)^N))
    );

-- Known positive control: the twisted cubic on a singular quadric.
A = QQ[x,y,z,w];
I = ideal(x*z-y^2,x*w-y*z,y*w-z^2);
F = y*w-z^2;
G = x^2*w-2*x*y*z+y^3;
J = ideal(F,G);
assert(isSubset(J,I));
assert(isSubset(I^2,J));
assert(degree(A/I)==3);
assert(degree(A/J)==6);
print "twisted cubic: J subset I and I^2 subset J; degrees 6 and 3";

K = frac(QQ[t]);
R = K[u,v];
-- w=1, z=t, y=t^2+u, x=t^3+v. These are exact coordinates.
f = u;
g = (t^3+v)^2-2*(t^3+v)*(t^2+u)*t+(t^2+u)^3;
assert(jetLength(f,g,3)==2);
print "twisted cubic: finite normal-jet length 2, target 2, PASS";

-- Binomial positive-characteristic mechanism, with genuine generic parameter t.
-- F_n=y*w^(n-1)-z^n, G_n=x^n*w-y^(n+1), degrees n,n+1.
-- C_n has degree n+1; target generic length n.
scan({0,2,3,5}, p -> (
    kk := if p==0 then QQ else ZZ/p;
    Kp := frac(kk[t]);
    Rp := Kp[u,v];
    scan({2,3,4,6}, n -> (
        fp := u;
        gp := (t^(n+1)+v)^n-(t^n+u)^(n+1);
        observed := jetLength(fp,gp,n+1);
        predicted := 1;
        nn := n;
        if p>0 then while nn%p==0 do (predicted=predicted*p; nn=nn//p);
        assert(observed==predicted);
        print("binomial family: char="|toString p|", n="|toString n|
            ", length="|toString observed|", target="|toString n|
            ", STCI="|toString(observed==n));
        ));
    ));

K = frac(QQ[t]);
R = K[u,v];
-- Dropping the extra jet falsely accepts a common surface:
-- C=V(x,y), F=x*z^(M-1), G=x, degrees M,1. At eta_C, z is a unit.
scan(1..6, M -> (
    assert(jetLength(u,u,M)==M);
    assert(jetLength(u,u,M+1)==M+1);
    ));
print "common-surface control: cutoff M falsely accepts; M+1 rejects, M=1..6";

-- Global coefficient trap on the SMOOTH quadric x*w-y*z.
-- Now v=x-y*z, u=y-z^n, w=1, z=t.
-- G1=y*S_n and G2=w*S_n have degree n+1.
scan(2..6, n -> (
    g1 := (t^n+u)*u;
    g2 := u;
    assert(jetLength(v,g1-t^n*g2,3)==2);
    scan({{1,0},{0,1},{1,1},{2,-3}}, ab -> (
        assert(jetLength(v,ab#0*g1+ab#1*g2,3)==1);
        ));
    ));
print "global coefficient trap: K(t) combination has length 2; tested constant combinations length 1";
print "All exact checks passed. General constant-coefficient exclusion is proved in Artifact 012.";
