R=QQ[symbol targetAa,symbol targetCc,symbol targetDd,symbol targetTt];
supportForm=targetTt^4+targetAa*targetTt^3+targetCc*targetTt+targetDd;
assert(supportForm==targetTt*(targetTt^3+targetCc)+(targetAa*targetTt^3+targetDd));
assert(sub(supportForm,{targetDd=>targetAa*targetCc})==(targetTt+targetAa)*(targetTt^3+targetCc));
assert((-targetAa)*targetCc-(-targetDd)*1==targetDd-targetAa*targetCc);
print "ZERO_MIDDLE_SUPPORT_MOBIUS_AND_DEGENERATE_IDENTITIES_PASS";
