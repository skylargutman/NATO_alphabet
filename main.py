# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}


def get_list():
    target_word = input("please enter the word to be spelled: ").upper()
    try:
        target_word_list = [nato_dict[letter] for letter in target_word]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        target_word_list = get_list()
    return target_word_list
print(get_list())


