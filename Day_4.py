import general_functions

class Pair:
    def __init__(self, string):
        self.first_list = string.split(",")
        self.working_list = []
        for item in self.first_list:
            tmplist = item.split("-")
            for num in tmplist:
                self.working_list.append(int(num))

    def range2_contains_range1(self):
        #first range in pair is 1a and 1b, second range is 2a and 2b
        #index 0 1a, 1 1b, 2 2a, 3 2b
        #2a <= 1a AND 2b >= 1b
        #2, 99, 1, 100 - yes, yes
        #2, 100, 2, 99 - yes, no
        if (self.working_list[2] <= self.working_list[0] and self.working_list[3] >= self.working_list[1]):
            stat1 = True
        else:
            stat1 = False
        return stat1

    def range1_contains_range2(self):
        #first range in pair is 1a and 1b, second range is 2a and 2b
        #index 0 1a, 1 1b, 2 2a, 3 2b
        #1a <= 2a AND 1b >= 2b
        #2, 99, 1, 100 - no, no
        #2, 100, 2, 99! - yes, yes
        #1, 99, 2, 100 - yes, no
        #1, 100, 2, 99! - yes, yes
        if (self.working_list[0] <= self.working_list[2] and self.working_list[1] >= self.working_list[3]):
            stat1 = True
        else:
            stat1 = False
        return stat1
    
    def range_contains_range(self):
        if self.range1_contains_range2() == True or self.range2_contains_range1() == True:
            return True
        else:
            return False

    def range_overlap(self):
        #first range in pair is 1a and 1b, second range is 2a and 2b
        #index 0 1a, 1 1b, 2 2a, 3 2b
        #if either number in pair 1, is between 2a and 2b
        #OR if either number in pair 2, is between 1a and 1b
        #2, 9, 10, 100 - no, no
        #2, 10, 10, 10! - yes, yes
        #1, 99, 100, 100 - no, no
        #1, 100, 2, 99! - no, yes
        #1, 50, 49, 51! - yes, yes
        #100, 100, 1, 99 - no, no
        test_1 = False
        test_2 = False
        for num in self.working_list[:1]:
            if num >= self.working_list[2] and num <= self.working_list[3]:
                test_1 = True
        for num in self.working_list[2:3]:
            if num >= self.working_list[0] and num <= self.working_list[1]:
                test_2 = True
        if test_1 == True or test_2 == True:
            return True
        else:
            return False
#end of class methods

#part 1 calc
def count_duplicating_pairs(list):
    counter = 0
    for item in list:
        two_elves = Pair(item)
        if two_elves.range_contains_range() == True:
            counter += 1
    return counter

#part 2 calc
def count_overlapping_pairs(list):
    counter = 0
    for item in list:
        two_elves = Pair(item)
        if two_elves.range_overlap() == True:
            counter += 1
    return counter

#execute code in one go
init_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2022\Day_4.txt")
duplicate_count = count_duplicating_pairs(init_list)
overlap_count = count_overlapping_pairs(init_list)

#answer to part 1
print(duplicate_count)

#answer to part 2
print(overlap_count)