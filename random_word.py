import random
from nltk.corpus import words
from nltk.corpus import brown

#english_words = set(words.words())
#print(brown.categories())

random_banned = {'the', 'on', 'as', 'such', 'then', 'than', 'of',
    'and', 'but', 'or', 'nor', 'for', 'yet', 'so',
    'in', 'out', 'up', 'down', 'off', 'over', 'under',
    'a', 'an', 'this', 'that', 'these', 'those',
    'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'do', 'does', 'did',
    'will', 'would', 'shall', 'should', 'can', 'could', 'may', 'might', 'must',
    'at', 'by', 'with', 'from', 'into', 'to', 'for',
    'he', 'she', 'it', 'they', 'them', 'his', 'her', 'its', 'their',
    'there', 'where', 'when', 'why', 'how'}

# Prepositions
prepositions = {
    'about', 'above', 'across', 'after', 'against', 'along', 'amid', 'among',
    'around', 'before', 'behind', 'below', 'beneath', 'beside', 'between',
    'beyond', 'during', 'except', 'inside', 'outside', 'through', 'throughout',
    'toward', 'underneath', 'until', 'upon', 'within', 'without'
}

# Conjunctions
conjunctions = {
    'although', 'because', 'since', 'unless', 'whereas', 'while'
}

# Articles
articles = {'a', 'an', 'the'}

# Pronouns
pronouns = {
    'I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us',
    'them', 'my', 'your', 'his', 'our', 'your', 'their', 'mine', 'yours',
    'hers', 'ours', 'theirs'
}

# Auxiliary Verbs
auxiliary_verbs = {
    'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
    'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should', 'can',
    'could', 'may', 'might', 'must'
}

# Other Common Non-Descriptive Words
other_common = {
    'here', 'there', 'where', 'when', 'why', 'how', 'what', 'which', 'who',
    'whom', 'whose', 'this', 'that', 'these', 'those', 'not'
}

excluded_words = prepositions | conjunctions | articles | pronouns | auxiliary_verbs | other_common | random_banned


def get_word(categories, min_len, max_len):
    cat = random.choice(categories)
    word = random.choice(brown.words(categories=cat)).lower()

    #filter na semi-bullshit slova
    while (not word.isalpha()) or (len(word) < min_len) or (len(word) > max_len) or (word in excluded_words):
        word = random.choice(brown.words(categories=cat)).lower()

    return word.lower()
