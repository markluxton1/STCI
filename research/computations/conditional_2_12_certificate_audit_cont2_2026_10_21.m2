-- Independent reconstruction from original factor coefficients.
U=QQ[a0,a1,a2,b0,b1,b2,c0,c1,c2,h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11];
universalFirst={-5*a0+3*b1-a0*h2-a1*h1-a2*h0,-4*a1+3*b2-a0*h3-a1*h2-a2*h1,-3*a2-a0*h4-a1*h3-a2*h2,-a0*h5-a1*h4-a2*h3,-7/2*b0+6*c1-a0*h8-a1*h7-a2*h6-b0*h2-b1*h1-b2*h0,-6*a0-5/2*b1+6*c2-a0*h9-a1*h8-a2*h7-b0*h3-b1*h2-b2*h1,-11/2*a1-3/2*b2-a0*h10-a1*h9-a2*h8-b0*h4-b1*h3-b2*h2,-5*a2-a0*h11-a1*h10-a2*h9-b0*h5-b1*h4-b2*h3,-2*c0-b0*h8-b1*h7-b2*h6-c0*h2-c1*h1-c2*h0,-21/4*b0-c1-b0*h9-b1*h8-b2*h7-c0*h3-c1*h2-c2*h1,-3/4*a0-19/4*b1-b0*h10-b1*h9-b2*h8-c0*h4-c1*h3-c2*h2,-3/4*a1-17/4*b2-b0*h11-b1*h10-b2*h9-c0*h5-c1*h4-c2*h3,-c0*h8-c1*h7-c2*h6,-9/2*c0-c0*h9-c1*h8-c2*h7,-3/8*b0-4*c1-c0*h10-c1*h9-c2*h8,-3/8*b1-7/2*c2-c0*h11-c1*h10-c2*h9};
K=QQ;
R=K[h4,h5,h6,h7,a,x];
w=1_R;
-- f=l1*l2, with no separate ruling action.
A1=a-x;D1=(a+x)/2;A2=-w^2*(a+x);D2=w^2*(a-x)/2;
ff={A1*A2,A1*w+A2,w,A1+A2,A1*D2+A2*D1+1+w,D2+w*D1,1,D1+D2,D1*D2};
-- Solve only original rows 0..3 and 12..15; w is a unit.
hh3=-(ff#0*h5+ff#1*h4)*w^2;
hh2=-3-(ff#0*h4+ff#1*hh3)*w^2;
hh1=(-4*ff#1+3*ff#5-ff#0*hh3-ff#1*hh2)*w^2;
hh0=(-5*ff#0+3*ff#4-ff#0*hh2-ff#1*hh1)*w^2;
hh8=-ff#7*h7-ff#8*h6;
hh9=-9/2-ff#7*hh8-ff#8*h7;
hh10=-3*ff#3/8-4*ff#7-ff#7*hh9-ff#8*hh8;
hh11=-3*ff#4/8-7*ff#8/2-ff#7*hh10-ff#8*hh9;
phi=map(R,U,join(ff,{hh0,hh1,hh2,hh3,h4,h5,h6,h7,hh8,hh9,hh10,hh11}));
actual=apply(universalFirst,e->phi(e));
exported={-h6-9*x+2*h7*x+6*(a*a)*x-6*h4*(a*a)*x-2*h5*(a*a)*(a*a)+1/4*h6*(a*a)*(a*a)-h7*(a*a)*x+3*h4*(a*a)*(a*a)*x-2*h4*x*x*x+h5*(a*a)*(a*a)*(a*a)-1/2*h6*(a*a)*x*x+h7*x*x*x-2*h4*(a*a)*x*x*x-h5*(a*a)*(a*a)*x*x+2*h5*x*x*x*x+1/4*h6*x*x*x*x-h4*x*x*x*x*x-h5*(a*a)*x*x*x*x+h5*x*x*x*x*x*x,1-h7-1/2*(a*a)-2*h4*(a*a)-11/2*x*x+h4*(a*a)*(a*a)-2*h4*x*x-2*h5*(a*a)*x+1/2*h6*(a*a)*x+1/4*h7*(a*a)*(a*a)-2*h7*x*x+h5*(a*a)*(a*a)*x+2*h5*x*x*x-1/4*h6*(a*a)*(a*a)*x-1/2*h6*x*x*x+1/2*h7*(a*a)*x*x-h4*x*x*x*x-2*h5*(a*a)*x*x*x+1/2*h6*(a*a)*x*x*x-3/4*h7*x*x*x*x+h5*x*x*x*x*x-1/4*h6*x*x*x*x*x,7/2*x-2*h4*x-2*h5*(a*a)-1/4*h6*(a*a)+h7*x+5/4*(a*a)*x+h4*(a*a)*x+h5*(a*a)*(a*a)+2*h5*x*x+1/4*h6*x*x+1/2*h7*(a*a)*x-5/4*x*x*x-h4*x*x*x-2*h5*(a*a)*x*x+1/16*h6*(a*a)*(a*a)*(a*a)-1/2*h6*(a*a)*x*x-1/2*h7*(a*a)*(a*a)*x+3/2*h7*x*x*x+h5*x*x*x*x+1/16*h6*(a*a)*(a*a)*x*x+1/2*h6*x*x*x*x-5/16*h6*(a*a)*x*x*x*x+1/2*h7*x*x*x*x*x+3/16*h6*x*x*x*x*x*x,-1/2-2*h4-3/4*(a*a)+h4*(a*a)+2*h5*x-1/4*h7*(a*a)+1/8*(a*a)*(a*a)+13/4*x*x-h4*x*x-h5*(a*a)*x+1/4*h6*(a*a)*x-3/4*h7*x*x-3/4*(a*a)*x*x+h5*x*x*x+1/8*h6*(a*a)*(a*a)*x-1/4*h6*x*x*x+1/16*h7*(a*a)*(a*a)*(a*a)-h7*(a*a)*x*x+5/8*x*x*x*x-1/8*h6*(a*a)*(a*a)*(a*a)*x+1/4*h6*(a*a)*x*x*x+9/16*h7*(a*a)*(a*a)*x*x-h7*x*x*x*x+1/8*h6*(a*a)*(a*a)*x*x*x-3/8*h6*x*x*x*x*x-5/16*h7*(a*a)*x*x*x*x+1/8*h6*(a*a)*x*x*x*x*x-5/16*h7*x*x*x*x*x*x-1/8*h6*x*x*x*x*x*x*x,1-2*h7+3/2*(a*a)-h4*(a*a)-h6*x+h7*(a*a)-1/4*(a*a)*(a*a)-13/2*x*x-3*h4*x*x-2*h5*(a*a)*x+1/2*h6*(a*a)*x-h7*x*x+3/2*(a*a)*x*x+1/4*h4*(a*a)*(a*a)*(a*a)-4*h4*(a*a)*x*x-h5*(a*a)*(a*a)*x+2*h5*x*x*x-1/2*h6*x*x*x-5/4*x*x*x*x+9/4*h4*(a*a)*(a*a)*x*x-4*h4*x*x*x*x+h5*(a*a)*(a*a)*(a*a)*x-2*h5*(a*a)*x*x*x-5/4*h4*(a*a)*x*x*x*x-h5*(a*a)*(a*a)*x*x*x+3*h5*x*x*x*x*x-5/4*h4*x*x*x*x*x*x-h5*(a*a)*x*x*x*x*x+h5*x*x*x*x*x*x*x,7/2*x-2*h4*x-h5*(a*a)-1/2*h6*(a*a)+h7*x+5/4*(a*a)*x-h4*(a*a)*x+h5*x*x+1/4*h6*(a*a)*(a*a)+1/2*h6*x*x-1/2*h7*(a*a)*x-5/4*x*x*x+h4*(a*a)*(a*a)*x-3*h4*x*x*x+1/4*h5*(a*a)*(a*a)*(a*a)-2*h5*(a*a)*x*x-1/2*h6*(a*a)*x*x+1/2*h7*x*x*x+1/4*h5*(a*a)*(a*a)*x*x+2*h5*x*x*x*x+1/4*h6*x*x*x*x-h4*x*x*x*x*x-5/4*h5*(a*a)*x*x*x*x+3/4*h5*x*x*x*x*x*x,-1/2-h4+1/4*(a*a)-1/2*h7*(a*a)+11/4*x*x+1/4*h4*(a*a)*(a*a)-2*h4*x*x-h5*(a*a)*x+1/4*h6*(a*a)*x+1/4*h7*(a*a)*(a*a)-1/2*h7*x*x+1/2*h4*(a*a)*x*x+1/2*h5*(a*a)*(a*a)*x+h5*x*x*x-1/8*h6*(a*a)*(a*a)*x-1/4*h6*x*x*x-3/4*h4*x*x*x*x-h5*(a*a)*x*x*x+1/4*h6*(a*a)*x*x*x-1/4*h7*x*x*x*x+1/2*h5*x*x*x*x*x-1/8*h6*x*x*x*x*x,-h5-9/4*x-h4*x+3/2*(a*a)*x+1/2*h4*(a*a)*x+1/4*h5*(a*a)*(a*a)-1/8*h6*(a*a)*(a*a)+3/4*h7*(a*a)*x-1/2*h4*x*x*x-1/2*h5*(a*a)*x*x+1/16*h6*(a*a)*(a*a)*(a*a)-3/8*h7*(a*a)*(a*a)*x+1/4*h7*x*x*x+1/4*h5*x*x*x*x-1/16*h6*(a*a)*(a*a)*x*x+1/8*h6*x*x*x*x+1/4*h7*(a*a)*x*x*x-1/16*h6*(a*a)*x*x*x*x+1/8*h7*x*x*x*x*x+1/16*h6*x*x*x*x*x*x};
assert all({0,1,2,3,12,13,14,15},i->actual#i==0);
assert(take(drop(actual,4),8)==exported);
print("W1_LINE_SAVED_FIRST_EXACT_MATCH");
-- Reconstruct trace and determinant directly from factor matrices.
M1=matrix{{-1,-D1},{A1,1}};M2=matrix{{-1,-D2},{A2,w}};
N=matrix{{1,D1},{-A1,-1}}*M2;
tau=trace N;de=det N;
assert(tau==-w^2*(a^2+x^2)-1-w);
assert(de==w*((a^2-x^2-2)/2)^2);
disc=tau^2-4*de;
expectedDisc=4*(a^2)*(x^2+2);
assert(disc==expectedDisc);
print("W1_LINE_TRACE_DETERMINANT_OPEN_MATCH");
K=toField(QQ[ww]/ideal(ww^2+ww+1));
R=K[h4,h5,h6,h7,a,x];
w=sub(K_0,R);
-- f=l1*l2, with no separate ruling action.
A1=a-x;D1=(a+x)/2;A2=-w^2*(a+x);D2=w^2*(a-x)/2;
ff={A1*A2,A1*w+A2,w,A1+A2,A1*D2+A2*D1+1+w,D2+w*D1,1,D1+D2,D1*D2};
-- Solve only original rows 0..3 and 12..15; w is a unit.
hh3=-(ff#0*h5+ff#1*h4)*w^2;
hh2=-3-(ff#0*h4+ff#1*hh3)*w^2;
hh1=(-4*ff#1+3*ff#5-ff#0*hh3-ff#1*hh2)*w^2;
hh0=(-5*ff#0+3*ff#4-ff#0*hh2-ff#1*hh1)*w^2;
hh8=-ff#7*h7-ff#8*h6;
hh9=-9/2-ff#7*hh8-ff#8*h7;
hh10=-3*ff#3/8-4*ff#7-ff#7*hh9-ff#8*hh8;
hh11=-3*ff#4/8-7*ff#8/2-ff#7*hh10-ff#8*hh9;
phi=map(R,U,join(ff,{hh0,hh1,hh2,hh3,h4,h5,h6,h7,hh8,hh9,hh10,hh11}));
actual=apply(universalFirst,e->phi(e));
exported={1/2*a-1/2*x-8*w*x-w*h6-1/2*w*w*a-1/2*w*w*x-w*a*h7+w*x*h7-1/4*a*a*a+7/4*a*a*x-11/4*a*x*x+5/4*x*x*x+w*w*a*h7+w*w*x*h7+5/2*w*a*a*x-5/2*w*x*x*x-a*a*a*h4-3*a*a*x*h4-3*a*x*x*h4-x*x*x*h4+1/4*w*w*a*a*a+7/4*w*w*a*a*x+11/4*w*w*a*x*x+5/4*w*w*x*x*x+w*a*a*a*h4+1/2*w*a*a*a*h7-3*w*a*a*x*h4-1/2*w*a*a*x*h7+3*w*a*x*x*h4-1/2*w*a*x*x*h7-w*x*x*x*h4+1/2*w*x*x*x*h7-a*a*a*a*h5-2*a*a*a*x*h5+2*a*x*x*x*h5+x*x*x*x*h5-1/2*w*w*a*a*a*h7-1/2*w*w*a*a*x*h7+1/2*w*w*a*x*x*h7+1/2*w*w*x*x*x*h7+1/4*w*a*a*a*a*h6-1/2*w*a*a*x*x*h6+1/4*w*x*x*x*x*h6+1/2*a*a*a*a*a*h4+3/2*a*a*a*a*x*h4+a*a*a*x*x*h4-a*a*x*x*x*h4-3/2*a*x*x*x*x*h4-1/2*x*x*x*x*x*h4-w*w*a*a*a*a*h5+2*w*w*a*a*a*x*h5-2*w*w*a*x*x*x*h5+w*w*x*x*x*x*h5-1/2*w*a*a*a*a*a*h4+3/2*w*a*a*a*a*x*h4-w*a*a*a*x*x*h4-w*a*a*x*x*x*h4+3/2*w*a*x*x*x*x*h4-1/2*w*x*x*x*x*x*h4+1/2*a*a*a*a*a*a*h5+a*a*a*a*a*x*h5-1/2*a*a*a*a*x*x*h5-2*a*a*a*x*x*x*h5-1/2*a*a*x*x*x*x*h5+a*x*x*x*x*x*h5+1/2*x*x*x*x*x*x*h5+1/2*w*w*a*a*a*a*a*a*h5-w*w*a*a*a*a*a*x*h5-1/2*w*w*a*a*a*a*x*x*h5+2*w*w*a*a*a*x*x*x*h5-1/2*w*w*a*a*x*x*x*x*h5-w*w*a*x*x*x*x*x*h5+1/2*w*w*x*x*x*x*x*x*h5,1/2+1/2*w-w*h7-1/4*a*a+3/2*a*x-5/4*x*x-1/4*w*a*a-3/2*w*a*x-5/4*w*x*x-1/2*a*a*h7+a*x*h7-1/2*x*x*h7-3*w*w*x*x-w*a*a*h4+w*a*a*h7+2*w*a*x*h4-w*x*x*h4-w*x*x*h7-1/4*a*a*a*h6+1/4*a*a*x*h6+1/4*a*x*x*h6-1/4*x*x*x*h6-w*w*a*a*h4-1/2*w*w*a*a*h7-2*w*w*a*x*h4-w*w*a*x*h7-w*w*x*x*h4-1/2*w*w*x*x*h7+1/4*w*a*a*a*h6+1/4*w*a*a*x*h6-1/4*w*a*x*x*h6-1/4*w*x*x*x*h6+1/4*a*a*a*a*h7-1/2*a*a*a*x*h7+1/2*a*x*x*x*h7-1/4*x*x*x*x*h7-2*w*w*a*a*x*h5+2*w*w*x*x*x*h5+1/2*w*a*a*a*a*h4-1/4*w*a*a*a*a*h7-w*a*a*a*x*h4+1/2*w*a*a*x*x*h7+w*a*x*x*x*h4-1/2*w*x*x*x*x*h4-1/4*w*x*x*x*x*h7+1/8*a*a*a*a*a*h6-1/8*a*a*a*a*x*h6-1/4*a*a*a*x*x*h6+1/4*a*a*x*x*x*h6+1/8*a*x*x*x*x*h6-1/8*x*x*x*x*x*h6+1/2*w*w*a*a*a*a*h4+1/4*w*w*a*a*a*a*h7+w*w*a*a*a*x*h4+1/2*w*w*a*a*a*x*h7-w*w*a*x*x*x*h4-1/2*w*w*a*x*x*x*h7-1/2*w*w*x*x*x*x*h4-1/4*w*w*x*x*x*x*h7-1/8*w*a*a*a*a*a*h6-1/8*w*a*a*a*a*x*h6+1/4*w*a*a*a*x*x*h6+1/4*w*a*a*x*x*x*h6-1/8*w*a*x*x*x*x*h6-1/8*w*x*x*x*x*x*h6+w*w*a*a*a*a*x*h5-2*w*w*a*a*x*x*x*h5+w*w*x*x*x*x*x*h5,-1/4*w*a+7/4*w*x-1/2*a*h7+1/2*x*h7+1/4*w*w*a+7/4*w*w*x+1/2*w*a*h7-2*w*x*h4+1/2*w*x*h7-1/4*a*a*h6+1/4*x*x*h6+1/8*w*a*a*a+5/8*w*a*a*x-w*a*a*h5-1/8*w*a*x*x-5/8*w*x*x*x+w*x*x*h5+1/2*a*a*a*h7-1/2*a*a*x*h7-1/2*a*x*x*h7+1/2*x*x*x*h7-1/8*w*w*a*a*a+5/8*w*w*a*a*x-w*w*a*a*h5+1/8*w*w*a*x*x-5/8*w*w*x*x*x+w*w*x*x*h5-1/2*w*a*a*a*h7+w*a*a*x*h4-1/2*w*a*a*x*h7+1/2*w*a*x*x*h7-w*x*x*x*h4+1/2*w*x*x*x*h7+1/4*a*a*a*a*h6-1/2*a*a*x*x*h6+1/4*x*x*x*x*h6+3/2*w*w*a*a*x*h7+1/2*w*w*x*x*x*h7+1/2*w*a*a*a*a*h5-1/8*w*a*a*a*a*h6-1/4*w*a*a*a*x*h6-w*a*a*x*x*h5+1/4*w*a*x*x*x*h6+1/2*w*x*x*x*x*h5+1/8*w*x*x*x*x*h6-1/8*a*a*a*a*a*h7+1/8*a*a*a*a*x*h7+1/4*a*a*a*x*x*h7-1/4*a*a*x*x*x*h7-1/8*a*x*x*x*x*h7+1/8*x*x*x*x*x*h7+1/2*w*w*a*a*a*a*h5-1/8*w*w*a*a*a*a*h6+1/4*w*w*a*a*a*x*h6-w*w*a*a*x*x*h5-1/4*w*w*a*x*x*x*h6+1/2*w*w*x*x*x*x*h5+1/8*w*w*x*x*x*x*h6+1/8*w*a*a*a*a*a*h7+1/8*w*a*a*a*a*x*h7-1/4*w*a*a*a*x*x*h7-1/4*w*a*a*x*x*x*h7+1/8*w*a*x*x*x*x*h7+1/8*w*x*x*x*x*x*h7-1/16*a*a*a*a*a*a*h6+3/16*a*a*a*a*x*x*h6-3/16*a*a*x*x*x*x*h6+1/16*x*x*x*x*x*x*h6-3/4*w*w*a*a*a*a*x*h7+1/2*w*w*a*a*x*x*x*h7+1/4*w*w*x*x*x*x*x*h7+1/16*w*a*a*a*a*a*a*h6+1/8*w*a*a*a*a*a*x*h6-1/16*w*a*a*a*a*x*x*h6-1/4*w*a*a*a*x*x*x*h6-1/16*w*a*a*x*x*x*x*h6+1/8*w*a*x*x*x*x*x*h6+1/16*w*x*x*x*x*x*x*h6+1/16*w*w*a*a*a*a*a*a*h6-1/8*w*w*a*a*a*a*a*x*h6-1/16*w*w*a*a*a*a*x*x*h6+1/4*w*w*a*a*a*x*x*x*h6-1/16*w*w*a*a*x*x*x*x*h6-1/8*w*w*a*x*x*x*x*x*h6+1/16*w*w*x*x*x*x*x*x*h6,-1/2*w-h4-w*h4-1/2*a*a-1/2*a*x-a*h5+x*x+x*h5+1/4*w*a*a+5/4*w*x*x+1/2*a*a*h4+1/4*a*a*h7-1/2*x*x*h4-1/4*x*x*h7-1/2*w*w*a*a+1/2*w*w*a*x+w*w*a*h5+w*w*x*x+w*w*x*h5+1/2*w*a*a*h4-1/4*w*a*a*h7-1/2*w*a*x*h7-1/2*w*x*x*h4-1/4*w*x*x*h7+1/16*a*a*a*a+1/4*a*a*a*x+1/2*a*a*a*h5+1/8*a*a*a*h6-3/8*a*a*x*x-1/2*a*a*x*h5+1/8*a*a*x*h6-1/4*a*x*x*x-1/2*a*x*x*h5-1/8*a*x*x*h6+5/16*x*x*x*x+1/2*x*x*x*h5-1/8*x*x*x*h6-1/4*w*w*a*a*h7+1/2*w*w*a*x*h7-1/4*w*w*x*x*h7-1/4*a*a*a*a*h7+1/2*a*a*x*x*h7-1/4*x*x*x*x*h7+1/16*w*w*a*a*a*a-1/4*w*w*a*a*a*x-1/2*w*w*a*a*a*h5-1/8*w*w*a*a*a*h6-3/8*w*w*a*a*x*x-1/2*w*w*a*a*x*h5+1/8*w*w*a*a*x*h6+1/4*w*w*a*x*x*x+1/2*w*w*a*x*x*h5+1/8*w*w*a*x*x*h6+5/16*w*w*x*x*x*x+1/2*w*w*x*x*x*h5-1/8*w*w*x*x*x*h6+1/8*w*a*a*a*a*h7+w*a*a*a*x*h7-3/4*w*a*a*x*x*h7-3/8*w*x*x*x*x*h7-1/8*a*a*a*a*a*h6-1/8*a*a*a*a*x*h6+1/4*a*a*a*x*x*h6+1/4*a*a*x*x*x*h6-1/8*a*x*x*x*x*h6-1/8*x*x*x*x*x*h6+1/8*w*w*a*a*a*a*h7-w*w*a*a*a*x*h7-3/4*w*w*a*a*x*x*h7-3/8*w*w*x*x*x*x*h7+3/8*w*a*a*a*a*x*h6-1/4*w*a*a*x*x*x*h6-1/8*w*x*x*x*x*x*h6+1/16*a*a*a*a*a*a*h7-3/16*a*a*a*a*x*x*h7+3/16*a*a*x*x*x*x*h7-1/16*x*x*x*x*x*x*h7+1/8*w*w*a*a*a*a*a*h6-1/8*w*w*a*a*a*a*x*h6-1/4*w*w*a*a*a*x*x*h6+1/4*w*w*a*a*x*x*x*h6+1/8*w*w*a*x*x*x*x*h6-1/8*w*w*x*x*x*x*x*h6-3/8*w*a*a*a*a*a*x*h7+3/8*w*a*a*a*a*x*x*h7+1/4*w*a*a*a*x*x*x*h7-1/4*w*a*a*x*x*x*x*h7+1/8*w*a*x*x*x*x*x*h7-1/8*w*x*x*x*x*x*x*h7+1/32*a*a*a*a*a*a*a*h6+1/32*a*a*a*a*a*a*x*h6-3/32*a*a*a*a*a*x*x*h6-3/32*a*a*a*a*x*x*x*h6+3/32*a*a*a*x*x*x*x*h6+3/32*a*a*x*x*x*x*x*h6-1/32*a*x*x*x*x*x*x*h6-1/32*x*x*x*x*x*x*x*h6+3/8*w*w*a*a*a*a*a*x*h7+3/8*w*w*a*a*a*a*x*x*h7-1/4*w*w*a*a*a*x*x*x*h7-1/4*w*w*a*a*x*x*x*x*h7-1/8*w*w*a*x*x*x*x*x*h7-1/8*w*w*x*x*x*x*x*x*h7-3/16*w*a*a*a*a*a*a*x*h6+5/16*w*a*a*a*a*x*x*x*h6-1/16*w*a*a*x*x*x*x*x*h6-1/16*w*x*x*x*x*x*x*x*h6-1/32*w*w*a*a*a*a*a*a*a*h6+1/32*w*w*a*a*a*a*a*a*x*h6+3/32*w*w*a*a*a*a*a*x*x*h6-3/32*w*w*a*a*a*a*x*x*x*h6-3/32*w*w*a*a*a*x*x*x*x*h6+3/32*w*w*a*a*x*x*x*x*x*h6+1/32*w*w*a*x*x*x*x*x*x*h6-1/32*w*w*x*x*x*x*x*x*x*h6,1-h7-w*h7-1/2*a*a-5/2*x*x+w*a*a-w*a*x-1/2*w*a*h6-2*w*x*x-1/2*w*x*h6-a*a*h4+1/2*a*a*h7+2*a*x*h4-x*x*h4-1/2*x*x*h7+w*w*a*a+w*w*a*x+1/2*w*w*a*h6-2*w*w*x*x-1/2*w*w*x*h6+w*a*a*h4+1/2*w*a*a*h7-w*x*x*h4-1/2*w*x*x*h7-w*w*a*a*h4-2*w*w*a*x*h4-w*w*x*x*h4-1/8*w*a*a*a*a+1/2*w*a*a*a*x+w*a*a*a*h5+1/4*w*a*a*a*h6+3/4*w*a*a*x*x-w*a*a*x*h5+1/4*w*a*a*x*h6-1/2*w*a*x*x*x-w*a*x*x*h5-1/4*w*a*x*x*h6-5/8*w*x*x*x*x+w*x*x*x*h5-1/4*w*x*x*x*h6+1/2*a*a*a*a*h4-4*a*a*a*x*h4-3*a*a*x*x*h4-3/2*x*x*x*x*h4-1/8*w*w*a*a*a*a-1/2*w*w*a*a*a*x-w*w*a*a*a*h5-1/4*w*w*a*a*a*h6+3/4*w*w*a*a*x*x-w*w*a*a*x*h5+1/4*w*w*a*a*x*h6+1/2*w*w*a*x*x*x+w*w*a*x*x*h5+1/4*w*w*a*x*x*h6-5/8*w*w*x*x*x*x+w*w*x*x*x*h5-1/4*w*w*x*x*x*h6-w*a*a*a*a*h4+2*w*a*a*x*x*h4-w*x*x*x*x*h4-3*a*a*a*a*x*h5+2*a*a*x*x*x*h5+x*x*x*x*x*h5+1/2*w*w*a*a*a*a*h4+4*w*w*a*a*a*x*h4-3*w*w*a*a*x*x*h4-3/2*w*w*x*x*x*x*h4-w*a*a*a*a*a*h5+w*a*a*a*a*x*h5+2*w*a*a*a*x*x*h5-2*w*a*a*x*x*x*h5-w*a*x*x*x*x*h5+w*x*x*x*x*x*h5+3/2*a*a*a*a*a*x*h4+3/2*a*a*a*a*x*x*h4-a*a*a*x*x*x*h4-a*a*x*x*x*x*h4-1/2*a*x*x*x*x*x*h4-1/2*x*x*x*x*x*x*h4+w*w*a*a*a*a*a*h5+w*w*a*a*a*a*x*h5-2*w*w*a*a*a*x*x*h5-2*w*w*a*a*x*x*x*h5+w*w*a*x*x*x*x*h5+w*w*x*x*x*x*x*h5+1/4*w*a*a*a*a*a*a*h4-3/4*w*a*a*a*a*x*x*h4+3/4*w*a*a*x*x*x*x*h4-1/4*w*x*x*x*x*x*x*h4+3/2*a*a*a*a*a*a*x*h5-5/2*a*a*a*a*x*x*x*h5+1/2*a*a*x*x*x*x*x*h5+1/2*x*x*x*x*x*x*x*h5-3/2*w*w*a*a*a*a*a*x*h4+3/2*w*w*a*a*a*a*x*x*h4+w*w*a*a*a*x*x*x*h4-w*w*a*a*x*x*x*x*h4+1/2*w*w*a*x*x*x*x*x*h4-1/2*w*w*x*x*x*x*x*x*h4+1/4*w*a*a*a*a*a*a*a*h5-1/4*w*a*a*a*a*a*a*x*h5-3/4*w*a*a*a*a*a*x*x*h5+3/4*w*a*a*a*a*x*x*x*h5+3/4*w*a*a*a*x*x*x*x*h5-3/4*w*a*a*x*x*x*x*x*h5-1/4*w*a*x*x*x*x*x*x*h5+1/4*w*x*x*x*x*x*x*x*h5-1/4*w*w*a*a*a*a*a*a*a*h5-1/4*w*w*a*a*a*a*a*a*x*h5+3/4*w*w*a*a*a*a*a*x*x*h5+3/4*w*w*a*a*a*a*x*x*x*h5-3/4*w*w*a*a*a*x*x*x*x*h5-3/4*w*w*a*a*x*x*x*x*x*h5+1/4*w*w*a*x*x*x*x*x*x*h5+1/4*w*w*x*x*x*x*x*x*x*h5,1/4*a+7/4*x+a*h4-x*h4+x*h7-1/4*w*w*a+7/4*w*w*x-w*a*h4-w*x*h4-1/8*a*a*a+5/8*a*a*x-1/4*a*a*h6+1/8*a*x*x-5/8*x*x*x+1/4*x*x*h6-w*a*a*h5+w*x*x*h5-a*a*a*h4+a*a*x*h4-1/2*a*a*x*h7+a*x*x*h4-x*x*x*h4+1/2*x*x*x*h7+1/8*w*w*a*a*a+5/8*w*w*a*a*x-1/4*w*w*a*a*h6-1/8*w*w*a*x*x-5/8*w*w*x*x*x+1/4*w*w*x*x*h6+w*a*a*a*h4+w*a*a*x*h4-w*a*x*x*h4-w*x*x*x*h4-1/2*a*a*a*a*h5+1/8*a*a*a*a*h6+a*a*a*x*h5-1/4*a*a*x*x*h6-a*x*x*x*h5+1/2*x*x*x*x*h5+1/8*x*x*x*x*h6-3*w*w*a*a*x*h4-w*w*x*x*x*h4+w*a*a*a*a*h5-2*w*a*a*x*x*h5+w*x*x*x*x*h5+1/4*a*a*a*a*a*h4-1/4*a*a*a*a*x*h4-1/2*a*a*a*x*x*h4+1/2*a*a*x*x*x*h4+1/4*a*x*x*x*x*h4-1/4*x*x*x*x*x*h4-1/2*w*w*a*a*a*a*h5+1/8*w*w*a*a*a*a*h6-w*w*a*a*a*x*h5-1/4*w*w*a*a*x*x*h6+w*w*a*x*x*x*h5+1/2*w*w*x*x*x*x*h5+1/8*w*w*x*x*x*x*h6-1/4*w*a*a*a*a*a*h4-1/4*w*a*a*a*a*x*h4+1/2*w*a*a*a*x*x*h4+1/2*w*a*a*x*x*x*h4-1/4*w*a*x*x*x*x*h4-1/4*w*x*x*x*x*x*h4+1/4*a*a*a*a*a*a*h5-1/2*a*a*a*a*a*x*h5-1/4*a*a*a*a*x*x*h5+a*a*a*x*x*x*h5-1/4*a*a*x*x*x*x*h5-1/2*a*x*x*x*x*x*h5+1/4*x*x*x*x*x*x*h5+3/2*w*w*a*a*a*a*x*h4-w*w*a*a*x*x*x*h4-1/2*w*w*x*x*x*x*x*h4-1/4*w*a*a*a*a*a*a*h5+3/4*w*a*a*a*a*x*x*h5-3/4*w*a*a*x*x*x*x*h5+1/4*w*x*x*x*x*x*x*h5+1/4*w*w*a*a*a*a*a*a*h5+1/2*w*w*a*a*a*a*a*x*h5-1/4*w*w*a*a*a*a*x*x*h5-w*w*a*a*a*x*x*x*h5-1/4*w*w*a*a*x*x*x*x*h5+1/2*w*w*a*x*x*x*x*x*h5+1/4*w*w*x*x*x*x*x*x*h5,-1/4-1/4*w-h4+1/8*a*a-3/4*a*x+5/8*x*x+1/8*w*a*a+3/4*w*a*x+5/8*w*x*x+a*a*h4-1/4*a*a*h7-1/2*a*x*h7-x*x*h4-1/4*x*x*h7+3/2*w*w*x*x-1/2*w*a*a*h4-w*a*x*h4-1/2*w*x*x*h4+1/2*a*a*a*h5-1/2*a*a*x*h5-1/2*a*x*x*h5+1/2*x*x*x*h5-1/2*w*w*a*a*h4-1/4*w*w*a*a*h7+w*w*a*x*h4+1/2*w*w*a*x*h7-1/2*w*w*x*x*h4-1/4*w*w*x*x*h7-1/2*w*a*a*a*h5-1/2*w*a*a*x*h5+1/2*w*a*x*x*h5+1/2*w*x*x*x*h5-1/4*a*a*a*a*h4+1/8*a*a*a*a*h7+1/4*a*a*a*x*h7+1/2*a*a*x*x*h4-1/4*a*x*x*x*h7-1/4*x*x*x*x*h4-1/8*x*x*x*x*h7+1/4*w*w*a*a*x*h6-1/4*w*w*x*x*x*h6+1/4*w*a*a*a*a*h4+1/2*w*a*a*a*x*h4-1/2*w*a*x*x*x*h4-1/4*w*x*x*x*x*h4-1/4*a*a*a*a*a*h5+1/4*a*a*a*a*x*h5+1/2*a*a*a*x*x*h5-1/2*a*a*x*x*x*h5-1/4*a*x*x*x*x*h5+1/4*x*x*x*x*x*h5+1/4*w*w*a*a*a*a*h4+1/8*w*w*a*a*a*a*h7-1/2*w*w*a*a*a*x*h4-1/4*w*w*a*a*a*x*h7+1/2*w*w*a*x*x*x*h4+1/4*w*w*a*x*x*x*h7-1/4*w*w*x*x*x*x*h4-1/8*w*w*x*x*x*x*h7+1/4*w*a*a*a*a*a*h5+1/4*w*a*a*a*a*x*h5-1/2*w*a*a*a*x*x*h5-1/2*w*a*a*x*x*x*h5+1/4*w*a*x*x*x*x*h5+1/4*w*x*x*x*x*x*h5-1/8*w*w*a*a*a*a*x*h6+1/4*w*w*a*a*x*x*x*h6-1/8*w*w*x*x*x*x*x*h6,-2*x-h5-1/8*w*a-1/8*w*x-1/2*a*h4-1/2*x*h4+1/8*w*w*a-1/8*w*w*x+5/8*a*a*x-5/8*x*x*x+1/2*w*w*a*h4-1/2*w*w*x*h4+1/16*w*a*a*a+7/16*w*a*a*x+11/16*w*a*x*x+5/16*w*x*x*x+1/4*a*a*a*h4+1/8*a*a*a*h7+1/4*a*a*x*h4+3/8*a*a*x*h7-1/4*a*x*x*h4+3/8*a*x*x*h7-1/4*x*x*x*h4+1/8*x*x*x*h7-1/16*w*w*a*a*a+7/16*w*w*a*a*x-11/16*w*w*a*x*x+5/16*w*w*x*x*x-1/8*w*a*a*a*h7+3/8*w*a*a*x*h7-3/8*w*a*x*x*h7+1/8*w*x*x*x*h7+1/4*a*a*a*a*h5-1/2*a*a*x*x*h5+1/4*x*x*x*x*h5-1/4*w*w*a*a*a*h4+1/4*w*w*a*a*x*h4+1/4*w*w*a*x*x*h4-1/4*w*w*x*x*x*h4-1/16*w*a*a*a*a*h6+1/8*w*a*a*a*x*h6-1/8*w*a*x*x*x*h6+1/16*w*x*x*x*x*h6-1/16*a*a*a*a*a*h7-3/16*a*a*a*a*x*h7-1/8*a*a*a*x*x*h7+1/8*a*a*x*x*x*h7+3/16*a*x*x*x*x*h7+1/16*x*x*x*x*x*h7-1/16*w*w*a*a*a*a*h6-1/8*w*w*a*a*a*x*h6+1/8*w*w*a*x*x*x*h6+1/16*w*w*x*x*x*x*h6+1/16*w*a*a*a*a*a*h7-3/16*w*a*a*a*a*x*h7+1/8*w*a*a*a*x*x*h7+1/8*w*a*a*x*x*x*h7-3/16*w*a*x*x*x*x*h7+1/16*w*x*x*x*x*x*h7+1/32*w*a*a*a*a*a*a*h6-1/16*w*a*a*a*a*a*x*h6-1/32*w*a*a*a*a*x*x*h6+1/8*w*a*a*a*x*x*x*h6-1/32*w*a*a*x*x*x*x*h6-1/16*w*a*x*x*x*x*x*h6+1/32*w*x*x*x*x*x*x*h6+1/32*w*w*a*a*a*a*a*a*h6+1/16*w*w*a*a*a*a*a*x*h6-1/32*w*w*a*a*a*a*x*x*h6-1/8*w*w*a*a*a*x*x*x*h6-1/32*w*w*a*a*x*x*x*x*h6+1/16*w*w*a*x*x*x*x*x*h6+1/32*w*w*x*x*x*x*x*x*h6};
assert all({0,1,2,3,12,13,14,15},i->actual#i==0);
assert(take(drop(actual,4),8)==exported);
print("PRIMITIVE_LINE_SAVED_FIRST_EXACT_MATCH");
-- Reconstruct trace and determinant directly from factor matrices.
M1=matrix{{-1,-D1},{A1,1}};M2=matrix{{-1,-D2},{A2,w}};
N=matrix{{1,D1},{-A1,-1}}*M2;
tau=trace N;de=det N;
assert(tau==-w^2*(a^2+x^2)-1-w);
assert(de==w*((a^2-x^2-2)/2)^2);
disc=tau^2-4*de;
expectedDisc=w*(2*a^2-3)*(2*x^2+1);
assert(disc==expectedDisc);
print("PRIMITIVE_LINE_TRACE_DETERMINANT_OPEN_MATCH");
K=QQ;
R=K[h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,t];
w=1_R;
-- Direct multiplication of (t+z)u+zv and (-2w^2+z)u-w^2*t*z*v/2.
ff={-2*w^2*t,t-2*w^2,1,0,-w^2*(t^2/2+2),1-w^2*t/2,0,0,-w^2*t/2};
phi=map(R,U,join(ff,{h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11}));
actual=apply(universalFirst,e->phi(e));
exported={-h0-h1*t-6*w*w+2*h1*w*w+10*t*w*w+2*h2*t*w*w-3/2*t*t*w*w,3-h1-4*t-h2*t+8*w*w+2*h2*w*w-3/2*t*w*w+2*h3*t*w*w,-3-h2-h3*t+2*h3*w*w+2*h4*t*w*w,-h3-h4*t+2*h4*w*w+2*h5*t*w*w,-h0-h6-h7*t+2*h1*w*w+2*h7*w*w+1/2*h0*t*w*w+2*h8*t*w*w+1/2*h1*t*t*w*w,-h1-h7-h8*t+5*w*w+2*h2*w*w+2*h8*w*w+9*t*w*w+1/2*h1*t*w*w+2*h9*t*w*w+5/4*t*t*w*w+1/2*h2*t*t*w*w,-3/2-h2-h8-11/2*t-h9*t+11*w*w+2*h3*w*w+2*h9*w*w+3/4*t*w*w+1/2*h2*t*w*w+2*h10*t*w*w+1/2*h3*t*t*w*w,-5-h3-h9-h10*t+2*h4*w*w+2*h10*w*w+1/2*h3*t*w*w+2*h11*t*w*w+1/2*h4*t*t*w*w,-h6+2*h7*w*w+1/2*h0*t*w*w+1/2*h6*t*w*w+1/2*h7*t*t*w*w,-h7+2*h8*w*w+1/2*h1*t*w*w+1/2*h7*t*w*w+1/2*h8*t*t*w*w,-h8+19/2*w*w+2*h9*w*w+3/2*t*w*w+1/2*h2*t*w*w+1/2*h8*t*w*w+19/8*t*t*w*w+1/2*h9*t*t*w*w,-17/4-h9-3/4*t+3/2*w*w+2*h10*w*w+17/8*t*w*w+1/2*h3*t*w*w+1/2*h9*t*w*w+1/2*h10*t*t*w*w,1/2*h6*t*w*w,1/2*h7*t*w*w,1/2*h8*t*w*w,3/4*w*w+7/4*t*w*w+1/2*h9*t*w*w+3/16*t*t*w*w};
assert(actual==exported);
print("W1_BOUNDARY_SAVED_FIRST_EXACT_MATCH");
A1=t;D1=1;A2=-2*w^2;D2=-w^2*t/2;
N=matrix{{1,D1},{-A1,0}}*matrix{{0,-D2},{A2,1}};
tau=trace N;de=det N;
assert(tau==-w^2*(t^2/2+2));assert(de==w*t^2);
assert(tau^2-4*de==w*(t^2-4)^2/4);
print("W1_BOUNDARY_TRACE_DETERMINANT_OPEN_MATCH");
K=toField(QQ[ww]/ideal(ww^2+ww+1));
R=K[h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,t];
w=sub(K_0,R);
-- Direct multiplication of (t+z)u+zv and (-2w^2+z)u-w^2*t*z*v/2.
ff={-2*w^2*t,t-2*w^2,1,0,-w^2*(t^2/2+2),1-w^2*t/2,0,0,-w^2*t/2};
phi=map(R,U,join(ff,{h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11}));
actual=apply(universalFirst,e->phi(e));
exported={-h0-h1*t-6*w*w+2*h1*w*w+10*t*w*w+2*h2*t*w*w-3/2*t*t*w*w,3-h1-4*t-h2*t+8*w*w+2*h2*w*w-3/2*t*w*w+2*h3*t*w*w,-3-h2-h3*t+2*h3*w*w+2*h4*t*w*w,-h3-h4*t+2*h4*w*w+2*h5*t*w*w,-h0-h6-h7*t+2*h1*w*w+2*h7*w*w+1/2*h0*t*w*w+2*h8*t*w*w+1/2*h1*t*t*w*w,-h1-h7-h8*t+5*w*w+2*h2*w*w+2*h8*w*w+9*t*w*w+1/2*h1*t*w*w+2*h9*t*w*w+5/4*t*t*w*w+1/2*h2*t*t*w*w,-3/2-h2-h8-11/2*t-h9*t+11*w*w+2*h3*w*w+2*h9*w*w+3/4*t*w*w+1/2*h2*t*w*w+2*h10*t*w*w+1/2*h3*t*t*w*w,-5-h3-h9-h10*t+2*h4*w*w+2*h10*w*w+1/2*h3*t*w*w+2*h11*t*w*w+1/2*h4*t*t*w*w,-h6+2*h7*w*w+1/2*h0*t*w*w+1/2*h6*t*w*w+1/2*h7*t*t*w*w,-h7+2*h8*w*w+1/2*h1*t*w*w+1/2*h7*t*w*w+1/2*h8*t*t*w*w,-h8+19/2*w*w+2*h9*w*w+3/2*t*w*w+1/2*h2*t*w*w+1/2*h8*t*w*w+19/8*t*t*w*w+1/2*h9*t*t*w*w,-17/4-h9-3/4*t+3/2*w*w+2*h10*w*w+17/8*t*w*w+1/2*h3*t*w*w+1/2*h9*t*w*w+1/2*h10*t*t*w*w,1/2*h6*t*w*w,1/2*h7*t*w*w,1/2*h8*t*w*w,3/4*w*w+7/4*t*w*w+1/2*h9*t*w*w+3/16*t*t*w*w};
assert(actual==exported);
print("PRIMITIVE_BOUNDARY_SAVED_FIRST_EXACT_MATCH");
A1=t;D1=1;A2=-2*w^2;D2=-w^2*t/2;
N=matrix{{1,D1},{-A1,0}}*matrix{{0,-D2},{A2,1}};
tau=trace N;de=det N;
assert(tau==-w^2*(t^2/2+2));assert(de==w*t^2);
assert(tau^2-4*de==w*(t^2-4)^2/4);
print("PRIMITIVE_BOUNDARY_TRACE_DETERMINANT_OPEN_MATCH");
-- Exact Cayley-Hamilton U_11 recurrence and scalar-matrix scheme.
R=QQ[tau,de];u0=1_R;u1=tau;
scan(2..11,i->(ui=tau*u1-de*u0;u0=u1;u1=ui));
q=tau*(tau^2-de)*(tau^2-2*de)*(tau^2-3*de)*((tau^2-2*de)^2-3*de^2);
assert(u1==q);print("Q12_EXACT_RECURRENCE_MATCH");
