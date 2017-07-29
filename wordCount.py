import collections

testSentence = "ana are mere si are SI pere"


def word_count(sentence):
    words = collections.Counter(sentence.lower().split())
    return words


word_count(testSentence)
