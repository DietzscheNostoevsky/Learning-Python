#!/usr/bin/env python
# coding: utf-8

# # Final Project - Word Cloud

# For this project, you'll create a "word cloud" from a text by writing a script.  This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words.  A dictionary is the output of the `calculate_frequencies` function.  The `wordcloud` module will then generate the image from your dictionary.

# For the input text of your script, you will need to provide a file that contains text only.  For the text itself, you can copy and paste the contents of a website you like.  Or you can use a site like [Project Gutenberg](https://www.gutenberg.org/) to find books that are available online.  You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen. Save this as a .txt file somewhere on your computer.
# <br><br>
# Now you will need to upload your input file here so that your script will be able to process it.  To do the upload, you will need an uploader widget.  Run the following cell to perform all the installs and imports for your word cloud script and uploader widget.  It may take a minute for all of this to run and there will be a lot of output messages. But, be patient. Once you get the following final line of output, the code is done executing. Then you can continue on with the rest of the instructions for this notebook.
# <br><br>
# **Enabling notebook extension fileupload/extension...**
# <br>
# **- Validating: <font color =green>OK</font>**

# In[4]:


# Here are all the installs and imports you will need for your word cloud script and uploader widget

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


# Whew! That was a lot. All of the installs and imports for your word cloud script and uploader widget have been completed. 
# <br><br>
# **IMPORTANT!** If this was your first time running the above cell containing the installs and imports, you will need save this notebook now. Then under the File menu above,  select Close and Halt. When the notebook has completely shut down, reopen it. This is the only way the necessary changes will take affect.
# <br><br>
# To upload your text file, run the following cell that contains all the code for a custom uploader widget. Once you run this cell, a "Browse" button should appear below it. Click this button and navigate the window to locate your saved text file.

# In[44]:


# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


# The uploader widget saved the contents of your uploaded file into a string object named *file_contents* that your word cloud script can process. This was a lot of preliminary work, but you are now ready to begin your script. 

# Write a function in the cell below that iterates through the words in *file_contents*, removes punctuation, and counts the frequency of each word.  Oh, and be sure to make it ignore word case, words that do not contain all alphabets and boring words like "and" or "the".  Then use it in the `generate_from_frequencies` function to generate your very own word cloud!
# <br><br>
# **Hint:** Try storing the results of your iteration in a dictionary before passing them into wordcloud via the `generate_from_frequencies` function.

# In[45]:


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
        for word in newnewtext :
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
                           "can", "will", "just" , 'a', 'about', 'above', 
                               'after', 'again', 'against', 'all', 'am', 
                               'an', 'and', 'any', 'are', "aren't", 'as', 
                               'at', 'be', 'because', 'been', 'before', 'didst','us','one',
                               'being', 'below', 'between', 'both', 
                               'but', 'by', "can't", 'cannot', 'could', 
                               "couldn't", 'did', "didn't", 'do', 'does', 
                               "doesn't", 'doing', "don't", 'down', 'during',
                               'each', 'few', 'for', 'from', 'further', 'had', 
                               "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 
                               'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 
                               'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 
                               'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', 
                               "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 
                               'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of',
                               'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 
                               'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 
                               'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 
                               'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs',
                               'them', 'themselves', 'then', 'there', "there's", 'these', 'they', 
                               "they'd", "they'll", "they're", "they've", 'this', 'those', 'through',
                               'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we',
                               "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's",
                               'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 
                               'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you',
                               "you'd", "you'll", "you're", "you've", 'your',"thou","thee","thy","but","man", 'yours', 'yourself', 'yourselves']
        
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


# If you have done everything correctly, your word cloud image should appear after running the cell below.  Fingers crossed!

# In[46]:


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


# If your word cloud image did not appear, go back and rework your `calculate_frequencies` function until you get the desired output.  Definitely check that you passed your frequecy count dictionary into the `generate_from_frequencies` function of `wordcloud`. Once you have correctly displayed your word cloud image, you are all done with this project. Nice work!

# In[ ]:




