from tayga import Tayga

with open("./tayga-r1.pream.conf") as fd:
    tayga1_pream = "".join(fd.readlines())

Tayga.gen_conf(
    "./run/tayga-1.conf",
    tayga1_pream,
    {"10.0.1.0/24": "2001::/120", "10.0.2.0/24": "2002::/120"})

Tayga.reload("./run/tayga-1.pid")
