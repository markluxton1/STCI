-- Independent reconstruction of the double-to-triple obstruction.
-- Uses Macaulay2 over ZZ, independently of the proposing SymPy script.
-- Run: /opt/homebrew/bin/M2 --script research/computations/audit_z4_lift_2026_10_20.m2
S=ZZ[a,b,d,h,r,s,u,iu,e,MonomialOrder=>Lex];
T=S/ideal(u*iu-1,e^3);
p=a+b*u+3*h*u^2;
q=d+2*h*u;
X=p*e+r*e^2;
Y=q*e+s*e^2;
-- Reconstruct from the exact homogeneous chart divisions, without using a
-- stored normal-transition formula.  The inverse is exact because e^3=0.
dinv=iu^4-iu^8*X+iu^12*X^2;
assert((u^4+X)*dinv==1);
c=(u^3+Y)*dinv;
A=dinv-c^4;
B=u*dinv-c^3;
P=3*a*c^2+(3*b-4*d)*c+h;
Q=2*a*c+2*b-3*d;
mU=q*X-p*Y;
mV=Q*A-P*B;
C1=h*(a*h+3*b^2-5*b*d+3*d^2);
C2=(b-d)*(4*a*h+3*b^2-8*b*d+6*d^2);
C3=a*(a*h+9*b^2-23*b*d+15*d^2);
K=3*a^3*iu^5+(9*a^2*b-12*a^2*d)*iu^4+C3*iu^3+C2*iu^2+C1*iu+3*b*h^2+3*h^3*u;
assert(u^8*(mV+iu^8*mU)==K*e^2);
-- This identity holds with free r,s; it verifies that every local quadratic
-- embedding correction contributes only the transported kernel relation.
print "PASS independent ZZ raw rational-chart cocycle with arbitrary r,s";
print("C1 = "|toString C1);
print("C2 = "|toString C2);
print("C3 = "|toString C3);
-- Gauge eta = u^-6 e+t e^2 has the same square u^-12 e^2.
G=ZZ[u,iu,e,t,MonomialOrder=>Lex]/ideal(u*iu-1,e^3);
assert((iu^6*e+t*e^2)^2==iu^12*e^2);
print "PASS independent quadratic nilpotent-coordinate gauge identity";
-- A single universal polynomial identity modulo 4; no parameter sampling.
W=(ZZ/4)[wa,wb,wd,wh];
middle=(2*wb-(1+2*wd))*(4*(2*wa)*(2*wh)+3*(2*wb)^2-8*(2*wb)*(1+2*wd)+6*(1+2*wd)^2);
assert(middle==2_W);
print "PASS independent universal middle coefficient = 2 modulo 4";
print "ALL INDEPENDENT Z4 OBSTRUCTION CHECKS PASS";
