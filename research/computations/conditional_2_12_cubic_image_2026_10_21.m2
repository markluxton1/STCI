-- New exact cubic-image calculation. No actual pair is constructed.
R=QQ[y0,y1,y2,y3,y4,y5,y6];
I=ideal(y0*y5-y2*y4+y1^2,
        y0*y6-y2*y5+y1*y3,
        y1*y5-y3*y4+y0*y2,
        y1*y6-y3*y5+y2^2,
        y4*y6-y5^2+y1*y2);
assert(dim(R/I)==4);
assert(degree(R/I)==5);
singIdeal=I+minors(3,jacobian gens I);
assert(dim(R/singIdeal)==0);
F=res(coker gens I);
assert(length F==3);
assert(degrees F_1==toList(5:{2}));
assert(degrees F_2==toList(5:{3}));
assert(degrees F_3=={{5}});
S=QQ[x0,x1,x2,x3];
q=x0*x3-x1*x2;
A=x0^2*x2-x1^3;
B=x0*x2^2-x1^2*x3;
D=x2^3-x1*x3^2;
phi=map(S,R,{q*x0,q*x1,q*x2,q*x3,A,B,D});
assert(phi(I)==ideal(0_S));
print("CUBIC_IMAGE_EXACT: projectively smooth threefold, degree5, resolution(1,5,5,1) shifts(0,2,3,5)");
print("CUBIC_SYZYGIES_ZERO: canonical sheaf O(-2), by the codimension3 selfdual resolution");
print betti F;
print("NO_GLOBAL_PAIR_OR_EMPTINESS_CERTIFICATE_CLAIMED");
