import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Choices and their winning pairs
choices = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
user_score, computer_score = 0, 0

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(list(choices.keys()))
    
    # Determine the winner
    if user_choice == computer_choice:
        result_text.set("It's a Tie!")
    elif choices[user_choice] == computer_choice:
        result_text.set("You Win!")
        user_score += 1
    else:
        result_text.set("You Lose!")
        computer_score += 1
    
    user_choice_label.config(text=f"You: {user_choice}")
    computer_choice_label.config(text=f"Computer: {computer_choice}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score, computer_score = 0, 0
    result_text.set("Let's Play!")
    score_label.config(text="Score - You: 0 | Computer: 0")
    user_choice_label.config(text="You: ")
    computer_choice_label.config(text="Computer: ")

def exit_game():
    if messagebox.askyesno("Exit", "Are you sure you want to quit?"):
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("600x500")
root.configure(bg="#d1f7ff")

# Title
tk.Label(root, text="Rock Paper Scissors", font=("Comic Sans MS", 22, "bold"), bg="#d1f7ff", fg="#333").pack(pady=10)

# Result Label
result_text = tk.StringVar(value="Let's Play!")
tk.Label(root, textvariable=result_text, font=("Comic Sans MS", 18, "bold"), bg="#d1f7ff", fg="#ff5733").pack(pady=10)

# Choices Frame
frame = tk.Frame(root, bg="#d1f7ff")
frame.pack()

# Load images
images = {}
for choice in ["Rock", "Paper", "Scissors"]:
    img = Image.open(f"{choice.lower()}.png").resize((90, 90))
    images[choice] = ImageTk.PhotoImage(img)
    tk.Button(frame, image=images[choice], command=lambda c=choice: play_game(c), 
              bg="#ffffff", bd=5, relief="solid", activebackground="#ffcccb").pack(side=tk.LEFT, padx=20, pady=10)

# Choice Labels
user_choice_label = tk.Label(root, text="You: ", font=("Comic Sans MS", 14, "bold"), bg="#d1f7ff", fg="#333")
user_choice_label.pack()
computer_choice_label = tk.Label(root, text="Computer: ", font=("Comic Sans MS", 14, "bold"), bg="#d1f7ff", fg="#333")
computer_choice_label.pack()

# Score Label
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Comic Sans MS", 14, "bold"), bg="#d1f7ff", fg="#007acc")
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#d1f7ff")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Reset", command=reset_game, font=("Comic Sans MS", 12, "bold"), 
          bg="#ffdd57", fg="#333", width=12, height=2, bd=3, relief="solid", activebackground="#ffee77").pack(side=tk.LEFT, padx=20)
tk.Button(button_frame, text="Exit", command=exit_game, font=("Comic Sans MS", 12, "bold"), 
          bg="#ff4d4d", fg="#fff", width=12, height=2, bd=3, relief="solid", activebackground="#ff6666").pack(side=tk.RIGHT, padx=20)

# Run the app
root.mainloop()
