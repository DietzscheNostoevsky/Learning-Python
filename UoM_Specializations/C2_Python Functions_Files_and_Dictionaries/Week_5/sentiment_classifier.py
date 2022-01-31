punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    input_string = word
    for w in punctuation_chars:
        if w in input_string:
            input_string = input_string.replace(w, "")

    return input_string


positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(sentence):
    new = strip_punctuation(sentence)
    wordlist = new.split()
    count = 0
    for w in wordlist:

        if w.lower() in positive_words:
            count += 1
    return count


testing = "what a truly wonderful day it is today! #incredible"
print(get_pos(testing))
