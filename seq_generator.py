#!/usr/bin/python3
# Copyright (c) 2018 Jeff Lund
# Takes in four arguments from CL
#   Lower Bound
#   Upper Bound
#   Number of elements in list
#   File to write to

from random import *
from sys import argv

fout = open(argv[4], 'w')
for i in range(0, int(argv[3])):
    x = randint(int(argv[1]), int(argv[2]))
    print(x, file=fout)
fout.close()
