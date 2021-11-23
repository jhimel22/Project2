
import turtle
import time
from playsound import playsound
from multiprocessing import Process

# create a turtle and a window for drawing
if __name__ == "__main__":
    turt = turtle.Turtle()
    window = turtle.getscreen()
    window.bgcolor('slate gray')
    turtle.hideturtle()
    turt.hideturtle()
    turt.shape('square')
    turt.shapesize(2.5, 2.5)

    # set offsets and tile size for drawing the grid
    x_offset = -150
    y_offset = 200
    tile_size = 50

    # create an int variable for counting steps
    steps = 0


def draw_grid(grid, turt, x_pos, y_pos, tile_size):
    ''' draws a grid at x_pos, y_pos with a specific tile_size '''

    # turn off tracer for fast drawing
    window.tracer(False)
    
    # move turtle to initial drawing position
    turt.up()
    turt.goto(x_pos, y_pos)
    turt.down()

    # go over every cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            
            # move turtle to the position of the cell in the grid
            turt.up()
            turt.goto(x_pos + col * tile_size, y_pos -row * tile_size)
            turt.down()

            # if the cell is an obstacle (X) draw a black dot
            if grid[row][col] == 'X':
                #turt.dot(tile_size-5, "Black")
                turt.color('grey', "black")
                turt.stamp()
            
            # if the cell is the start drawing position (S) draw a yellow dot
            elif grid[row][col] == 'S':
                #turt.dot(tile_size-5, "yellow")
                turt.color('grey', "yellow")
                turt.stamp()
            
            # if the cell is the End position (E) draw a Red dot
            elif grid[row][col] == 'E':
                #turt.dot(tile_size-5, "red")
                turt.color('grey', "red")
                turt.stamp()

            # if the cell is part of a path (P) draw a royalblue dot
            elif grid[row][col] == 'P':
                #turt.dot(tile_size-5, "royalblue")
                turt.color('grey', "royalblue")
                turt.stamp()

            # if the cell has been tried before (T) draw a light blue dot
            elif grid[row][col] == 'T':
                #turt.dot(tile_size-5, "light blue")
                turt.color('grey', "light blue")
                turt.stamp()

            # if the cell is part of a deadend (D) draw a gray dot
            elif grid[row][col] == 'D':
                #turt.dot(tile_size-5, "gray")
                turt.color('gainsboro', "gray")
                turt.stamp()
            
            # else draw a white dot
            else:
                #turt.dot(tile_size-5, "white")
                turt.color( 'grey', "white")
                turt.stamp()
    
    # turn tracer back on
    window.tracer(True)


def find_start(grid):
    ''' finds the start position (S) in the grid
    returns a tuple of start row and col
    '''

    # go over every cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            # cell at row, col is 'S' return row and col as a tuple
            if grid[row][col] == 'S':
                return (row, col)


def search_from(grid, row, col):
    ''' recursive function to search the grid for the end (E) '''

    global steps

    steps += 1

    # make sure row and col are valid points on the grid
    if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]):
        # return False if not valid
        return False

    # check that the grid cell at row and col is not obstacle, tried, or deadend
    if grid[row][col] == 'X' or grid[row][col] == 'T' or grid[row][col] == 'D':
        # return False if obstacle, tried, or deadend
        return False

    # If end is found at row, col return True
    if grid[row][col] == 'E':
        return True
    
    # If the cell at row, col is not the start cell, mark the cell as tried (T)
    if grid[row][col] != 'S':
        grid[row][col] = 'T'

    # draw the grid
    draw_grid(grid, turt, x_offset, y_offset, tile_size)

    # pause the program for a short duration, try 0.5 and 0.01 seconds
    time.sleep(0.25)

    # recursively search differnt directions adjacent to current row, col (up, down, left, right)
    found = (search_from(grid, row-1, col)
            or search_from(grid, row+1, col)
            or search_from(grid, row, col-1)
            or search_from(grid, row, col+1)
            )

    # if any of the 4 directions returns True, mark the cel at row, col as part of the path and return True
    if found and grid[row][col] != 'S':
        grid[row][col] = 'P'
        return True
    # else, if the cell at row, col is not the start cell (S), mark it as a deadend
    elif grid[row][col] != 'S':
        grid[row][col] = 'D'
    

def background_music():
    ''' plays tetris music in the background '''

    playsound('Tetris.mp3')    


def main():
    ''' reads a maze file and sets the search parameters '''

    

    # read maze file and create playground grid
    playground = read_grid("maze2.txt")

    # find start position
    row, col = find_start(playground)

    # call the search function, it takes the grid, row, column, and steps
    search_from(playground, row, col)

    # create a list of tuples representing the path
    path = []
    for row in range(len(playground)):
        for col in range(len(playground[0])):
            if playground[row][col] == 'P':
                path.append((row, col))

    # print path length
    print('path length:', len(path))

    # draw the final grid
    draw_grid(playground, turt, x_offset, y_offset, tile_size)
    
    # pause the grid drawing for 4 seconds
    time.sleep(4)

    # print the number of steps taken to find the path
    print("number of steps taken to reach answer:", steps)
    


if __name__ == "__main__":

    p = Process(target=background_music, args=())
    p.start()
    main()
    p.terminate()

