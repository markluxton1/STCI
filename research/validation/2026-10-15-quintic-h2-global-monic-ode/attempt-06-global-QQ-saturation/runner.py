"""One guarded new global QQ prospect; preflight every monitor before M2."""
from pathlib import Path
import ctypes
import datetime
import hashlib
import json
import os
import resource
import select
import signal
import subprocess
import sys
import time

ROOT=Path.cwd()
OUT=ROOT/"research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation"
SOURCE=ROOT/"research/computations/generalization_quintic_h2_global_QQ_saturation_2026_10_16.m2"
LOADER=ROOT/"research/computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2"
BINDING=ROOT/"research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-05-load-only/input-binding.json"
LOAD_RECORD=ROOT/"research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-05-load-only/execution-record.json"
WALL_SECONDS=120
CPU_SECONDS=120
RSS_STOP_BYTES=1536*1024*1024
POLL_SECONDS=0.25

class Usage(ctypes.Structure):
    # rusage_info_v2, as declared in the local macOS SDK sys/resource.h.
    _fields_=[("uuid",ctypes.c_uint8*16)]+[(name,ctypes.c_uint64) for name in
        ["user","system","pkg","interrupt","pageins","wired","resident",
         "footprint","start","exit","child_user","child_system","child_pkg",
         "child_interrupt","child_pageins","child_elapsed","disk_read","disk_write"]]

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_json(path,value):
    temporary=path.with_name(path.name+".tmp")
    temporary.write_text(json.dumps(value,indent=2)+"\n")
    os.replace(temporary,path)

def cpu_limit():
    resource.setrlimit(resource.RLIMIT_CPU,(CPU_SECONDS,CPU_SECONDS))

def stop_group(process):
    events=[]
    try:
        os.killpg(process.pid,signal.SIGTERM);events.append("SIGTERM-private-group")
    except ProcessLookupError:
        events.append("private-group-already-absent")
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(process.pid,signal.SIGKILL);events.append("SIGKILL-private-group")
        except ProcessLookupError:
            events.append("private-group-exited-before-SIGKILL")
        process.wait(timeout=5)
    # A direct child can exit before another member of its private group.
    try:
        os.killpg(process.pid,0)
    except ProcessLookupError:
        events.append("private-group-absent")
    else:
        try:
            os.killpg(process.pid,signal.SIGKILL);events.append("SIGKILL-remaining-private-group")
        except ProcessLookupError:
            events.append("private-group-absent")
        for _ in range(20):
            try:
                os.killpg(process.pid,0)
            except ProcessLookupError:
                events.append("private-group-absent");break
            time.sleep(0.05)
    return events

