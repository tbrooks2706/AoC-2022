import general_functions

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_10.txt")
#print(init_list)

cut_list = init_list[:10]
print(cut_list)

#time measured in cycles
#X is a component of signal strength
#noop = 1 cycle, does nothing
#addx num = 2 cycles, increases X by num at the end of the second cycle. nothing happens at the end of the first cycle
#during the cycle, X is still what it was at the start

class Cycle_Set:
    def __init__(self, num, start_x, instruction):
        self.start_x = start_x
        self.num = num
        self.instruction = instruction
        if instruction != "noop":
            self.add_x = int(instruction[5:])
    
    def __repr__(self):
        return self.num
    
    def end_x(self):
        new_x = 0
        if self.instruction == "noop":
            new_x = self.start_x
        else:
            new_x = self.start_x + self.add_x
        return new_x

    def cycle_ends(self):
        end_list = []
        cycle_count = self.num
        #optional first item is start_x if it's addx
        if self.instruction != "noop":
            end_list.append(self.start_x)
            cycle_count += 1
        #last item is always end_x
        end_list.append(self.end_x())
        cycle_count += 1
        #increase cycle count by 2 if addx, 1 if noop
        end_list.append(cycle_count)
        return end_list
 
example_cycle = Cycle_Set(1, 7, "noop")
#print(example_cycle.end_x())
#print(example_cycle.cycle_ends())

def create_list_of_cycle_ends(input_list):
    #including starting value of X as index 0
    end_list = [1]
    cycle_count = 1
    for instruction in input_list:
        new_cycles = Cycle_Set(cycle_count, end_list[-1], instruction)
        output_list = new_cycles.cycle_ends()
        #print("before:",output_list)
        cycle_count = output_list.pop()
        #print("after:",output_list)
        for item in output_list:
            end_list.append(item)
    return end_list
list_of_x = create_list_of_cycle_ends(init_list)
print(list_of_x)
print(len(list_of_x))
#during cycle 1, value is index 0
#value at end of cycle 1 (and during cycle 2), is index 1

#DONE
#work out what x is at the end of each cycle
#add it to a list

#TO DO
#signal strength at any point = cycle number * X
    #during cycle 3, X = 15 so signal strength 45
    #create a signal strength class to calculate this? inputs are cycle num and x value
#iterate through list_of_x and find value at turns below
#sum of signal strengths DURING 20, 60, 100, 140, 180, 220
