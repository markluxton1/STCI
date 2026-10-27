-- PROVISIONAL bounded experiment, 2026-10-27.
-- Rational properness, residual degree 32 and genus 112 completed.
-- Interrupted during subsequent scheme-union comparison; smoothness and
-- reduced attachments below were NOT reached or certified in this run.
-- First attempted run had an intersect syntax error, corrected here.
R=QQ[x0,x1,x2,x3];
Q=x0*x3-x1*x2;
A=x0^2*x2-x1^3;
B=x0*x2^2-x1^2*x3;
D=x2^3-x1*x3^2;
IC=ideal(Q,A,B,D);
F=Q*(-2*x3^4-3*x2^1*x3^3+3*x2^2*x3^2-2*x2^3*x3^1-2*x2^4+1*x1^1*x3^3-2*x1^1*x2^1*x3^2-3*x1^1*x2^3-2*x1^2*x3^2-3*x1^2*x2^1*x3^1-3*x1^2*x2^2+1*x0^1*x3^3+3*x0^1*x2^1*x3^2-3*x0^1*x2^2*x3^1-3*x0^1*x2^3+2*x0^1*x1^1*x3^2-2*x0^1*x1^1*x2^2+3*x0^1*x1^2*x3^1+2*x0^1*x1^3+2*x0^2*x3^2-2*x0^2*x2^1*x3^1-1*x0^2*x2^2+3*x0^2*x1^1*x2^1-2*x0^2*x1^2-2*x0^3*x3^1+3*x0^3*x1^1-1*x0^4)+A*(-2*x2^1*x3^2-1*x2^2*x3^1-1*x2^3-1*x1^1*x3^2-3*x1^1*x2^1*x3^1-3*x1^1*x2^2+3*x1^2*x3^1+3*x1^2*x2^1-3*x1^3+2*x0^1*x3^2-2*x0^1*x2^1*x3^1-1*x0^1*x2^2-1*x0^1*x1^1*x3^1+1*x0^1*x1^1*x2^1+2*x0^1*x1^2+1*x0^2*x3^1+2*x0^2*x2^1-2*x0^2*x1^1-1*x0^3)+B*(-3*x3^3-1*x2^1*x3^2-2*x2^2*x3^1+1*x2^3+3*x1^1*x3^2-1*x1^1*x2^2+1*x1^2*x3^1-1*x1^2*x2^1+2*x1^3+1*x0^1*x3^2-3*x0^1*x2^1*x3^1+1*x0^1*x1^1*x3^1+1*x0^1*x1^1*x2^1+2*x0^1*x1^2+2*x0^2*x3^1+2*x0^2*x2^1+2*x0^3)+D*(3*x3^3-1*x2^1*x3^2+3*x2^2*x3^1-1*x2^3+2*x1^1*x2^1*x3^1-1*x1^1*x2^2+1*x1^2*x3^1-2*x1^2*x2^1-3*x1^3-2*x0^1*x3^2+1*x0^1*x2^2+3*x0^1*x1^1*x3^1-1*x0^1*x1^1*x2^1-1*x0^1*x1^2+3*x0^2*x3^1-2*x0^2*x2^1+1*x0^2*x1^1+3*x0^3);
G=Q*(-3*x3^4+1*x2^1*x3^3+2*x2^2*x3^2+1*x2^3*x3^1+1*x2^4-3*x1^1*x3^3-2*x1^1*x2^1*x3^2-3*x1^1*x2^2*x3^1-2*x1^2*x3^2+3*x1^2*x2^1*x3^1+1*x1^2*x2^2+2*x1^3*x3^1-2*x1^3*x2^1-2*x1^4-1*x0^1*x3^3+1*x0^1*x2^1*x3^2-2*x0^1*x2^2*x3^1-1*x0^1*x2^3+1*x0^1*x1^1*x3^2+2*x0^1*x1^1*x2^1*x3^1-2*x0^1*x1^1*x2^2+2*x0^1*x1^2*x2^1+3*x0^1*x1^3+2*x0^2*x3^2-3*x0^2*x2^1*x3^1+3*x0^2*x2^2+1*x0^2*x1^1*x3^1+1*x0^2*x1^1*x2^1-1*x0^2*x1^2+3*x0^3*x3^1+1*x0^3*x2^1-1*x0^3*x1^1)+A*(2*x2^1*x3^2+2*x2^3-1*x1^1*x3^2+2*x1^1*x2^1*x3^1-3*x1^1*x2^2-1*x1^2*x2^1-1*x1^3+3*x0^1*x2^1*x3^1+1*x0^1*x2^2+1*x0^1*x1^1*x3^1+1*x0^1*x1^1*x2^1-3*x0^1*x1^2-3*x0^2*x3^1-3*x0^2*x2^1+1*x0^2*x1^1-2*x0^3)+B*(1*x3^3-1*x2^2*x3^1-3*x1^1*x3^2+1*x1^1*x2^1*x3^1-2*x1^1*x2^2-1*x1^2*x3^1-3*x1^2*x2^1+2*x1^3+3*x0^1*x3^2-1*x0^1*x2^1*x3^1-2*x0^1*x2^2-2*x0^1*x1^1*x3^1-3*x0^1*x1^1*x2^1+1*x0^1*x1^2-2*x0^2*x3^1-2*x0^2*x2^1-2*x0^2*x1^1+1*x0^3)+D*(1*x3^3+3*x2^1*x3^2+3*x2^3+2*x1^1*x3^2+2*x1^1*x2^1*x3^1+2*x1^1*x2^2-1*x1^2*x3^1-2*x1^2*x2^1+2*x1^3+1*x0^1*x3^2+2*x0^1*x2^1*x3^1-1*x0^1*x1^1*x3^1+3*x0^1*x1^1*x2^1+2*x0^1*x1^2-2*x0^2*x3^1+1*x0^2*x2^1-3*x0^2*x1^1+3*x0^3);
Y=ideal(F,G);
assert(codim Y==2);
print("PAIR PROPER");
J=trim saturate(Y:IC);
print("RESIDUAL COMPUTED");
assert(degree J==32);
assert(genus J==112);
print("RESIDUAL DEGREE32 GENUS112");
assert(saturate(intersect(IC,J))==saturate Y);
print("SCHEME UNION CHECKED");
S=trim saturate(J+minors(2,jacobian J));
assert(S==ideal(1_R));
print("RESIDUAL SMOOTH");
T=trim saturate(IC+J);
assert(degree T==34);
assert(saturate(T+minors(3,jacobian T))==ideal(1_R));
print("34 REDUCED ATTACHMENTS");
print("NEW RATIONAL SEXTIC BENCHMARK PASS");
