#!/usr/bin/env python3

def validate_user(username, minlen):
    assert type(username) == str, 'username must be string'
    if minlen < 1:
        raise ValueError("minlen must be >1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

# use raise if we know what kinda condition we expect to happen during execeution
# use assertion when unexpected
