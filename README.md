# Preparation

- C compile environment
- Python
- tmux

```bash
git clone https://github.com/wenxin-wang/bgp-eam-tayga
cd bgp-eam-tayga
git clone https://github.com/wenxin-wang/exabgp
git clone https://salsa.debian.org/debian/tayga.git
cd tayga
git apply debian/patches/*.patch
git apply ../tayga-patches/*.patch
./configure
make
```

# Test

```bash
cd 1-IPv4-IPv6
sudo ./1-pre
# prepare packet capture
./2-test
# run ping/iperf
sudo ./3-post

cd 2-IPv4-IPv6-IPv4
sudo ./1-pre
# prepare packet capture
./2-test
# run ping/iperf
sudo ./3-post
```
