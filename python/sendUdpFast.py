#!/usr/bin/python

import socket, sys, time
from struct import pack
import numpy as np


def main():

    port = 5432  # arbitrary port
    ip = "127.0.0.1"

    freq = 1
    samples = 2000
    period = 1 / freq
    bit_depth = 10

    t = np.arange(samples) * 1000 / samples

    x = np.arange(samples)
    values = np.sin(2 * np.pi * freq * x / samples)
    values = ((2**bit_depth/2-1)*(values+1)).astype(int)

    args = ["4000I"]
    for i in t:
        args.append(i)
    for i in values:
        args.append(i)
    packed = pack(*args) 

    print("UDP target IP: {}".format(ip))
    print("UDP target port: {}".format(port))
    print(t)
    print(values)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    time.sleep(1)

    while True:
        sock.sendto(packed, (ip, port))
        #time.sleep(1)


if __name__ == "__main__":
    main()
