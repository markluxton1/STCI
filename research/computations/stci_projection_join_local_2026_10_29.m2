-- Exact counterexample to a proposed local residual-contact <=4*ramification bound.
-- All equations are actual members of the marked (2,2) source.
-- This example is basepoint free and birational, but NOT singleton admissible.
K0=QQ[j]; K=toField(K0/ideal(j^2+1));
P=K[x,z];
H2=x*(1-z/4)+j*z/4;
H3=-10*j*x-2*x^2-x^2*z/2+z^3/16+z^2/2+5*z/2;
f=1-z/4;
num=(-10*j*(-j*z/4)*f-2*(-j*z/4)^2-((-j*z/4)^2*z/2)
    +(z^3/16+z^2/2+5*z/2)*f^2);
assert(num==z^5/256);
assert(sub(H2,{z=>0})==x);
assert(sub(H3,{z=>0})==-10*j*x-2*x^2);
localQ=saturate(ideal(H2,H3),ideal f);
assert(dim(P/localQ)==0 and degree(P/localQ)==5);
print("CLEARED_BRANCH_RESTRICTION="|toString num);
print("SIMPLE_NORMAL_ROOT_AND_LOCAL_RESIDUAL_LENGTH_FIVE_VERIFIED");

R=K[a,y,d,w];
S=ideal(a*d-y^2+w^2/4);
U={a^2,a*y,y*d+w*y+j*w^2/4,d^2+w*(-10*j*y-2*d)+5*w^2/2};
BP=saturate(S+ideal U,ideal(a,y,d,w));
assert(BP==ideal 1_R);
print("BASEPOINT_FREE_VERIFIED");
chart=map(P,R,{1,x,x^2-z^2/4,z});
assert(chart(U_2-U_1^3)==z*H2);
assert(chart(U_3-U_1^4)==z*H3);
assert(sub(diff(z,chart(U_0*U_3-U_1*U_2)),{z=>0})==-10*j*x-3*x^2);
print("ORDER_ONE_DETERMINANT_AND_GRAPH_PULLBACKS_VERIFIED");

G=1-(10*j+2)*z+2*z^2+z^3/2+z^4/16;
reflection=-4/(j-1)-z;
reflectionDifference=G-sub(G,{z=>reflection});
assert(coefficient(z^3,reflectionDifference)==(j+3)/2);
print("DECK_INVOLUTION_DIFFERENCE_CUBIC="|toString coefficient(z^3,reflectionDifference));
print("BIRATIONALITY_NONINVARIANCE_VERIFIED");

J=S+ideal(w-1)+ideal(
 U_0*U_3-U_1*U_2,
 U_1^3-U_0^2*U_2,
 U_1^2*U_3-U_0*U_2^2,
 U_2^3-U_1*U_3^2);
assert(dim(R/J)==0 and degree(R/J)==8);
print("OFF_DIAGONAL_INVERSE_DIMENSION="|toString dim(R/J));
print("OFF_DIAGONAL_INVERSE_LENGTH="|toString degree(R/J));
print("OFF_DIAGONAL_INVERSE_GROEBNER_BASIS="|toString gens gb J);
print("LOCAL_MULTIPLICITY_BOUND_COUNTEREXAMPLE_PASS");

-- Stronger example: finite contact six at a simple normal root.
K20=QQ[rho]; K2=toField(K20/ideal(rho^2-5));
P2=K2[xx,zz];
parA=5*rho/16; parL=rho/10; parB=-8*rho/15; parC=-1/2; parM=-4/15;
Knormal2=parA*xx^2+xx*(1-zz/4)+parL*zz-parA*zz^2/4;
Knormal3=parB*xx+parC*xx^2-xx^2*zz/2+zz^3/16-parC*zz^2/4+parM*zz;
sixIdeal=ideal(Knormal2,Knormal3);
assert(dim(P2/sixIdeal)==0 and degree(P2/sixIdeal)==6);
assert(xx^6%sixIdeal==0 and zz^6%sixIdeal==0);
assert(sub(Knormal2,{zz=>0})==xx+parA*xx^2);
assert(sub(Knormal3,{zz=>0})==parB*xx+parC*xx^2);
P3=K2[vv]; T3=P3/ideal(vv^8); jetX=0_T3;
for n from 1 to 7 do (
 jetH2=parA*jetX^2+jetX*(1-vv/4)+parL*vv-parA*vv^2/4;
 jetX=jetX-sub(coefficient(vv^n,lift(jetH2,P3)),T3)*vv^n;
);
jetH3=parB*jetX+parC*jetX^2-jetX^2*vv/2+vv^3/16-parC*vv^2/4+parM*vv;
assert(coefficient(vv^6,lift(jetH3,P3))==-9/65536);
assert(sub(lift(jetH3,P3),K2[vv]/ideal(vv^6))==0);
print("STRONGER_LOCAL_CONTACT_SIX_AND_SIMPLE_NORMAL_ROOT_VERIFIED");
print("SIXTH_CONTACT_COEFFICIENT="|toString coefficient(vv^6,lift(jetH3,P3)));
R2=K2[aa,yy,dSix,ww];
S2=ideal(aa*dSix-yy^2+ww^2/4);
U2={aa^2,aa*yy,yy*dSix+ww*(yy+parA*dSix)+parL*ww^2,
    dSix^2+ww*(parB*yy+parC*dSix)+parM*ww^2};
BP2=saturate(S2+ideal U2,ideal(aa,yy,dSix,ww));
assert(BP2==ideal 1_R2);
chart2=map(P2,R2,{1,xx,xx^2-zz^2/4,zz});
assert(chart2(U2_2-U2_1^3)==zz*Knormal2);
assert(chart2(U2_3-U2_1^4)==zz*Knormal3);
assert(sub(diff(zz,chart2(U2_0*U2_3-U2_1*U2_2)),{zz=>0})
       ==parB*xx+(parC-1)*xx^2-parA*xx^3);
Off2=S2+ideal(ww-1)+ideal(
 U2_0*U2_3-U2_1*U2_2,
 U2_1^3-U2_0^2*U2_2,
 U2_1^2*U2_3-U2_0*U2_2^2,
 U2_2^3-U2_1*U2_3^2);
assert(dim(R2/Off2)==0 and degree(R2/Off2)==8);
print("STRONGER_EXAMPLE_BASEPOINT_FREE_ORDER_ONE_AND_OFF_DIAGONAL_LENGTH_EIGHT_VERIFIED");
print("LOCAL_CONTACT_SIX_COUNTEREXAMPLE_PASS");
