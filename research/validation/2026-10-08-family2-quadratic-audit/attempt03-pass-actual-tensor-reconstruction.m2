-- Independent reconstruction, not an execution of the tensor exporter.
-- All output belongs to the dedicated 2026-10-08 quadratic audit folder.
-- Run from repository root using M2 --script on this source.
-- Frozen input text files are bound by actual-tensor-input-manifest.json.
S=QQ[x,y,z,w];
q=x*w-y*z;
a=x^2*z-y^3;
b=x*z^2-y^2*w;
d=y*w^2-z^3;
IC=ideal(q,a,b,d);
J=ideal(q^4,b^4);
Jgb=gens gb J;

-- Reconstruct the stage-four ancestor numerators from the actual Ext map.
MI=coker gens(IC^4);
MJ=coker gens J;
quotientMap=map(MI,MJ,matrix{{1_S}});
extMap=Ext^2(quotientMap,S^1);
ancestorSource=basis(-7,source extMap);
assert(numColumns ancestorSource==30);
assert(numColumns basis(-7,kernel extMap)==0);
H=lift(extMap*ancestorSource,S);
assert(numRows H==1 and numColumns H==30);
assert(all(0..29,i->degree H_(0,i)=={13}));
print("PASS: reconstructed 30 degree-13 ancestor numerators; Ext-stage map is injective.");

-- Independently test the support condition against every generator of I^4.
I4gens=gens(IC^4);
assert(all(0..29,i->all(0..numColumns I4gens-1,k->
    ((H_(0,i)*I4gens_(0,k)) % Jgb)==0)));
print("PASS: every ancestor satisfies I^4*h subset (q^4,b^4), using all I^4 generators.");

-- basis(4,IC) is a four-generator coordinate matrix, not quartic forms.
Wcoordinates=basis(4,IC);
Igenerators=gens IC;
assert(numRows Wcoordinates==4 and numRows Igenerators==1);
W=matrix{apply(toList(0..numColumns Wcoordinates-1),j->
    sum(0..3,k->Igenerators_(0,k)*Wcoordinates_(k,j)))};
assert(numRows W==1 and numColumns W==18);
assert(all(0..17,j->degree W_(0,j)=={4}));
assert(rank sub((coefficients W)#1,QQ)==18);

-- A separate restriction-map test verifies that this is the full I_C(4).
Param=QQ[s,t];
restriction=map(Param,S,{s^4,s^3*t,s*t^3,t^4});
allQuartics=basis(4,S);
assert(numColumns allQuartics==35);
restrictedQuartics=restriction allQuartics;
assert(rank sub((coefficients restrictedQuartics)#1,QQ)==17);
assert(restriction W==0);
print("PASS: all 18 actual quartic forms are independent and span the restriction kernel (35-17=18).");

-- Bind these exact column bases to the displayed, frozen data.
use S;
dataLines=lines get "research/validation/2026-10-08-family2-quadratic-audit/localcoh-incidence-bases.txt";
assert(#dataLines==50);
assert(dataLines#0=="ancestor stage4 numerators");
assert(dataLines#31=="quartic multipliers");
Hstored=matrix{apply(toList(1..30),i->value(dataLines#i))};
Wstored=matrix{apply(toList(32..49),i->value(dataLines#i))};
-- Ext matrices carry a degree-minus-twenty target shift; compare polynomial entries.
assert(all(0..29,i->H_(0,i)==Hstored_(0,i)));
assert(all(0..17,j->W_(0,j)==Wstored_(0,j)));
print("PASS: literal equality of all 30 ancestor and all 18 quartic displayed basis columns.");

-- Reconstruct the full bilinear tensor before any row compression.
products=matrix{flatten apply(toList(0..29),i->apply(toList(0..17),j->
    (H_(0,i)*W_(0,j)) % Jgb))};
targets=matrix{{(x*z*(q*b)^3) % Jgb,(y*w*(q*b)^3) % Jgb}};
allColumns=products|targets;
assert(numColumns products==540 and numColumns allColumns==542);
coefficientsAll=sub((coefficients allColumns)#1,QQ);
coefficientsProducts=sub((coefficients products)#1,QQ);
assert(rank coefficientsProducts==74);
assert(rank coefficientsAll==74);
compressed=transpose gens gb image transpose coefficientsAll;
assert(numRows compressed==74 and numColumns compressed==542);

-- Read the frozen 74x542 tensor without running the original exporter.
tensorLines=lines get "research/validation/2026-10-08-family2-quadratic-audit/localcoh-incidence-tensor.txt";
assert(tensorLines#0=="30 18 74 542");
storedMutable=mutableMatrix(QQ,74,542);
seenEntries=new MutableHashTable;
for i from 1 to #tensorLines-1 do (
    triple=apply(separate(" ",tensorLines#i),value);
    assert(#triple==3);
    assert(triple#0>=0 and triple#0<74 and triple#1>=0 and triple#1<542);
    entryKey=(triple#0,triple#1);
    assert(not seenEntries#?entryKey);
    seenEntries#entryKey=true;
    storedMutable_(triple#0,triple#1)=triple#2;
);
stored=matrix storedMutable;
assert(rank stored==74);
assert(rank(coefficientsAll||stored)==74);
assert(rank(compressed||stored)==74);
assert(compressed==stored);
print("PASS: literal 74x542 compressed-row equality and full coefficient/stored rowspace rank 74.");

-- Verify the tensor image has the dimension of the complete next-stage piece.
nextStage=Ext^2(coker gens(IC^3),S^1);
assert(numColumns basis(-3,nextStage)==74);
print("PASS: image dimension 74 equals the complete degree-minus-three Ext-stage-three piece.");
print("PASS: ACTUAL_TENSOR_RECONSTRUCTION_COMPLETE; 30 ancestors, 18 quartics, 540 product columns, two targets.");
