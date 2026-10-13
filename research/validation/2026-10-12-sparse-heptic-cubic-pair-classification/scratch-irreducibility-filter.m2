S=QQ[spU,spV,MonomialOrder=>Lex]; R=S[spZ];
for spN in {1,2,3,6} do (
 spP=6-spN;
 spH=(spZ-1)*(spU*spZ+1-spU)^spN*(spV*spZ+1-spV)^spP;
 spC=apply(8,spI->coefficient(spZ^spI,spH));
 spRes=det matrix{{spC#6,spC#3,spC#0,0},{0,spC#6,spC#3,spC#0},{spC#7,spC#4,spC#1,0},{0,spC#7,spC#4,spC#1}};
 spI=if spN==6 then ideal(sub(spC#2,{spV=>spU}),sub(spC#5,{spV=>spU})) else saturate(ideal(spC#2,spC#5),ideal(spU-spV));
 spGood=saturate(spI,ideal(spRes));
 print("PROFILE "|toString(spN)|","|toString(spP));
 print("RES "|toString factor spRes);
 print("GOOD "|toString gens gb spGood);
 print("GOOD DIM "|toString dim spGood|" DEG "|toString degree spGood);
 print("BAD "|toString gens gb(spI+ideal(spRes)));
 if spN!=6 then print("GOOD RAD "|toString gens gb radical spGood);
);
