import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def word_to_nato(word_dict):
    word = input('Enter a word: ')
    letter_list = [letter.upper() for letter in word if letter.isalpha()]
    word_list = [word_dict[letter] for letter in letter_list]
    print(word_list)


word_to_nato(nato_dict)
