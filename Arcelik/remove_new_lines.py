#!/usr/bin/python

from __future__ import print_function
import sys

filename = sys.argv[1] 
output_filename = sys.argv[2] 
one_string = ""

with open(filename, "r") as fh:
	for line in fh:
		line = line.rstrip("\n")
		one_string += line

with open(output_filename, "w+") as fw:
	fw.write(one_string)