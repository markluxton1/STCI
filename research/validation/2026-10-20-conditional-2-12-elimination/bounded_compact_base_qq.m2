-- Compact chart; d0=d4=1 is a finite torus/projective cover only over d0*d4 !=0.
-- alpha_can is imposed; its necessity on all actual pairs uses the separately reviewed quadric-intersection norm argument.
R=QQ[d1,d2,d3,y0,y1,y2,y3,h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,smoothInverse,MonomialOrder=>GRevLex];
firstEquations={-5*d2-7*y1+20*y3-h0-d2*h2-d3*h1-2*y1*h2-2*y2*h1+4*y3*h2,-4*d3-5*y2-h1-d2*h3-d3*h2-2*y1*h3-2*y2*h2+4*y3*h3,-3-h2-d2*h4-d3*h3-2*y1*h4-2*y2*h3+4*y3*h4,-h3-d2*h5-d3*h4-2*y1*h5-2*y2*h4+4*y3*h5,3/2*d1-1/2*y0-h6-d2*h8-d3*h7-y0*h2-y1*h1-2*y1*h8-y2*h0-2*y2*h7+4*y3*h8,-6*d2-29/2*y1+30*y3-h7-d2*h9-d3*h8-y0*h3-y1*h2-2*y1*h9-y2*h1-2*y2*h8+4*y3*h9,-11/2*d3-25/2*y2-h8-d2*h10-d3*h9-y0*h4-y1*h3-2*y1*h10-y2*h2-2*y2*h9+4*y3*h10,-5-h9-d2*h11-d3*h10-y0*h5-y1*h4-2*y1*h11-y2*h3-2*y2*h10+4*y3*h11,-1/2-1/4*h2-1/4*d1*h1-1/2*y0*h1-y0*h8-y1*h7-y2*h6-y3*h0,-1/4*d1-23/4*y0-1/4*h3-1/4*d1*h2-1/2*y0*h2-y0*h9-y1*h8-y2*h7-y3*h1,-3/4*d2-25/4*y1+3*y3-1/4*h4-1/4*d1*h3-1/2*y0*h3-y0*h10-y1*h9-y2*h8-y3*h2,-3/4*d3-23/4*y2-1/4*h5-1/4*d1*h4-1/2*y0*h4-y0*h11-y1*h10-y2*h9-y3*h3,-1/4*h8-1/4*d1*h7-1/2*y0*h7-y3*h6,-9/8-1/4*h9-1/4*d1*h8-1/2*y0*h8-y3*h7,-d1-19/8*y0-1/4*h10-1/4*d1*h9-1/2*y0*h9-y3*h8,-3/8*y1-7/2*y3-1/4*h11-1/4*d1*h10-1/2*y0*h10-y3*h9};
symbolEquations={d3+4*y2-d1*d2-4*d1*y1+16*d1*y3+4*d2*y0-d1*d1*d1-4*d1*d1*y0,-d2-2*y1+8*y3-d1*d1-4*d1*y0+d3*d3+4*d3*y2-d1*d2*d3-2*d1*d2*y2-2*d1*d3*y1+8*d1*d3*y3+d2*d2*d2+2*d2*d2*y1-8*d2*d2*y3+2*d2*d3*y0,-d1-4*y0-3*d2*d3-4*d2*y2-4*d3*y1+16*d3*y3+d3*d3*d3+4*d3*d3*y2};
S=R[zz];
aa=d2+2*y1-4*y3+(d3+2*y2)*zz+zz^2;
bb=y0+y1*zz+y2*zz^2;
cc=1/4+(d1/4+y0/2)*zz+y3*zz^2;
uu=1+d3*zz^3; vv=d1*zz+zz^4; ww=d2*zz^2;
alphaCanonical=uu^2+vv^2+ww^2-uu*vv-uu*ww-vv*ww;
coeffR=(p,j)->sub(coefficient(zz^j,p),R);
delta=bb^2-4*aa*cc;
compactDeltaCoeffs=apply(5,j->coeffR(delta,j));
compactInvI=12*(compactDeltaCoeffs#4)*(compactDeltaCoeffs#0)-3*(compactDeltaCoeffs#3)*(compactDeltaCoeffs#1)+(compactDeltaCoeffs#2)^2;
compactInvJ=72*(compactDeltaCoeffs#4)*(compactDeltaCoeffs#2)*(compactDeltaCoeffs#0)+9*(compactDeltaCoeffs#3)*(compactDeltaCoeffs#2)*(compactDeltaCoeffs#1)-27*(compactDeltaCoeffs#4)*(compactDeltaCoeffs#1)^2-27*(compactDeltaCoeffs#3)^2*(compactDeltaCoeffs#0)-2*(compactDeltaCoeffs#2)^3;
smoothDiscriminant=(4*compactInvI^3-compactInvJ^2)/27;
baseIdeal=ideal join(firstEquations,symbolEquations,{smoothInverse*smoothDiscriminant-1});
print "COMPACT_BASE_MODEL_READY";
G=gb baseIdeal;
print "BASE_GB_COMPLETE";
print("UNIT="|toString(baseIdeal==ideal(1_R)));
print("DIM="|toString dim baseIdeal);
print gens G;
