import sys,time,traceback,itertools

# Creates words from letters passed
def gen_word_list(letter): 
    foo = itertools.permutations(''.join(letter))
    element=[''.join(item) for item in foo]
    return set(element)

# Checks if words exist in dictionary
def get_word_from_dict(word_list,word_dict_list):
    wordFound = [i for i in word_list if i in word_dict_list]
    return wordFound
