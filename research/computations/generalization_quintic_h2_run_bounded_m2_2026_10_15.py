"""Run one new bounded M2 source, retaining PID, source/input hashes and exit."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import os
import signal
import subprocess

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("source",type=Path)
    parser.add_argument("output",type=Path)
    parser.add_argument("--seconds",type=int,default=45)
    parser.add_argument("--inputs-from",type=Path,required=True)
    parser.add_argument("--scope",default="NEW one bounded global shared ODE prospect; finite field only, not a QQ emptiness certificate")
    args=parser.parse_args()
    root=Path.cwd(); source=args.source.resolve(); out=args.output.resolve()
    out.mkdir(parents=True,exist_ok=True)
    previous=json.loads(args.inputs_from.read_text())
    inputs=previous.get("input_sha256",previous.get("inputs",{}))
    assert inputs, "An explicit previous input binding is required"
    for name,expected in inputs.items():
        assert digest(root/name)==expected, f"Input drift: {name}"
    captured=out/"source.m2"; captured.write_bytes(source.read_bytes())
    record={"started_utc":now(),"command":["/opt/homebrew/bin/M2","--script",str(captured)],
            "timeout_seconds":args.seconds,"source_sha256":digest(source),
            "input_sha256":inputs,"scope":args.scope,
            "prior_record":str(args.inputs_from)}
    process=subprocess.Popen(record["command"],cwd=root,stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,start_new_session=True)
    record.update(status="running",pid=process.pid,own_process_group=process.pid)
    record_path=out/"execution-record.json"
    record_path.write_text(json.dumps(record,indent=2)+"\n")
    print(f"running PID {process.pid}",flush=True)
    try:
        stdout,stderr=process.communicate(timeout=args.seconds)
        status="completed"
    except subprocess.TimeoutExpired:
        os.killpg(process.pid,signal.SIGTERM)
        try:
            stdout,stderr=process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid,signal.SIGKILL)
            stdout,stderr=process.communicate()
        status="interrupted-timeout"
    (out/"stdout.txt").write_bytes(stdout);(out/"stderr.txt").write_bytes(stderr)
    record.update(status=status,exit_code=process.returncode,finished_utc=now(),
                  stdout_sha256=hashlib.sha256(stdout).hexdigest(),
                  stderr_sha256=hashlib.sha256(stderr).hexdigest())
    record_path.write_text(json.dumps(record,indent=2)+"\n")
    print(stdout.decode());print(stderr.decode());print(status,process.returncode)
    print((out/"stage.txt").read_text() if (out/"stage.txt").exists() else "no-stage")

if __name__=="__main__":
    main()
