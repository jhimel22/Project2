'''
name: Naser Al Madi
file: .py
data: 9/22/2020
course: CS151 fall
description: 
'''

import turtle


def make_window(window_title, bgcolor, width, height):
	''' this function creates a screen object and returns it '''

	window = turtle.getscreen() # Set the window size
	window.title(window_title)
	window.bgcolor(bgcolor)
	window.setup(width, height)
	window.tracer(0) #turns off screen updates for the window Speeds up the game
	return window


def make_turtle(shape, color, stretch_width, stretch_length, x_pos, y_pos):
    ''' creates a turtle and sets initial position '''

    turt = turtle.Turtle()
    turt.speed(0)    # Speed of animation, 0 is max
    turt.shape(shape)
    turt.color(color)
    turt.shapesize(stretch_width, stretch_length) 
    turt.penup()
    turt.goto(x_pos, y_pos) # Start position
    return turt


def draw_grid(grid, turt, x_pos, y_pos, tile_size):
    ''' draws a grid at x, y with a specific tile_size '''

    turt.up()
    turt.goto(x_pos, y_pos)
    turt.down()

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            
            turt.up()
            turt.goto(x_pos + col * tile_size, y_pos -row * tile_size)
            turt.down()

            if grid[row][col] == 1:
                turt.dot(tile_size-5, "red")
            
            elif grid[row][col] == 2:
                turt.dot(tile_size-5, "yellow")
            
            else:
                turt.dot(tile_size-5, "white")


def check_win(grid, player):
    ''' checks the winner in the grid
    returns true if player won
    returns false if player lost
     '''

    count = 0

    # check rows
    for row in range(len(grid)):
        count = 0
        for col in range(len(grid[0])):
            if grid[row][col] == player:
                count += 1

                if count == 4:
                    return True
            else:
                count = 0
            

    # check columns
    for col in range(len(grid[0])):
        count = 0
        for row in range(len(grid)):
            if grid[row][col] == player:
                count += 1
                
                if count == 4:
                    return True
            else:
                count = 0

    # check diagonal
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            if row + 3 < len(grid) and col + 3 < len(grid[row]):
                if grid[row][col] == 1\
                   and grid[row+1][col+1] == 1\
                   and grid[row+2][col+2] == 1\
                   and grid[row+3][col+3] == 1:
                   return True 



# setting up the window
window = make_window("Connect 4", "light sky blue", 800, 600)


# the grid
grid = []

for rows in range(5):
    grid.append([0]*7)

# drawing_turtle
my_turtle = make_turtle('classic', "white", 1, 1, 0, 0 )

x_offset = -150
y_offset = 200
tile_size = 50

turn = 1

def play(x_pos, y_pos):
    ''' '''
    global turn
    row = int(abs((y_pos - y_offset - 25) // (50) + 1))
    col = int(abs((x_pos - x_offset - 25) // (50) + 1))
    print(row, col)
    grid[row][col] = turn
    draw_grid(grid, my_turtle, x_offset, y_offset, tile_size)
    window.update()

    if check_win(grid, 1):
        print("player 1 won")

    elif check_win(grid, 2):
        print("player 2 won")

    if turn == 1:
        turn = 2
    else:
        turn = 1


window.onscreenclick(play)
window.listen()

def main():
    ''' the main function where the game events take place '''

    global turn

    draw_grid(grid, my_turtle, x_offset, y_offset, tile_size)

    while True:

        # grid[1][0] = 1
        # grid[2][1] = 1
        # grid[3][2] = 1
        # grid[4][3] = 1

        selected_row = int(input("enter row, player "+ str(turn) +": "))
        selected_col = int(input("enter col, player "+ str(turn) +": "))

        if grid[selected_row][selected_col] == 0:

            if turn == 1:
                grid[selected_row][selected_col] = 1
            else:
                grid[selected_row][selected_col] = 2

        draw_grid(grid, my_turtle, -150, 200, 50)
        window.update()

        if check_win(grid, 1):
            print("player 1 won")

        elif check_win(grid, 2):
            print("player 2 won")

        if turn == 1:
            turn = 2
        else:
            turn = 1


    # window.exitonclick()

if __name__ == "__main__":
	main()

