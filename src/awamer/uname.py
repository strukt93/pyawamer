import os

def uname(a=False, m=False, n=False, p=False, r=False, s=False, v=False):
    basic_command = "uname"
    if a:
        basic_command += " -a"
        out = os.popen(basic_command).read().strip()
        return out
    if m:
        basic_command += " -m"
    if n:
        basic_command += " -n"
    if p:
        basic_command += " -p"
    if r:
        basic_command += " -r"
    if s:
        basic_command += " -s"
    if v:
        basic_command += " -v"
    out = os.popen(basic_command).read().strip()
    return out