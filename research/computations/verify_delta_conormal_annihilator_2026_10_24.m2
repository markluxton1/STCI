-- New exact samples for the scheme-theoretic conormal-annihilator proposal.
-- Full Rees saturation; finite samples do not prove the general theorem.
R=QQ[t,x,y,s,MonomialOrder=>Eliminate 1];
initialAlongI=(L)->trim sub(saturate(sub(L,{x=>s*x,y=>s*y}),ideal(s)),{s=>0});
I=ideal(x,y);
scan({1,2,3}, rr->(
 aa=t^rr;
 ff=aa*x+y^2;
 gg=aa*y+x^2;
 cancelElement=x^3-y^3;
 sampleIdeal=ideal(ff,gg);
 actualH=initialAlongI sampleIdeal;
 actualT=initialAlongI(I*sampleIdeal);
 positiveH=I*actualH;
 assert(x*gg-y*ff==cancelElement);
 assert(y*ff-x*gg+cancelElement==0);
 assert(-x^2*ff+y^2*gg+aa*cancelElement==0);
 assert(actualH==ideal(aa*x,aa*y,cancelElement));
 assert(actualT==ideal(aa*x^2,aa*x*y,aa*y^2,cancelElement));
 assert(isSubset(aa*actualT,positiveH));
 assert(not isSubset(t^(rr-1)*ideal(cancelElement),positiveH));
 print("PASS conormal annihilator: r="|toString rr|", degree=3, Ann(Delta)=(t^r)");
));
print "ALL 3 EXACT ANNIHILATOR SAMPLES PASS";
print "Boundary: these finite samples do not replace the general proof or establish a global projective realization.";
exit 0;
