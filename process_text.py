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
                continue
            frequency_count[word] += 1
            line_numbers[word].append(i)
            length_dict[len(word)].add(word)

# let's do some inspection

# print the top 20 most frequent words
import operator
most_frequent_words = sorted(frequency_count.items(), key=operator.itemgetter(1), reverse=True)[:20]
print most_frequent_words

# print the line numbers of the top 20 most frequent words
for word in most_frequent_words:
    print word, "\t", line_numbers[word]
    
# print the number of types of each length
for length, words in sorted(length_dict.items()):
    print length, "\t", len(words)
