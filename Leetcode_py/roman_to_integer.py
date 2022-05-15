class Solution:
    def romanToInt(self, s: str) -> int:

        # defining variable values
        roman_dict = {

            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,

        }

        s = s.upper()
