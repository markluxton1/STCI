-- Load-only exact QQ import of verified format-only Horner expressions.
-- No generator construction, gb, saturation, elimination, factor, or dimension.
R=QQ[deltaPar,vPar,wPar];
genDir="research/validation/2026-10-15-h2-horner-input/attempt-03-exact-export-trim-repair";
outDir="research/validation/2026-10-15-h2-horner-input/attempt-04-qq-load-only";
save=(label,object)->((outDir|"/"|label|".txt") << toString object << close);
expectedDegrees={37,52,52,52,52,52,50,50,50,50,50,49};
expectedCounts={2984,6629,6845,7016,7191,7303,6082,6278,6459,6622,6736,6580};
loadedGenerators=apply(toList(0..11),i->(
    save("stage","before-generator-"|toString i);
    f:=value get(genDir|"/horner-generator-"|toString i|".txt");
    assert(first degree f==expectedDegrees#i);
    assert(#terms f==expectedCounts#i);
    save("loaded-generator-"|toString i,{first degree f,#terms f});
    print("PASS loaded QQ generator "|toString i|" degree "|toString(first degree f)|" terms "|toString(#terms f));
    save("stage","after-generator-"|toString i);
    f));
assert(#loadedGenerators==12);
save("stage","complete-load-only");
print("COMPLETE QQ load-only: 12 Horner generators, expected degrees and exact term counts; no GB or saturation");
exit 0;
