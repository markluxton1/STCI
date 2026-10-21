-- One full-dimensional factor chart A1=A2=1; other charts retained.
S=QQ[h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,B1,C1,D1,B2,C2,D2,MonomialOrder=>Eliminate 12];
firstEquations={-5-h2+3*D1+3*D2-h1*C1-h1*C2+3*B1*C2+3*C1*B2-h0*C1*C2,-h3-4*C1-4*C2-h2*C1-h2*C2+3*C1*D2+3*D1*C2-h1*C1*C2,-h4-h3*C1-h3*C2-3*C1*C2-h2*C1*C2,-h5-h4*C1-h4*C2-h3*C1*C2,-h8-7/2*B1-7/2*B2-h1*D1-h1*D2-h2*B1-h2*B2-h7*C1-h7*C2+6*B1*D2+6*D1*B2-h0*C1*D2-h0*D1*C2-h1*B1*C2-h1*C1*B2-h6*C1*C2,-6-h9-5/2*D1-5/2*D2-h2*D1-h2*D2-h3*B1-h3*B2-h8*C1-h8*C2-5/2*B1*C2-5/2*C1*B2+6*D1*D2-h1*C1*D2-h1*D1*C2-h2*B1*C2-h2*C1*B2-h7*C1*C2,-h10-11/2*C1-11/2*C2-h3*D1-h3*D2-h4*B1-h4*B2-h9*C1-h9*C2-3/2*C1*D2-3/2*D1*C2-h2*C1*D2-h2*D1*C2-h3*B1*C2-h3*C1*B2-h8*C1*C2,-h11-h4*D1-h4*D2-h5*B1-h5*B2-h10*C1-h10*C2-5*C1*C2-h3*C1*D2-h3*D1*C2-h4*B1*C2-h4*C1*B2-h9*C1*C2,-h7*D1-h7*D2-h8*B1-h8*B2-2*B1*B2-h0*D1*D2-h1*B1*D2-h1*D1*B2-h2*B1*B2-h6*C1*D2-h6*D1*C2-h7*B1*C2-h7*C1*B2,-21/4*B1-21/4*B2-h8*D1-h8*D2-h9*B1-h9*B2-B1*D2-D1*B2-h1*D1*D2-h2*B1*D2-h2*D1*B2-h3*B1*B2-h7*C1*D2-h7*D1*C2-h8*B1*C2-h8*C1*B2,-3/4-19/4*D1-19/4*D2-h9*D1-h9*D2-h10*B1-h10*B2-19/4*B1*C2-19/4*C1*B2-h2*D1*D2-h3*B1*D2-h3*D1*B2-h4*B1*B2-h8*C1*D2-h8*D1*C2-h9*B1*C2-h9*C1*B2,-3/4*C1-3/4*C2-h10*D1-h10*D2-h11*B1-h11*B2-17/4*C1*D2-17/4*D1*C2-h3*D1*D2-h4*B1*D2-h4*D1*B2-h5*B1*B2-h9*C1*D2-h9*D1*C2-h10*B1*C2-h10*C1*B2,-h6*D1*D2-h7*B1*D2-h7*D1*B2-h8*B1*B2,-9/2*B1*B2-h7*D1*D2-h8*B1*D2-h8*D1*B2-h9*B1*B2,-3/8*B1-3/8*B2-4*B1*D2-4*D1*B2-h8*D1*D2-h9*B1*D2-h9*D1*B2-h10*B1*B2,-3/8*D1-3/8*D2-3/8*B1*C2-3/8*C1*B2-7/2*D1*D2-h9*D1*D2-h10*B1*D2-h10*D1*B2-h11*B1*B2};
I=ideal firstEquations;
print("GENERAL_PATCH_FIRST_ELIMINATION_START");
E=eliminate({h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11},I);
print("GENERAL_PATCH_FIRST_ELIMINATION_READY");print gens E;
tau=D1+D2-B1*C2-C1*B2;
delta=D1*D2-B1*C1*D2-D1*B2*C2+B1*C1*B2*C2;
-- Defer the degree22 torsion expansion until after first elimination.
torsionEquation=tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)*((tau^2-2*delta)^2-3*delta^2);
twoNodeOpen=delta*(tau^2-4*delta);
J=saturate(E+ideal(torsionEquation),ideal(twoNodeOpen));
print("GENERAL_PATCH_TORSION_SATURATION_READY");print gens gb J;
print("GENERAL_PATCH_DIMENSION");print dim J;
