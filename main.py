# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

df_nato = pandas.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary

nato_dict = {row.letter: row.code for (index, row) in df_nato.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    generating = True
    while generating:
        word = input("Type a word and convert it to the NATO phonetic alphabet: \n").upper()
        if '  ' in word:
            break
        elif ' ' in word:
            word = word.replace(' ', '')
        else:
            pass
        try:
            result_nato_list = [nato_dict[letter] for letter in word]
        except KeyError:
            print('Sorry, please input only letters of the alphabet please')
            generate_phonetic()
        else:
            print(result_nato_list)


generate_phonetic()

