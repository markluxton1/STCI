-- Literal double-root identities on an explicitly defined rational family.
-- The separate quotient-fiber argument must establish its necessity under SUP.
doubleCheck=(label,condition)->(assert(condition);print("PASS "|label));
coefRing=QQ[delta,a,B,q];
coefPrefix="research/validation/2026-10-12-nonendpoint-single-root-taylor/20261013T142033115594Z/nonendpoint_single_root_u";
u0=value get(coefPrefix|"0.txt");
u1=value get(coefPrefix|"1.txt");
doubleBase=QQ[da,dq]; doubleField=frac doubleBase;
Pc=dq^2-6*dq+6;
deltaS=Pc*(dq-2)/(dq*(dq-1));
kappaS=deltaS+deltaS^2*(2*dq-3)/(3*(dq-1)*(dq-2));
BS=kappaS-da*dq;
branchMap=map(doubleField,coefRing,{deltaS,da,BS,dq});
expectedSecond=(dq-2)^4*Pc^12/(9*dq^8*(dq-1)^8);
doubleCheck("specified branch first derivative",branchMap(u0)==0);
doubleCheck("specified branch exact second coefficient",branchMap(u1)==expectedSecond);
doubleCheck("retained fiber-rank denominator",dq*(kappaS-deltaS)-deltaS^2==-deltaS^2*Pc/(3*(dq-1)*(dq-2)));
print "PASS all three regular L1 double-root checks";
