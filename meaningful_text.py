import random
import nltk.corpus
from nltk.corpus import gutenberg

#polorozjebane
book = random.choice(nltk.corpus.gutenberg.fileids())
words = []
for word in gutenberg.words(book):
    if word.isalpha():
        words.append(word)

def next_word(i):
    word = words[i]
    return word


print(next_word(i=0))