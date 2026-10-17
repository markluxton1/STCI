-- Supporting identities only; the note supplies the global geometry.
R = QQ[aa,bb,gg,dd,delta,rr,tt];
tau = tt+rr^2;
v0 = tt^2-rr^3;
u3 = -rr*tt;
u4 = v0-rr*tt;
f0 = u4+aa*tau;
f1 = u4-delta*u3+bb*tau;
f2 = u4-3*delta*u3+3*delta^2*rr^2-delta^3*rr+gg*tau;
f3 = u4-4*delta*u3+6*delta^2*rr^2-4*delta^3*rr+delta^4+dd*tau;
q0 = f0*f3-f1*f2;
residual = q0 // tau;
assert(q0 == tau*residual);
print "PASS 1: exact quadric factor by the affine equation of c";
print("RESIDUAL " | toString residual);
-- Let A=aa+dd-bb-gg, B=aa*dd-bb*gg.
coefV = aa+dd-bb-gg;
coefT = aa*dd-bb*gg;
expected = (coefV+coefT+delta^2)*tt^2
 + (4*aa-3*bb-gg)*delta*rr*tt
 + (-coefV+coefT+6*aa*delta^2-3*bb*delta^2-3*delta^2)*rr^2
 + ((-4*aa+bb)*delta^3+3*delta^3)*rr
 + aa*delta^4-3*delta^2*rr^3-delta^3*rr*tt
 -delta^4*tt;
assert(residual == expected);
print "PASS 2: seven dimensional pole filtered expression";
-- Rewrite tt^2 as rr^3+v0: coefficient of the weight-six rr^3
-- is coefV+coefT+delta^2-3delta^2.  This will be examined geometrically.
S = QQ[aa,bb,gg,dd,delta,xx,uu];
z0 = uu;
z1 = 1+xx*uu;
z2 = xx^2*(1+xx*uu)^2;
z3 = xx*(1+xx*uu);
z4 = xx^3*(1+xx*uu)^2;
z5 = xx^5*(1+xx*uu)^3;
hh = z2+z3;
u0 = z5;
u1 = z4;
u2 = z3;
u3 = -z1;
u4 = z0-z1;
F0 = u4+aa*hh;
F1 = u4-delta*u3+bb*hh;
F2 = u4-3*delta*u3+3*delta^2*u2-delta^3*u1+gg*hh;
F3 = u4-4*delta*u3+6*delta^2*u2-4*delta^3*u1+delta^4*u0+dd*hh;
atEll = f -> substitute(f,{xx=>0});
jetEll = f -> atEll(diff(xx,f));
assert(atEll(F0*F3-F1*F2) == -3*delta^2);
print "PASS 3: quadric restricts nontrivially to ell";
assert(atEll(F0)==uu-1 and atEll(F1)==uu-1+delta
 and atEll(F2)==uu-1+3*delta and atEll(F3)==uu-1+4*delta);
print "PASS 4: entire nonendpoint image tangent line";
J = matrix {{atEll(F0),atEll(F1),atEll(F2),atEll(F3)},
 {1,1,1,1},{jetEll(F0),jetEll(F1),jetEll(F2),jetEll(F3)}};
assert(ideal mingens minors(3,J) == ideal(delta*(gg+3*delta^2+2*aa-3*bb),
 delta*(dd+6*delta^2+3*aa-4*bb)));
print "PASS 5: exact ramification rank ideal along ell";
-- Polynomial numerator of K(log(Q/F0^4)) on the rank-one stratum.
-- lambda=(bb-aa)/delta, so multiply by delta to avoid division.
kernelNum = delta*uu^2+(bb-aa)*uu-(bb-aa)-delta*aa;
rhoNum = delta*uu+bb-aa;
assert(delta*(aa-uu)+kernelNum == rhoNum*(uu-1));
print "PASS 6: transverse differential kernel";
qSection = (1+xx*uu)^2*(1+xx+xx^2*uu)^5;
assert(atEll(qSection)==1 and jetEll(qSection)==2*uu+5);
logNum = delta*(uu-1)*jetEll(qSection)-4*(delta*jetEll(F0)+kernelNum);
assert(logNum == (uu-1)*(delta*(5-2*uu)-4*(bb-aa)));
print "PASS 7: nonzero characteristic-zero unit jet for every ramified-ell projection";
print "PASS ALL: 7 supporting checks";
