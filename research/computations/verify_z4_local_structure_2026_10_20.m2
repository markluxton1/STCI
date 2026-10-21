-- Exact checks for the prescribed characteristic-two quadruple.
-- Run from repository root:
-- /opt/homebrew/bin/M2 --script research/computations/verify_z4_local_structure_2026_10_20.m2
needsPackage "Elimination";
for kk in {QQ,ZZ/2} do (
    S=kk[x0,x1,x2,x3];
    q=x0*x3-x1*x2;
    f=x1^3-x0^2*x2;
    h=x1^2*x3-x0*x2^2;
    g=x2^3-x1*x3^2;
    I=ideal(q,f,h,g); Ip=ideal(q,f,g);
    T=kk[s,t]; phi=map(T,S,{s^4,s^3*t,s*t^3,t^4});
    assert(I==ker phi);
    assert(saturate Ip==I);
    assert(not isSubset(ideal h,Ip));
    assert(saturate I==I);
    print("C kernel and saturation PASS over "|toString kk);
    print("C generators: "|toString gens I);
    print("C Hilbert polynomial: "|toString hilbertPolynomial(S/I));
    if char kk==2 then (
        F=x1^4-x0^3*x3; G=x2^4-x0*x3^3; K=ideal(F,G);
        assert(saturate K==K);
        assert(radical K==I);
        assert(isSubset(I^4,K));
        assert(not isSubset(I^3,K));
        assert(codim K==2);
        print("Z4 saturated, radical C, I_C^4 contained, I_C^3 not contained: PASS");
        print("Z4 Hilbert polynomial: "|toString hilbertPolynomial(S/K));
        for nn from 1 to 4 do (
            Kn=saturate(K+I^nn);
            print("Z"|toString nn|" saturated ideal: "|toString gens trim Kn);
            print("Z"|toString nn|" Hilbert polynomial: "|toString hilbertPolynomial(S/Kn));
        );
    );
);
-- Local equations in the user's coordinates; signs are kept literally.
P=(ZZ/2)[u,X,Y];
localF=u^4-(u^4+X);
localG=(u^3+Y)^4-(u^4+X)^3;
assert(ideal(localF,localG)==ideal(X,Y^4));
print "U chart ideal (F,G)=(X,Y^4): PASS";
Q=(ZZ/2)[c,A,B];
localF=(c^3+B)^4-(c^4+A)^3;
localG=c^4-(c^4+A);
assert(ideal(localF,localG)==ideal(A,B^4));
print "V chart ideal (F,G)=(A,B^4): PASS";
-- Laurent overlap, including exact cubic terms and inverse transition.
L=(ZZ/2)[u,iu,Y,MonomialOrder=>Lex]/ideal(u*iu-1,Y^4);
cc=iu+iu^4*Y;
bb=iu^6*Y+iu^9*Y^2+iu^12*Y^3;
assert(cc==(u^3+Y)*iu^4);
assert(bb==u*iu^4-cc^3);
assert(iu^4-cc^4==0);
assert(bb^2==iu^12*Y^2);
assert(bb^3==iu^18*Y^3);
-- c^{-1}=u(1+u^{-3}Y)^{-1}; all terms through Y^3 are retained.
ic=u+iu^2*Y+iu^5*Y^2+iu^8*Y^3;
assert(cc*ic==1);
assert(ic+ic^4*bb==u);
assert(ic^6*bb+ic^9*bb^2+ic^12*bb^3==Y);
print "Complete transitions, inverse transitions, and multiplication: PASS";
-- General coefficient substitutions use Hasse derivatives, not division by r!.
-- Verify the displayed rule on c^m B^j, a spanning set on k[c,B]/B^4.
chooseMod2=(m,r)->sub(binomial(m,r),L);
for mm from 0 to 12 do for jj from 0 to 3 do (
    D0=ic^0*cc^0; -- initialize a ring element
    if jj==0 then D0=(iu^mm
        +chooseMod2(mm,1)*iu^(mm+3)*Y
        +chooseMod2(mm,2)*iu^(mm+6)*Y^2
        +chooseMod2(mm,3)*iu^(mm+9)*Y^3);
    if jj==1 then D0=(iu^(mm+6)*Y
        +(iu^(mm+9)+chooseMod2(mm,1)*iu^(mm+9))*Y^2
        +(iu^(mm+12)+chooseMod2(mm,1)*iu^(mm+12)+chooseMod2(mm,2)*iu^(mm+12))*Y^3);
    if jj==2 then D0=(iu^(mm+12)*Y^2
        +chooseMod2(mm,1)*iu^(mm+15)*Y^3);
    if jj==3 then D0=iu^(mm+18)*Y^3;
    assert(cc^mm*bb^jj==D0);
);
print "Coefficient transition Hasse formula checked for c^m B^j, 0<=m<=12, 0<=j<=3: PASS";
-- Universal normal-coordinate expansions over ZZ through total degree 3.
-- z counts total normal degree and z^4=0, so no analytic approximation is used.
N=ZZ[u,iu,X,Y,z,MonomialOrder=>Lex]/ideal(u*iu-1,z^4);
dinv=iu^4-iu^8*X*z+iu^12*X^2*z^2-iu^16*X^3*z^3;
assert((u^4+X*z)*dinv==1);
cn=(u^3+Y*z)*dinv;
an=dinv-cn^4;
bn=u*dinv-cn^3;
cExpected=(iu+(iu^4*Y-iu^5*X)*z
    +(-iu^8*X*Y+iu^9*X^2)*z^2
    +(iu^12*X^2*Y-iu^13*X^3)*z^3);
aExpected=((3*iu^8*X-4*iu^7*Y)*z
    +(-9*iu^12*X^2+16*iu^11*X*Y-6*iu^10*Y^2)*z^2
    +(19*iu^16*X^3-40*iu^15*X^2*Y+24*iu^14*X*Y^2-4*iu^13*Y^3)*z^3);
bExpected=((2*iu^7*X-3*iu^6*Y)*z
    +(-5*iu^11*X^2+9*iu^10*X*Y-3*iu^9*Y^2)*z^2
    +(9*iu^15*X^3-18*iu^14*X^2*Y+9*iu^13*X*Y^2-iu^12*Y^3)*z^3);
assert(cn==cExpected);
assert(an==aExpected);
assert(bn==bExpected);
print "Ambient normal-coordinate expansions over ZZ through cubic degree: PASS";
print "ALL LOCAL/GLOBAL STRUCTURE CHECKS PASS";
