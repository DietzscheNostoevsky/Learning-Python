from pyparsing import line


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

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_pos(sentence):
    new = strip_punctuation(sentence)
    wordlist = new.split()
    count = 0
    for w in wordlist:

        if w.lower() in positive_words:
            count += 1
    return count


def get_neg(sentence):
    new = strip_punctuation(sentence)
    wordlist = new.split()
    count = 0
    for w in wordlist:

        if w.lower() in negative_words:
            count += 1
    return count


twitter = open("project_twitter_data.csv", 'r')
outfile = open("resulting_data.csv", "w")

firstline = 0

for lines in twitter:
    if firstline == 0:
        outfile.write(
            "Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score\n")
        firstline = 1
        continue

    line = lines.strip().split(",")
    tweet = line[0]
    pos_score = get_pos(tweet)
    neg_score = get_neg(tweet)
    net_score = pos_score - neg_score
    retweets = line[1]
    replies = line[2]
    outfile.write("{},{},{},{},{}\n".format(
        retweets, replies, pos_score, neg_score, net_score))


outfile.close()
twitter.close()
