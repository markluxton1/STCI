from pathlib import Path
import subprocess, hashlib, json, time, datetime
root=Path.cwd()
audit=root/"research/validation/2026-10-08-family2-quadratic-audit"
source=audit/"actual-tensor-reconstruction.m2"
input_manifest=audit/"actual-tensor-input-manifest.json"
for rec in json.loads(input_manifest.read_text())["inputs"]:
    assert hashlib.sha256((root/rec["snapshot"]).read_bytes()).hexdigest()==rec["sha256"]
source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
t0=time.monotonic()
cmd=["/opt/homebrew/bin/M2","--script",str(source.relative_to(root))]
log=audit/"actual-tensor-reconstruction.log"
with log.open("w") as stream:
    proc=subprocess.Popen(cmd,cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    for line in proc.stdout:
        stream.write(line)
        stream.flush()
        print(line,end="",flush=True)
    rc=proc.wait()
assert hashlib.sha256(source.read_bytes()).hexdigest()==source_hash, "Source changed during execution"
content=log.read_text()
passed=rc==0 and "ACTUAL_TENSOR_RECONSTRUCTION_COMPLETE" in content
result={"command":cmd,"started_utc":started,"elapsed_seconds":time.monotonic()-t0,"exit_code":rc,"status":"PASS" if passed else "FAIL","source_sha256":source_hash,"log_sha256":hashlib.sha256(log.read_bytes()).hexdigest(),"input_manifest_sha256":hashlib.sha256(input_manifest.read_bytes()).hexdigest(),"macaulay2_version":"1.26.06","scope":{"ancestor_columns":30,"actual_quartic_columns":18,"product_columns":540,"target_columns":2,"tensor_shape":[74,542],"literal_displayed_basis_equality":passed,"literal_compressed_matrix_equality":passed,"full_rowspace_equality":passed}}
(audit/"actual-tensor-reconstruction-result.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2),flush=True)
raise SystemExit(0 if passed else 1)
