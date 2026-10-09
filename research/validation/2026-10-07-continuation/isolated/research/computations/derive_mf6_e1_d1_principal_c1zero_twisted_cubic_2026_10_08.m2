print "c1zero_infinity_defect";
Ka=QQ[a];
K=toField(Ka/ideal(a^2+2));
R=K[x0,x1,x2,x3];
F=x0^3*x2 - x0^3*x3 - 4*x0^2*x1*x2/3 + a*x0^2*x1*x2/3 + 8*x0^2*x1*x3/3 - 2*a*x0^2*x1*x3/3 + 32*x0^2*x2^2/9 - 17*a*x0^2*x2^2/9 - 47*x0^2*x2*x3/9 + 32*a*x0^2*x2*x3/9 + 17*x0^2*x3^2/9 - 20*a*x0^2*x3^2/9 - x0*x1^3 - 8*x0*x1^2*x2/3 + 2*a*x0*x1^2*x2/3 - x0*x1^2*x3 + a*x0*x1^2*x3 + 25*x0*x1*x2^2/9 - 13*a*x0*x1*x2^2/9 - 10*x0*x1*x2*x3/9 + 7*a*x0*x1*x2*x3/9 - 2*x0*x1*x3^2/9 + 14*a*x0*x1*x3^2/9 + x0*x2^3/9 - 7*a*x0*x2^3/9 + 7*x1^4/3 - a*x1^4/3 - 23*x1^3*x2/9 + 8*a*x1^3*x2/9 + 22*x1^3*x3/9 - 19*a*x1^3*x3/9 - 7*x1^2*x2^2/9 + 13*a*x1^2*x2^2/9 + x1^2*x2*x3/9 - 7*a*x1^2*x2*x3/9 - x1^2*x3^2/9 - 2*a*x1^2*x3^2/9 + x1*x2^3/9 + 2*a*x1*x2^3/9;

J=ideal(diff(x0,F),diff(x1,F),diff(x2,F),diff(x3,F));
Tc=ideal(3*a*x2^2+3*a*x0*x3-6*a*x1*x3-3*x0^2+17*x1^2-11*x0*x2-23*x1*x2-4*x2^2+5*x0*x3+19*x1*x3,
 3*a*x1*x2-3*a*x0*x3+3*x0^2-8*x1^2+2*x0*x2+2*x1*x2+x2^2+4*x0*x3-4*x1*x3,
 a*x0*x2-2*a*x0*x3+a*x1*x3+3*x0*x1-3*x1^2-4*x0*x2+5*x0*x3-x1*x3);
print (dim(R/Tc),degree(R/Tc),genera(R/Tc));
print (dim(R/(Tc+minors(2,jacobian gens Tc))),degree(R/(Tc+minors(2,jacobian gens Tc))));
print isSubset(J,Tc);
print hilbertPolynomial(R/Tc);
print degrees gens trim Tc;
