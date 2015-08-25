#!/usr/bin/env python2

import re
import argparse
from IPy import IP

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="Filename to extract IPs from")
    return parser.parse_args()

def sort_ips(ips):
    """Sort an IP address list."""
    ipl = [(IP(ip).int(), ip) for ip in ips]
    ipl.sort()
    return [ip[1] for ip in ipl]

def main(args):
    ips = []
    with open(args.f, 'r') as f:
        for line in f.readlines():
            ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line)
            if len(ip) > 0:
                for i in ip:
                    ips.append(i)
    ips = sort_ips(ips)
    ips = list(set(ips))
    for ip in ips:
        print ip

main(parse_args())
