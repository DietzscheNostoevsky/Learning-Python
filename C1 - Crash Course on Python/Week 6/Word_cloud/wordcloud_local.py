import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

####################################################################

import os
file = "/Users/saurabhkumarsingh/Documents/GitHub/ Google IT Automation with Python Professional Certificate/C1 - Crash Course on Python/Week 6/Word_cloud/testfile.txt"
f = open(file)
file_contents = f.read()

####################################################################


def calculate_frequencies(file_contents):

    text = file_contents

    def RemovePunchuations(text):
        # removes all the special characters supplied in
        # the variable punchuations from the supplied
        # text string
        newtext = text

        punctuations = '''!()-[]{};:'"\,<>./?@—#$%^&*_~'''

        for punchuation in punctuations:
            newtext = newtext.replace(punchuation, " ")

        return newtext

    def TokenfromText(text):
        # take a string as input
        # return a list of words in the text

        newtext = text
        newnewtext = newtext.split()
        return_list = []
        for word in newnewtext:
            newword = word.lower()
            return_list.append(newword)
        return return_list

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
                               "can", "will", "just", 'a', 'about', 'above',
                               'after', 'again', 'against', 'all', 'am',
                               'an', 'and', 'any', 'are', "aren't", 'as',
                               'at', 'be', 'because', 'been', 'before', 'didst',
                               'us', 'one',
                               'being', 'below', 'between', 'both',
                               'but', 'by', "can't", 'cannot', 'could',
                               "couldn't", 'did', "didn't", 'do', 'does',
                               "doesn't", 'doing', "don't", 'down', 'during',
                               'each', 'few', 'for', 'from', 'further', 'had',
                               "hadn't", 'has', "hasn't", 'have', "haven't", 'having',
                               'he', "he'd", "he'll", "he's", 'her', 'here', "here's",
                               'hers', 'herself', 'him', 'himself', 'his', 'how', "how's",
                               'i', "i'd", "i'll", "i'm", "i've", 'if', 'in',
                               'into', 'is',
                               "isn't", 'it', "it's", 'its', 'itself', "let's",
                               'me', 'more',
                               'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of',
                               'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our',
                               'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't",
                               'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so',
                               'some', 'such', 'than', 'that', "that's", 'the',
                               'their', 'theirs',
                               'them', 'themselves', 'then', 'there', "there's", 'these', 'they',
                               "they'd", "they'll", "they're", "they've", 'this',
                               'those', 'through',
                               'to', 'too', 'under', 'until', 'up', 'very', 'was',
                               "wasn't", 'we',
                               "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's",
                               'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's",
                               'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you',
                               "you'd", "you'll", "you're", "you've", 'your', "thou",
                               "thee", "thy", "but", "man", 'yours', 'yourself', 'yourselves']

        for uword in uninteresting_words:
            if uword in frequency:
                del frequency[uword]

        return frequency

    text1 = RemovePunchuations(text)
    listofwords = TokenfromText(text1)
    frequencyofwords = FrequencyWithUninterestingRemoved(listofwords)

    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencyofwords)

    return cloud.to_array()

##############################################################################

# Display your wordcloud image


myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
