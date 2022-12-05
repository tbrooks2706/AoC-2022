import general_functions

moves_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_5_moves.txt")
#print(moves_list)

init_stack_table = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_5_table.txt")
#print(init_stack_table)

#create dictionary of the stacks, with stack numbers as keys and lists of the letters as values
def clean_stacks_list(list):
    #remove the last item which is the stack numbers
    list.pop()
    stack_table_clean = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    stack_table_strings = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    #the letters are at 1, 5, 9, 13, 17, 21, 25, 29, 33
    index_keys = {1: 1, 5: 2, 9: 3, 13: 4, 17: 5, 21: 6, 25: 7, 29: 8, 33: 9}
    #add each set of letters in the stack to the strings dictionary
    for string in list:
        string_index = 0
        for char in string:
            stack = 0
            for key, value in index_keys.items():
                if key == string_index:
                    stack = value
            string_index += 1
            for num in range(1, 10):
                if stack == num:
                    stack_table_strings[stack] += char
    #strip out whitespace from strings and add each letter to dictionary of lists
    for key, value in stack_table_strings.items():
        value = value.strip()
        for char in value:
            stack_table_clean[key].append(char)
    return stack_table_clean

stacks_dict = clean_stacks_list(init_stack_table)
print(stacks_dict)

#execute moves in order
#within a move, crates are moved one at a time, from top first
#after all the moves, which letter is on top of each stack - as a 9 letter code