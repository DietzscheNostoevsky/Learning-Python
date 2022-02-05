#!/usr/bin/env python3

import re
result = re.search(r"^(\w*), (\w*)$", "Singh, Saurabh")


def rearrange_name(name):
    result = re.search(r"^([\w. ]*), ([\w. ]*)$", name)
    if result == None:
        return None
    return "{} {}".format(result[2], result[1])


name = rearrange_name("Kennedy, John F.")
print(name)
