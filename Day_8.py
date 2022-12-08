import general_functions
import copy

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_8.txt")
#print(init_list[98])

#class for tree (is_visible)
class Tree:
    def __init__(self, height, row_number, column_number, row_string):
        self.height = height
        self.row_number = row_number
        self.column_number = column_number
        self.row_column = [row_number, column_number]
        self.row_string = row_string
        self.trees_to_left = row_string[:column_number]
        self.trees_to_right = row_string[column_number+1:]
    
    def __repr__(self):
        return self.row_column
        
#2 does the same index in previous rows contain any numbers >= to it
    def visible_up(self):
        return False

#3 does the same index in following rows contain any numbers >= to it
    def visible_down(self):
        return False

#1 does the rest of the row contain any numbers >= to it
    def visible_right(self):
        pass
    #use trees_to_right

    def visible_left(self):
        return True

    def is_visible(self):
        results = [self.visible_up(), self.visible_down(), self.visible_right(), self.visible_left()]
        if True in results:
            return True
        else:
            return False

#class for row (count visible trees)
class Row:
    def __init__(self, name, row_number):
        self.name = name
        self.row_number = row_number
        self.length = len(name)
    
    def __repr__(self):
        return self.name
    
    #first and last row all visible
    def all_visible(self):
        if self.row_number in [0, 98]:
            return True
        else:
            return False

    def number_visible(self):
        iteration_counter = 0
        visible_counter = 0
        for num in self.name:
            new_tree = Tree(num, self.row_number, iteration_counter, self.name)
            if new_tree.is_visible() == True:
                visible_counter += 1
            iteration_counter += 1  
        return visible_counter

example_row = Row("100002203323321203402423434324400223225443334554221555514312335522000320202144212403130203231300110", 0)
print(example_row.number_visible())



example_tree = Tree(2, 5, 10, "1000022033233212034024")
print(example_tree.visible_right())
#print(example_tree.trees_to_left)
#print(example_tree.height)
#print(example_tree.trees_to_right)

#visible:

#if in any other row, do three checks:

#sum up list of rows - how many visible trees are in each