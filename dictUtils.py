import pickle

dict_pickle_path = 'word_dict'

def serialize_word_dict(): 
    with open('words_alpha.txt') as word_dict:
        words = [word.strip('\n') for word in word_dict.readlines()]
        with open(dict_pickle_path,'wb') as outfile:
            pickle.dump(words,outfile)

def deserialize_word_dict(): 
    with open(dict_pickle_path,'rb') as infile:
        word_dict = pickle.load(infile)
    return word_dict

 
