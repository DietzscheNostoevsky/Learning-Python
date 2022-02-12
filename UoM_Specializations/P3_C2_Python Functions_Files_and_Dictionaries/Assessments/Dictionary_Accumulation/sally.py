sally = "sally sells sea shells by the sea shore"
freq = {}
for char in sally:
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1
sorted_freq = dict((sorted(freq.items(), key=lambda kv: kv[-1], reverse=True)))
best_char = list(sorted_freq.keys())[0]
print(sorted_freq)
