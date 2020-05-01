# Make a function that encrypts a given input with these steps:
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# a => 0
# e => 1
# o => 2
# u => 3
# "1lpp0"
# Step 3: Add "aca" to the end of the word: "1lpp0aca"
# Output: "1lpp0aca"


ef encr(rec):
    vokali = {'a': 0, 'e': 1, 'o': 2, 'i': 3, 'u': 4}
    novo = ''

    for i in rec:
        if i in vokali:
            i = str(vokali[i])
            novo += i
        else:
            novo += i
    print(novo)

encr('jabuke')

#############


def encrypt(word):
    return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'
