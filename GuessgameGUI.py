import random
import tkinter as tk

# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("🎮 Number Guessing Game")
root.geometry("400x300")

# Global Variables
number = 0
attempts = 0


# ---------------- START WINDOW ---------------- #

def start_game():
    root.withdraw()  # Hide main window
    difficulty_window()


start_label = tk.Label(
    root,
    text="🎮 Number Guessing Game",
    font=("Arial", 20)
)
start_label.pack(pady=40)

start_button = tk.Button(
    root,
    text="Start Game 🚀",
    font=("Arial", 14),
    command=start_game
)
start_button.pack()


# ---------------- DIFFICULTY WINDOW ---------------- #

def difficulty_window():

    df = tk.Toplevel()

    df.title("Select Difficulty")
    df.geometry("400x300")

    label = tk.Label(
        df,
        text="Select Difficulty",
        font=("Arial", 18)
    )
    label.pack(pady=20)

    # Difficulty Function
    def set_difficulty(max_num):

        global number

        number = random.randint(1, max_num)

        df.destroy()
        game_window()

    # Easy Button
    easy = tk.Button(
        df,
        text="Easy (1 - 100)",
        width=20,
        font=("Arial", 12),
        command=lambda: set_difficulty(100)
    )
    easy.pack(pady=10)

    # Medium Button
    medium = tk.Button(
        df,
        text="Medium (1 - 500)",
        width=20,
        font=("Arial", 12),
        command=lambda: set_difficulty(500)
    )
    medium.pack(pady=10)

    # Hard Button
    hard = tk.Button(
        df,
        text="Hard (1 - 1000)",
        width=20,
        font=("Arial", 12),
        command=lambda: set_difficulty(1000)
    )
    hard.pack(pady=10)


# ---------------- GAME WINDOW ---------------- #

def game_window():

    game = tk.Toplevel()

    game.title("Game Window")
    game.geometry("400x350")

    global attempts
    attempts = 0

    # Title
    title = tk.Label(
        game,
        text="🎯 Guess The Number",
        font=("Arial", 18)
    )
    title.pack(pady=10)

    # Entry Box
    entry = tk.Entry(
        game,
        font=("Arial", 14)
    )
    entry.pack(pady=10)

    # Result Label
    result = tk.Label(
        game,
        text="",
        font=("Arial", 14)
    )
    result.pack(pady=10)

    # Hint Label
    hint = tk.Label(
        game,
        text="",
        font=("Arial", 12)
    )
    hint.pack(pady=10)

    # Attempts Label
    attempt_label = tk.Label(
        game,
        text="Attempts: 0",
        font=("Arial", 12)
    )
    attempt_label.pack(pady=10)

    # ---------------- CHECK GUESS FUNCTION ---------------- #

    def check_guess():

        global attempts

        try:
            guess = int(entry.get())

            attempts += 1

            attempt_label.config(
                text=f"Attempts: {attempts}"
            )

            distance = abs(number - guess)

            if guess < number:

                result.config(
                    text="📈 Number is Higher!"
                )

            elif guess > number:

                result.config(
                    text="📉 Number is Lower!"
                )

            else:

                result.config(
                    text=f"🎉 Correct! You Won!"
                )

                hint.config(
                    text=f"🏆 Total Attempts: {attempts}"
                )

                return

            # ---------------- HINTS ---------------- #

            if distance <= 10:

                hint.config(
                    text="🔥 Very Very Close!"
                )

            elif distance <= 30:

                hint.config(
                    text="🙂 Close!"
                )

            elif distance <= 50:

                hint.config(
                    text="😐 Far!"
                )

            else:

                hint.config(
                    text="🥶 Too Far Away!"
                )

        except ValueError:

            result.config(
                text="❌ Enter Numbers Only!"
            )

    # ---------------- BUTTON ---------------- #

    button = tk.Button(
        game,
        text="Check Guess",
        font=("Arial", 12),
        command=check_guess
    )
    button.pack(pady=10)


# ---------------- RUN APP ---------------- #

root.mainloop()