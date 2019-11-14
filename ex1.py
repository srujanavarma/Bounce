from tkinter import Tk, Button, Label
from tkinter import Canvas
from random import randint
import pygame

root = Tk()
root.title("Bounce")
root.resizable(False, False)

canvas = Canvas(root, width=600, height=600)
canvas.pack()
white = (255, 255, 255)

limit = 0

dist = 5

score = 0

#functions related to ball
class Ball:

    # for creation of ball on the canvas
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2,fill="red", tags='dot1')

    # for moving the ball
    def move_ball(self):

        offset = 10
        global limit

        if limit >= 510:
            global dist, score, next

            if (dist - offset <= self.x1 and dist + 40 + offset >= self.x2):

                score += 10

                canvas.delete('dot1')

                ball_set()

            else:

                canvas.delete('dot1')
                bar.delete_bar(self)
                score_board()
            return

        limit += 1
        self.canvas.move(self.ball, 0, 1)
        self.canvas.after(10, self.move_ball) # for continuous moving of ball again call move_ball

#functions related to bar
class bar:

    # method for creating bar
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.rod = canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                           fill="yellow", tags='dot2')

    # method for moving the bar
    def move_bar(self, num):
        global dist
        if (num == 1):

            self.canvas.move(self.rod, 20, 0)
            dist += 20

        else:
            self.canvas.move(self.rod, -20, 0)
            dist -= 20

    def delete_bar(self):
        canvas.delete('dot2')

# Function to define the dimensions of the ball
def ball_set():
    global limit
    limit = 0

    value = randint(0, 570) # for random x-axis distance from where the ball starts to fall

    ball1 = Ball(canvas, value, 20, value + 30, 50)

    ball1.move_ball()

# Function for displaying the score
def score_board():
    root2 = Tk()
    root2.title("Bounce")
    root2.resizable(False, False)
    canvas2 = Canvas(root2, width=300, height=300)
    canvas2.pack()

    w = Label(canvas2, text="\nGAME OVER\n\nYOUR SCORE = "
                            + str(score) + "\n\n")
    w.pack()

    button3 = Button(canvas2, text="PLAY AGAIN", bg="green",
                     command=lambda: play_again(root2))
    button3.pack()

    button4 = Button(canvas2, text="EXIT", bg="green",
                     command=lambda: exit_handler(root2))
    button4.pack()

# Function for handling the play again request
def play_again(root2):
    root2.destroy()
    main()

# Function for handling exit request
def exit_handler(root2):
    root2.destroy()
    root.destroy()

#main loop
def main():
    global score, dist
    score = 0
    dist = 0
    bar1 = bar(canvas, 5, 560, 45, 575)

    button = Button(canvas, text="==>", bg="green",command=lambda: bar1.move_bar(1))

    button.place(x=300, y=580)

    button2 = Button(canvas, text="<==", bg="green",command=lambda: bar1.move_bar(0))
    button2.place(x=260, y=580)

    ball_set()
    root.mainloop()

if (__name__ == "__main__"):
   main()