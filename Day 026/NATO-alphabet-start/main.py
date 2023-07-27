import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def word_to_nato(word_dict):
    word = input('Enter a word: ')
    try:
        # letter_list = [letter.upper() for letter in word if letter.isalpha()]
        # word_list = [word_dict[letter] for letter in letter_list]
        word_list = [f'{letter.upper()} as in {word_dict[letter.upper()]}' for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        word_to_nato(word_dict)
    else:
        for nato in word_list:
            print(nato)


word_to_nato(nato_dict)
