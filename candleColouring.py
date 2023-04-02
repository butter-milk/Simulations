from random import randint
import numpy as np

class Grid:
    # Example of square numbering in a 3x3 Grid
    #---------------------
    #|      |      |     |
    #|   0  |   1  |  2  |
    #---------------------
    #|      |      |     |
    #|   3  |   4  |  5  |
    #---------------------
    #|      |      |     |
    #|   6  |   7  |  8  |
    #---------------------

    def __init__(self, size) -> None:
        #Make square grid of correct size and Colour the grid
        self.size = size
        self.grid = [[randint(0,1) for _ in range(size)] if i%2==0 else [randint(0,1) for _ in range(size+1)]  for i in range(2*size+1)]
        pass

    def getUnitSquare(self, nr) -> list:
        #Returns edges adjacent to the unit square
        return[self.grid[2*int(nr/self.size)][nr%self.size],self.grid[2*(int(nr/self.size)+1)][nr%self.size], self.grid[1+2*int(nr/self.size)][nr%self.size]   , self.grid[1+2*int(nr/self.size)][(nr%self.size)+1]]
    
    def sameColour(self, square:list) -> bool:
        return all(square) or not any(square)

def simulate(size: int, no: int) -> float:
    #Simulate colourings, returns ratio of successes
    success = 0
    for _ in range(no):
        grid = Grid(size)
        DifferentColours = True
        for i in range(size**2):
            DifferentColours = DifferentColours & (not grid.sameColour(grid.getUnitSquare(i)))
        success += DifferentColours
    return success/no


print(simulate(3,10**4))