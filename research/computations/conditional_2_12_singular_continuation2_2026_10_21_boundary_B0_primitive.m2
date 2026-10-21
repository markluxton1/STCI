K=toField(QQ[ww]/ideal(ww^2+ww+1));
-- Full nonzero-kappa B=0 boundary; C1=C2=D1=1, parameter t.
R=K[h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,t,MonomialOrder=>Eliminate 12];
w=sub(K_0,R);
firstEquations={-h0-h1*t-6*w*w+2*h1*w*w+10*t*w*w+2*h2*t*w*w-3/2*t*t*w*w,3-h1-4*t-h2*t+8*w*w+2*h2*w*w-3/2*t*w*w+2*h3*t*w*w,-3-h2-h3*t+2*h3*w*w+2*h4*t*w*w,-h3-h4*t+2*h4*w*w+2*h5*t*w*w,-h0-h6-h7*t+2*h1*w*w+2*h7*w*w+1/2*h0*t*w*w+2*h8*t*w*w+1/2*h1*t*t*w*w,-h1-h7-h8*t+5*w*w+2*h2*w*w+2*h8*w*w+9*t*w*w+1/2*h1*t*w*w+2*h9*t*w*w+5/4*t*t*w*w+1/2*h2*t*t*w*w,-3/2-h2-h8-11/2*t-h9*t+11*w*w+2*h3*w*w+2*h9*w*w+3/4*t*w*w+1/2*h2*t*w*w+2*h10*t*w*w+1/2*h3*t*t*w*w,-5-h3-h9-h10*t+2*h4*w*w+2*h10*w*w+1/2*h3*t*w*w+2*h11*t*w*w+1/2*h4*t*t*w*w,-h6+2*h7*w*w+1/2*h0*t*w*w+1/2*h6*t*w*w+1/2*h7*t*t*w*w,-h7+2*h8*w*w+1/2*h1*t*w*w+1/2*h7*t*w*w+1/2*h8*t*t*w*w,-h8+19/2*w*w+2*h9*w*w+3/2*t*w*w+1/2*h2*t*w*w+1/2*h8*t*w*w+19/8*t*t*w*w+1/2*h9*t*t*w*w,-17/4-h9-3/4*t+3/2*w*w+2*h10*w*w+17/8*t*w*w+1/2*h3*t*w*w+1/2*h9*t*w*w+1/2*h10*t*t*w*w,1/2*h6*t*w*w,1/2*h7*t*w*w,1/2*h8*t*w*w,3/4*w*w+7/4*t*w*w+1/2*h9*t*w*w+3/16*t*t*w*w};
I=ideal firstEquations;
E=eliminate({h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11},I);
print("BOUNDARY_B0_FIRST_ELIMINATION");print gens E;
S=K[t];phi=map(S,R,{0,0,0,0,0,0,0,0,0,0,0,0,t});
ES=ideal phi(gens E);
w=sub(K_0,S);
tau=-w^2*(t^2/2+2);delta=w*t^2;
q=tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)*((tau^2-2*delta)^2-3*delta^2);
J=saturate(ES+ideal(q),ideal(t*(t^2-4)));
print("BOUNDARY_B0_FIRST_TORSION_RESULT");print gens gb J;
