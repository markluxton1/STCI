-- Generic one-pair collision chart; rank-drop factors explicitly retained.
K=ZZ/1009; omega=374_K;
R=K[ee,ff,lambda,tt,H4,H5,H6,H7,fi,MonomialOrder=>GRevLex];
d0=omega*ff; d1=omega^2*ff+omega*ee; d2=ff+omega^2*ee+omega; d3=ee+omega^2;
a0=4*tt+2*ee*lambda; a1=d3/2+2*lambda; a2=1;
b0=-d1/4-ff*lambda; b1=4*tt-d2/2+ee*lambda; b2=-d3/4+lambda;
c0=d0/4; c1=d1/8-ff*lambda/2; c2=tt;
h4=H4; h5=H5; h6=H6; h7=H7;
h3=-a0*h5-a1*h4;
h2=-3-a0*h4-a1*h3;
h1=-4*a1+3*b2-a0*h3-a1*h2;
h0=-5*a0+3*b1-a0*h2-a1*h1;
c0Inverse=4*omega^2*fi;
h8=-c0Inverse*(c2*h6+c1*h7);
h9=-9/2-c0Inverse*(c2*h7+c1*h8);
h10=c0Inverse*(-4*c1-3/8*b0-c2*h8-c1*h9);
h11=c0Inverse*(-7/2*c2-3/8*b1-c2*h9-c1*h10);
firstEquations={(a2)*h0+(a1)*h1+(a0)*h2-(-5*a0+3*b1),(a2)*h1+(a1)*h2+(a0)*h3-(-4*a1+3*b2),(a2)*h2+(a1)*h3+(a0)*h4-(-3*a2),(a2)*h3+(a1)*h4+(a0)*h5-(0),(b2)*h0+(b1)*h1+(b0)*h2+(a2)*h6+(a1)*h7+(a0)*h8-(-7/2*b0+6*c1),(b2)*h1+(b1)*h2+(b0)*h3+(a2)*h7+(a1)*h8+(a0)*h9-(-6*a0-5/2*b1+6*c2),(b2)*h2+(b1)*h3+(b0)*h4+(a2)*h8+(a1)*h9+(a0)*h10-(-11/2*a1-3/2*b2),(b2)*h3+(b1)*h4+(b0)*h5+(a2)*h9+(a1)*h10+(a0)*h11-(-5*a2),(c2)*h0+(c1)*h1+(c0)*h2+(b2)*h6+(b1)*h7+(b0)*h8-(-2*c0),(c2)*h1+(c1)*h2+(c0)*h3+(b2)*h7+(b1)*h8+(b0)*h9-(-21/4*b0-c1),(c2)*h2+(c1)*h3+(c0)*h4+(b2)*h8+(b1)*h9+(b0)*h10-(-3/4*a0-19/4*b1),(c2)*h3+(c1)*h4+(c0)*h5+(b2)*h9+(b1)*h10+(b0)*h11-(-3/4*a1-17/4*b2),(c2)*h6+(c1)*h7+(c0)*h8-(0),(c2)*h7+(c1)*h8+(c0)*h9-(-9/2*c0),(c2)*h8+(c1)*h9+(c0)*h10-(-3/8*b0-4*c1),(c2)*h9+(c1)*h10+(c0)*h11-(-3/8*b1-7/2*c2)};
endpointUnit=ff*fi-1;
S=R[zz];
aa=a0+a1*zz+zz^2; bb=b0+b1*zz+b2*zz^2; cc=c0+c1*zz+c2*zz^2;
DD=(zz-1)*(zz-omega)*(zz^2+ee*zz+ff);
U=d0+d3*zz^3; V=d1*zz+zz^4; W=d2*zz^2;
alphaCanonical=U^2+V^2+W^2-U*V-U*W-V*W;
coeffR=(p,j)->sub(coefficient(zz^j,p),R);
normSymbol=apply(3,j->coeffR(alphaCanonical*aa,3*j+1)-coeffR(alphaCanonical*bb,3*j+2)-(j+1)*coeffR(alphaCanonical*DD,3*j+3)/4);
assert(all(normSymbol,p->p==0));
g30=-(a1*h5+a2*h4)-a2*h5*zz;
g21=-(b1*h5+b2*h4+a1*h11+a2*h10)-(b2*h5+a2*h11)*zz;
g12=-(3/4*a2+c1*h5+c2*h4+b1*h11+b2*h10)-(c2*h5+b2*h11)*zz;
g03=-(3/8*b2+c1*h11+c2*h10)-c2*h11*zz;
GG=g30*(-zz/2)^3+g21*(-zz/2)^2+g12*(-zz/2)+g03;
LL=diff(zz,DD)-12*zz^2*GG;
qlCoefficients=new MutableList from apply(7,j->coeffR(LL,j));
scan(reverse toList(2..6),j->(v:=qlCoefficients#j;qlCoefficients#(j-2)=qlCoefficients#(j-2)-ff*v;qlCoefficients#(j-1)=qlCoefficients#(j-1)-ee*v;qlCoefficients#j=0));
qlineEquations={qlCoefficients#0,qlCoefficients#1};
collisionBoundary=((omega+1)*ee-ff-omega)*(ee^2-ff);
collisionIdeal=ideal join(firstEquations,qlineEquations,{endpointUnit});
print "ONE_PAIR_COLLISION_9VAR_MODEL_READY";
-- Necessity on ff*collisionBoundary !=0. The boundary needs separate charts.
-- No Groebner basis is run by this exporter.

print "FF1009_COLLISION_GB_START";
B=gb collisionIdeal;
print "FF1009_COLLISION_GB_DONE";
print(1_R % B == 0);
print dim collisionIdeal;
print degree collisionIdeal;
print numgens source gens B;
