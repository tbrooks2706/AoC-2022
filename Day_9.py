import general_functions

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_9.txt")

#rope with knot at each end - knots are head and tail

#grid is a very large (theoretically infinite?) 2 dimensional space for the rope to move in
    #size can be driven by just running the moves and seeing whether I get an index error
    #could do this as eg.
    #grid = [[".",".","#"],[".",".","."],[".",".","."]]
    #print(grid[0][1])
    #just use a loop to make a 500x500 grid and start at the centre?


#input is a series of motions made by the head

#rules:
#head and tail must always be touching (vert, horiz or diag) OR the head can cover the tail
#if head moves away from tail, tail moves towards it to keep up
#IMPORTANT if the head moves but is still touching (or on top of) the tail, the tail doesn't move
#head can move up down left right
#tail will move diagonally if it needs to, to make sure it stays touching the head
#they move simultaneously, so any move by the head moves the tail at the same time

#how many positions on the grid does the tail visit at least once?