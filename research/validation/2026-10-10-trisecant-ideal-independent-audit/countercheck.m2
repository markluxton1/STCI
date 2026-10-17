-- Independent exact certificate: fixed C0 and its trisecant ruling.
-- Scope: affine parameter a, over QQ[a], plus selected rational fibers.
-- Coordinates are u=x0, v=x1, z=x2-a*x0, w=x3-a*x1.
R = QQ[a,u,v,z,w, Degrees=>{0,1,1,1,1}];
q = u*w-v*z;
A = u^2*(z+a*u)-v^3;
B = u*(z+a*u)^2-v^2*(w+a*v);
D = (z+a*u)^3-v*(w+a*v)^2;
T = z^3+a*u*z^2-v*w^2;
I = ideal(q,A,B,D);
J = ideal(z,w);
K = intersect(I,J^2);
E = ideal(q*z,q*w,T);
assert(T == D-2*a*B+a^2*A);
assert(K == E);
print "QQ[a] ideal equality: PASS";
print gens gb K;
-- The monomial-curve ideal is independently obtained as an exact kernel.
P = QQ[s,t];
S = QQ[x0,x1,x2,x3];
param = map(P,S,{s^4,s^3*t,s*t^3,t^4});
IC = ideal(x0*x3-x1*x2,x0^2*x2-x1^3,
           x0*x2^2-x1^2*x3,x2^3-x1*x3^2);
assert(kernel param == IC);
print "Original C0 kernel: PASS";
-- Rational fibers independently repeat the actual intersection computation.
scan({0,1,-1,2,-2,3/2}, aa -> (
    RR := QQ[u,v,z,w];
    qq := u*w-v*z;
    AA := u^2*(z+aa*u)-v^3;
    BB := u*(z+aa*u)^2-v^2*(w+aa*v);
    DD := (z+aa*u)^3-v*(w+aa*v)^2;
    TT := z^3+aa*u*z^2-v*w^2;
    II := ideal(qq,AA,BB,DD);
    JJ := ideal(z,w);
    KK := intersect(II,JJ^2);
    EE := ideal(qq*z,qq*w,TT);
    assert(KK == EE);
    Q4 := matrix{{qq*u*z,qq*u*w,qq*v*z,qq*v*w,qq*z^2,qq*z*w,qq*w^2}};
    T4 := matrix{{TT*u,TT*v,TT*z,TT*w}};
    -- Eleven literal polynomial columns; degree-four quotient dimension
    -- independently proves spanning without interpreting basis(4,Ideal).
    dim4 := numColumns basis(4,RR) - hilbertFunction(4,RR/KK);
    assert(dim4 == 11);
    assert(numColumns Q4 == 7);
    assert(numColumns T4 == 4);
    all4 := Q4 | T4;
    mon4 := basis(4,RR);
    coeff := last coefficients(all4, Monomials=>mon4);
    assert(rank substitute(coeff,QQ) == 11);
    assert(isSubset(ideal all4,KK));
    print("fiber a=" | toString aa | ": ideal equality and quartic ranks 7+4=11 PASS");
    ));
print "All checks passed.";
