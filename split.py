from spellchecker import SpellChecker

spell = SpellChecker()
import re
from collections import Counter

def viterbi_segment(text):
    text=re.sub('[^A-z]','',text)
    probs, lasts = [1.0], [0]
    for i in range(1, len(text) + 1):
        prob_k, k = max((probs[j] * word_prob(text[j:i]), j)
                        for j in range(max(0, i - max_word_length), i))
        probs.append(prob_k)
        lasts.append(k)
    words = []
    i = len(text)
    while 0 < i:
        words.append(text[lasts[i]:i])
        i = lasts[i]
    words.reverse()
    return words, probs[-1]

def word_prob(word): return dictionary[word] / total
def words(text): return re.findall('[a-z]+', text.lower()) 
dictionary = Counter(words(open('big.txt').read()))
count=[]
for i in dictionary.keys():
    if len(i)<=2:
        count.append(i)
for i in sorted(count):
    del dictionary[i]
max_word_length = max(map(len, dictionary))
total = float(sum(dictionary.values()))
