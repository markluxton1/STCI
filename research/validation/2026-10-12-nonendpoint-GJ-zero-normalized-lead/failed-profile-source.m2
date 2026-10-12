S=QQ[s];
K=toField(S/ideal(s^2-3));
coeffRing=K[k,del];
R=coeffRing[p];
Elinear=(1+3*k)*p-3-6*k;
V=(p*(p^2-3*p+3)*Elinear^2-9*del*(p-2)*(k*p^2-2*k*p-1)*(2*k^2*p^2-6*k^2*p+k*p^2+6*k^2-4*k*p+6*k+1));
cc=apply(0..5,j->sub(coefficient(p^j,V),coeffRing));
leadC=last cc;
units=k*del*leadC;
for i from 0 to 5 do for j from 0 to 5-i do (
    kk=5-i-j;
    profile=p^i*(p-(3+s))^j*(p-(3-s))^kk;
    hc=apply(0..4,t->sub(coefficient(p^t,profile),coeffRing));
    II=ideal apply(0..4,t->cc#t-leadC*hc#t);
    JJ=saturate(II,ideal units);
    print ((i,j,kk),toString mingens JJ);
);
