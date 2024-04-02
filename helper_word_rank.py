import nltk
from nltk.corpus import brown

import random_word

# Ensure you have the necessary NLTK data downloaded
nltk.download('brown')

# Example: A simplistic frequency-based approach using the Brown corpus
# word_freqs = nltk.FreqDist(w.lower() for w in brown.words())
#
# lst=[]
# for i in range(100):
#     print(i)
#     lst.append(random_word.get_word(['lore','news'],3,10))
#
# ranked_words = sorted(lst, key=lambda w: word_freqs[w], reverse=True)
#
# print("Words ranked from easiest to hardest based on frequency in the Brown corpus:")
# for word in ranked_words:
#     print(word, "-> Frequency:", word_freqs[word])


print(brown.categories())