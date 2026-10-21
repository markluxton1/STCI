-- New finite-normalization audit of the LOCAL nodal caution family only.
-- It does not construct homogeneous global coefficients or a supported pair.
R=QQ[t,z,w,v];
scan(1..4,n->(
    m:=10-2*n;
    d:=z-t^n;
    e:=z-t^m;
    f:=z*w^2-d^2*e;
    J:=ideal(v^2-z*e,z*w-d*v,v*w-d*e);
    assert(dim(R/J)==2);
    -- Hilbert--Burch: these are all 2x2 minors of a 2x3 matrix,
    -- and height two gives CM. Do not use the length of M2's
    -- nonminimal inhomogeneous resolution as a CM test.
    assert(J==minors(2,matrix{{z,v,d},{v,e,w}}));
    assert(dim(R/(J+ideal(z)))==1);
    -- On z!=0 this is the integral double cover v^2=z(z-t^m).
    -- Hence CM + dimension drop gives an integral ring.
    assert(dim(R/(J+minors(2,jacobian gens J)))==0);
    -- R1 + CM gives normality. v is monic-integral over the original ring.
    assert(eliminate(J,{v})==ideal(f));
    conductor:=J+ideal(d,w);
    expected:=ideal(z-t^n,w,v^2-t^n*(t^n-t^m));
    assert(conductor==expected);
    print("LOCAL_NODAL_FINITE_NORMALIZATION n="|toString n|", m="|toString m|": PASS");
    print("CONDUCTOR_EQUATION: "|toString(v^2-t^n*(t^n-t^m)));
    ));
print("NO_GLOBAL_SEXTIC_OR_PAIR_ASSERTED");
