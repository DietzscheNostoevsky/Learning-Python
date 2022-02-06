#!/usr/bin/env python3

import unittest
from uservalidation import validate_user


class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        user = "validuser"
        length = 3
        expect = True
        self.assertEqual(validate_user(user, length), expect)

    def test_too_short(self):
        user = "inv"
        length = 5
        expect = False
        self.assertEqual(validate_user(user, length), expect)

    def test_invalid_characters(self):
        user = "invali_duser"
        length = 5
        expect = False
        self.assertEqual(validate_user(user, length), expect)

    def test_invalid_len(self):
        user = "user"
        length = -1
        expect = True
        self.assertRaises(ValueError, validate_user, user, length)


unittest.main()
