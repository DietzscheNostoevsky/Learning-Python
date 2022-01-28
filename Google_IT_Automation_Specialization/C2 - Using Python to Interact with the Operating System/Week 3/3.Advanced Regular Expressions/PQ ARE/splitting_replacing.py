import re

print(re.split(r"[.,!]", "This. Is a line ! Not a sentence !"))

print(re.split(r"([.,!])", "This. Is a line ! Not a sentence !"))

print(re.sub(r"[\w._+%-]+@[\w.-]+", "[REDACTED]",
      "This is my email heehaa@goo.gle.in"))


print(re.sub(r"^([\w.-]+), ([\w.-]+)$", r'\2 \1', "Singh, Saurabh"))
