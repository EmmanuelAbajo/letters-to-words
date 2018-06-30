"""
This Program has three modes: Random, Single-Selection and Selection mode. Only the first letter is specified
in the single mode while the first and last letter can be specified in the selection mode. Due to the computational
efficiency of the system, it is advised to genarate a max of 6 words
Name: Kehinde-Abajo, Emmanuel
Handle: @Psyche
"""
import sys,time,traceback,itertools

def word_list_foo(letter): #Creates a word list from letters passed
    letter_formed = ''.join(letter)
    foo = itertools.permutations(letter_formed)
    element=[]
    for items in foo:
        word = ''.join(items)
        element.append(word)
    word_list=list(set(element)) #handles repititions in the list
    return word_list

def dict_foo(): #Creates a dictionary list
    word_dict_list = []
    with open('words_alpha.txt') as dict_file:
        for word in dict_file.readlines():
            word_dict = word.rstrip('\n')
            word_dict_list.append(word_dict)
    return word_dict_list

def word_check(word_list,word_dict_list):# Checks out for meaningful words
    element = [i for i in word_list if i in word_dict_list]
    for i in element:
        print('Word generated:',i)
    else:
        if len(element) < 1:
            print("No word found")
            sys.exit(0)


def random_gen(letter):
    print('-----------RANDOM MODE WORD GENERATOR------------')
    time.sleep(2)
    print('Generating %s letter words'%(str(len(letter))))
    time.sleep(2)
    print('loading...')
    word_list = word_list_foo(letter)
    word_dict_list = dict_foo()
    word_check(word_list,word_dict_list)

def single_selection_gen(letter):
    print('-----------SINGLE SELECTION MODE WORD GENERATOR------------')
    time.sleep(2)
    first_letter = input("Enter first letter: ")
    print('Generating %s letter words'%(str(len(letter))))
    time.sleep(2)
    print('loading...')
    if first_letter in letter:
        letter_1 = letter.pop(letter.index(first_letter))
    else:
        print("Sorry, letter not found in list of letters parsed")
        sys.exit(0)
    word_list = word_list_foo(letter)
    word_dict_list = dict_foo()
    word_formed = []
    for i in word_list: # Adds the first letter to every word
        foo = first_letter + i
        word_formed.append(foo)
    word_check(word_formed,word_dict_list)

def selection_gen(letter):
    print('-----------SELECTION MODE WORD GENERATOR------------')
    time.sleep(2)
    first_letter = input("Enter first letter: ")
    last_letter = input("Enter last letter: ")
    print('Generating %s letter words'%(str(len(letter))))
    time.sleep(2)
    print('loading...')
    if first_letter in letter and last_letter in letter:
        letter_1 = letter.pop(letter.index(first_letter))
        letter_2 = letter.pop(letter.index(last_letter))
    else:
        print("Letter specified not in letters passed")
        sys.exit(0)
    word_list = word_list_foo(letter)
    word_dict_list = dict_foo()
    word_formed = []
    for i in word_list: # Adds the first and last letter to every word
        foo = first_letter + i + last_letter
        word_formed.append(foo)
    word_check(word_formed,word_dict_list)

if __name__=="__main__":
# creates a list of the letters from the command line
    if len(sys.argv) <= 2:
        print('Sorry,Enter at least two letters to generate word')
        time.sleep(3)
        print('Logging out...')
        time.sleep(2)
        exit(0)
    else:
        del sys.argv[0]
        letters = sys.argv[0:]

    # Mode selection
    try:
        mode = int(input("Enter '0' for random mode and '1' for single-selection mode and '2' for selection mode: "))
        if mode == 0:
            random_gen(letters)
        elif mode == 1:
            single_selection_gen(letters)
        elif mode == 2:
            selection_gen(letters)
        else:
            print('Sorry, wrong Input')
    except Exception as err:
        print(str(err))
        with open('C:\\Python_Practice\\Apps\\Errorfile.txt','w') as errorfile:
                errorfile.write(traceback.format_exc())
