punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    input_string = word
    for w in punctuation_chars:
        if w in input_string:
            input_string = input_string.replace(w, "")

    return input_string


strip_punctuation("#Amazing")
