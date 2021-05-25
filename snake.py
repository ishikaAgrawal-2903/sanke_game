from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.turtle = []
        self.create_snake()
        self.head = self.turtle[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segments = Turtle("square")
        segments.color("white")
        segments.penup()
        segments.goto(position)
        self.turtle.append(segments)

    def extend(self):
        self.add_segment(self.turtle[-1].position())

    def move(self):
        for seg in range(len(self.turtle) - 1, 0, -1):
            new_x = self.turtle[seg - 1].xcor()
            new_y = self.turtle[seg - 1].ycor()
            self.turtle[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def reset(self):
        for seg in self.turtle:
            seg.goto(1500,1500)
        self.turtle.clear()
        self.create_snake()
        self.head = self.turtle[0]
