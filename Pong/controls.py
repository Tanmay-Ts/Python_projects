from turtle import Turtle, Screen
class Control:
    paddle1 = Turtle()
    paddle1.color("white")
    paddle1.penup()
    paddle1.shape("square")
    paddle1.shapesize(5,1)
    paddle1.goto(400,0)
    def up(self):
        self.paddle1.left(20)

    def down(self):
        self.paddle1.right(20)

