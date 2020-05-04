# Zadatak 36: Value of a sentence
# Each letter in a sentence is worth its position in the alphabet (i.e. a = 1, b = 2, c = 3, etc...).
# However, if a word is all in UPPERCASE, the value of that word is doubled.
# Create a function which returns the value of a sentence.

# get_sentence_value("abc ABC Abc") ➞ 24
# a = 1, b = 2, c = 3

# abc = 1 + 2 + 3 = 6
# ABC = (1+2+3) * 2 = 12 (ALL letters are in uppercase)
# Abc = 1 + 2 + 3 = 6 (NOT ALL letters are in uppercase)

# 6 + 12 + 6 = 24

# Examples
# get_sentence_value("HELLO world") ➞ 176
# get_sentence_value("Edabit is LEGENDARY") ➞ 251
# get_sentence_value("Her seaside sea-shelling business is really booming!") ➞ 488

# Notes
#     Ignore spaces and punctuation.
#     Remember that the value of a word isn't doubled unless all the letters in it are uppercase.


def get_sentence_value(txt):
    recnik = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
              'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    zbir = 0
    reci = txt.split()
    for i in reci:
        if i.isupper():
            for j in i:
                if j.lower() in recnik:
                    zbir += recnik[j.lower()] * 2

        elif i.isalpha():
            for j in i:
                if j.lower() in recnik:
                    zbir += recnik[j.lower()]
    return zbir


print(get_sentence_value('Her seaside sea-shelling business is really booming!'))
