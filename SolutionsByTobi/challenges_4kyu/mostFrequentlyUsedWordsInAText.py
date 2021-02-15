########################################################################
#                                                                      #
#   NAME:     Most frequently used words in a text                     #
#   RANK:     4kyu                                                     #
#   URL:      https://www.codewars.com/kata/51e056fe544cf36c410000fb   #
#                                                                      #
########################################################################
import re


def top_3_words(text):
    text = text.lower()
    words = [word for word in re.findall(r"[a-z']+", text) if re.search(r"[a-z]", word) is not None]
    return sorted(set(words), key=lambda word: words.count(word), reverse=True)[:3]
