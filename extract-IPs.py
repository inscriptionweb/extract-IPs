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
    #ipl = [(IP(ip).int(), ip) for ip in ips]
    #ipl.sort()
    #return [ip[1] for ip in ipl]

    #for i in range(len(ips)):
    #    ips[i] = "%3s.%3s.%3s.%3s" % tuple(ips[i].split("."))
    #    ips.sort()
    #    for i in range(len(ips)):
    #        ips[i] = ips[i].replace(" ", "")
    #return ips

    return sorted(ips, key=lambda ip:IP(ip).int())

def main(args):
    ips = []
    with open(args.f, 'r') as f:
        for line in f.readlines():
            ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line)
            if len(ip) > 0:
                for i in ip:
                    ips.append(i)
    ips = list(set(ips))
    ips = sort_ips(ips)
    for ip in ips:
        print ip

main(parse_args())
