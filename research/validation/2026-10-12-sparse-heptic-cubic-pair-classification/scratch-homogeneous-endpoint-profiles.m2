S=QQ[spU,spV,MonomialOrder=>Lex]; R=S[spZ];
for spN in {1,2,3,6} do (
 spP=6-spN;
 spH=(spZ-1)*(spU*spZ+1-spU)^spN*(spV*spZ+1-spV)^spP;
 spC2=coefficient(spZ^2,spH); spC5=coefficient(spZ^5,spH);
 spI=if spN==6 then ideal(sub(spC2,{spV=>spU}),sub(spC5,{spV=>spU})) else saturate(ideal(spC2,spC5),ideal(spU-spV));
 print("PROFILE "|toString(spN)|","|toString(spP));
 print spC2; print spC5;
 print gens gb spI;
 print("DIM "|toString dim spI|" DEG "|toString degree spI);
);
