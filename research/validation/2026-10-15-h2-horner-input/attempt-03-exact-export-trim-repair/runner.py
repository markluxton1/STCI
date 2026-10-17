#!/usr/bin/env python3
"""Bounded format-only export and M2 load probe of already prepared polynomials."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shlex
import shutil
import signal
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "research/computations/generalization_quintic_h2_horner_input_2026_10_15.c"
INPUT = ROOT / "research/validation/2026-10-15-quintic-h2-unified-incidence/attempt-04-flint-preparation"
OUTPUT = ROOT / "research/validation/2026-10-15-h2-horner-input"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_bounded(command, directory, timeout):
    record = {"started_utc": datetime.now(timezone.utc).isoformat(),
              "command": [str(x) for x in command], "timeout_seconds": timeout,
              "scope": "Format-only conversion / load; no generator reconstruction, GB, saturation, or elimination."}
    started = time.monotonic()
    with (directory / "stdout.txt").open("wb") as out, (directory / "stderr.txt").open("wb") as err:
        process = subprocess.Popen(command, cwd=ROOT, stdout=out, stderr=err, start_new_session=True)
        try:
            record["exit_code"] = process.wait(timeout=timeout)
            record["status"] = "completed" if record["exit_code"] == 0 else "failed"
        except subprocess.TimeoutExpired:
            record["status"] = "interrupted-timeout"
            signal.killpg(process.pid, signal.SIGTERM)
            try:
                record["exit_code"] = process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                signal.killpg(process.pid, signal.SIGKILL)
                record["exit_code"] = process.wait()
    record["elapsed_seconds"] = time.monotonic() - started
    record["finished_utc"] = datetime.now(timezone.utc).isoformat()
    (directory / "execution-record.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record), flush=True)
    return record


def main():
    export = OUTPUT / "attempt-03-exact-export-trim-repair"
    load = OUTPUT / "attempt-04-qq-load-only"
    export.mkdir(parents=True, exist_ok=False)
    load.mkdir(parents=True, exist_ok=False)
    shutil.copyfile(SOURCE, export / "source.c")
    executable = Path("/private/tmp/stci-h2-horner-input-2026-10-15")
    flags = shlex.split(subprocess.check_output(["pkg-config", "--cflags", "--libs", "flint"], text=True))
    compile_command = ["/usr/bin/cc", "-O2", "-Wall", "-Wextra", str(SOURCE), "-o", str(executable), *flags]
    compiled = subprocess.run(compile_command, cwd=ROOT, capture_output=True, timeout=30)
    (export / "compile-stdout.txt").write_bytes(compiled.stdout)
    (export / "compile-stderr.txt").write_bytes(compiled.stderr)
    (export / "compile-command.json").write_text(json.dumps(compile_command, indent=2) + "\n")
    compiled.check_returncode()
    input_files = [INPUT / f"normalized-generator-{i}.txt" for i in range(12)]
    result = run_bounded([executable, export, *input_files], export, 30)
    if result["status"] != "completed":
        raise SystemExit("Export did not complete; no M2 load attempted")
    rows = [line.split("\t") for line in (export / "statistics.tsv").read_text().splitlines()[1:]]
    assert len(rows) == 12 and all(row[-1] == "true" for row in rows)
    manifest = {"scope": "Exact format-only export of the 12 existing normalized-generator files.",
                "source_sha256": sha(SOURCE), "runner_sha256": sha(Path(__file__)),
                "inputs": {f"normalized-generator-{i}.txt": sha(INPUT / f"normalized-generator-{i}.txt") for i in range(12)},
                "outputs": {f"horner-generator-{i}.txt": sha(export / f"horner-generator-{i}.txt") for i in range(12)}}
    (export / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    degrees = ",".join(row[1] for row in rows)
    counts = ",".join(row[2] for row in rows)
    relative_export = export.relative_to(ROOT).as_posix()
    relative_load = load.relative_to(ROOT).as_posix()
    script = f'''-- Load-only exact QQ import of verified format-only Horner expressions.
-- No generator construction, gb, saturation, elimination, factor, or dimension.
R=QQ[deltaPar,vPar,wPar];
genDir="{relative_export}";
outDir="{relative_load}";
save=(label,object)->((outDir|"/"|label|".txt") << toString object << close);
expectedDegrees={{{degrees}}};
expectedCounts={{{counts}}};
loadedGenerators=apply(toList(0..11),i->(
    save("stage","before-generator-"|toString i);
    f:=value get(genDir|"/horner-generator-"|toString i|".txt");
    assert(first degree f==expectedDegrees#i);
    assert(#terms f==expectedCounts#i);
    save("loaded-generator-"|toString i,{{first degree f,#terms f}});
    print("PASS loaded QQ generator "|toString i|" degree "|toString(first degree f)|" terms "|toString(#terms f));
    save("stage","after-generator-"|toString i);
    f));
assert(#loadedGenerators==12);
save("stage","complete-load-only");
print("COMPLETE QQ load-only: 12 Horner generators, expected degrees and exact term counts; no GB or saturation");
exit 0;
'''
    (load / "source.m2").write_text(script)
    load_result = run_bounded(["/opt/homebrew/bin/M2", "--script", load / "source.m2"], load, 45)
    load_result["source_sha256"] = sha(load / "source.m2")
    (load / "execution-record.json").write_text(json.dumps(load_result, indent=2) + "\n")
    print((export / "stdout.txt").read_text(), flush=True)
    print((load / "stdout.txt").read_text(), flush=True)
    print((load / "stderr.txt").read_text(), flush=True)


if __name__ == "__main__":
    main()
