
import pandas


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#reading file using pandas and saving to 'data'
data = pandas.read_csv('nato_phonetic_alphabet.csv')



#TODO 1. Create a dictionary in this format:
# Using dictionary comprehension to create a new dictionary where the letter is the key and
# the code is the value from 'data'
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Getting input from user
word_from_user = input("Enter a word: ").upper()

# using list comprehension to loop through every letter in users word and getting the value from the above dictionary
letter_list = [phonetic_dict[letter] for letter in word_from_user]
print(letter_list)

















