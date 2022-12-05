import general_functions

class Move:
    def __init__(self, string):
        self.first_list = string.split()
        self.final_list = []
        for num in [1, 3, 5]:
            self.final_list.append(int(self.first_list[num]))
        self.number_to_move = self.final_list[0]
        self.from_stack = self.final_list[1]
        self.to_stack = self.final_list[2]
#move1 = Move('move 15 from 69 to 5')
#print(move1.final_list)

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

init_stack_table = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_5_table.txt")
stacks_dict = clean_stacks_list(init_stack_table)
#print("START")
#print(stacks_dict)

moves_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_5_moves.txt")
#print(moves_list)
cut_moves = moves_list[:20]
#print("MOVES")
#print(cut_moves)

#execute moves in order
#within a move, crates are moved one at a time, from top first
#start of the list is the top of the stack
#move 1 from 1 to 2
# removes G from 1
# inserts G at position 0 in 2

def move_crates_one_at_a_time(string):
    crate_move = Move(string)
    for num in range(crate_move.number_to_move):
            move_char = stacks_dict[crate_move.from_stack].pop(0)
            stacks_dict[crate_move.to_stack].insert(0, move_char)
    #print("AFTER MOVE")
    #print(stacks_dict)

def all_the_moves(list):
    for string in list:
        move_crates_one_at_a_time(string)
    #print(stacks_dict)
all_the_moves(moves_list)

#after all the moves, which letter is on top of each stack - as a 9 letter code
def top_crates(dictionary):
    new_string = ""
    for key, value in dictionary.items():
        new_string += value[0]
    return new_string
print(top_crates(stacks_dict))









