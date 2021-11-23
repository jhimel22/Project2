'''
name: Naser Al Madi
file: .py
data: 9/22/2020
course: CS151 fall
description: 
'''

from graphics import *
from grid import *

class ConnectFour():
    __x_offset = -150
    __y_offset = 200
    __tile_size = 50

    turn = 1

    def __init__(self):
        self.graphics = TurtleGraphics()
        # setting up the window
        self.window = self.graphics.make_window("Connect 4", "light sky blue")
        # the grid
        self.grid = Grid("connect_four").get_grid()
        self.graphics.turtle_style()
        # drawing_turtle
        self.turt = self.graphics.get_turtle()
        self.window.onscreenclick(self.click_play)
        self.window.listen()


    def draw_grid(self, x_pos= -150, y_pos = 200):
        ''' draws a grid at x, y with a specific tile_size '''
        self.graphics.teleport(x_pos, y_pos)

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):

                self.graphics.teleport(x_pos + col * self.__tile_size, y_pos -row * self.__tile_size)

                if self.grid[row][col] == 1:
                    self.turt.dot(self.__tile_size-5, "red")

                elif self.grid[row][col] == 2:
                    self.turt.dot(self.__tile_size-5, "yellow")

                else:
                    self.turt.dot(self.__tile_size-5, "white")

    def __checkRows(self, player):
        for row in range(len(self.grid)):
            count = 0
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == player:
                    count += 1

                    if count == 4:
                        return True
                else:
                    count = 0
                

    def __checkCollumns(self, player):
        for col in range(len(self.grid[0])):
            count = 0
            for row in range(len(self.grid)):
                if self.grid[row][col] == player:
                    count += 1
                    
                    if count == 4:
                        return True
                else:
                    count = 0

    def __checkDiagonal(self, player):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if row + 3 < len(self.grid) and col + 3 < len(self.grid[row]):
                    if self.grid[row][col] == 1\
                    and self.grid[row+1][col+1] == 1\
                    and self.grid[row+2][col+2] == 1\
                    and self.grid[row+3][col+3] == 1:
                        return True 

    def check_win(self, player):
        ''' checks the winner in the grid
        returns true if player won
        returns false if player lost
        '''
        if(self.__checkRows(player)):
            return True
        if(self.__checkCollumns(player)):
            return True
        if(self.__checkDiagonal(player)):
            return True
        return False

    def switch_turns(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def click_play(self, x_pos, y_pos):
        ''' a version where the user clicks on screen'''
        row = int(abs((y_pos - self.__y_offset - 25) // (50) + 1))
        col = int(abs((x_pos - self.__x_offset - 25) // (50) + 1))
        print(row, col)
        if self.grid[row][col] == 0:
            if self.turn == 1:
                self.grid[row][col] = 1
            else:
                self.grid[row][col] = 2
        self.prepare_next_turn()


    def normal_play(self):
        ''' the main function where the player types their selection '''
        self.draw_grid()

        while True:
            selected_row = int(input("enter row, player "+ str(self.turn) +": "))
            selected_col = int(input("enter col, player "+ str(self.turn) +": "))


    def prepare_next_turn(self):
        self.draw_grid()
        self.window.update()

        if self.check_win(1):
            print("player 1 won")

        elif self.check_win(2):
            print("player 2 won")

        self.switch_turns()

def main():
    game = ConnectFour()
    game.normal_play()
    # window.exitonclick()

if __name__ == "__main__":
	main()

