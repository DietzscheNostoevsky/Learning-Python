
# %%
import os
f = open("/Users/saurabhkumarsingh/Documents/GitHub/Learning-Python/Course-1/Week 6/Word_cloud/testfile.txt")
text = f.read()


# %%
def RemovePunchuations(text):
    # removes all the special characters supplied in
    # the variable punchuations from the supplied
    # text string
    newtext = text

    punctuations = '''!()-[]{};:'"\,<>./?@—#$%^&*_~'''
    for punchuation in punctuations:
        newtext = newtext.replace(punchuation, " ")

    return newtext

# %%


def TokenfromText(text):
    # take a string as input
    # return a list of words in the text

    newtext = text
    newnewtext = newtext.split()
    return_list = newnewtext
    return return_list

# %%


def FrequencyWithUninterestingRemoved(listofwords):
    # takes the tokens from text
    # calculates frequency of words supplied in the list
    # removes uninteresting words based on corpus supplied
    # returns a dictionary of frequency

    frequency = {}
    supplied_list = listofwords

    for word in supplied_list:
        if word not in frequency:
            frequency[word] = 1
        frequency[word] += 1

    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of",
                           "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours",
                           "he", "she", "him", "his", "her", "hers",
                           "its", "they", "them",     "their", "what",
                           "which", "who", "whom", "this", "that",
                           "am", "are", "was", "were", "be", "been",
                           "being",     "have", "has", "had", "do",
                           "does", "did", "but", "at", "by", "with",
                           "from", "here", "when", "where", "how",
                           "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]
    for uword in uninteresting_words:
        if uword in frequency:
            del frequency[uword]
    return frequency


# %%
text1 = RemovePunchuations(text)

listofwords = TokenfromText(text1)

frequencyofwords = FrequencyWithUninterestingRemoved(listofwords)

print(frequencyofwords)

# %%
