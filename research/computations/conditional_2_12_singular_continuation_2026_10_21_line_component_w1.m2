-- Exact w=1,y=x generic norm component, p=a^2; p nonzero.
R=QQ[h4,h5,h6,h7,p,x,MonomialOrder=>Eliminate 4];
firstEquations={-h6-9*x+2*h7*x+6*p*x-6*h4*p*x-2*h5*p*p+1/4*h6*p*p-h7*p*x+3*h4*p*p*x-2*h4*x*x*x+h5*p*p*p-1/2*h6*p*x*x+h7*x*x*x-2*h4*p*x*x*x-h5*p*p*x*x+2*h5*x*x*x*x+1/4*h6*x*x*x*x-h4*x*x*x*x*x-h5*p*x*x*x*x+h5*x*x*x*x*x*x,1-h7-1/2*p-2*h4*p-11/2*x*x+h4*p*p-2*h4*x*x-2*h5*p*x+1/2*h6*p*x+1/4*h7*p*p-2*h7*x*x+h5*p*p*x+2*h5*x*x*x-1/4*h6*p*p*x-1/2*h6*x*x*x+1/2*h7*p*x*x-h4*x*x*x*x-2*h5*p*x*x*x+1/2*h6*p*x*x*x-3/4*h7*x*x*x*x+h5*x*x*x*x*x-1/4*h6*x*x*x*x*x,7/2*x-2*h4*x-2*h5*p-1/4*h6*p+h7*x+5/4*p*x+h4*p*x+h5*p*p+2*h5*x*x+1/4*h6*x*x+1/2*h7*p*x-5/4*x*x*x-h4*x*x*x-2*h5*p*x*x+1/16*h6*p*p*p-1/2*h6*p*x*x-1/2*h7*p*p*x+3/2*h7*x*x*x+h5*x*x*x*x+1/16*h6*p*p*x*x+1/2*h6*x*x*x*x-5/16*h6*p*x*x*x*x+1/2*h7*x*x*x*x*x+3/16*h6*x*x*x*x*x*x,-1/2-2*h4-3/4*p+h4*p+2*h5*x-1/4*h7*p+1/8*p*p+13/4*x*x-h4*x*x-h5*p*x+1/4*h6*p*x-3/4*h7*x*x-3/4*p*x*x+h5*x*x*x+1/8*h6*p*p*x-1/4*h6*x*x*x+1/16*h7*p*p*p-h7*p*x*x+5/8*x*x*x*x-1/8*h6*p*p*p*x+1/4*h6*p*x*x*x+9/16*h7*p*p*x*x-h7*x*x*x*x+1/8*h6*p*p*x*x*x-3/8*h6*x*x*x*x*x-5/16*h7*p*x*x*x*x+1/8*h6*p*x*x*x*x*x-5/16*h7*x*x*x*x*x*x-1/8*h6*x*x*x*x*x*x*x,1-2*h7+3/2*p-h4*p-h6*x+h7*p-1/4*p*p-13/2*x*x-3*h4*x*x-2*h5*p*x+1/2*h6*p*x-h7*x*x+3/2*p*x*x+1/4*h4*p*p*p-4*h4*p*x*x-h5*p*p*x+2*h5*x*x*x-1/2*h6*x*x*x-5/4*x*x*x*x+9/4*h4*p*p*x*x-4*h4*x*x*x*x+h5*p*p*p*x-2*h5*p*x*x*x-5/4*h4*p*x*x*x*x-h5*p*p*x*x*x+3*h5*x*x*x*x*x-5/4*h4*x*x*x*x*x*x-h5*p*x*x*x*x*x+h5*x*x*x*x*x*x*x,7/2*x-2*h4*x-h5*p-1/2*h6*p+h7*x+5/4*p*x-h4*p*x+h5*x*x+1/4*h6*p*p+1/2*h6*x*x-1/2*h7*p*x-5/4*x*x*x+h4*p*p*x-3*h4*x*x*x+1/4*h5*p*p*p-2*h5*p*x*x-1/2*h6*p*x*x+1/2*h7*x*x*x+1/4*h5*p*p*x*x+2*h5*x*x*x*x+1/4*h6*x*x*x*x-h4*x*x*x*x*x-5/4*h5*p*x*x*x*x+3/4*h5*x*x*x*x*x*x,-1/2-h4+1/4*p-1/2*h7*p+11/4*x*x+1/4*h4*p*p-2*h4*x*x-h5*p*x+1/4*h6*p*x+1/4*h7*p*p-1/2*h7*x*x+1/2*h4*p*x*x+1/2*h5*p*p*x+h5*x*x*x-1/8*h6*p*p*x-1/4*h6*x*x*x-3/4*h4*x*x*x*x-h5*p*x*x*x+1/4*h6*p*x*x*x-1/4*h7*x*x*x*x+1/2*h5*x*x*x*x*x-1/8*h6*x*x*x*x*x,-h5-9/4*x-h4*x+3/2*p*x+1/2*h4*p*x+1/4*h5*p*p-1/8*h6*p*p+3/4*h7*p*x-1/2*h4*x*x*x-1/2*h5*p*x*x+1/16*h6*p*p*p-3/8*h7*p*p*x+1/4*h7*x*x*x+1/4*h5*x*x*x*x-1/16*h6*p*p*x*x+1/8*h6*x*x*x*x+1/4*h7*p*x*x*x-1/16*h6*p*x*x*x*x+1/8*h7*x*x*x*x*x+1/16*h6*x*x*x*x*x*x};
I=ideal firstEquations;
print("W1_LINE_FIRST_ELIMINATION_START");
E=eliminate({h4,h5,h6,h7},I);
print("W1_LINE_FIRST_ELIMINATION_READY");print gens E;
S=QQ[p,x];phi=map(S,R,{0,0,0,0,p,x});
ES=ideal phi(gens E);
tau=-(p+x^2+2);delta=((p-x^2-2)/2)^2;
q=tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)*((tau^2-2*delta)^2-3*delta^2);
op=p*(2*x^2+1)*(p-x^2-2)*(x^2+2);
J=saturate(ES+ideal(q),ideal(op));
print("W1_LINE_FIRST_TORSION_RESULT");print gens gb J;
