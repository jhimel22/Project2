'''
name: Naser Al Madi
file: pong.py
data: 9/20/2020
course: CS151 fall
description: simple implementation of the game Pong using python 3 turtles.
'''

import turtle


class Paddle:
    # implements a Pong game paddle

    def __init__(self, x_position, y_position):
        ''' initializes a paddle with a position '''

        self.x_position = x_position
        self.y_position = y_position

        self.turt = make_turtle("square", "white", 5, 1, self.x_position, self.y_position)


    def up(self):
        y = self.turt.ycor()
        y += 20
        self.turt.sety(y)
        self.y_position = y


    def down(self):
        y = self.turt.ycor() #Get the current y coordinate
        y -= 20             #add 20px could also be y=y+20
        self.turt.sety(y)    #move the paddle to the new y position
        self.y_position = y


    def xcor(self):
        ''' returns turtle x_cord '''
        return self.turt.xcor()

    
    def ycor(self):
        ''' returns turtle y_cord '''
        return self.turt.ycor()



class Ball:
    # implements a Pong game ball

    def __init__(self):
        ''' intializes a ball with default direction and position '''

        self.turt = make_turtle("square", "white", 1, 1, 0, 0)
        self.ball_dx = 0.0925 #speed in x direction
        self.ball_dy = 0.0925 #speed in y direction
        self.x_position = 0
        self.y_position = 0


    def move(self):
        ''' moves the ball in x and y directions '''

        # Move the ball
        self.turt.setx(self.turt.xcor() + self.ball_dx)
        self.turt.sety(self.turt.ycor() + self.ball_dy)

        self.x_position = self.turt.xcor()
        self.y_position = self.turt.ycor()

        # Top and bottom
        if self.turt.ycor() > 290:
            self.turt.sety(290)
            self.ball_dy *= -1

        elif self.turt.ycor() < -290:
            self.turt.sety(-290)
            self.ball_dy *= -1

    
    def xcor(self):
        ''' returns turtle x_cord '''
        return self.turt.xcor()

    
    def ycor(self):
        ''' returns turtle y_cord '''
        return self.turt.ycor()


    def goto(self, x_pos, y_pos):
        ''' moves ball to new x, y positions '''
        self.turt.goto(x_pos, y_pos)
        self.x_position = x_pos
        self.y_position = y_pos


    def setx(self, x_cor):
        ''' sets the ball x position '''
        self.turt.setx(x_cor)
        self.x_position = x_cor



def make_window(window_title, bgcolor, width, height):
    '''this function creates a screen object and returns it'''

    window = turtle.getscreen() #Set the window size
    window.title(window_title)
    window.bgcolor(bgcolor)
    window.setup(width, height)
    window.tracer(0) #turns off screen updates for the window Speeds up the game
    return window


def make_turtle(shape, color, stretch_width, stretch_length, x_pos, y_pos):
    ''' creates a turtle and sets initial position '''

    turt = turtle.Turtle()
    turt.speed(0) # Speed of animation, 0 is max
    turt.shape(shape) # square defualt is 20,20
    turt.color(color)
    turt.shapesize(stretch_width, stretch_length) 
    turt.penup()
    turt.goto(x_pos, y_pos) #Start position
    return turt


def main():
    ''' the main function where the game events take place '''

    window = make_window("Pong - A CS151 Reproduction!", "black", 800, 600)

    # Score
    score_player1 = 0
    score_player2 = 0

    # paddels
    paddle_1 = Paddle(-350, 0)
    paddle_2 = Paddle(350, 0)

    # ball
    ball = Ball()

    # Pen
    pen = make_turtle("square", "white", 1, 1, 0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
    pen.hideturtle()

    # Keyboard bindings
    window.listen() #Listen for keyboard input
    window.onkeypress(paddle_1.up, "w") #when you press w run paddle_a_up
    window.onkeypress(paddle_1.down, "s")
    window.onkeypress(paddle_2.up, "Up")
    window.onkeypress(paddle_2.down, "Down")

    # Main game loop
    while True:
        window.update() #This is the update to offset the wn.tracer(0)

        ball.move()

        # Border checking    
        # Left and right
        if ball.xcor() > 350:
            score_player1 += 1
            pen.clear()
            pen.write("Player A: "+ str(score_player1) + "  Player B: "+ str(score_player2), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.ball_dx *= -1

        elif ball.xcor() < -350:
            score_player2 += 1
            pen.clear()
            pen.write("Player A: "+ str(score_player1) + "  Player B: "+ str(score_player2), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.ball_dx *= -1

        # Paddle and ball collisions
        if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
            ball.setx(-340)
            ball.ball_dx *= -1.5
        
        elif ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
            ball.setx(340)
            ball.ball_dx *= -1.5




if __name__ == "__main__":
	main()