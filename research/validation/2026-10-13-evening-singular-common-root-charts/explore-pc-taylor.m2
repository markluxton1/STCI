pcBase=QQ[q]; KK=frac(pcBase/ideal(q^2-6*q+6));
S=KK[delta,a,kappa]; qvalue=sub(KK_0,S);
origRing=QQ[delta,a,B,q];
uFiles=apply(0..7,i->value get ("research/validation/2026-10-12-nonendpoint-single-root-taylor/20261013T142033115594Z/nonendpoint_single_root_u"|toString i|".txt"));
mapper=map(S,origRing,{S_0,S_1,S_2-S_1*qvalue,qvalue});
uPc=apply(uFiles,x->mapper(x));
scan(0..7,i->print("u"|toString i|"="|toString uPc#i));
