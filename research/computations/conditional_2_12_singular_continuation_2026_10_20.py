#!/usr/bin/env python3
"""Exact singular-root continuation: factor-coordinate exports and diagonal slice.

Loads the inherited universal formulas without rewriting inherited artifacts.
The diagonal slice is a proper slice, not a normal form under C0 automorphisms.
"""
import ast
from fractions import Fraction as Q
import json
from pathlib import Path


def load_equations():
    source = Path(__file__).with_name('generalization_quadratic_root_global_second_model.py')
    tree = ast.parse(source.read_text())
    stop = next(i for i,n in enumerate(tree.body) if isinstance(n,ast.Assign)
                and any(isinstance(t,ast.Name) and t.id=='stem' for t in n.targets))
    env={'__file__':str(source),'__name__':'singular_continuation_equations'}
    exec(compile(ast.Module(body=tree.body[:stop],type_ignores=[]),str(source),'exec'),env)
    return env


def main():
    env=load_equations()
    ca,cm,cs,var,fmt=(env[k] for k in ('ca','cm','cs','var','fmt'))
    stem=Path(__file__).with_suffix('')

    def substitute(p,values):
        result={}
        for m,c in p.items():
            term={():c}
            for i in m: term=cm(term,values[i])
            result=ca(result,term)
        return result

    def equations(name,polys):
        return name+'={'+','.join(fmt(p) for p in polys)+'};'

    # Full original-coordinate factors; no ambient PGL2 change is made.
    names=['A1','B1','C1','D1','A2','B2','C2','D2']+[f'h{i}' for i in range(12)]
    env['NAMES'][:]=names
    l1={(1,0,0):var(0),(1,0,1):var(2),(0,1,0):var(1),(0,1,1):var(3)}
    l2={(1,0,0):var(4),(1,0,1):var(6),(0,1,0):var(5),(0,1,1):var(7)}
    f=env['pm'](l1,l2)
    values=[f.get((2-i,i,j),{}) for i in range(3) for j in range(3)]
    values += [var(8+i) for i in range(12)]
    first=[substitute(p,values) for p in env['FIRST']]
    second=[substitute(p,values) for p in env['SECOND']]
    tau=ca(cm(var(0),var(7)),cm(var(4),var(3)),
           cs(cm(var(1),var(6)),Q(-1)),cs(cm(var(5),var(2)),Q(-1)))
    d1=ca(cm(var(0),var(3)),cs(cm(var(1),var(2)),Q(-1)))
    d2=ca(cm(var(4),var(7)),cs(cm(var(5),var(6)),Q(-1)))
    delta=cm(d1,d2)
    torsion_factored='tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)*((tau^2-2*delta)^2-3*delta^2)'
    full=stem.with_name(stem.name+'_two_node.m2')
    full.write_text('\n'.join([
        '-- Full two-node factors in original coordinates; exact incidence export.',
        'R=QQ['+','.join(names)+',MonomialOrder=>GRevLex];',
        equations('firstEquations',first),equations('secondEquations',second),
        'tau='+fmt(tau)+';','delta='+fmt(delta)+';',
        'torsionEquation='+torsion_factored+';',
        'twoNodeOpen=delta*(tau^2-4*delta);',
        'twoNodeIncidence=ideal join(firstEquations,secondEquations,{torsionEquation});',
        '-- Required open D(twoNodeOpen); h is unique on the root incidence.',
        '-- Add the global symbol and sextic cubic conditions before realization.',
        'print("TWO_NODE_ORIGINAL_COORDINATE_MODEL_READY");','']) )
    general_patch=stem.with_name(stem.name+'_general_patch.m2')
    patch_names=[f'h{i}' for i in range(12)]+['B1','C1','D1','B2','C2','D2']
    patch_values=[{():Q(1)},var(12),var(13),var(14),
                  {():Q(1)},var(15),var(16),var(17)]+[var(i) for i in range(12)]
    patch_first=[substitute(poly,patch_values) for poly in first]
    patch_tau=substitute(tau,patch_values)
    patch_delta=substitute(delta,patch_values)
    env['NAMES'][:]=patch_names
    general_patch.write_text('\n'.join([
        '-- One full-dimensional factor chart A1=A2=1; other charts retained.',
        'S=QQ['+','.join(patch_names)+',MonomialOrder=>Eliminate 12];',
        equations('firstEquations',patch_first),
        'I=ideal firstEquations;',
        'print("GENERAL_PATCH_FIRST_ELIMINATION_START");',
        'E=eliminate({'+','.join(patch_names[:12])+'},I);',
        'print("GENERAL_PATCH_FIRST_ELIMINATION_READY");print gens E;',
        'tau='+fmt(patch_tau)+';','delta='+fmt(patch_delta)+';',
        '-- Defer the degree22 torsion expansion until after first elimination.',
        'torsionEquation='+torsion_factored+';',
        'twoNodeOpen=delta*(tau^2-4*delta);',
        'J=saturate(E+ideal(torsionEquation),ideal(twoNodeOpen));',
        'print("GENERAL_PATCH_TORSION_SATURATION_READY");print gens gb J;',
        'print("GENERAL_PATCH_DIMENSION");print dim J;',
        '']) )

    # Proper torus-fixed diagonal slice: li=ti*u+z*v, ti nonzero/distinct.
    diag_names=[f'h{i}' for i in range(12)]+['t1','t2','iv']
    env['NAMES'][:]=diag_names
    t1,t2=var(12),var(13)
    zero={}
    diag_values=[cm(t1,t2),zero,zero,zero,ca(t1,t2),zero,zero,zero,{():Q(1)}]
    diag_values += [var(i) for i in range(12)]
    diag_first=[substitute(p,diag_values) for p in env['FIRST']]
    diag_second=[substitute(p,diag_values) for p in env['SECOND']]
    diag_g0={str(key):fmt(substitute(poly,diag_values)) for key,poly in env['G0'].items()}
    diagonal=stem.with_name(stem.name+'_diagonal.m2')
    diagonal.write_text('\n'.join([
        '-- Proper diagonal slice only; not full two-node coverage.',
        'R=QQ['+','.join(diag_names)+',MonomialOrder=>Eliminate 12];',
        equations('firstEquations',diag_first),equations('secondEquations',diag_second),
        'I1=ideal firstEquations;',
        'E1=eliminate({'+','.join(diag_names[:12])+'},I1);',
        'print("DIAGONAL_FIRST_ELIMINATION");print gens E1;',
        'torsion=sum(0..11,j->t1^(11-j)*t2^j);',
        'I1T=I1+ideal(torsion,iv*t1*t2*(t1-t2)-1);',
        'print("DIAGONAL_FIRST_PLUS_TORSION_GROEBNER");',
        'print gens gb I1T;',
        'I2T=I1T+ideal secondEquations;',
        'print("DIAGONAL_SECOND_PLUS_TORSION_GROEBNER");',
        'print gens gb I2T;',
        '']) )
    stem.with_suffix('.json').write_text(json.dumps({
        'status':'factor-coordinate exact export and proper diagonal-slice computation input',
        'full_two_node_parameters':names,
        'full_two_node_open':'Delta1*Delta2*(tau^2-4delta) != 0',
        'full_two_node_torsion':'tau*(tau^2-delta)*(tau^2-2delta)*(tau^2-3delta)*((tau^2-2delta)^2-3delta^2)=0',
        'diagonal_slice':'f=(t1*u+z*v)*(t2*u+z*v), t1*t2*(t1-t2)!=0',
        'diagonal_g0':diag_g0,
        'full_coverage_claimed':False,
    },indent=2)+'\n')
    print(json.dumps({'full_two_node_model':str(full),'general_patch_model':str(general_patch),
                      'diagonal_model':str(diagonal)},indent=2))


if __name__=='__main__':main()
