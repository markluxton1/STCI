S=QQ[spS,spP,spT,spQ];
spK=2*spP+2/3-spS; spL=11-21*spK; spW=spP-11*spK+16/3;
spK2=2*spQ+2/3-spT; spL2=11-21*spK2; spW2=spQ-11*spK2+16/3;
spTypes={
 ideal(spS-2*spP-5/21,441*spP^2-336*spP-125),
 ideal(63*spK^2-48*spK+8,spW^2-spL*spW+spK*spL^2),
 ideal(spS-1,7*spP^2-5*spP+1)};
spTypes2={
 ideal(spT-2*spQ-5/21,441*spQ^2-336*spQ-125),
 ideal(63*spK2^2-48*spK2+8,spW2^2-spL2*spW2+spK2*spL2^2),
 ideal(spT-1,7*spQ^2-5*spQ+1)};
spE=spS*spT-3*spS*spQ-3*spT*spP+spP+spQ+6*spP*spQ-1/3;
for spI from 0 to 2 do for spJ from spI to 2 do (
 spMatch=spTypes#spI+spTypes2#spJ+ideal(spE);
 print("PAIR "|toString(spI+1)|","|toString(spJ+1));
 print gens gb spMatch;
 assert(1_S % spMatch == 0);
 print "PASS unit ideal"
);
print "ALL PAIRS PASS";
