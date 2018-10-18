#!/usr/bin/env python3
import re
import subprocess
from subprocess import PIPE

import env

cmd = ['mysqldump']
cmd += ['-h' + env.db_host]
cmd += ['-u' + env.db_user]
cmd += ['-p' + env.db_password]
cmd += ['--column-statistics=0']
cmd += ['--comments']
cmd += ['--databases', 'crowdpic']
cmd += ['--hex-blob']
cmd += ['--no-create-info']
cmd += ['--single-transaction']
cmd += ['--skip-extended-insert']

data = subprocess.Popen(cmd, stdout=PIPE).communicate()[0].decode()
line = data.split('\n')
for ll in line:
    ll = re.sub('^-- MySQL dump.*$', '', ll)
    ll = re.sub('^-- Host.*$', '', ll)
    ll = re.sub('^-- Server version.*$', '', ll)
    ll = re.sub('^-- Dump completed on.*$', '', ll)
    print(ll)