def preflight_monitor():
    library=ctypes.CDLL("/usr/lib/libproc.dylib",use_errno=True)
    api=library.proc_pid_rusage
    api.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_void_p]
    api.restype=ctypes.c_int
    assert ctypes.sizeof(Usage)==160

    def usage(pid):
        value=Usage();ctypes.set_errno(0)
        result=api(pid,2,ctypes.byref(value))
        if result!=0:
            raise OSError(ctypes.get_errno(),"proc_pid_rusage monitor failed")
        return {"resident_bytes":value.resident,"footprint_bytes":value.footprint,
                "user_time_raw":value.user,"system_time_raw":value.system}

    own=usage(os.getpid())
    probe_code=("import os,resource,json,time; "
                "data=bytearray(b'x')*(32*1024*1024); "
                "print(json.dumps({'pid':os.getpid(),'pgid':os.getpgrp(),"
                "'cpu_limit':resource.getrlimit(resource.RLIMIT_CPU)}),flush=True); "
                "time.sleep(30)")
    probe=subprocess.Popen([sys.executable,"-c",probe_code],stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,start_new_session=True,preexec_fn=cpu_limit)
    try:
        readable,_,_=select.select([probe.stdout],[],[],5)
        if not readable:
            raise RuntimeError("preflight child did not become ready")
        child=json.loads(probe.stdout.readline())
        assert child["pid"]==probe.pid and child["pgid"]==probe.pid
        assert child["cpu_limit"]==[CPU_SECONDS,CPU_SECONDS]
        sample=usage(probe.pid)
        assert sample["resident_bytes"]>1024*1024
        # Simulate a one-MiB stop threshold. This tests the same own-group
        # termination/wait path without approaching the actual job limit.
        cleanup=stop_group(probe)
        assert probe.returncode is not None
        assert "private-group-absent" in cleanup
        return usage,{"status":"passed","own_process_sample":own,"probe_child":child,
                      "probe_sample":sample,"simulated_stop_bytes":1024*1024,
                      "probe_actual_exit_code":probe.returncode,"cleanup":cleanup}
    finally:
        if probe.poll() is None:
            stop_group(probe)
        if probe.stdout:probe.stdout.close()
        if probe.stderr:probe.stderr.close()

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    if (OUT/"execution-record.json").exists():
        raise RuntimeError("This single-attempt output already has a record; refusing restart")
    runner=Path(__file__).resolve()
    record={"prepared_utc":now(),"scope":"ONE NEW whole-h2 global QQ saturation prospect; no accepted assembly or verifier replay",
            "wall_seconds":WALL_SECONDS,"cpu_seconds_soft_hard":[CPU_SECONDS,CPU_SECONDS],
            "rss_stop_bytes":RSS_STOP_BYTES,"rss_poll_seconds":POLL_SECONDS,
            "rss_guard_kind":"polled max(resident,physical-footprint) stop threshold, not a hard virtual-address limit",
            "runner_sha256":sha(runner),"source_sha256":sha(SOURCE),
            "input_sha256":json.loads(BINDING.read_text())["input_sha256"]}
    record["input_sha256"][str(LOADER.relative_to(ROOT))]=json.loads(LOAD_RECORD.read_text())["source_sha256"]
    record["expected_loader_hash_record"]=str(LOAD_RECORD.relative_to(ROOT))
    (OUT/"source.m2").write_bytes(SOURCE.read_bytes())
    (OUT/"runner.py").write_bytes(runner.read_bytes())
    try:
        for name,expected in record["input_sha256"].items():
            assert sha(ROOT/name)==expected,"Input drift: "+name
        monitor,preflight=preflight_monitor()
        record["preflight"]=preflight
        write_json(OUT/"preflight-record.json",preflight)
    except Exception as error:
        record.update(status="blocked-before-M2-launch",error=repr(error),m2_started=False)
        write_json(OUT/"execution-record.json",record)
        print("PREFLIGHT BLOCKED; no Macaulay2 process started:",repr(error),flush=True)
        return 2
    command=["/opt/homebrew/bin/M2","--script",str(OUT/"source.m2")]
    record.update(command=command,started_utc=now(),m2_started=False)
    start=time.monotonic();before=resource.getrusage(resource.RUSAGE_CHILDREN)
    cleanup=[];reason=None;peak_resident=0;peak_footprint=0
    process=None;caught_exception=None;cleanup_exception=None
    with (OUT/"stdout.txt").open("wb") as stdout,(OUT/"stderr.txt").open("wb") as stderr:
        try:
            process=subprocess.Popen(command,cwd=ROOT,stdout=stdout,stderr=stderr,
                                     start_new_session=True,preexec_fn=cpu_limit)
            # ALL operations after Popen, including initial provenance writes,
            # are inside this try/finally's guaranteed group cleanup.
            record.update(status="running",pid=process.pid,own_process_group=process.pid,
                          m2_started=True)
            write_json(OUT/"execution-record.json",record)
            print("PREFLIGHT PASS; M2 running PID",process.pid,flush=True)
            while process.poll() is None:
                elapsed=time.monotonic()-start
                if elapsed>=WALL_SECONDS:
                    reason="wall-time-limit";break
                try:
                    sample=monitor(process.pid)
                except Exception as error:
                    if process.poll() is not None:break
                    reason="monitor-failed-closed: "+repr(error);break
                peak_resident=max(peak_resident,sample["resident_bytes"])
                peak_footprint=max(peak_footprint,sample["footprint_bytes"])
                write_json(OUT/"live-metrics.json",dict(elapsed_wall_seconds=elapsed,
                    pid=process.pid,peak_resident_bytes=peak_resident,
                    peak_footprint_bytes=peak_footprint,**sample))
                if max(sample["resident_bytes"],sample["footprint_bytes"])>RSS_STOP_BYTES:
                    reason="polled-memory-stop-threshold";break
                time.sleep(POLL_SECONDS)
            if reason is None:
                process.wait(timeout=5)
        except BaseException as error:
            caught_exception=repr(error)
            reason="guard-or-launch-exception"
        finally:
            if process is not None:
                try:
                    cleanup=stop_group(process)
                except BaseException as error:
                    cleanup_exception=repr(error)
                    # A direct-child fallback is retained and reported if an
                    # unexpected group-cleanup error occurs after preflight.
                    try:
                        if process.poll() is None:process.kill()
                        process.wait(timeout=5)
                        cleanup.append("fallback-direct-child-reaped")
                    except BaseException as fallback_error:
                        cleanup.append("fallback-error: "+repr(fallback_error))
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    actual_exit=None if process is None else process.returncode
    if caught_exception is not None or cleanup_exception is not None:
        status="failed-guard-or-launch"
    elif reason is not None:
        status="interrupted"
    elif actual_exit==0:
        status="completed"
    elif actual_exit is not None and actual_exit<0:
        status="interrupted-process-signal"
        reason="process-signal-"+str(-actual_exit)
    else:
        status="failed-process"
        reason="nonzero-process-exit"
    record.update(status=status,stop_reason=reason,actual_exit_code=actual_exit,
                  caught_exception=caught_exception,cleanup_exception=cleanup_exception,
                  finished_utc=now(),elapsed_wall_seconds=time.monotonic()-start,
                  cpu_seconds=(after.ru_utime-before.ru_utime)+(after.ru_stime-before.ru_stime),
                  peak_resident_bytes=peak_resident,peak_footprint_bytes=peak_footprint,
                  cleanup=cleanup,stdout_sha256=sha(OUT/"stdout.txt"),stderr_sha256=sha(OUT/"stderr.txt"))
    # Terminal evidence is persisted after cleanup even for caught exceptions.
    write_json(OUT/"execution-record.json",record)
    print("TERMINAL",status,reason,"exit",actual_exit,flush=True)
    print((OUT/"stage.txt").read_text() if (OUT/"stage.txt").exists() else "no-stage",flush=True)
    return 1 if status.startswith("failed") else 0

if __name__=="__main__":
    raise SystemExit(main())
