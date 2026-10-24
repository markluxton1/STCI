-- Independent exact ideal checks for the October 24 ruled-surface proposal.
-- Run: M2 --script research/computations/verify_p4_ruled_surfaces_2026_10_24.m2
-- This is finite computational evidence, not a normalization or global proof.

scrollRing = QQ[xmid, xa, xb, xc, xd];
scrollIdeal = ideal(xa*xd-xmid^2, xa*xc-xb*xmid, xmid*xc-xb*xd);
scrollElimination = eliminate(xmid, scrollIdeal);
assert(scrollElimination == ideal(xa*xc^2-xb^2*xd));
print "PASS: cubic scroll projection elimination";

pinchRing = QQ[ww, rr];
curveInverse = ideal(rr*ww-rr^3, ww^2-rr^4);
assert(curveInverse == (ww-rr^2)*ideal(rr, ww));
assert(saturate(curveInverse, ideal(rr, ww)) == ideal(ww-rr^2));
print "PASS: inverse curve ideal and endpoint embedded defect";

endpointRing = QQ[uu, yy, zz];
endpointPair = ideal(yy-uu^3, zz-uu^4, yy+uu^3);
assert(endpointPair == ideal(yy, zz, uu^3));
assert(degree(endpointRing/endpointPair) == 3);
print "PASS: distinct component images have intersection length3";

specialRing = (ZZ/2)[qq, uu];
assert(qq^4-uu^12 == (qq-uu^3)^4);
print "PASS: characteristic-two fourth-power graph";

print "PASS: all new M2 ruled-surface checks";
