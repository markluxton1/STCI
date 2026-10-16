"""Bind and complete the fully written new model; do not reconstruct it."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT=Path.cwd()
INPUT=ROOT/"research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-02-name-repair"
OUTPUT=ROOT/"research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-04-completion"

def digest(data):
    return hashlib.sha256(data).hexdigest()

def matrix_entries(name):
    # The saved entries are expanded commutative polynomials, containing
    # no commas. A matrix is one row written as matrix {{...,...}}.
    text=(INPUT/name).read_text().strip()
    assert text.startswith("matrix {{") and text.endswith("}}"),name
    return text[len("matrix {{"):-2].split(",")

def main():
    OUTPUT.mkdir(parents=True,exist_ok=True)
    groups=[("h2CoverEquations-four-equations.txt",4),
            ("conductor-two-remainders.txt",2),
            ("ODE-eight-equations.txt",8),
            ("derived-three-accelerators.txt",3)]
    joined=[]
    for name,count in groups:
        entries=matrix_entries(name)
        assert len(entries)==count,name
        joined.extend(entries)
    whole=matrix_entries("global-seventeen-equations.txt")
    assert len(whole)==17 and joined==whole
    assert len(matrix_entries("actual-Q-coefficients.txt"))==7
    for name in ["global-seventeen-equations.txt","global-domain-unit.txt","actual-Q-coefficients.txt","equation-degrees.txt"]:
        (OUTPUT/name).write_bytes((INPUT/name).read_bytes())
    files=[p for p in sorted(INPUT.glob("*.txt"))]
    source=Path(__file__).resolve()
    record={"completed_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "source_path":str(source.relative_to(ROOT)),"source_sha256":digest(source.read_bytes()),
            "input_sha256":{str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in files},
            "assembly_record":str((INPUT/"execution-record.json").relative_to(ROOT)),
            "assembly_status":"all model files written; quotient/cofactor assertions passed; final informational count print failed",
            "scope":"NEW shape/group binding and completion of saved exact global model; no M2 or primitive polynomial replay",
            "status":"complete","exit_code":0}
    (OUTPUT/"execution-record.json").write_text(json.dumps(record,indent=2)+"\n")
    message="PASS exact group binding: 4 cover + 2 conductor remainders + 8 ODE + 3 accelerators = 17 equations; complete global input retained\n"
    (OUTPUT/"stdout.txt").write_text(message);(OUTPUT/"stderr.txt").write_text("")
    print(message,end="")

if __name__=="__main__":
    main()
