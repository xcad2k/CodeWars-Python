#####################################################################################
#                                                                                   #
#   NAME:     Typoglycemia Generator                                                #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/55953e906851cf2441000032/train/python   #
#                                                                                   #
#####################################################################################
import re


def scramble_word(word: str) -> str:
    return word[0] + ''.join(sorted(word[1:-1])) + word[-1]


def scramble_words(words):
    regex = re.compile(r'(?:\s|^)[a-zA-Z\'-.,]{2,}(?:\s|$)', re.IGNORECASE)
    return re.sub(regex, lambda x: scramble_word(x.group()), words)


print(scramble_words('professionals'))
