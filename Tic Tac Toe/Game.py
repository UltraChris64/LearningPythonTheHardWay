grid = [[7,8,9],[4,5,6],[1,2,3]] # Sets this as grid

def print_grid(g):# Defines the printing of the grid
    for y in g: 
        print(y)
    
print_grid(grid)

in = input(f"{turn}'s turn. Choose a square: ")

def findmatch(grid, turn, in)