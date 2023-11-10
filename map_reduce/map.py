#!/usr/bin/env python3

import re
import sys

for line in sys.stdin:
    line = line.strip()
    keys = line.split(",")
    qual = keys[2]
    size = keys[9]
    pr = keys[11]
    if (pr == "Male"):
        print( "%s\t%s" % (qual, size) )
    # for key in keys:
    #     print(key)