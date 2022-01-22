#! /usr/bin/env python3

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New File Created\n")
else:
    print("ERROR , file {} already exits!".format(filename))
    sys.exit(1)
