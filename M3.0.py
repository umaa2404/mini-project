import turtle
import random
import winsound

# Screen setup
window = turtle.Screen()
window.title("Math Quiz Game")
window.bgcolor("#1e1e2e")
window.setup(width=800, height=600)

# Pen setup
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()

# Level display setup
level_display = turtle.Turtle()
level_display.speed(0)
level_display.color("yellow")
level_display.penup()
level_display.hideturtle()
level_display.goto(300, 260)

# Score display setup
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("cyan")
score_display.penup()
score_display.hideturtle()
score_display.goto(-350, 260)

# Fonts
font_style = ("Arial", 24, "bold")
header_font = ("Arial", 30, "bold")

# Game variables
score = 0
question_num = 0
level = 1  # Start from Level 1 (Easy)

# Function to play correct sound
def play_correct_sound():
    winsound.Beep(1000, 200)

# Function to play wrong sound
def play_wrong_sound():
    winsound.Beep(400, 200)

# Function to display the current question
def display_question(question):
    pen.goto(0, 150)
    pen.clear()
    pen.color("#00ffea")
    pen.write(question, align="center", font=header_font)

# Function to display correct answer message
def display_reward():
    pen.goto(0, -50)
    pen.clear()
    pen.color("green")
    pen.write("Correct!", align="center", font=font_style)
    play_correct_sound()

# Function to display wrong answer message
def display_wrong():
    pen.goto(0, -50)
    pen.clear()
    pen.color("red")
    pen.write("Wrong answer. Try again.", align="center", font=font_style)
    play_wrong_sound()

# Function to generate questions based on the current level
def generate_question():
    global level
    if level == 1:  # Easy
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-"])
    elif level == 2:  # Medium
        num1 = random.randint(20, 50)
        num2 = random.randint(20, 50)
        operator = random.choice(["+", "-", "*"])
    else:  # Hard
        num1 = random.randint(40, 80)
        num2 = random.randint(40, 80)
        operator = random.choice(["+", "-", "*", "/"])

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    else:
        num2 = random.randint(1, 10)
        answer = round(num1 / num2, 2)

    question = f"What is {num1} {operator} {num2}?"
    return question, answer

# Function to check if the user's answer is correct
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

# Function to update the level display
def update_level_display():
    level_display.clear()
    level_display.goto(300, 260)
    level_display.write(f"Level: {level}", align="right", font=("Arial", 24, "bold"))

# Function to update the score display
def update_score_display():
    score_display.clear()
    score_display.write(f"Score: {score}", align="left", font=("Arial", 24, "bold"))

# Function to start the game
def start_game():
    global score, question_num, level
    score = 0
    question_num = 1

    update_level_display()
    update_score_display()

    while question_num <= 10:
        question, correct_answer = generate_question()
        display_question(question)

        user_answer = turtle.numinput("Math Quiz", f"Question {question_num}: Enter your answer:")

        if user_answer is not None:
            user_answer = round(user_answer, 2)

            if check_answer(user_answer, correct_answer):
                score += 1
                display_reward()
                update_score_display()
            else:
                display_wrong()

            turtle.delay(250)
            question_num += 1
        else:
            pen.goto(0, -50)
            pen.clear()
            pen.color("orange")
            pen.write("Enter a valid number!", align="center", font=font_style)
            turtle.delay(250)

    display_level_result()

# Function to display the result of the current level
def display_level_result():
    global level

    pen.goto(0, 0)
    pen.clear()
    pen.color("white")
    pen.write(f"Your score: {score}/10", align="center", font=header_font)

    if score >= 7:
        if level < 3:
            level += 1
            update_level_display()
            pen.goto(0, -50)
            pen.color("green")
            pen.write("Great job! Next level incoming.", align="center", font=font_style)
            window.update()
            turtle.delay(250)
            start_game()

        else:
            pen.goto(0, -50)
            pen.color("gold")
            pen.write("Congratulations! All levels complete!", align="center", font=font_style)

    else:
        pen.goto(0, -50)
        pen.color("red")
        pen.write("Failed! Click anywhere to retry.", align="center", font=font_style)
        window.onclick(start_quiz)

# Function to start quiz on mouse click
def start_quiz(x, y):
    window.onclick(None)
    pen.clear()
    update_level_display()
    start_game()

# Introduction screen
def display_intro():
    pen.goto(0, 100)
    pen.clear()
    pen.color("cyan")
    pen.write("Welcome to the Math Quiz!", align="center", font=header_font)

    pen.goto(0, 50)
    pen.color("lightblue")
    pen.write("Prove your math skills and rise to champion status!", align="center", font=font_style)

    pen.goto(0, -50)
    pen.color("yellow")
    pen.write("Click anywhere to start!", align="center", font=font_style)

# Set up the game window
display_intro()
window.onclick(start_quiz)

# Keep the window open
turtle.mainloop()
