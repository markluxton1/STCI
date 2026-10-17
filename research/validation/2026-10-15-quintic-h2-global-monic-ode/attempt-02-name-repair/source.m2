-- NEW denominator-free global monic h2 incidence export; no GB/saturation.
-- Accepted actual primitive conductor is an input, not reconstructed.
outDir="research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-02-name-repair";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
base=QQ[delta,a,B,G,J,vH2,wH2,h2DGlobal,h2EtaGlobal];
actual=base[p];
F=value get "research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt";
f=apply(toList(0..8),i->lift(coefficient(p^i,F),base));
q=new MutableList from toList(7:0_base);
qi=i->if i<0 or i>6 then 0_base else q#i;
scan(reverse toList(0..6),i->q#i=f#(6-i)-vH2*qi(i+1)-wH2*qi(i+2));
q=toList q;
frem={f#8-wH2*qi(0),f#7-vH2*qi(0)-wH2*qi(1)};
Plead=G; Pconstant=6*B+delta^2-3*delta-vH2*G;
Jlead=G+2*J; Jconstant=6*B+3*G+5*delta^2-3*delta-vH2*(G+2*J);
h2CoverEquations={-2*a-wH2*Pconstant,
       3*a-3*B+2*delta-vH2*Pconstant-wH2*Plead,
       -a-B-wH2*Jconstant,
       3*a+3*B+delta-delta^2-vH2*Jconstant-wH2*Jlead};
cofactorDet=Plead*Jconstant-Pconstant*Jlead;
assert(cofactorDet==G*(3*G+4*delta^2)-2*J*(6*B+delta^2-3*delta));
delta1=G*(G+3*delta^2)*(G+delta^2+2*B)+J*((delta^2-5*B)*G-3*B*(delta^2+3*B))-B*J^2;
domainUnit=delta*cofactorDet*delta1;
disc=vH2^2-4*wH2;
ode=apply(toList(0..7),i->2*wH2*(i+1)*qi(i+1)+((2*i-h2DGlobal)*vH2+h2EtaGlobal)*qi(i)+2*(i-1-h2DGlobal)*qi(i-1));
poly6=h2EtaGlobal*(h2EtaGlobal^2-4*disc)*(h2EtaGlobal^2-16*disc)*(h2EtaGlobal^2-36*disc);
poly5=(h2EtaGlobal^2-disc)*(h2EtaGlobal^2-9*disc)*(h2EtaGlobal^2-25*disc);
accelerators={(h2DGlobal-5)*(h2DGlobal-6),J*(h2DGlobal-6),(h2DGlobal-5)*poly6+(6-h2DGlobal)*poly5};
allEquations=join(h2CoverEquations,frem,ode,accelerators);
save("h2CoverEquations-four-equations",matrix{h2CoverEquations});
save("conductor-two-remainders",matrix{frem});
save("ODE-eight-equations",matrix{ode});
save("derived-three-accelerators",matrix{accelerators});
save("global-seventeen-equations",matrix{allEquations});
save("global-domain-unit",domainUnit);
save("actual-Q-coefficients",matrix{q});
scan(toList(0..6),i->save("actual-Q-coefficient-"|toString i,qi(i)));
-- The following is only the new export's division identity, not a claim
-- that the two remainders vanish on arbitrary parameter tuples.
h2SourceRing=base[xH2];
H=xH2^2+vH2*xH2+wH2;
Q=sum(toList(0..6),i->sub(qi(i),h2SourceRing)*xH2^i);
Fsource=sum(toList(0..8),i->sub(f#i,h2SourceRing)*xH2^(8-i));
assert(Fsource==H*Q+sub(frem#1,h2SourceRing)*xH2+sub(frem#0,h2SourceRing));
save("equation-degrees",apply(allEquations,g->first degree g));
print "PASS new monic quotient/remainder export and exact cofactor-determinant formula";
print("COMPLETE GLOBAL denominator-free monic h2 ODE incidence: "|toString #allEquations|" equations, delta*cofactor*Delta1 unit; no h2CoverEquations determinant inverted");
exit 0;
