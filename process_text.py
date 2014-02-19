from collections import defaultdict

frequency_count = defaultdict(int)
line_numbers = defaultdict(list)
length_dict = defaultdict(set)

# get a list of English stopwords 
stopwords = dict()
with open('englishST.txt','r') as g:
    for line in g:
        stopwords[line.strip()] = 1

with open('blue.txt','r') as f:
    for i, line in enumerate(f):
        words = line.lower().split()
        for word in words:
            # eliminate stopwords
            if word in stopwords:
                continue # continue means to stop processing this and 
                         # go to the next word in the for-loop
            frequency_count[word] += 1
            line_numbers[word].append(i)
            length_dict[len(word)].add(word)

# let's do some inspection of the resulting defaultdicts

# print the top 20 most frequent words

# if you just do this, you'll just get 20 random words
print frequency_count.items()[:20]

# how to sort by frequency:
import operator
# frequency_count.items() is a list of key-value pairs.
# operator.itemgetter(1) says to take the second item, i.e. the value
# and use that as the key to sort with
# you have to do reverse=True otherwise you get the least frequent words.
most_frequent_words = sorted(frequency_count.items(), key=operator.itemgetter(1), reverse=True)[:20]
print most_frequent_words

# another way to to do the sorting, with a lambda:
most_frequent_words = sorted(frequency_count.items(), key=lambda x: x[1], reverse=True)[:20]

# aside: if you do this without filtering the stopwords, you'll see that the
# most frequent words are things like "the" and "a", which aren't in the Wordle.
# This is because Wordle by default filters out "stop words", which are
# non-content words that are really frequent in English but don't contribute to
# differentiating one text from another. That's why I've filtered by stopword
# above. There are more things you could do, like split off punctuation and
# clitics like "n't", to do a more principled word count.

# print the line numbers of the top 20 most frequent words
for word in most_frequent_words:
    print word, "\t", line_numbers[word]
    
# print the number of types of each length
for length, words in sorted(length_dict.items()):
    print length, "\t", len(words)
