'''
name: Naser Al Madi
file: pong.py
data: 9/20/2020
course: CS151 fall
description: simple implementation of the game Pong using python 3 turtles.
'''
from graphics import *


class Paddle:
    # implements a Pong game paddle
    dy = 20

    def __init__(self, x_position, y_position):
        ''' initializes a paddle with a position '''
        self.x_position = x_position
        self.y_position = y_position
        self.paddle = TurtleGraphics()
        self.paddle.teleport(x_position, y_position)
        self.paddle.turtle_style(shape = "square", stretch_width = 5)
        #self.paddle.get_turtle().hideturtle()

    def up(self):
        current_y = self.get_paddle_ycor()
        new_y = current_y + self.dy
        self.paddle.teleport(self.x_position, new_y)
        self.y_position = new_y

    def down(self):
        current_y = self.get_paddle_ycor()
        new_y = current_y - self.dy
        self.paddle.teleport(self.x_position, new_y)
        self.y_position = new_y

    def get_paddle_ycor(self):
        ''' returns turtle y_cord '''
        return self.paddle.get_turtle().ycor()


class Ball:
    # implements a Pong game ball

    def __init__(self):
        ''' intializes a ball with default direction and position '''
        self.ball_dx = 0.0925 #speed in x direction
        self.ball_dy = 0.0925 #speed in y direction
        self.x_position = 0
        self.y_position = 0
        self.ball = TurtleGraphics()
        self.turtle_ball = self.ball.get_turtle()
        self.ball.teleport(self.x_position, self.y_position)
        self.ball.turtle_style(shape = "square")

    def get_ball_xcor(self):
        return self.ball.get_turtle().xcor()

    def get_ball_ycor(self):
        return self.ball.get_turtle().ycor()


    def move(self):
        ''' moves the ball in x and y directions '''

        new_x_cor = self.get_ball_xcor() + self.ball_dx
        new_y_cor = self.get_ball_ycor() + self.ball_dy

        # Move the ball
        self.ball.teleport(new_x_cor,new_y_cor)

        self.x_position = new_x_cor
        self.y_position = new_y_cor

        # Top and bottom
        self.bounce_off_window()

    def set_ycor(self, new_y):
        '''set turtle y_cor helper function for bounce_off_window'''
        return self.ball.teleport(self.get_ball_xcor(),new_y)

    def set_xcor(self, new_x):
        '''set turtle x_cor helper function for bounce_off_paddle'''
        return self.ball.teleport(new_x, self.get_ball_ycor())

    def bounce_off_window(self):
        ''' Checks if ball is out of bounds and "bounces" the ball off the window'''
        y_pos = self.get_ball_ycor()
        if y_pos > 290:
            self.set_ycor(290)
            self.ball_dy *= -1

        elif y_pos < -290:
            self.set_ycor(-290)
            self.ball_dy *= -1

    def bounce_off_paddle(self):
        ''' Checks which side the ball is on and "bounces" the ball off the paddle'''
        x_pos = self.get_ball_xcor()
        if x_pos > 330:
            self.set_xcor(329)
            self.ball_dx *= -1.5

        elif x_pos < -330:
            self.set_xcor(-329)
            self.ball_dx *= -1.5

    def goto(self, x_pos, y_pos):
        ''' moves ball to new x, y positions '''
        self.ball.teleport(x_pos, y_pos)
        self.x_position = x_pos
        self.y_position = y_pos

    



class PongWindow:
    def __init__(self, title):
        self.turt = TurtleGraphics()
        self.window = self.turt.make_window(title)
        # display words on window
        self.turt.teleport(0, 260)
        self.turt.turtle_style("square")
        self.pen = self.turt.get_turtle()

    def display_score(self, score):
        self.turt.teleport(0, 260)
        self.pen.clear()
        font = ("Courier", 24, "normal")
        self.pen.write(score, align="center", font = font)
        self.pen.hideturtle()


    def get_window(self):
        return self.window


class Pong:
    # implements a Pong game

    def __init__(self):
        ''' intializes a game window, players, and the game objects '''
        self.pong = PongWindow("Pong - A CS151 Reproduction!")
        self.window = self.pong.get_window()
        self.initialize_game()

    def initialize_game(self):
        self.score_player1 = 0
        self.score_player2 = 0
        self.display_score()
        self.paddle_1 = Paddle(-350, 0)
        self.paddle_2 = Paddle(350, 0)
        self.ball = Ball()
        self.set_key_bindings()

    def set_key_bindings(self):
        self.window.listen() #Listen for keyboard input
        self.window.onkeypress(self.paddle_1.up, "w") #when you press w run paddle_a_up
        self.window.onkeypress(self.paddle_1.down, "s")
        self.window.onkeypress(self.paddle_2.up, "Up")
        self.window.onkeypress(self.paddle_2.down, "Down")

    def display_score(self):
        player1Score = str(self.score_player1)
        player2Score = str(self.score_player2)
        print(f"Player A: {player1Score}  Player B: {player2Score}")
        self.pong.display_score(f"Player A: {player1Score}  Player B: {player2Score}")

    
    def point_scored_left(self):
        self.score_player1 += 1
        self.display_score()
        self.ball.goto(0, 0)
        self.ball.ball_dx = -.0925

    def point_scored_right(self):
        self.score_player2 += 1
        self.display_score()
        self.ball.goto(0, 0)
        self.ball.ball_dx = .0925

    def check_point_scored(self):
        left_bound = -360
        right_bound = 360
        ball_x_pos = self.ball.get_ball_xcor()
        if ball_x_pos > right_bound:
            self.point_scored_left()

        elif ball_x_pos < left_bound:
            self.point_scored_right()

    def collisionLeftPaddle(self):
        ballPaddle_x_intercept = (self.ball.get_ball_xcor() < -340)
        ballPaddle_y_intercept = (self.ball.get_ball_ycor() < self.paddle_1.get_paddle_ycor() + 50) and (self.ball.get_ball_ycor() > self.paddle_1.get_paddle_ycor() - 50)
        if ballPaddle_x_intercept and ballPaddle_y_intercept:
            self.ball.bounce_off_paddle()

    def collisionRightPaddle(self):
        ballPaddle_x_intercept = (self.ball.get_ball_xcor() > 340)
        ballPaddle_y_intercept = (self.ball.get_ball_ycor() < self.paddle_2.get_paddle_ycor() + 50) and (self.ball.get_ball_ycor() > self.paddle_2.get_paddle_ycor() - 50)
        if ballPaddle_x_intercept and ballPaddle_y_intercept:
            self.ball.bounce_off_paddle()

    def collisions(self):
        self.collisionLeftPaddle()
        self.collisionRightPaddle()

    def run(self):
        while True:
            self.window.update() #This is the update to offset the wn.tracer(0)
            self.ball.move()
            self.collisions()
            self.check_point_scored()

def main():
    pong = Pong()
    pong.run()

if __name__ == "__main__":
    main()
