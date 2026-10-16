-- NEW degree-five characteristic and unified ODE residual identities.
-- The accepted degree-six characteristic polynomial is a premise;
-- its characteristic/Cayley-Hamilton verifier is deliberately not rerun.
outDir="research/validation/2026-10-15-quintic-h2-unified-spectral-accelerator/attempt-01";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
A=QQ[v,w,u,d,q0,q1,q2,q3,q4,q5,q6];
qf={q0,q1,q2,q3,q4,q5,q6};
qi=i->if i<0 or i>6 then 0_A else qf#i;
disc=v^2-4*w;
actMatrix=n->matrix apply(toList(0..n),i->apply(toList(0..n),k->(
 if k==i then (n-2*i)*v
 else if k==i-1 then 2*n-2*i+2
 else if k==i+1 then -2*(i+1)*w
 else 0_A)));
A5=actMatrix(5);
xiRing=A[xi];
charFive=det(xi*id_(xiRing^6)-sub(A5,xiRing));
expectedFive=(xi^2-disc)*(xi^2-9*disc)*(xi^2-25*disc);
assert(charFive==expectedFive);
idFive=id_(A^6); sqFive=A5*A5;
chFive=(sqFive-disc*idFive)*(sqFive-9*disc*idFive)*(sqFive-25*disc*idFive);
assert(all(flatten entries chFive,x->x==0));
save("new-Sym5-action-matrix",A5);
save("new-Sym5-characteristic-polynomial",charFive);
print "PASS NEW Sym5 six-by-six characteristic polynomial and Cayley-Hamilton identity";
eta=d*v-2*u; dp=(d-5)*(d-6); eSix=d-5; eFive=6-d;
assert(eSix+eFive==1);
assert(eSix*eFive==-dp);
assert(eSix^2-eSix==dp and eFive^2-eFive==dp);
assert(eSix*(d-6)==dp and eFive*(d-5)==-dp);
ec=apply(toList(0..7),i->w*(i+1)*qi(i+1)+(v*i-u)*qi(i)+(i-1-d)*qi(i-1));
assert(ec#7==eFive*q6);
A6=actMatrix(6);
qSix=transpose matrix{qf}; qFive=transpose matrix{take(qf,6)};
eSixVec=transpose matrix{take(ec,7)}; eFiveVec=transpose matrix{take(ec,6)};
bSix=transpose matrix{apply(toList(0..6),i->2*qi(i-1)+v*qi(i))};
bFive=transpose matrix{apply(toList(0..5),i->2*qi(i-1)+v*qi(i))};
lastFive=transpose matrix{{0_A,0_A,0_A,0_A,0_A,1_A}};
resSix=eSix*(A6-eta*id_(A^7))*qSix+2*eSix*eSixVec+dp*bSix;
resFive=eFive*(A5-eta*id_(A^6))*qFive+2*eFive*eFiveVec-dp*bFive-12*w*(ec#7)*lastFive;
assert(all(flatten entries resSix,x->x==0));
assert(all(flatten entries resFive,x->x==0));
print "PASS unified idempotent algebra and both exact projected eigen-residual identities";
P6=eta*(eta^2-4*disc)*(eta^2-16*disc)*(eta^2-36*disc);
P5=(eta^2-disc)*(eta^2-9*disc)*(eta^2-25*disc);
unified=(d-5)*P6+(6-d)*P5;
save("unified-spectral-accelerator",unified);
save("degree-five-spectral-factor",P5);
save("accepted-degree-six-spectral-factor",P6);
save("idempotents-and-degree-polynomial",matrix{{eSix,eFive,dp}});
save("degree-six-residual-zero",resSix);
save("degree-five-residual-zero",resFive);
print "COMPLETE NEW unified spectral identities; accepted Sym6 characteristic is only a premise";
exit 0;
