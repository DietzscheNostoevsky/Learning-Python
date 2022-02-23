import urllib.request
import urllib.parse
import urllib.error

hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# for line in hand:
#    print(line.decode().strip())

# when above code is uncomemnted, file handle closes after the for loop and counts return blank dict
# it happens because hand is just a file handle, not the actual file itself.
# so after looping the first time, the pointer has nothing to point at for the next for loop.


counts = dict()

for line in hand:
    words = line.decode().strip()
    for word in words.split():
        counts[word] = counts.get(word, 0) + 1

print(counts)
