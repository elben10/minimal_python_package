#!/usr/bin/env python
import ctypes, os
import os
import shlex
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def has_admin():
    if os.name == 'nt':
        try:
            # only windows users with admin privileges can read the C:\windows\temp
            os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\\windows'),'temp']))
        except:
            return False
        else:
            return True
    else:
        if 'SUDO_USER' in os.environ and os.geteuid() == 0:
            return True
        else:
            return False


def gen_link(src, dist):
    if os.name == 'nt' and has_admin() == False:
        link = os.path.join(PROJECT_DIRECTORY, dist)
        target = os.path.join(PROJECT_DIRECTORY, src)
        subprocess.run(shlex.split(f'mklink /H "{link}" "{target}"'), shell=True)
    else:
        os.symlink(os.path.join(PROJECT_DIRECTORY, src), os.path.join(PROJECT_DIRECTORY, dist))


if __name__ == '__main__':
    gen_link('README.md', os.path.join('docs', 'index.md'))