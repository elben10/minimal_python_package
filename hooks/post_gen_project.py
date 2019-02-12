#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def gen_symlink(src, dist):
    os.symlink(os.path.join(PROJECT_DIRECTORY, src), os.path.join(PROJECT_DIRECTORY, dist))


if __name__ == '__main__':
    gen_symlink('README.md', 'docs/index.md')