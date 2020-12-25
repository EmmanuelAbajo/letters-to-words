import pickle

def serialize_word_dict(): 
    with open('words_alpha.txt') as word_dict:
        words = [word.strip('\n') for word in word_dict.readlines()]
        with open('app/api/word_dict','wb') as outfile:
            pickle.dump(words,outfile)

def deserialize_word_dict(): 
    with open('app/api/word_dict','rb') as infile:
        word_dict = pickle.load(infile)
    return word_dict

 
