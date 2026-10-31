-- Fresh independent binary contact audit. Coefficients are binomial sums,
-- rather than extraction of coefficients from the owner's polynomial expansion.
cpaCount=0;
cpaAssert=(label,value)->(assert value; cpaCount=cpaCount+1; print("PASS "|toString cpaCount|": "|label));
cpaRing=QQ[cpaU,cpaV];
cpaCoeff=(powerN,powerP,powerK)->(
    if powerK<0 or powerK>powerN+powerP then 0_cpaRing else (
        sum(toList(0..powerN),indexI -> (
            indexJ=powerK-indexI;
            if indexJ<0 or indexJ>powerP then 0_cpaRing else
                binomial(powerN,indexI)*binomial(powerP,indexJ)*
                cpaU^indexI*(1-cpaU)^(powerN-indexI)*
                cpaV^indexJ*(1-cpaV)^(powerP-indexJ)
        ))));
cpaExpected={
 ideal(cpaU-11*cpaV+5,21*cpaV^2-21*cpaV+5),
 ideal(cpaU-42*cpaV^3+63*cpaV^2-42*cpaV+10,
       63*cpaV^4-126*cpaV^3+111*cpaV^2-48*cpaV+8),
 ideal(cpaU+cpaV-1,7*cpaV^4-14*cpaV^3+12*cpaV^2-5*cpaV+1)};
