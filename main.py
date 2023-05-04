import turtle
from random import randint

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Cath The Turtle")

#turtle
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.penup()

#counter
turtle_counter = turtle.Turtle(visible=False)
turtle_counter.penup()
turtle_counter.goto(-20, 280)

#score
turtle_score = turtle.Turtle(visible=False)
turtle_score.color("blue")
turtle_score.penup()
turtle_score.goto(-20, 240)

#text font
font = ("Arial", 20, "bold")

#difficulty
difficulty = "easy"
difficultyStage = {"easy": 20, "medium": 10, "hard": 5}

time = 10
score = 0


def countdown():
    global time
    time -= 1
    turtle_counter.clear()
    turtle_counter.write("Time: " + str(time), align="center", font=font)
    turtle_score.write("Score: " + str(score), align="center", font=font)

    if time > 0:
        turtle.ontimer(countdown, 1000)
    else:
        turtle_counter.clear()
        turtle_counter.write("Game Over!", align="center", font=font)


def gotoRandom(turtleInstance):
    turtleInstance.goto(randint(-150, 0), randint(0, 150))
    return turtleInstance.pos()


def catchTurtle(x, y):
    global turtleCoor
    global score
    global time

    if time > 0:
        for i in range(difficultyStage[difficulty]):
            for j in range(difficultyStage[difficulty]):
                if (x + i, y + j) == turtleCoor or (x - i, y + j) == turtleCoor or (x - i, y - j) == turtleCoor or (
                        x + i, y - j) == turtleCoor:
                    print((x, y), turtleCoor, "catched")
                    turtleCoor = gotoRandom(turtle_instance)
                    getScore()


def getScore():
    global score
    score += 1
    turtle_score.clear()
    turtle_score.write("Score: " + str(score), align="center", font=font)


turtleCoor = gotoRandom(turtle_instance)
countdown()

turtle.onscreenclick(catchTurtle)

turtle.mainloop()
