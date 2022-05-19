#!/usr/bin/python

import socket, sys, time
from struct import pack
import numpy as np


def send(ip, port, sock, values, t):

    for i in range(200):
        args = ["2I"]
        args.append(t[i])
        args.append(values[i])
        print(args)
        sock.sendto(pack(*args), (ip, port))
        time.sleep(0.005)


def main():

    port = 5432  # arbitrary port
    ip = "127.0.0.1"

    freq = 1
    samples = 200
    period = 1 / freq
    bit_depth = 10

    t = np.arange(samples) * 1000 / samples

    x = np.arange(samples)
    values = np.sin(2 * np.pi * freq * x / samples)

    print("UDP target IP: {}".format(ip))
    print("UDP target port: {}".format(port))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    time.sleep(period)

    while True:
	noise = np.random.normal(scale=0.01, size=values.size)
	noisy = (values + noise)
        noisy /= np.max(np.abs(noisy), axis=0) 
        noisy = ((2**bit_depth/2-1)*(noisy+1)).astype(int)
        send(ip, port, sock, noisy, t)
        t = t + 1000
        # time.sleep(period)


if __name__ == "__main__":
    main()
