-- Independent literal controls for the entire [2,1,1] interface proof.
-- This verifies identities over QQ, not the geometric quantifier chain.
-- Uses no input file, no finite-parameter sampling, and no direction search.
R = QQ[A,B,C,u,v,t,x,y];
checks = 0;
ck = (label, expression) -> (
    if expression != 0 then error ("FAIL " | label | ": " | toString expression);
    checks = checks + 1;
    );

K = matrix {{A,B,C,0,0,0},{0,A,B,B,C,0},{0,0,A,0,B,C}};
ck("net rank A chart",det submatrix(K,{0,1,2},{0,1,2})-A^3);
ck("net rank B chart",det submatrix(K,{0,1,2},{1,3,4})-B^3);
ck("net rank C chart",det submatrix(K,{0,1,2},{2,4,5})-C^3);
ME2 = matrix {{0,0,1},{0,1,0},{1,0,0}};
ck("derivative kernel misses all nets",det ME2+1);

direction = matrix {{1},{u},{v}};
netCoefficients = {
    {u^2,-u,0,1,0,0},
    {2*u*v,-v,-u,u,1,0},
    {v^2,0,-v,v,0,1}
    };
M = d -> matrix {{d#0,d#1,d#2},{d#1,d#2+d#3,d#4},{d#2,d#4,d#5}};
W = d -> d#0-d#1*t-2*d#3*t^2-d#4*t^3+d#5*t^4;
G = {(u-t)*(u+2*t),(2*u+t)*(v-t^2),(v-t^2)^2};
scan(0..2,i -> (
    scan(flatten entries(M(netCoefficients#i)*direction),e -> ck("net kernel",e));
    ck("literal derivative",W(netCoefficients#i)-G#i)
    ));
ck("simple common basepoint",sub(diff(t,G#0),{t=>-u/2})-3*u);
scan(G,e -> ck("basepoint vanishing",sub(e,{v=>u^2/4,t=>-u/2})));

Gn = apply(G,e -> sub(e,{u=>1,v=>1/4}));
g = {-2*(t-1),-(t+2)*(t-1/2),(t-1/2)^2*(t+1/2)};
scan(0..2,i -> ck("base divisor removal",Gn#i-(t+1/2)*g#i));
gX = apply(g,e -> sub(e,{t=>x}));
gY = apply(g,e -> sub(e,{t=>y}));
p = x+y; q = x*y;
ck("first double fiber cross product",
    gX#0*gY#1-gX#1*gY#0-(x-y)*(2*p-2*q+1));
ck("second double fiber cross product",
    gX#0*gY#2-gX#2*gY#0-(x-y)*(-2*p^2+2*p*q+p+q+1/4));
I = ideal(x+y+1/4,x*y-1/4);
ck("third cross product on unique candidate",
    (gX#1*gY#2-gX#2*gY#1)%I);
ck("double fiber discriminant",(1/4)^2-4*(1/4)+15/16);

N = t^2+t/4+1/4;
remainders = apply(Gn,e -> e%ideal N);
expected = {3/2*t+3/2,15/16*t+15/16,15/64*t+15/64};
scan(0..2,i -> ck("remainder matrix entry",remainders#i-expected#i));
constraint = matrix {{3/2,15/16,15/64},{3/2,15/16,15/64},{1,1,1/4}};
ck("constraint rank witness",det submatrix(constraint,{0,2},{0,1})-9/16);
solution = matrix {{0},{-1/4},{1}};
scan(flatten entries(constraint*solution),e -> ck("unique candidate kernel",e));
L = Gn#2-Gn#1/4;
ck("candidate four-root factorization",
    L-(2*t-1)*(2*t+1)*(4*t^2+t+1)/16);
ck("extra root is not basepoint",sub(t+1/2,{t=>1/2})-1);
ck("extra root has derivative point [1,0,0]",sub(Gn#1,{t=>1/2}));
ck("extra root has derivative point [1,0,0] second",sub(Gn#2,{t=>1/2}));
ck("extra root derivative first coordinate",sub(Gn#0,{t=>1/2})-1);
ck("double fiber excludes extra root",sub(N,{t=>1/2})-5/8);
ck("double fiber excludes basepoint",sub(N,{t=>-1/2})-3/8);
ck("special remaining direction derivative conic",(2*t^2)^2-4*t^4);
print("PASS: " | toString checks | " exact [211] interface identities over QQ");
exit 0;
