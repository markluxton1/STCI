#!/usr/bin/env python3
"""Run exactly one bounded QQ global quadratic-root K2 Groebner prospect."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import resource
import signal
import subprocess
import time

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research/validation/2026-10-15-quadratic-root-global-second/attempt-01-QQ-full-smooth-family'
MODEL=ROOT/'research/computations/generalization_quadratic_root_global_second_model.m2'
GENERATOR=MODEL.with_suffix('.py')
CPU_SECONDS=45
WALL_SECONDS=60
RSS_LIMIT_KIB=1536*1024

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def limits():resource.setrlimit(resource.RLIMIT_CPU,(CPU_SECONDS,CPU_SECONDS+2))

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    record_path=OUT/'execution-record.json'
    if record_path.exists():raise SystemExit('Refusing to repeat this one prospect: execution record already exists')
    # Refuse to create an unmonitorable child. This sandbox may deny ps.
    try:
        probe=subprocess.run(['/bin/ps','-o','rss=','-p',str(os.getpid())],text=True,capture_output=True,check=True)
        int(probe.stdout.strip())
    except (OSError,subprocess.CalledProcessError,ValueError) as exc:
        raise SystemExit('Process monitor unavailable; no M2 launched: '+repr(exc))
    source=OUT/'source.m2' 
    source.write_text('\n'.join([
        'load "'+str(MODEL)+'";',
        'print("GB_START_QQ_FULL_SMOOTH_FAMILY");',
        'globalBasis=gb globalSecondIdeal;',
        'globalRemainder=1_R % globalBasis;',
        'print("GB_COMPLETE");',
        'print("BASIS_COLUMNS="+toString numColumns gens globalBasis);',
        'print("UNIT_REMAINDER="+toString globalRemainder);',
        'if globalRemainder==0 then print("EXACT_QQ_UNIT_IDEAL") else print("EXACT_QQ_NONUNIT_IDEAL");'
    ])+'\n')
    record={
        'status':'starting','started_utc':utc(),
        'command':['/opt/homebrew/bin/M2','--script',str(source)],
        'source_sha256':sha(source),
        'input_sha256':{str(MODEL.relative_to(ROOT)):sha(MODEL),str(GENERATOR.relative_to(ROOT)):sha(GENERATOR)},
        'cpu_limit_seconds':CPU_SECONDS,'wall_limit_seconds':WALL_SECONDS,
        'rss_kib_stop_threshold':RSS_LIMIT_KIB,
        'rss_monitor_note':'Observed process RSS polled every 0.25 seconds; threshold triggers termination of this own process group, not a kernel hard memory cap.',
        'scope':'ONE exact QQ global K1+K2 full smooth-family prospect; no coefficient chart; no emptiness inferred from timeout/failure.'
    }
    stdout=OUT/'stdout.txt';stderr=OUT/'stderr.txt'
    with stdout.open('wb') as out,stderr.open('wb') as err:
        process=subprocess.Popen(record['command'],cwd=ROOT,stdout=out,stderr=err,start_new_session=True,preexec_fn=limits)
        record.update(status='running',pid=process.pid,own_process_group=process.pid)
        record_path.write_text(json.dumps(record,indent=2)+'\n')
        print('RUNNING_PID='+str(process.pid),flush=True)
        start=time.monotonic();maximum_rss=0;reason=None
        while process.poll() is None:
            elapsed=time.monotonic()-start
            if elapsed>WALL_SECONDS:reason='wall-limit';break
            try:
                rss_text=subprocess.check_output(['/bin/ps','-o','rss=','-p',str(process.pid)],text=True,stderr=subprocess.DEVNULL).strip()
                current_rss=int(rss_text) if rss_text else 0
                maximum_rss=max(maximum_rss,current_rss)
                if current_rss>RSS_LIMIT_KIB:reason='rss-threshold';break
            except (OSError,subprocess.CalledProcessError,ValueError) as exc:
                reason='monitor-unavailable'
                record['monitor_error']=repr(exc)
                break
            time.sleep(.25)
        if reason:
            os.killpg(process.pid,signal.SIGTERM)
            try:process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid,signal.SIGKILL);process.wait(timeout=3)
        else:process.wait()
    record.update(status='terminated-'+reason if reason else 'exited',exit_code=process.returncode,finished_utc=utc(),elapsed_wall_seconds=time.monotonic()-start,max_observed_rss_kib=maximum_rss,reaped=True)
    if process.returncode<0:record['exit_signal']=-process.returncode
    record['stdout_sha256']=sha(stdout);record['stderr_sha256']=sha(stderr)
    record['exact_unit_marker_present']='EXACT_QQ_UNIT_IDEAL' in stdout.read_text(errors='replace')
    record_path.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2),flush=True)
    print('STDOUT_TAIL\n'+stdout.read_text(errors='replace')[-5000:],flush=True)
    print('STDERR_TAIL\n'+stderr.read_text(errors='replace')[-5000:],flush=True)

if __name__=='__main__':main()
