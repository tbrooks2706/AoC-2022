import general_functions

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_3.txt")

cut_list = init_list[:10]
print(cut_list)

#tried OOP at first but couldn't get it to work - come back later
#class Rucksack:
#    def __init__(self, contents):
#        self.contents = contents
#        self.split = len(contents)
#        self.first_half = contents[0]

#rucksack1 = Rucksack("fsHtVbjtqstBghhwwPBw")
#print(rucksack1.first_half())

def find_common_character(string):
    split_point = int(len(string) / 2)
    first_half = string[:split_point]
    second_half = string[split_point:]
    for char in first_half:
        if char in second_half:
            common = char
    return common

def string_common_characters(list):
    common_string = ""
    for string in list:
        common_string += find_common_character(string)
    return common_string

def get_scores(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    full_alphabet = alphabet
    total_score = 0
    for letter in alphabet:
        full_alphabet += letter.upper()
    for char in string:
        score = full_alphabet.index(char) + 1
        total_score += score
    return total_score

common_characters = string_common_characters(init_list)
final_score = get_scores(common_characters)
#answer to part 1
print(final_score)


