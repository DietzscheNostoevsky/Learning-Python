
import re
print(re.search(r"py.*o", "pythagoras"))
print(re.search(r"py.*n", "python programming"))  # greedy behaviour
print(re.search(r"py[a-z]*n", "python programming"))
print(re.search(r"py[a-z]*n", "pyn"))  # o times also a possibility
print(re.search(r"o+l+", "goldfish"))  # shortest possible matching string
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))


def repeating_letter_a(text):
    result = re.search(r"[aA].*[aA]", text)
    return result != None


print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True
print(repeating_letter_a("paanmfssfl"))  # ?

# means p before ? is optional
print(re.search(r"p?each", "To each thier own"))

print(re.search(r"p?each", "To  thier own peaches"))
