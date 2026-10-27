#!/usr/bin/env python3
"""Exact rational Newton-hull and valuation-budget experiment (stdlib only).

This checks hull combinatorics, integer coefficient valuations, and the stated
budget identities. It does not calculate algebraic 2-adic roots or certify
residue-field cancellation strata. Optional argv[1] selects the JSON output.
"""
from fractions import Fraction as Q
import json
from pathlib import Path
import sys

def lower_hull(points):
    hull=[]
    for point in sorted(points):
        while len(hull)>1:
            p,q=hull[-2:]
            cross=(q[0]-p[0])*(point[1]-q[1])-(q[1]-p[1])*(point[0]-q[0])
            if cross>0: break
            hull.pop()
        hull.append(point)
    return hull

def root_weights(points):
    hull=lower_hull(points); values=[]
    for p,q in zip(hull,hull[1:]):
        weight=-(q[1]-p[1])/(q[0]-p[0])
        values += [weight]*(q[0]-p[0])
    return sorted(values),hull

def v2(n):
    n=abs(n); out=0
    if n==0: raise ValueError('zero has infinite valuation')
    while n%2==0: n//=2; out+=1
    return out

checks={}
checks['coefficient_v2']=[v2(n) for n in [4,6,288,176,27]]==[2,1,5,4,0]
# Cubic discriminant for x^3+b*x^2+c*x+d, with b=4,c=6,d=-eps.
checks['residual_discriminant_coefficients']=[4*4*6*6-4*6**3, 4*4**3-18*4*6, -27]==[-288,-176,-27]
# B(4+eps)=-27*(4+eps)^2+40*(4+eps)-16.
checks['parameter_discriminant_translation']=[-27*16+40*4-16,-27*8+40,-27]==[-288,-176,-27]
# epsilon=4*sqrt(2): B=A+Bcoef*sqrt(2); the two term weights differ.
quad_constant=-288-27*(4**2*2); quad_linear=-176*4
checks['ramified_example_coefficients']=(quad_constant,quad_linear)==(-1152,-704)
checks['ramified_example_weight']=min(Q(v2(quad_constant)),Q(v2(quad_linear))+Q(1,2))==Q(13,2)
checks['ramified_example_pair_depth']=Q(13,2)/2-1==Q(9,4)
samples=[]
for gamma in [Q(1,2),Q(1),Q(3,2),Q(7,4),Q(2),Q(9,4),Q(5,2),Q(3),Q(4),Q(5)]:
    h=Q(1)
    values,hull=root_weights([(0,gamma),(1,h),(2,2*h),(3,Q(0))])
    expected=sorted([gamma/3]*3 if gamma<=3*h/2 else [gamma-h,h/2,h/2])
    checks['hull_gamma_'+str(gamma)]=values==expected
    checks['marked_product_gamma_'+str(gamma)]=sum(values)==gamma
    row={'gamma_over_h':str(gamma),'root_weights_over_h':[str(v) for v in values], 'hull':[[x,str(y)] for x,y in hull]}
    if gamma>3*h/2:
        beta=min(2*gamma,5*h) # Generic value; at gamma=5h/2 cancellation can increase it.
        delta=beta/2-h
        pair_sum=gamma+h+delta
        full_disc=2*gamma+beta
        ell=gamma+delta-2*h
        checks['pair_budget_gamma_'+str(gamma)]=2*pair_sum==full_disc
        checks['elliptic_budget_gamma_'+str(gamma)]=8*h-2*ell==14*h-full_disc
        row.update({'generic_residual_pair_depth':str(delta),'generic_cross_ratio_depth':str(ell),'generic_discriminant_weight':str(full_disc),'critical_residue_possible':gamma==5*h/2})
    else:
        checks['star_pair_budget_gamma_'+str(gamma)]=2*6*(gamma/3)==4*gamma
    samples.append(row)
# The two epsilon-values for residual-sheet collisions both have weight5h/2.
bvals,bhull=root_weights([(0,Q(5)),(1,Q(4)),(2,Q(0))])
checks['residual_collision_parameter_weights']=bvals==[Q(5,2),Q(5,2)]
# At epsilon=-4, a=0: marked differences (h,h/2,h/2), other close pair h.
checks['mu4_recovery']=samples[4]['root_weights_over_h']==['1/2','1/2','1'] and samples[4]['generic_residual_pair_depth']=='1'
# Generic critical shell: beta=5h; cancellation beta>5h deepens residual pair.
critical=[]
for beta in [Q(5),Q(6),Q(7),Q(8),Q(10)]:
    gamma=Q(5,2); delta=beta/2-1; ell=gamma+delta-2
    checks['critical_budget_beta_'+str(beta)]=(2*gamma+beta)==2*(gamma+1+delta) and (14-(2*gamma+beta))==(8-2*ell)
    critical.append({'v_B_over_h':str(beta),'residual_pair_depth_over_h':str(delta),'cross_ratio_depth_over_h':str(ell)})
out={'scope':'Exact rational hull and budget checks; no algebraic root or residue cancellation computation.', 'passed':sum(checks.values()), 'total':len(checks),'checks':checks,'samples_h_equals_1':samples,'critical_shell_gamma_over_h_5_over_2':critical}
if not all(checks.values()): raise AssertionError(out)
encoded=json.dumps(out,indent=2)+'\n'
if len(sys.argv)>1: Path(sys.argv[1]).write_text(encoded)
print(encoded,end='')
