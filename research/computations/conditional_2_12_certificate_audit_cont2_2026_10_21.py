#!/usr/bin/env python3
"""Independent substitutions into the preserved universal FIRST operator.

Only new line/boundary certificates are replayed. This file does not execute
the inherited Python generator or any inherited mathematical verifier.
"""
from pathlib import Path
import re
import subprocess
import json

HERE = Path(__file__).resolve().parent
STEM = HERE / 'conditional_2_12_certificate_audit_cont2_2026_10_21'


def first_block(path):
    return path.read_text().split('firstEquations={', 1)[1].split('};', 1)[0]


def main():
    universal = first_block(HERE / 'generalization_quadratic_root_global_second_model.m2')
    original_names = [f'{s}{i}' for s in 'abc' for i in range(3)] + [f'h{i}' for i in range(12)]
    rows = ['-- Independent reconstruction from original factor coefficients.',
            'U=QQ[' + ','.join(original_names) + '];',
            'universalFirst={' + universal + '};']
    for primitive in [False, True]:
        tag = 'PRIMITIVE' if primitive else 'W1'
        field = 'K=toField(QQ[ww]/ideal(ww^2+ww+1));' if primitive else 'K=QQ;'
        rows += [field, 'R=K[h4,h5,h6,h7,a,x];',
                 'w=sub(K_0,R);' if primitive else 'w=1_R;',
                 '-- f=l1*l2, with no separate ruling action.',
                 'A1=a-x;D1=(a+x)/2;A2=-w^2*(a+x);D2=w^2*(a-x)/2;',
                 '-- Universal FIRST uses a0,a1,a2,b0,b1,b2,c0,c1,c2 (not z-degree grouping).',
                 'ff={A1*A2,A1+A2,1,A1*w+A2,A1*D2+A2*D1+1+w,D1+D2,w,D2+w*D1,D1*D2};',
                 '-- Solve only original rows 0..3 and 12..15; w is a unit.',
                 'hh3=-(ff#0*h5+ff#1*h4)/ff#2;',
                 'hh2=(-3*ff#2-ff#0*h4-ff#1*hh3)/ff#2;',
                 'hh1=(-4*ff#1+3*ff#5-ff#0*hh3-ff#1*hh2)/ff#2;',
                 'hh0=(-5*ff#0+3*ff#4-ff#0*hh2-ff#1*hh1)/ff#2;',
                 'hh8=(-ff#7*h7-ff#8*h6)/ff#6;',
                 'hh9=(-9/2*ff#6-ff#7*hh8-ff#8*h7)/ff#6;',
                 'hh10=(-3*ff#3/8-4*ff#7-ff#7*hh9-ff#8*hh8)/ff#6;',
                 'hh11=(-3*ff#4/8-7*ff#8/2-ff#7*hh10-ff#8*hh9)/ff#6;',
                 'phi=map(R,U,join(ff,{hh0,hh1,hh2,hh3,h4,h5,h6,h7,hh8,hh9,hh10,hh11}));',
                 'actual=apply(universalFirst,e->phi(e));']
        suffix = 'primitive' if primitive else 'w1'
        source = HERE / f'conditional_2_12_singular_continuation_2026_10_21_line_component_{suffix}.m2'
        target = first_block(source)
        if not primitive:
            target = re.sub(r'\bp\b', '(a*a)', target)
        rows += ['exported={' + target + '};',
                 f'assert all({{0,1,2,3,12,13,14,15}},i->actual#i==0);',
                 'assert(take(drop(actual,4),8)==exported);',
                 f'print("{tag}_LINE_SAVED_FIRST_EXACT_MATCH");',
                 '-- Reconstruct trace and determinant directly from factor matrices.',
                 'M1=matrix{{-1,-D1},{A1,1}};M2=matrix{{-1,-D2},{A2,w}};',
                 'N=matrix{{1,D1},{-A1,-1}}*M2;',
                 'tau=trace N;de=det N;',
                 'assert(tau==-w^2*(a^2+x^2)-1-w);',
                 'assert(de==w*((a^2-x^2-2)/2)^2);',
                 'disc=tau^2-4*de;',
                 'expectedDisc=4*(a^2)*(x^2+2);' if not primitive else 'expectedDisc=w*(2*a^2-3)*(2*x^2+1);',
                 'assert(disc==expectedDisc);',
                 f'print("{tag}_LINE_TRACE_DETERMINANT_OPEN_MATCH");']
    for primitive in [False, True]:
        tag = 'PRIMITIVE' if primitive else 'W1'
        rows += ['K=toField(QQ[ww]/ideal(ww^2+ww+1));' if primitive else 'K=QQ;',
                 'R=K[' + ','.join([f'h{i}' for i in range(12)] + ['t']) + '];',
                 'w=sub(K_0,R);' if primitive else 'w=1_R;',
                 '-- Direct multiplication of (t+z)u+zv and (-2w^2+z)u-w^2*t*z*v/2.',
                 'ff={-2*w^2*t,t-2*w^2,1,0,-w^2*(t^2/2+2),1-w^2*t/2,0,0,-w^2*t/2};',
                 'phi=map(R,U,join(ff,{' + ','.join(f'h{i}' for i in range(12)) + '}));',
                 'actual=apply(universalFirst,e->phi(e));']
        suffix = 'primitive' if primitive else 'w1'
        source = HERE / f'conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_{suffix}.m2'
        rows += ['exported={' + first_block(source) + '};',
                 'assert(actual==exported);',
                 f'print("{tag}_BOUNDARY_SAVED_FIRST_EXACT_MATCH");',
                 'A1=t;D1=1;A2=-2*w^2;D2=-w^2*t/2;',
                 'N=matrix{{1,D1},{-A1,0}}*matrix{{0,-D2},{A2,1}};',
                 'tau=trace N;de=det N;',
                 'assert(tau==-w^2*(t^2/2+2));assert(de==w*t^2);',
                 'assert(tau^2-4*de==w*(t^2-4)^2/4);',
                 f'print("{tag}_BOUNDARY_TRACE_DETERMINANT_OPEN_MATCH");']
    rows += ['-- Exact Cayley-Hamilton U_11 recurrence and scalar-matrix scheme.',
             'R=QQ[tau,de];u0=1_R;u1=tau;',
             'scan(2..11,i->(ui=tau*u1-de*u0;u0=u1;u1=ui));',
             'q=tau*(tau^2-de)*(tau^2-2*de)*(tau^2-3*de)*((tau^2-2*de)^2-3*de^2);',
             'assert(u1==q);print("Q12_EXACT_RECURRENCE_MATCH");']
    model = STEM.with_suffix('.m2')
    model.write_text('\n'.join(rows) + '\n')
    reports = []
    for source in [model] + [
        HERE / 'conditional_2_12_singular_continuation_2026_10_21_line_component_w1.m2',
        HERE / 'conditional_2_12_singular_continuation_2026_10_21_line_component_primitive.m2',
        HERE / 'conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_w1.m2',
        HERE / 'conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_primitive.m2',
    ]:
        run = subprocess.run(['/opt/homebrew/bin/M2', '--script', str(source)], text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=30)
        reports.append({'source': source.name, 'returncode': run.returncode, 'output': run.stdout})
        if run.returncode:
            break
    STEM.with_suffix('.json').write_text(json.dumps(reports, indent=2) + '\n')
    print(json.dumps(reports, indent=2))
    assert all(r['returncode'] == 0 for r in reports)


if __name__ == '__main__':
    main()
