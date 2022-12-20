from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 15, "bold")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = -1
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=280)
        self.color("white")
        self.add_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)
    def add_score(self):
        self.clear()
        self.current_score += 1
        display = "Score: " + str(self.current_score)
        self.write(display, move=False, align=ALIGN, font=FONT)