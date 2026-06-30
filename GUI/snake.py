import tkinter as tk
import random

# ------------------- CONFIG -------------------
WIDTH = 600
HEIGHT = 600
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#111111"
SPEED = 120

# ------------------- SNAKE -------------------
class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y,
                x + SPACE_SIZE,
                y + SPACE_SIZE,
                fill=SNAKE_COLOR,
                outline="black"
            )

            self.squares.append(square)


# ------------------- FOOD -------------------
class Food:

    def __init__(self):

        x = random.randint(0, (WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(
            x, y,
            x + SPACE_SIZE,
            y + SPACE_SIZE,
            fill=FOOD_COLOR,
            tags="food"
        )


# ------------------- GAME -------------------
def next_turn(snake, food):
    global score

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(
        x, y,
        x + SPACE_SIZE,
        y + SPACE_SIZE,
        fill=SNAKE_COLOR,
        outline="black"
    )

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        score += 10
        label.config(text=f"Score : {score}")

        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


# ------------------- DIRECTION -------------------
def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction

    elif new_direction == "right":
        if direction != "left":
            direction = new_direction

    elif new_direction == "up":
        if direction != "down":
            direction = new_direction

    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


# ------------------- COLLISION -------------------
def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= WIDTH:
        return True

    if y < 0 or y >= HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


# ------------------- GAME OVER -------------------
def game_over():

    canvas.delete(tk.ALL)

    canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2 - 30,
        text="GAME OVER",
        fill="red",
        font=("Arial", 35, "bold")
    )

    canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2 + 20,
        text=f"Final Score : {score}",
        fill="white",
        font=("Arial", 20)
    )

    restart_btn = tk.Button(
        window,
        text="Restart",
        font=("Arial", 14, "bold"),
        bg="#00AAFF",
        fg="white",
        command=restart_game
    )

    canvas.create_window(WIDTH / 2, HEIGHT / 2 + 80, window=restart_btn)


# ------------------- RESTART -------------------
def restart_game():
    global score, direction

    score = 0
    direction = "down"

    label.config(text="Score : 0")

    canvas.delete(tk.ALL)

    snake = Snake()
    food = Food()

    next_turn(snake, food)


# ------------------- WINDOW -------------------
window = tk.Tk()
window.title("🐍 Snake Game")
window.resizable(False, False)
window.configure(bg="#222222")

score = 0
direction = "down"

label = tk.Label(
    window,
    text="Score : 0",
    font=("Consolas", 20, "bold"),
    bg="#222222",
    fg="#00FF00"
)

label.pack()

canvas = tk.Canvas(
    window,
    bg=BACKGROUND_COLOR,
    height=HEIGHT,
    width=WIDTH,
    highlightthickness=0
)

canvas.pack()

window.update()

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()