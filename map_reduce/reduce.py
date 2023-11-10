#!/usr/bin/env python3

import sys

last_key = None
running_total = 0
running_count = 0

for input_line in sys.stdin:
    input_line = input_line.strip()
    this_key, value = input_line.split("\t")
    value = int(value)

    if last_key == this_key:
        running_total += value
        running_count += 1
    else:
        if last_key:
            print( "%s\t%d" % (last_key, running_total / running_count) )
        running_total = value
        last_key = this_key

if last_key == this_key:
    print( "%s\t%d" % (last_key, running_total / running_count) )