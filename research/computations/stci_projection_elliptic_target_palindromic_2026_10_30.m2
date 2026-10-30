-- Balanced palindromic target incidence; symbolic parameters retained.
R=QQ[symbol aa,symbol bb]; P=R[symbol tt];
quartic=tt^4+aa*tt^3+bb*tt^2+aa*tt+1;
targetRestriction=quartic^5;
T=R[symbol xx];
coefficientTriple=apply(toList(0..2),j->sum(toList(0..6),i->sub(coefficient(tt^(3*i+j),targetRestriction),T)*xx^i));
quadDiscriminant=coefficientTriple#1^2-4*coefficientTriple#0*coefficientTriple#2;
assert(all(toList(0..12),i->coefficient(xx^i,quadDiscriminant)==coefficient(xx^(12-i),quadDiscriminant)));
Z=R[symbol zz];
chebyshevList={2_Z,zz};
for i from 2 to 6 do chebyshevList=append(chebyshevList,zz*chebyshevList#(i-1)-chebyshevList#(i-2));
dSix=sub(coefficient(xx^6,quadDiscriminant),Z)+sum(toList(1..6),i->sub(coefficient(xx^(6+i),quadDiscriminant),Z)*chebyshevList#i);
assert(sub(dSix,{zz=>2})==sub(quadDiscriminant,{xx=>1}));
print("PALINDROMIC_DISCRIMINANT="|toString quadDiscriminant);
print("Z_DEGREE_SIX_POLYNOMIAL="|toString dSix);
print("Z_PLUS_TWO_VALUE="|toString sub(dSix,{zz=>-2}));
print("Z_MINUS_TWO_VALUE="|toString sub(dSix,{zz=>2}));
print("QUARTIC_DISCRIMINANT="|toString resultant(quartic,diff(tt,quartic),tt));
print("SYMBOLIC_REDUCTION_COMPLETE");

-- An actual primitive genus-one target candidate in the balanced locus.
K=QQ[symbol eta,symbol tau,symbol ax];
etaRelation=ideal(5*eta^2+4);
reduceEta=f->f%etaRelation;
nonzeroEta=f->reduceEta f!=0;
coprimeEta=(f,g)->ideal(5*eta^2+4,f,g)==ideal 1_K;
rCandidate=tau^4+eta*tau^3+eta*tau+1;
assert(coprimeEta(rCandidate,diff(tau,rCandidate)));
assert(sub(rCandidate,{tau=>0})==1);
candidateP=rCandidate^5;
candidateE=apply(toList(0..2),j->sum(
 select(terms candidateP,term->((first exponents term)#1)%3==j),
 term->sub(term,{tau=>1})*ax^(((first exponents term)#1)//3)));
axCoefficient=(i,f)->sum(select(terms f,term->(first exponents term)#2==i),
 term->sub(term,{ax=>1}));
candidateDelta=candidateE#1^2-4*candidateE#0*candidateE#2;
candidateS=(eta*ax+1)*(ax+eta)*(ax^2-7*eta*ax+1);
candidateD=5*ax^4+(28/5)*eta*ax^3+(102/25)*ax^2+(28/5)*eta*ax+5;
assert(reduceEta(candidateDelta+3*candidateS^2*candidateD)==0);
assert(coprimeEta(candidateD,diff(ax,candidateD)));
assert(ideal(5*eta^2+4,candidateE#0,candidateE#1,candidateE#2)==ideal 1_K);
assert(nonzeroEta(axCoefficient(6,candidateE#0)) and nonzeroEta(axCoefficient(6,candidateE#2)));
print("EXPLICIT_CANDIDATE_ELLIPTIC_DISCRIMINANT_PASS");
print("EXPLICIT_CANDIDATE_EQUATION_COEFFICIENTS="|toString apply(candidateE,reduceEta));
print("EXPLICIT_CANDIDATE_SQUARE_FACTOR="|toString reduceEta candidateS);
print("EXPLICIT_CANDIDATE_ELLIPTIC_QUARTIC="|toString candidateD);

-- Every target-C root is smooth and has one point on the normalization.
deltaAtC=sub(candidateDelta,{ax=>tau^3});
assert(coprimeEta(rCandidate,deltaAtC));
assert(sub(candidateE#0,{ax=>tau^3})+tau*sub(candidateE#1,{ax=>tau^3})+tau^2*sub(candidateE#2,{ax=>tau^3})==rCandidate^5);
print("EXACT_FOUR_NORMALIZED_C_POINTS_CONTACT_FIVE_PASS");

-- Check reduced B-zero and B-pole divisors, including the two old nodes.
zeroResidual=10*ax^4+(eta^3+30*eta)*ax^3+33*eta^2*ax^2+(10*eta^3+3*eta)*ax+1;
poleResidual=ax^4+(10*eta^3+3*eta)*ax^3+33*eta^2*ax^2+(eta^3+30*eta)*ax+10;
assert(candidateE#0==(eta*ax+1)^2*zeroResidual);
assert(candidateE#2==(ax+eta)^2*poleResidual);
assert(coprimeEta(zeroResidual,diff(ax,zeroResidual)));
assert(coprimeEta(poleResidual,diff(ax,poleResidual)));
assert(coprimeEta(zeroResidual,candidateE#1));
assert(coprimeEta(poleResidual,candidateE#1));
zeroNode=5*eta/4; poleNode=-eta;
assert(nonzeroEta(sub(zeroResidual,{ax=>zeroNode})));
assert(nonzeroEta(sub(poleResidual,{ax=>poleNode})));
assert(nonzeroEta(sub(candidateE#2,{ax=>zeroNode})));
assert(nonzeroEta(sub(candidateE#0,{ax=>poleNode})));
assert(nonzeroEta(sub(candidateD,{ax=>zeroNode})));
assert(nonzeroEta(sub(candidateD,{ax=>poleNode})));
squareExtra=ax^2-7*eta*ax+1;
assert(nonzeroEta(sub(squareExtra,{ax=>zeroNode})));
assert(nonzeroEta(sub(squareExtra,{ax=>poleNode})));
assert(nonzeroEta(sub(candidateE#0,{ax=>0})) and nonzeroEta(sub(candidateE#2,{ax=>0})));
assert(nonzeroEta(sub(candidateD,{ax=>0})));
print("REDUCED_DISJOINT_RULING_BOUNDARIES_PASS");
print("PRIMITIVE_BALANCED_ELLIPTIC_TARGET_CANDIDATE_VERIFIED");
