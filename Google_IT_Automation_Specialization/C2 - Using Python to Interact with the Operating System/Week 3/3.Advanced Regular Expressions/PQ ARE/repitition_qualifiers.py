import re


def long_words(text):
    pattern = r"\w{7,}"
    result = re.findall(pattern, text)
    return result


print(long_words("I like to drink coffee in the morning."))  # ['morning']
# ['chocolate', 'afternoon']
print(long_words("I also have a taste for hot chocolate in the afternoon."))
print(long_words("I never drink tea late at night."))  # []


print(re.search(r"\w{5}", "Bohemian Raphsody"))
print(re.search(r"\w{5}", "Queen Bohemian Raphsody"))
print(re.findall(r"\w{5}", "Queen Bohemian Raphsody"))
print(re.findall(r"\b\w{5}\b", "Queen Bohemian Raphsody"))
