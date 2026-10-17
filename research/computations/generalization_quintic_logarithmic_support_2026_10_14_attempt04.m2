-- Postprocess the completed NEW coefficients from attempt02; no rational-map rerun.
par=QQ[deltaPar,vPar,wPar];
inDir="research/validation/2026-10-14-quintic-logarithmic-support/attempt-02";
outDir="research/validation/2026-10-14-quintic-logarithmic-support/attempt-04";
cf=apply(toList(0..8),ii->value get(inDir|"/F-coefficient-"|toString ii|".txt"));
ci=ii->if ii<0 or ii>8 then 0_par else cf#ii;
eigenCf=apply(toList(0..8),jj->(8-2*jj)*vPar*ci(jj)+(18-2*jj)*ci(jj-1)-2*(jj+1)*wPar*ci(jj+1));
eigenMat=transpose matrix{cf,eigenCf};
(outDir|"/support-eigenvector-matrix.txt") << toString eigenMat << close;
(outDir|"/support-eigenvector-image.txt") << toString matrix{eigenCf} << close;
print("COMPLETE homogeneous Hamiltonian incidence 9x2; coefficient degrees "|toString apply(cf,degree));
print("common content, common denominator and nonzero F locus retained from attempt02");
exit 0;
