'''
name: Jackie Himel and Erik Cohen
file: grid.py
data: 11/15/2021
course: CS321 fall
description: grid implementation for connect four and search_maze.
We used the factory design pattern to make this grid class extensible
// built on a geeksforgeeks design pattern template https://www.geeksforgeeks.org/factory-method-python-design-patterns/
'''


# Python Code for factory method
# it comes under the creational
# Design Pattern

class ConnectFourGrid:
    """ it simply returns the connect-4 version """
 
    def __init__(self):
        grid = []
        for rows in range(5):
            grid.append([0]*7)
        self.grid = grid
    
    def get_grid(self):
        return self.grid
 

class SearchMazeGrid:
    """it simply returns the search_maze version"""
 
    def __init__(self):
        self.grid =[]
 
    def get_grid(self):
        return self.grid

    def read_grid(self, file_name):
        ''' reads a maze file and initializes a gird with its contents '''

        # open the text file
        file = open(file_name)

        # read a line from the file
        line = file.readline()

        # replace \n with nothing
        line = line.replace('\n', '')

        while line:
            # split the line into tokens
            tokens = line.split(',')

            # add the tokens to the grid as a single row
            self.grid.append(tokens)

            line = file.readline()
            
            # replace \n with nothing
            line = line.replace('\n', '')

        # return the grid
        return self.grid

def Grid(purpose= "connect_four"):
    """Factory Method"""
    grid = {
        "connect_four": ConnectFourGrid,
        "search_maze": SearchMazeGrid,
    }
    return grid[purpose]()
 
if __name__ == "__main__":
 
    connect_four_grid = Grid("connect_four")
    print(connect_four_grid.get_grid())

    search_maze_grid = Grid("search_maze")
    search_maze_grid.read_grid("maze1.txt")
    print(search_maze_grid.get_grid())
