-- NEW complete support-incidence exclusion on lambda=1.
-- These displayed H and Q4 are specializations of the accepted actual octic.
h3lcBase=QQ[dl];h3lcField=frac h3lcBase;h3lcRing=h3lcField[q];
h3lcH=(dl+1)*q^3-6*q^2+(6-6*dl)*q+4*dl;
h3lcQ=(90*dl^2-76*dl-58)*q^4+(-405*dl^2+458*dl+203)*q^3+
    (675*dl^2-858*dl-261)*q^2+(-450*dl^2+800*dl+174)*q-400*dl;
h3lcRem=h3lcH^4 % h3lcQ;
h3lcCs=apply(toList(0..3),i->lift(numerator coefficient(q^i,h3lcRem),h3lcBase));
h3lcDs=apply(toList(0..3),i->lift(denominator coefficient(q^i,h3lcRem),h3lcBase));
h3lcI=ideal h3lcCs;
assert(h3lcI==ideal(1_h3lcBase));
h3lcBez=(matrix{{1_h3lcBase}})//(gens h3lcI);
assert((gens h3lcI)*h3lcBez==matrix{{1_h3lcBase}});
print "PASS compact support remainders generate the unit ideal";
print "PASS literal original-generator Bezout product is one";
print("NUMERATOR DEGREES="|toString apply(h3lcCs,cc->degree cc));
print("DENOMINATOR FACTORS="|toString apply(h3lcDs,cc->factor cc));
-- The exceptional leading-drop locus has an actual conductor infinity root,
-- while neither allowed homogeneous factor H nor q vanishes at infinity.
h3lcT=lift(45*dl^2-38*dl-29,h3lcBase);
assert(ideal(h3lcT,lift(dl+1,h3lcBase))==ideal(1_h3lcBase));
assert(sub(h3lcQ,{q=>0})==-400*dl);
print "PASS leading-drop has no allowed infinity root";
print "PASS no extra A4 root in Q4 when delta is nonzero";
"research/validation/2026-10-13-evening-h3-proportional/lambda1-compact-numerators.txt" << toString h3lcCs << close;
"research/validation/2026-10-13-evening-h3-proportional/lambda1-compact-denominators.txt" << toString h3lcDs << close;
"research/validation/2026-10-13-evening-h3-proportional/lambda1-bezout.txt" << toString h3lcBez << close;
print "DONE lambda1 complete support exclusion";
