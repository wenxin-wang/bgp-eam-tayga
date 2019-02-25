#!/usr/bin/env python

import sys
import time

from tayga import Tayga


with open(Tayga.exapath("./tayga-r2.pream.conf")) as fd:
    tayga2_pream = "".join(fd.readlines())


messages = [
    'announce ipv6-eam 10.0.1.0/24 2001::/120\n'
    'announce ipv6-eam 10.0.2.0/24 2002::/120\n'
    'announce eor ipv6 eam',
    'withdraw ipv6-eam 10.0.1.0/24 2001::/120\n'
    'withdraw ipv6-eam 10.0.2.0/24 2002::/120\n'
    'announce ipv6-eam 10.0.1.0/24 2011::/120\n'
    'announce ipv6-eam 10.0.2.0/24 2022::/120\n'
    'announce eor ipv6 eam',
]

map_rules = {}

time.sleep(2)  # wait for the EOR

while messages:
    message = messages.pop(0)
    # line = sys.stdin.readline().strip()
    # sys.stderr.write('-- ' + line + '\n')
    # sys.stderr.flush()
    for line in message.split('\n'):
        if 'ipv6-eam' in line:
            tokens = line.split(' ')
            if tokens[0] == 'announce':
                map_rules[tokens[2]] = tokens[3]
            elif tokens[0] == 'withdraw' and map_rules[tokens[2]] == tokens[3]:
                del map_rules[tokens[2]]
    Tayga.gen_conf("./run/tayga-2.conf", tayga2_pream, map_rules)
    Tayga.reload("./run/tayga-2.pid")
    sys.stdout.write(message + '\n')
    sys.stdout.flush()
    time.sleep(5)

try:
    now = time.time()
    while True:
        line = sys.stdin.readline().strip()
        if 'shutdown' in line:
            break
except IOError:
    pass
