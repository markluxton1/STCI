#!/usr/bin/env python3
"""One-pair mu3 collision chart, retaining its explicit rank-drop boundary.

D=(z-1)(z-omega)(z^2+e*z+ff), monic. On ff*S!=0, norm-symbol
compatibility is the displayed four-parameter family; no arbitrary root
coefficient chart or global sextic search is introduced.
"""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
accepted=HERE/'generalization_quadratic_root_curve_universal_incidence.json'
data=json.loads(accepted.read_text())
first=[]
for row,rhs in zip(data['A_f'],data['d_f']):
    terms=[f'({p})*h{j}' for j,p in enumerate(row) if p!='0']
    first.append('+'.join(terms)+f'-({rhs})')
stem=Path(__file__).with_suffix('')
lines=[
 '-- Generic one-pair collision chart; rank-drop factors explicitly retained.',
 'K=QQ[omega]/ideal(omega^2+omega+1);',
 'R=K[ee,ff,lambda,tt,H4,H5,H6,H7,fi,MonomialOrder=>GRevLex];',
 'd0=omega*ff; d1=omega^2*ff+omega*ee; d2=ff+omega^2*ee+omega; d3=ee+omega^2;',
 'a0=4*tt+2*ee*lambda; a1=d3/2+2*lambda; a2=1;',
 'b0=-d1/4-ff*lambda; b1=4*tt-d2/2+ee*lambda; b2=-d3/4+lambda;',
 'c0=d0/4; c1=d1/8-ff*lambda/2; c2=tt;',
 'h4=H4; h5=H5; h6=H6; h7=H7;',
 'h3=-a0*h5-a1*h4;',
 'h2=-3-a0*h4-a1*h3;',
 'h1=-4*a1+3*b2-a0*h3-a1*h2;',
 'h0=-5*a0+3*b1-a0*h2-a1*h1;',
 'c0Inverse=4*omega^2*fi;',
 'h8=-c0Inverse*(c2*h6+c1*h7);',
 'h9=-9/2-c0Inverse*(c2*h7+c1*h8);',
 'h10=c0Inverse*(-4*c1-3/8*b0-c2*h8-c1*h9);',
 'h11=c0Inverse*(-7/2*c2-3/8*b1-c2*h9-c1*h10);',
 'firstEquations={'+','.join(first)+'};',
 'endpointUnit=ff*fi-1;',
 'S=R[zz];',
 'aa=a0+a1*zz+zz^2; bb=b0+b1*zz+b2*zz^2; cc=c0+c1*zz+c2*zz^2;',
 'DD=(zz-1)*(zz-omega)*(zz^2+ee*zz+ff);',
 'U=d0+d3*zz^3; V=d1*zz+zz^4; W=d2*zz^2;',
 'alphaCanonical=U^2+V^2+W^2-U*V-U*W-V*W;',
 'coeffR=(p,j)->sub(coefficient(zz^j,p),R);',
 'normSymbol=apply(3,j->coeffR(alphaCanonical*aa,3*j+1)-coeffR(alphaCanonical*bb,3*j+2)-(j+1)*coeffR(alphaCanonical*DD,3*j+3)/4);',
 'assert(all(normSymbol,p->p==0));',
 'g30=-(a1*h5+a2*h4)-a2*h5*zz;',
 'g21=-(b1*h5+b2*h4+a1*h11+a2*h10)-(b2*h5+a2*h11)*zz;',
 'g12=-(3/4*a2+c1*h5+c2*h4+b1*h11+b2*h10)-(c2*h5+b2*h11)*zz;',
 'g03=-(3/8*b2+c1*h11+c2*h10)-c2*h11*zz;',
 'GG=g30*(-zz/2)^3+g21*(-zz/2)^2+g12*(-zz/2)+g03;',
 'LL=diff(zz,DD)-12*zz^2*GG;',
 'qlCoefficients=new MutableList from apply(7,j->coeffR(LL,j));',
 'scan(reverse toList(2..6),j->(v:=qlCoefficients#j;qlCoefficients#(j-2)=qlCoefficients#(j-2)-ff*v;qlCoefficients#(j-1)=qlCoefficients#(j-1)-ee*v;qlCoefficients#j=0));',
 'qlineEquations={qlCoefficients#0,qlCoefficients#1};',
 'collisionBoundary=((omega+1)*ee-ff-omega)*(ee^2-ff);',
 'collisionIdeal=ideal join(firstEquations,qlineEquations,{endpointUnit});',
 'print "ONE_PAIR_COLLISION_9VAR_MODEL_READY";',
 '-- Necessity on ff*collisionBoundary !=0. The boundary needs separate charts.',
 '-- No Groebner basis is run by this exporter.',
]
stem.with_suffix('.m2').write_text('\n'.join(lines)+'\n')
out={'status':'new exact collision chart; no emptiness assertion',
     'accepted_first_input_sha256':hashlib.sha256(accepted.read_bytes()).hexdigest(),
     'D':'(z-1)(z-omega)(z^2+e*z+f)',
     'normalization':'torus fixes one collision root to1; projective f scale makesDmonic',
     'symbol_kernel':'(v0,v1,v2)=lambda*(-f,e,1)',
     'deviation_coordinates':'v0=y0+d1/4,v1=y1-4t+d2/2,v2=y2+d3/4',
     'rank_drop_boundary':'S=((omega+1)*e-f-omega)*(e^2-f)',
     'boundary_meanings':['first factor: complete orbit {1,omega,omega^2}',
                          'second factor: residual quadratic itself is a mu3 pair'],
     'qline_condition':'On f*S!=0, exact norm-alpha qline condition is rem_(z^2+e*z+f)(Dprime-12*z^2*G)=0, two equations',
     'variables':['e','f','lambda','t','H4','H5','H6','H7','fInverse'],
     'h_elimination':'Eight accepted first equations solve h0..3,h8..11 usinga2=1,c0=omega*f/4. f*fInverse=1 retains all endpoint-nonzero points.',
     'limitations':'Endpointzero, completeorbit and two-pair boundary separately retained; no globalpair claim.'}
stem.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'model':str(stem.with_suffix('.m2')),'variables':9,'qline_equations':2},indent=2))
