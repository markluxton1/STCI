-- New finite algebra controls for the provisional 2026-10-28 liaison note.
-- Does not assert smooth residuals or lifting of finite-field examples.
-- The all-degree proof is in the note, not inferred from these samples.
R=QQ[x0,x1,x2,x3];
M=map(R^{-1,-1,-1},R^{-2,-2,-2,-2,-2},
    matrix{{x1,0,x2,x3,0},{-x0,x1,0,-x2,x3},
           {0,-x0,-x1,0,-x2}});
N=map(R^{-2,-2,-2,-2,-2},R^{-3,-4},
    matrix{{x3,x2^2},{-x2,-x1*x3},{0,x0*x3-x1*x2},
           {-x1,-x0*x2},{x0,x1^2}});
assert(M*N==0);
assert(rank M==3);
assert(rank N==2);
assert(codim minors(2,N)==2);
print("CANONICAL MODULE MATRIX RANK/GRADE CONTROL PASS over QQ");

R=ZZ/32003[x0,x1,x2,x3];
Q=x0*x3-x1*x2;
A=x0^2*x2-x1^3;
B=x0*x2^2-x1^2*x3;
T=x2^3-x1*x3^2;
IC=ideal(Q,A,B,T);
setRandomSeed 20261028;
makeF=d->(Q*random(d-2,R)+A*random(d-3,R)
          +B*random(d-3,R)+T*random(d-3,R));
scan({{4,4},{4,5},{5,5},{5,6},{6,6}},p->{
    a:=p#0; b:=p#1; totalDegree:=a+b;
    F:=makeF(a); G:=makeF(b); Y:=ideal(F,G);
    assert(codim Y==2);
    J:=trim(Y:IC);
    C:=res J;
    assert(degrees C_1==sort {{a},{b},{totalDegree-3},
                             {totalDegree-3},{totalDegree-3}});
    assert(degrees C_2==apply(5,i->{totalDegree-2}));
    assert(degrees C_3=={{totalDegree-1}});
    assert(degree J==a*b-4);
    assert(genus J==(a+b-4)*(a*b-8)//2);
    print("PROPER LINK RESOLUTION PASS "|toString p
        |" degree="|toString degree J|" genus="|toString genus J);
    });
print("FIVE NEW FINITE-FIELD LINK CONTROLS PASS");
