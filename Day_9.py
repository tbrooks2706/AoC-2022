import general_functions

#input is a series of motions made by the head
init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_9.txt")

#rope with knot at each end - knots are head and tail
#grid is a very large (theoretically infinite?) 2 dimensional space for the rope to move in
    #size can be driven by just running the moves and seeing whether I get an index error
    #could do this as eg.
    #grid = [[".",".","#"],[".",".","."],[".",".","."]]
    #print(grid[0][1])
    #just use a loop to make a 500x500 grid and start at the centre?

#grid[x column[y row, y row, y row], x column[y row, y row, y row] etc]
#first number increase = movement to the right
#second number increase = movement down
def create_grid(width, height):
    grid = []
    for num in range(width):
        column = []
        for num in range(height):
            column.append(".")
        grid.append(column)
    return grid
working_grid = create_grid(200,200)
#print(working_grid)

#dictionary of changes to the head's coordinates based on the move that it makes
head_moves = {"L": [-1, 0], "R": [1, 0], "U": [0, -1], "D": [0, 1]}
print(head_moves["L"][0])

#first key is relative number on the x axis (-1 is head to the left)
#second key is relative number on the y axis (-1 is head above)
relative_positions = {0: {0: "on top", -1: "above", 1: "below"}, -1: {0: "left", -1: "above left", 1: "below left"}, 1: {0: "right", -1: "above right", 1: "below right"}}

class Move:
#for each move,
    #work out where the head and tail are at the start
    def __init__(self, direction, head_start, tail_start):
        self.direction = direction
        self.head_start = head_start
        self.tail_start = tail_start
        self.head_start_x = head_start[0]
        self.head_start_y = head_start[1]
        self.tail_start_x = tail_start[0]
        self.tail_start_y = tail_start[1]
        #working
        self.relative_head_position = relative_positions[self.head_start_x - self.tail_start_x][self.head_start_y - self.tail_start_y]
        
    #move head
    def move_head(self):
        self.head_end_x = self.head_start_x + head_moves[self.direction][0]
        self.head_end_y = self.head_start_y + head_moves[self.direction][1]
        return [self.head_end_x, self.head_end_y]
    
    #work out which coordinates[x][y] the tail is after it (based on move and relative position of head and tail before)
    def move_tail(self):
        pass

example_move = Move("U", [49, 50], [50, 51])
#print(example_move.move_head())
#print(example_move.relative_head_position)





#rules:
#head and tail must always be touching (vert, horiz or diag) OR the head can cover the tail
#if head moves away from tail, tail moves towards it to keep up
#IMPORTANT if the head moves but is still touching (or on top of) the tail, the tail doesn't move
#head can move up down left right
#tail will move diagonally if it needs to, to make sure it stays touching the head
#they move simultaneously, so any move by the head moves the tail at the same time

#9 relative positions of head to tail - above left, above, above right, left, on top, right, below left, below, below right
#4 possible head moves - up, down, left, right
#therefore 36 possible combinations of situation - each one will trigger a tail move
#9 possible tail moves - up left, up, up right, left, (not move), right, down left, down, down right

#work out how to represent each of 9 possible tail moves in code

#how many positions on the grid does the tail visit at least once?

#identify start point and mark it as visited

#mark that coordinate as visited
#then loop through entire grid - how many values marked as visited are there