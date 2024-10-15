from turtle import Turtle

FONT = ('Arial', 14, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.refresh_board()
        self.hideturtle()

    @staticmethod
    def read_highscore():
        with open("data.txt") as file:
            high_score = int(file.read())
        return high_score

    @staticmethod
    def save_highscore(score):
        with open("data.txt", mode="w") as file:
            file.write(score)


    def refresh_board(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh_board()

    def display_game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.high_score = max(self.score, self.high_score)
        self.save_highscore(f"{self.high_score}")
        self.score = 0
        self.refresh_board()
