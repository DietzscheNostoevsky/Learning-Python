# %%
text = """Alexey Fyodorovitch Karamazov was the third son of Fyodor Pavlovitch
Karamazov, a land owner well known in our district in his own day, and
still remembered among us owing to his gloomy and tragic death, which
happened thirteen years ago, and which I shall describe in its proper
place. For the present I will only say that this “landowner”—for so we
used to call him, although he hardly spent a day of his life on his own
estate—was a strange type, yet one pretty frequently to be met with, a
type abject and vicious and at the same time senseless. But he was one
of those senseless persons who are very well capable of looking after
their worldly affairs, and, apparently, after nothing else. Fyodor
Pavlovitch, for instance, began with next to nothing
his estate was of
the smallest
he ran to dine at other men’s tables, and fastened on
them as a toady, yet at his death it appeared that he had a hundred
thousand roubles in hard cash. At the same time, he was all his life
one of the most senseless, fantastical fellows in the whole district. I
repeat, it was not stupidity—the majority of these fantastical fellows
are shrewd and intelligent enough—but just senselessness, and a
peculiar national form of it."""

newtext = text
newnewtext = newtext.split()

return_list = newnewtext


frequency = {}

for word in return_list:
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


# %%
