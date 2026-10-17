-- Exact higher target jets for endpoint quintic a != 0.
-- Computational algebra certificate used by a written support proof.
JetRing=QQ[a,b,g,d,z,rho];
jetChecks=0;
jetAssert=(label,condition)->(
 if not condition then error("FAIL "|label);
 jetChecks=jetChecks+1;
 print("PASS "|label);
);
jetA=a*z-b;
jetU=2*a*z^3-3*b*z^2-z+g;
jetV=3*a*z^4-4*b*z^3-2*z^2-z+d;
jetH=a*z^3+z-g-1;
jetJ=jetA*jetV-(jetA*z-1)*jetU;
jetE=jetJ^2-(3*z*jetA-1)*jetH*jetJ+jetA*jetU*jetH^2;
jetCoef=(poly,j,at)->(
 derived:=poly; denominator:=1;
 for i from 1 to j do (derived=diff(z,derived); denominator=denominator*i);
 sub(derived,{z=>at})/denominator
);
jetCb=a^2*g-a*b-b^3;
jetDb=a^3*d-a^2*b-2*a*b^2-b^4-a^2;
jetP1=3*z*jetA^2-jetA;
jetP2=jetA^3;
jetR1=6*z^2*jetA^2-4*z*jetA-jetA+1;
jetR2=4*z*jetA^3-2*jetA^2;
jetR3=jetA^4;
jetAssert("degree-seven leading coefficient",jetCoef(jetE,7,0)==a*jetCb);
jetAssert("degrees above seven vanish",all(toList(8..10),j->jetCoef(jetE,j,0)==0));
jetAssert("cleared X0-zero P boundary",a^2*jetU-a*jetP1+jetP2==jetCb);
jetAssert("cleared X0-zero R boundary",a^3*jetV-a^2*jetR1+a*jetR2-jetR3==jetDb);
jetAssert("A-zero septic boundary",sub(jetE,{b=>a*z})==a*z^3+z-g);
jetRoot={g=>-2*a*rho^3+3*b*rho^2+rho,d=>-3*a*rho^4+4*b*rho^3+2*rho^2+rho};
jetK=a*rho-b;
jetAssert("exact first jet at a common root",sub(jetCoef(jetE,1,rho),jetRoot)==-(3*rho^2*jetK-1)*(6*rho^2*jetK^2+3*rho*jetK^2-6*rho*jetK+1));
jetSpecial={b=>a-1/3,g=>a,d=>a+5/3};
jetAssert("exceptional h-zero constant and linear jets",sub(jetCoef(jetE,0,1),jetSpecial)==0 and sub(jetCoef(jetE,1,1),jetSpecial)==0);
jetAssert("exceptional h-zero exact order two",sub(jetCoef(jetE,2,1),jetSpecial)==1/9);

JetParameterRing=QQ[q];
JetParameterField=frac JetParameterRing;
JetOrderRing=JetParameterField[alpha];
jetD=6*q^2-6*q+1;
jetB=3*q^2+3*q-1;
jetParameterK=-jetD/(3*q);
jetParameterRho=q/jetParameterK;
jetMap=map(JetOrderRing,JetRing,{
 alpha,alpha*jetParameterRho-jetParameterK,
 alpha*jetParameterRho^3-3*jetParameterK*jetParameterRho^2+jetParameterRho,
 alpha*jetParameterRho^4-4*jetParameterK*jetParameterRho^3+2*jetParameterRho^2+jetParameterRho,
 jetParameterRho,jetParameterRho
});
jetCoeffs=apply(toList(1..4),j->jetMap(jetCoef(jetE,j,rho)));
jetAssert("ramification parameter kills first jet",jetCoeffs#0==0);
jetLinearA=lift(diff(alpha,jetCoeffs#1),JetParameterField);
jetLinearB=lift(sub(jetCoeffs#1,{alpha=>0}),JetParameterField);
jetAssert("second jet is linear in a",diff(alpha,jetLinearA)==0);
jetAssert("second-jet coefficient and excluded factors",jetLinearA==-3*q*jetB*(3*q-1)^2/jetD^2);
jetR4=54*q^4-72*q^3+15*q^2-3*q+1;
jetSolvedA=-jetLinearB/jetLinearA;
jetAssert("unique order-three a value",jetSolvedA==-jetD^2*jetR4/(27*q^3*(3*q-1)^2));
jetN9=8748*q^9-20412*q^8+18954*q^7-8262*q^6+1458*q^5-252*q^4+180*q^3-66*q^2+12*q-1;
jetN11=17496*q^11-46656*q^10+39366*q^9-16848*q^8+12123*q^7-12231*q^6+8316*q^5-2934*q^4+612*q^3-129*q^2+25*q-2;
jetThird=lift(sub(jetCoeffs#2,{alpha=>jetSolvedA}),JetParameterField);
jetFourth=lift(sub(jetCoeffs#3,{alpha=>jetSolvedA}),JetParameterField);
jetAssert("exact solved third jet",jetThird==-jetB*jetD*jetN9/(81*q^4*(3*q-1)^3));
jetAssert("exact solved fourth jet",jetFourth==-jetD^2*jetN11/(81*q^4*(3*q-1)^3));
jetAssert("no simultaneous third and fourth zeros on allowed parameters",ideal gcd(numerator jetThird,numerator jetFourth)==ideal jetD);

jetOtherB=jetSolvedA*jetParameterRho-jetParameterK;
jetQu2=2*jetSolvedA;
jetQu1=2*jetSolvedA*jetParameterRho-3*jetOtherB;
jetQu0=2*jetSolvedA*jetParameterRho^2-3*jetOtherB*jetParameterRho-1;
jetQv3=3*jetSolvedA;
jetQv2=3*jetSolvedA*jetParameterRho-4*jetOtherB;
jetQv1=3*jetSolvedA*jetParameterRho^2-4*jetOtherB*jetParameterRho-2;
jetQv0=3*jetSolvedA*jetParameterRho^3-4*jetOtherB*jetParameterRho^2-2*jetParameterRho-1;
jetOtherSylvester=matrix {
 {jetQu2,jetQu1,jetQu0,0,0},
 {0,jetQu2,jetQu1,jetQu0,0},
 {0,0,jetQu2,jetQu1,jetQu0},
 {jetQv3,jetQv2,jetQv1,jetQv0,0},
 {0,jetQv3,jetQv2,jetQv1,jetQv0}
};
jetOtherResultant=det jetOtherSylvester;
jetAssert("order-four contact has no second common root",ideal gcd(numerator jetThird,numerator jetOtherResultant)==ideal jetD);
print("PASS endpoint a-nonzero target jets: "|toString jetChecks|" exact checks");
exit 0;
