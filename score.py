from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.setposition(0, 280)
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.write(f"Score : {self.score}", move=False, align='center', font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", move=False, align='center', font=('Arial', 12, 'normal'))


    def increase_score(self):
        self.clear()
        self.score += 1
        self.score_board()
