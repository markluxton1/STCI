-- Exact w=1 generic norm-symbol conic component; no arbitrary ruling action.
load "/Users/markluxton/Projects/STCI/research/computations/conditional_2_12_singular_continuation_2026_10_21.m2";
T=QQ[h4,h5,h6,h7,A2,a,x,y,MonomialOrder=>Eliminate 5];
phi=map(T,R,{1,a-x,(a+x)/2,A2,y+A2/2,h4,h5,h6,h7,0,0});
I=ideal join(apply(firstEquations,p->phi p),apply(normSymbolEquations,p->phi p),{2*(x^2+x*y+y^2)+3});
print("W1_CONIC_FIRST_ELIMINATION_START");
E=eliminate({h4,h5,h6,h7,A2},I);
print("W1_CONIC_FIRST_ELIMINATION_READY");
S=QQ[a,x,y];psi=map(S,T,{0,0,0,0,0,a,x,y});
ES=ideal psi(gens E);
print("ELIMINATED_GENERATOR_COUNT="|toString(numgens ES));
print("ELIMINATED_DIMENSION="|toString(dim ES));
L=x^2+2;nA=a-(L+a*x)*y;nD=a+(L-a*x)*y;
tauN=(a-x)*nD/2+nA*(a+x)/2-2*L;
deltaN=((a^2-x^2-2)/2)*(nA*nD/2-L^2);
op=a*(2*x^2+1)*L*(a^2-x^2-2)*(nA*nD/2-L^2)*(tauN^2-4*deltaN);
J0=saturate(ES,ideal(op));G=gb J0;
print("W1_CONIC_FIRST_ON_OPEN");print(numgens J0,dim J0,(1%G)==0);
-- Weighted-homogeneous clearing: Q12(tauN,deltaN)=L^11*Q12(tau,delta).
q=tauN%G;ts=tauN^2%G;de=deltaN%G;
scan({ts-de,ts-2*de,ts-3*de,(ts-2*de)^2-3*de^2},p->q=(q*p)%G);
J=saturate(J0+ideal(q),ideal(op));
print("W1_CONIC_FIRST_TORSION_RESULT");print gens gb J;
