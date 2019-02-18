#!/usr/bin/env python
import ctypes
import os
import shlex
import shutil
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
        with open(os.devnull, 'wb') as f:
            subprocess.run(shlex.split(f'mklink /H "{link}" "{target}"'), shell=True, stdout=f)
    else:
        os.symlink(os.path.join(PROJECT_DIRECTORY, src), os.path.join(PROJECT_DIRECTORY, dist))

def rmtree(path):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, path))

if __name__ == '__main__':
    if '{{cookiecutter.add_docs}}' == 'yes':
        gen_link('README.md', os.path.join('docs', 'index.md'))
    else:
        rmtree('docs')

    if '{{cookiecutter.add_test}}' == 'no':
        rmtree('tests')
