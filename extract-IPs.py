#!/usr/bin/env python2

import re
import argparse
from IPy import IP

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="Filename to extract IPs from")
    return parser.parse_args()


def main(args):
    ips = []
    with open(args.f, 'r') as f:
        for line in f.readlines():
            ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line)
            if len(ip) > 0:
                for i in ip:
                    ips.append(i)
    ips = list(set(ips))
    ips = sorted(ips, key=lambda ip:IP(ip).int())
    for ip in ips:
        print ip

main(parse_args())
