class Solution:
    def romanToInt(self, s: str) -> int:

        # defining variable values
        roman_dict = {

            'I': 1,
            # 'II': 2,
            # 'III': 3,
            # 'IV': 4,
            'V': 5,
            # 'IX': 9,
            'X': 10,
            # 'XL': 40,
            'L': 50,
            # 'XC': 90,
            'C': 100,
            # 'CD': 400,
            'D': 500,
            # 'CM': 900,
            'M': 1000,

        }

        # Problem is simpler to solve by working the string from back to front and using a map.
        # Test = "MCMXCIV"

        s = s.upper()
        s = s[::-1]
        for i in s:
            
