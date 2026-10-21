#!/usr/bin/env python3
"""Exact compact endpoint K1+actual-global-cubic models, no CAS launched."""
import ast,json
from pathlib import Path
from fractions import Fraction as Q
HERE=Path(__file__).resolve().parent
old=HERE/'conditional_2_12_elimination_2026_10_20.py'
tree=ast.parse(old.read_text());stop=next(i for i,n in enumerate(tree.body) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='first' for t in n.targets))
e={'__file__':str(old),'__name__':'cont2_endpoint_export'};exec(compile(ast.Module(body=tree.body[:stop],type_ignores=[]),str(old),'exec'),e)
ca,cm,cs,cp,var,const=(e[x] for x in ['ca','cm','cs','cp','var','const'])
padd,pscale,pmul=(e[x] for x in ['pzadd','pzscale','pzmul']);K=e['K'];inherited=e['e'];data=e['data']
def model(case):
 if case=='m4_a0unit':names=['q','t','hh4','hh5','hh10','hh11','eta','iv']
 elif case=='m4': names=['p','q','t','hh4','hh5','hh10','hh11','eta','iv','av']
 elif case=='m3_b0zero':names=['p','t','hh4','hh5','hh10','hh11','eta','iv','av']
 else:names=['p','q','t','hh4','hh5','hh6','hh11','eta','iv']
 V={n:var(i) for i,n in enumerate(names)};t=V['t'];p=V.get('p',ca(cs(t,2),const(Q(1,2))));q=V.get('q',ca(p,cs(t,-4),const(Q(-1,4))))
 b0={} if case!='m3_b0nonzero' else ca(const(Q(1,4)),q,cs(p,-1),cs(t,4))
 d3=0 if case.startswith('m4') else 1
 F=[ca(cs(p,2),cs(t,-4)),ca(const(d3),cs(q,2)),const(1),b0,p,q,{},cs(b0,Q(1,2)),t]
 H=[{} for _ in range(12)];H[4]=V['hh4'];H[5]=V['hh5'];H[11]=V['hh11']
 if case=='m3_b0nonzero':
  H[6]=V['hh6'];H[7]=cs(cm(cm(t,V['iv']),H[6]),-2);H[8]=cs(cm(cm(t,V['iv']),H[7]),-2)
  H[9]=ca(const(Q(-19,4)),cs(cm(cm(t,V['iv']),H[8]),-2))
  H[10]=ca(cs(cm(p,V['iv']),Q(-3,4)),cs(cm(t,V['iv']),-7),cs(cm(cm(t,V['iv']),H[9]),-2))
  inverse=ca(cm(b0,V['iv']),const(-1));opens=['b0 !=0']
 else:
  H[6]=H[7]=H[8]={};H[9]=ca(cs(cm(p,V['iv']),Q(-3,8)),const(Q(-7,2)));H[10]=V['hh10']
  inverse=ca(cm(t,V['iv']),const(-1));opens=['c2=t !=0','a0=2p-4t !=0']
 H[3]=ca(cs(cm(F[0],H[5]),-1),cs(cm(F[1],H[4]),-1))
 H[2]=ca(const(-3),cs(cm(F[0],H[4]),-1),cs(cm(F[1],H[3]),-1))
 H[1]=ca(cs(F[1],-4),cs(F[5],3),cs(cm(F[0],H[3]),-1),cs(cm(F[1],H[2]),-1))
 H[0]=ca(cs(F[0],-5),cs(F[4],3),cs(cm(F[0],H[2]),-1),cs(cm(F[1],H[1]),-1))
 replacement=F+H
 def sub(poly):
  out={}
  for m,v in poly.items():
   term=const(v)
   for j in m:term=cm(term,replacement[j])
   out=ca(out,term)
  return out
 first=[sub(poly) for poly in inherited['FIRST']];assert not any(first[:4])
 alpha={8:Q(1)} if case.startswith('m4') else {6:Q(1),7:Q(-1),8:Q(1)}
 af=[]
 for comp in range(3):
  af += [ca(*(cs(F[3*comp+j-k],a) for k,a in alpha.items() if 0<=j-k<=2)) for j in range(11)]
 symbols=[ca(*(cs(p,Q(c)) for p,c in zip(af,row) if Q(c))) for row in data['annihilator_11_by_33']];assert not any(symbols)
 G=[{j:sub(inherited['G0'].get((3-i,i,j),{})) for j in range(2)} for i in range(4)]
 T=[]
 imageRows=data['image_rank_certificate']['minor_rows_zero_based']
 for i in range(4):
  pol={j:ca(*(cs(af[imageRows[k]],K[10*i+j][k]) for k in range(22) if K[10*i+j][k])) for j in range(10)}
  pol=padd(pol,pscale(pmul({k:const(a) for k,a in alpha.items()},G[i]),-1))
  pol=padd(pol,{i:cs(V['eta'],[Q(1),Q(3,2),Q(3,4),Q(1,8)][i])});T.append(pol)
 a,b,c=[{j:F[3*i+j] for j in range(3)} for i in range(3)]
 a2,b2,c2,ab,ac,bc=[pmul(x,y) for x,y in [(a,a),(b,b),(c,c),(a,b),(a,c),(b,c)]]
 syz=[padd(pmul(padd(b2,pscale(ac,-1)),T[0]),pscale(pmul(ab,T[1]),-1),pmul(a2,T[2])),padd(pmul(bc,T[0]),pscale(pmul(ac,T[1]),-1),pmul(a2,T[3])),padd(pmul(c2,T[0]),pscale(pmul(ac,T[2]),-1),pmul(ab,T[3])),padd(pmul(c2,T[1]),pscale(pmul(bc,T[2]),-1),pmul(padd(b2,pscale(ac,-1)),T[3]))]
 cubic=[v for poly in syz for j,v in sorted(poly.items()) if v]
 def fmt(poly):
  terms=[]
  for m,v in sorted(poly.items(),key=lambda x:(len(x[0]),x[0])):
   mon='*'.join(names[i]+('^'+str(m.count(i)) if m.count(i)>1 else '') for i in sorted(set(m)))
   terms.append('('+str(v)+')'+('*'+mon if mon else ''))
  return '+'.join(terms) or '0'
 equations=lambda ps:'{'+','.join(fmt(p) for p in ps if p)+'}'
 opensEq=[inverse]
 if 'av' in V:opensEq.append(ca(cm(F[0],V['av']),const(-1)))
 stem=HERE/('conditional_2_12_cont2_endpoint_'+case+'_2026_10_21')
 lines=['-- Endpoint model, all alpha zeros retained; no smoothness inverse.', 'R=QQ['+','.join(names)+',MonomialOrder=>GRevLex];','firstEquations='+equations(first)+';','cubicEquations='+equations(cubic)+';','openEquations='+equations(opensEq)+';','endpointFirstIdeal=ideal join(firstEquations,openEquations);','endpointCubicIdeal=endpointFirstIdeal+ideal cubicEquations;','print("ENDPOINT_MODEL_READY '+case+': '+str(len(names))+' variables,'+str(sum(bool(p) for p in first))+' first,'+str(len(cubic))+' cubic");']
 stem.with_suffix('.m2').write_text('\n'.join(lines)+'\n')
 return {'case':case,'variables':names,'root_open':opens,'D':'z^4' if case.startswith('m4') else 'z^3+z^4','alpha':'z^8' if case.startswith('m4') else 'z^6-z^7+z^8','first_equations':sum(bool(p) for p in first),'cubic_equations':len(cubic),'file':str(stem.with_suffix('.m2'))}
meta={'status':'exact endpoint incidence presentations; no emptiness claimed','configuration':[2,12,6,16,2],'cases':[model(c) for c in ['m4','m4_a0unit','m3_b0zero','m3_b0nonzero']],'authority':'new proposal; endpoint reduction and norm multiplier necessity require separate audited arguments','preserves_singular_roots':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta,indent=2))
