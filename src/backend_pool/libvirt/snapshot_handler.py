# Copyright (c) 2019 Guilherme Borges <guilhermerosasborges@gmail.com>
# See the COPYRIGHT file for more information

import getpass
import shutil
import subprocess


def create_disk_snapshot(source_img, destination_img):
    try:
        shutil.chown(source_img, getpass.getuser())
    except Exception:  # TODO should be PermissionError under python 3, but python 2 does not have it
        # log.msg('Should have root to create snapshot')
        pass

    # could use `capture_output=True` instead of `stdout` and `stderr` args in Python 3.7
    out = subprocess.run(['qemu-img', 'create', '-f', 'qcow2', '-b', source_img, destination_img],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return out.returncode == 0
