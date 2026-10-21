-- Exact rational ideal-equality certificate for the four-candidate reduction.
load "research/computations/conditional_2_12_cubic_reduction_2026_10_21_family.m2";
candidateTriangularIdeal=ideal(
    h6,h5,h4+2*h7,d3,d1,
    y3-27/4*h7^3-15/32*h7,
    d2-108*h7^3+9/2*h7,
    648*h7^4+45*h7^2-4);
forwardCertificate=(gens candidateTriangularIdeal)//(gens familyIdeal);
reverseCertificate=(gens familyIdeal)//(gens candidateTriangularIdeal);
assert(gens familyIdeal*forwardCertificate==gens candidateTriangularIdeal);
assert(gens candidateTriangularIdeal*reverseCertificate==gens familyIdeal);
print "EXACT_IDEAL_EQUALITY_VERIFIED";
print("DIMENSION="|toString dim candidateTriangularIdeal);
print("DEGREE="|toString degree candidateTriangularIdeal);
out=openOut "research/computations/conditional_2_12_cubic_reduction_2026_10_21_family_lifts.m2";
out << "-- Exact coefficient matrices. Load family_certificate.m2's source definitions first.\n";
out << "forwardCertificate=matrix(R," << toExternalString entries forwardCertificate << ");\n";
out << "reverseCertificate=matrix(R," << toExternalString entries reverseCertificate << ");\n";
out << "assert(gens familyIdeal*forwardCertificate==gens candidateTriangularIdeal);\n";
out << "assert(gens candidateTriangularIdeal*reverseCertificate==gens familyIdeal);\n";
close out;
