import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# print(alphabet_df)

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

# print(alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Give me a word:\n").upper()

try:
    word_list = [alphabet_dict[letter] for letter in user_word]
except KeyError:
    print("Sorry, please enter a valid word.")
else:
    print(word_list)
