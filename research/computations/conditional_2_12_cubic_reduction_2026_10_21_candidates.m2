-- Exact four-candidate full global sextic cubic test.
R=QQ[h,eta,MonomialOrder=>GRevLex];
candidatePolynomial=648*h^4+45*h^2-4;
cubicEquations={-9/32-15/32*h*eta+27/4*h^2-27/4*h^3*eta,-45/16*eta-7335/64*h+99/2*h^2*eta+17901/8*h^3,1539/32-123/32*h*eta-3753/4*h^2+297/4*h^3*eta,3/4*eta+369/16*h-891/2*h^3,-237/64+21/64*h*eta+567/8*h^2-135/8*h^3*eta,-9/32*eta-891/128*h-9/4*h^2*eta+2025/16*h^3,-105/64-15/64*h*eta+243/8*h^2-27/8*h^3*eta,1/8*eta+27/32*h-81/4*h^3,1/16*eta+27/64*h-81/8*h^3,-105/128-15/128*h*eta+243/16*h^2-27/16*h^3*eta,-9/64*eta-891/256*h-9/8*h^2*eta+2025/32*h^3,-237/128+21/128*h*eta+567/16*h^2-135/16*h^3*eta,3/32*eta+369/128*h-891/16*h^3,1539/256-123/256*h*eta-3753/32*h^2+297/32*h^3*eta,-45/128*eta-7335/512*h+99/16*h^2*eta+17901/64*h^3,-9/256-15/256*h*eta+27/32*h^2-27/32*h^3*eta};
candidateCubicIdeal=ideal join({candidatePolynomial},cubicEquations);
print "CANDIDATE_FULL_C3_MODEL_READY";
-- No Groebner basis run by this exporter.
