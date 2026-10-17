-- Diagnose the failed library-discriminant assertion, not a new proof.
diagnosticBase=QQ[diagnosticR,diagnosticD,diagnosticEta];
diagnosticRing=diagnosticBase/ideal(diagnosticEta^2-3);
diagnosticK=5*diagnosticD^3+9*diagnosticEta*diagnosticD^2+45*diagnosticD+9*diagnosticEta;
print "Library discriminant value and class:";
print discriminant(diagnosticK,diagnosticD);
print class discriminant(diagnosticK,diagnosticD);
print "Explicit classical cubic discriminant:";
print ((9*diagnosticEta)^2*45^2-4*5*45^3-4*(9*diagnosticEta)^3*(9*diagnosticEta)-27*5^2*(9*diagnosticEta)^2+18*5*(9*diagnosticEta)*45*(9*diagnosticEta));
