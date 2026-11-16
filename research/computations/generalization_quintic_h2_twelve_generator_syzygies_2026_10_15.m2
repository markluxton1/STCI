-- NEW universal coefficient identities for one shared support system.
-- No actual conductor/map coefficients or accepted verifier are replayed.
outDir="research/validation/2026-10-15-quintic-h2-twelve-generator-reduction/attempt-02";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
R=QQ[q0,q1,q2,q3,q4,q5,q6,r0,r1,r2,r3,r4,r5,r6,j,v,w];
qf={q0,q1,q2,q3,q4,q5,q6}; rf={r0,r1,r2,r3,r4,r5,r6};
qi=i->if i<0 or i>6 then 0_R else qf#i;
ri=i->if i<0 or i>6 then 0_R else rf#i;
mi=(i,k)->qi(i)*ri(k)-qi(k)*ri(i);
di=(i,k)->qi(i)*qi(k-1)-qi(k)*qi(i-1);
bi=(i,k,l)->qi(i)*qi(k-1)*ri(l)-qi(i)*qi(l-1)*ri(k)-qi(k)*qi(i-1)*ri(l)+qi(k)*qi(l-1)*ri(i)+qi(l)*qi(i-1)*ri(k)-qi(l)*qi(k-1)*ri(i);
coeffMatrix=transpose matrix{apply(toList(0..7),i->qi(i)),apply(toList(0..7),i->qi(i-1)),apply(toList(0..7),i->ri(i))};
triples=subsets(toList(0..7),3);
scan(triples,ijk->assert(bi(ijk#0,ijk#1,ijk#2)==det submatrix(coeffMatrix,ijk,{0,1,2})));
scan(subsets(toList(0..6),3),ijk->assert(bi(ijk#0,ijk#1,ijk#2)==-qi(ijk#0-1)*mi(ijk#1,ijk#2)+qi(ijk#1-1)*mi(ijk#0,ijk#2)-qi(ijk#2-1)*mi(ijk#0,ijk#1)));
scan(subsets(toList(0..6),2),ik->assert(bi(ik#0,ik#1,7)==-q6*mi(ik#0,ik#1)));
print "PASS universal cubic expansions and row-seven identities";
assert(di(5,6)==q5^2-q4*q6);
assert(di(6,7)==q6^2);
scan({{5,6},{6,7}},ab->scan(triples,ijk->(
 i:=ijk#0; k:=ijk#1; l:=ijk#2; a:=ab#0; b:=ab#1;
 assert(di(a,b)*bi(i,k,l)==di(k,l)*bi(i,a,b)-di(i,l)*bi(k,a,b)+di(i,k)*bi(l,a,b));
 )));
print "PASS both fixed-pivot identities for all 56 cubic minors";
scan(toList(0..4),i->(
 assert(di(5,6)*j*mi(i,6)==(q5*qi(i)-q6*qi(i-1))*j*mi(5,6)-j*q6*bi(i,5,6));
 assert(q6*mi(i,5)==q5*mi(i,6)-qi(i)*mi(5,6));
 assert(q5*mi(i,5)==-bi(i,5,6)-qi(i-1)*mi(5,6)+q4*mi(i,6));
 ));
scan(subsets(toList(0..6),2),ik->scan({5,6},a->assert(qi(a)*mi(ik#0,ik#1)==qi(ik#1)*mi(ik#0,a)-qi(ik#0)*mi(ik#1,a))));
print "PASS first-minor absorption identities with j retained";
pivotTriples=join(apply(toList(0..4),i->{i,5,6}),apply(toList(0..5),i->{i,6,7}));
assert(#pivotTriples==11);
sharedGenerators=prepend(j*mi(5,6),apply(pivotTriples,ijk->bi(ijk#0,ijk#1,ijk#2)));
save("universal-twelve-generators",matrix{sharedGenerators});
save("pivot-row-triples",pivotTriples);
save("pivot-determinants",matrix{{di(5,6),di(6,7)}});
actionRing=R[s,t];
Q=sum(toList(0..6),i->qi(i)*s^(6-i)*t^i);
H=t^2+v*s*t+w*s^2;
actionR=diff(t,H)*diff(s,Q)-diff(s,H)*diff(t,Q);
actionW=diff(t,s*H)*diff(s,Q)-diff(s,s*H)*diff(t,Q);
assert(actionW==(3/2)*s*actionR-3*diff(t,H)*Q);
actionRf=apply(toList(0..6),i->coefficient(s^(6-i)*t^i,actionR));
assert(q5*actionRf#6-q6*actionRf#5==2*(q5^2-v*q5*q6-2*q4*q6+6*w*q6^2));
save("action-first-generator",j*(q5^2-v*q5*q6-2*q4*q6+6*w*q6^2));
print "PASS homogeneous Hamiltonian Euler identity and compact jM56 formula";
print "COMPLETE universal twelve-generator reduction identities; no elimination";
exit 0;
