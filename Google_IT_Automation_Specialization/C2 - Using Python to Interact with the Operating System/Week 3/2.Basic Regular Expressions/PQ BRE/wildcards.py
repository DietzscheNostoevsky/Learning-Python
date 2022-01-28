import re

print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "this is a highway"))
print(re.search(r"[a-z]way", "what a way to go"))
print(re.search(r"[a-zA-Z0-9]loud", "09loud"))


def check_punctuation(text):
    result = re.search(r"[,.:;?!]", text)
    return result != None  # cool code


print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?"))  # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False

print(re.search(r"cat|dog", "I have cats and dogs"))

print(re.findall(r"cat|dog", "I have cats and dogs"))
