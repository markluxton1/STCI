-- New supplemental source: previously frozen eight-check source is unchanged.
firstCheck=(label,condition)->(assert(condition);print("PASS "|label));
firstRing=QQ[delta,a,B,q,kappa];
L2old=value get "research/validation/2026-10-12-nonendpoint-single-root-taylor/20261013T142033115594Z/nonendpoint_single_root_L2.txt";
c1old=value get "research/validation/2026-10-12-nonendpoint-single-root-taylor/20261013T142033115594Z/nonendpoint_single_root_u0.txt";
Pq=q^2-6*q+6;
L1=3*kappa*(q-1)^2*Pq+delta*q*(3-2*q)*Pq-3*delta^2*(q-1)^2*(q-3);
L2=(3*q*(q-1)*(2*delta*(q-1)+q*(q-2))*kappa^2
   -6*delta*q*(q-1)*(delta^2+delta*(3*q-4)+q*(q-2))*kappa
   +delta^5*q+3*delta^4*(q-1)*(3*q-2)
   +6*delta^3*q*(q-1)*(2*q-3)+3*delta^2*q^2*(q-1)*(q-2));
firstCheck("compact quadratic second factor",sub(L2old,{B=>kappa-a*q})==L2);
firstCheck("compact first derivative product",sub(c1old,{B=>kappa-a*q})==-delta*q*L1*L2);
firstCheck("simple root at target zero",sub(L1,{q=>1})==delta and sub(L2,{q=>1})==delta^5 and sub(c1old,{q=>1})==-delta^7);
L2pc=L2%Pq;
firstCheck("retained collision-target quadratic",L2==Pq*(L2//Pq)+L2pc);
print("Pc=0 second factor: "|toString L2pc);
"/private/tmp/nonendpoint_single_root_L2_compact.txt" << toString L2 << close;
"/private/tmp/nonendpoint_single_root_L2_Pc_remainder.txt" << toString L2pc << close;
print "PASS all four supplemental first-coefficient checks";
