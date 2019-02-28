#!/usr/bin/env python

import sys
import time

from tayga import Tayga


with open(Tayga.exapath("./tayga-r2.pream.conf")) as fd:
    tayga2_pream = "".join(fd.readlines())


map_rules = {}

try:
    now = time.time()
    while True:
        line = sys.stdin.readline().strip()
        if 'shutdown' in line:
            break
        sys.stderr.write("--- " + line + '\n')
        sys.stderr.flush()
        if 'eor' in line:
            sys.stderr.write("eor " + str(map_rules) + '\n')
            sys.stderr.flush()
            if map_rules:
                map_rules = dict(map_rules)
                Tayga.gen_conf("./run/tayga-2.conf", tayga2_pream, map_rules)
                Tayga.reload("./run/tayga-2.pid")
        elif 'announced' in line:
            tokens = line.split(' ')
            map_rules[tokens[5]] = tokens[6]
        elif 'withdrawn' in line:
            tokens = line.split(' ')
            if map_rules[tokens[5]] == tokens[6]:
                del map_rules[tokens[5]]
except IOError as e:
    sys.stderr.write("ioerr " + e + '\n')
    sys.stderr.flush()
    pass
except Exception as e:
    sys.stderr.write("err " + e + '\n')
    sys.stderr.flush()
    raise e