cpaSizes={2,4,4};
for cpaN in {1,2,3} do (
    cpaCs=apply(8,indexK -> cpaCoeff(cpaN,6-cpaN,indexK-1)-cpaCoeff(cpaN,6-cpaN,indexK));
    cpaRaw=ideal(cpaCs#2,cpaCs#5);
    cpaBinaryResultant=det matrix{{cpaCs#6,cpaCs#3,cpaCs#0,0},
        {0,cpaCs#6,cpaCs#3,cpaCs#0},
        {cpaCs#7,cpaCs#4,cpaCs#1,0},{0,cpaCs#7,cpaCs#4,cpaCs#1}};
    cpaExcluded=(cpaU-cpaV)*cpaBinaryResultant;
    cpaGood=saturate(cpaRaw,ideal(cpaExcluded));
    cpaAssert("profile "|toString cpaN|" exact full saturated ideal",cpaGood==cpaExpected#(cpaN-1));
    cpaAssert("profile "|toString cpaN|" zero-dimensional count",dim(cpaRing/cpaGood)==0 and degree(cpaRing/cpaGood)==cpaSizes#(cpaN-1));
    cpaAssert("profile "|toString cpaN|" saturated bad locus absent in candidates",cpaGood+ideal(cpaExcluded)==ideal(1_cpaRing));
    cpaAssert("profile "|toString cpaN|" endpoints retained then excluded by irreducibility",cpaGood+ideal(cpaU*cpaV*(cpaU-1)*(cpaV-1))==ideal(1_cpaRing));
    cpaUnivar=(gens(cpaExpected#(cpaN-1)))_(0,1);
    cpaAssert("profile "|toString cpaN|" all branches reduced",ideal(cpaUnivar,diff(cpaV,cpaUnivar))==ideal(1_cpaRing));
    cpaS=cpaU+cpaV; cpaP=cpaU*cpaV; cpaH=cpaS-1;
    if cpaN==1 then (
        cpaAssert("profile15 h invariant",(7*cpaH^2-12)%cpaGood==0);
        cpaAssert("profile15 p invariant",(cpaP-cpaS/2+5/42)%cpaGood==0));
    if cpaN==2 then (
        cpaAssert("profile24 h invariant",(63*cpaH^4-30*cpaH^2-1)%cpaGood==0);
        cpaAssert("profile24 p invariant",(cpaP-5/12-cpaH/2+cpaH^2/4)%cpaGood==0));
    if cpaN==3 then (
        cpaAssert("profile33 s invariant",(cpaS-1)%cpaGood==0);
        cpaAssert("profile33 p invariant",(7*cpaP^2-5*cpaP+1)%cpaGood==0));
    print("EXACT CLASSIFICATION "|toString(cpaN,6-cpaN));print gens gb cpaGood;
);
cpaCs=apply(8,indexK -> cpaCoeff(6,0,indexK-1)-cpaCoeff(6,0,indexK));
cpaSingle=ideal(cpaCs#2,cpaCs#5);
cpaBinaryResultant=det matrix{{cpaCs#6,cpaCs#3,cpaCs#0,0},
    {0,cpaCs#6,cpaCs#3,cpaCs#0},
    {cpaCs#7,cpaCs#4,cpaCs#1,0},{0,cpaCs#7,cpaCs#4,cpaCs#1}};
cpaAssert("single support full missing-coefficient ideal",cpaSingle==ideal(cpaU*(cpaU-1)));
cpaAssert("single support all candidates reducible",saturate(cpaSingle,ideal(cpaBinaryResultant))==ideal(1_cpaRing));
-- Abstract Segre factorization gives exact complete contact after removing both
-- ambient ruling factors. Its binary section has degree seven.
cpaAbstract=QQ[cpaKappa,cpaSigma,cpaQ,cpaW,cpaLin,cpaConst][cpaR];
cpaL0=cpaR-cpaSigma; cpaL1=cpaL0+cpaKappa;
cpaQ0=-cpaR^2+cpaQ*cpaR+cpaW; cpaD=cpaLin*cpaR+cpaConst;
cpaQ1=cpaQ0+cpaD;
cpaX0=cpaL0*cpaQ0; cpaX1=cpaL0*cpaQ1;
cpaX2=cpaL1*cpaQ0; cpaX3=cpaL1*cpaQ1;
cpaK=cpaL1*cpaQ0^3-cpaL0*cpaQ1^3;
cpaAssert("abstract Segre rank one identity",cpaX0*cpaX3-cpaX1*cpaX2==0);
cpaAssert("first ambient cubic removes exact L0 squared",cpaX0^2*cpaX2-cpaX1^3==cpaL0^2*cpaK);
cpaAssert("opposite ambient cubic removes exact L1 squared",cpaX2^3-cpaX1*cpaX3^2==cpaL1^2*cpaK);
cpaAssert("complete heptic affine top coefficient cancels",coefficient(cpaR^7,cpaK)==0);
cpaAssert("complete heptic affine degree-six coefficient",coefficient(cpaR^6,cpaK)==-cpaKappa-3*cpaLin);
-- Fresh actual source-cubic expansion at its shared infinity point.
cpaParameterBase=QQ[cpaDelta,cpaM,cpaN0,cpaA,cpaB,cpaG,cpaJ];
cpaParameters=cpaParameterBase/ideal(cpaG+cpaJ+3*cpaDelta^2);
cpaAtInfinity=cpaParameters[cpaEpsilon];
cpaF0=-1+(cpaM^2+cpaM+cpaA)*cpaEpsilon+
    (cpaN0*(2*cpaM+1)-cpaA*cpaM)*cpaEpsilon^2+
    (cpaN0^2-cpaA*cpaN0)*cpaEpsilon^3;
cpaF1=-1+(cpaM^2+cpaM-cpaDelta*cpaM+cpaA+cpaB)*cpaEpsilon+
    (cpaN0*(2*cpaM+1-cpaDelta)-(cpaA+cpaB)*cpaM)*cpaEpsilon^2+
    (cpaN0^2-(cpaA+cpaB)*cpaN0)*cpaEpsilon^3;
cpaF2=-1+(cpaM^2+cpaM-3*cpaDelta*cpaM+3*cpaDelta^2+cpaA+3*cpaB+cpaG)*cpaEpsilon+
    (cpaN0*(2*cpaM+1-3*cpaDelta)-cpaDelta^3-(cpaA+3*cpaB+cpaG)*cpaM)*cpaEpsilon^2+
    (cpaN0^2-(cpaA+3*cpaB+cpaG)*cpaN0)*cpaEpsilon^3;
cpaActualContact=cpaF0^2*cpaF2-cpaF1^3;
cpaAssert("actual cubic shared infinity lies on C0",coefficient(cpaEpsilon^0,cpaActualContact)==0);
cpaAssert("actual cubic first full Cartier coefficient is J",coefficient(cpaEpsilon^1,cpaActualContact)==-cpaJ);
print("TOTAL INDEPENDENT CHECKS "|toString cpaCount);
