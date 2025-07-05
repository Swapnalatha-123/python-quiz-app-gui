import tkinter
from tkinter import messagebox

# Window
root = tkinter.Tk()
root.title("QUIZ")
root.geometry('900x700')

c = 0  # Score Counter

# Title Label
label_t = tkinter.Label(root, text="QUIZ", font=("Arial", 50))
label_t.place(x=300, y=50)

# Username Label and Entry
label_u = tkinter.Label(root, text="Username", font=("Arial", 30))
label_u.place(x=250, y=250)
entry = tkinter.Entry(root, font=("Arial", 30))
entry.place(x=500, y=250)

# Function to clear screen before each question
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# Function to check answer and update score
def check_answer(is_correct, next_question):
    global c
    if is_correct:
        messagebox.showinfo("Correct!", "Your answer is correct!")
        c += 1  # Increase score
    else:
        messagebox.showerror("Wrong!", "Your answer is incorrect.")

    next_question()  # Move to next question

# Question 1
def info1():
    clear_screen()
    label_q1 = tkinter.Label(root, text="Question 1", font=("Arial", 35))
    label_q1.place(x=250, y=50)
    
    label1 = tkinter.Label(root, text="Which of these is a keyword in Python?", font=("Arial", 30))
    label1.place(x=150, y=100)

    tkinter.Button(root, text="A. range", font=("Arial", 20), command=lambda: check_answer(False, info2)).place(x=400, y=200)
    tkinter.Button(root, text="B. def", font=("Arial", 20), command=lambda: check_answer(True, info2)).place(x=800, y=200)
    tkinter.Button(root, text="C. Val", font=("Arial", 20), command=lambda: check_answer(False, info2)).place(x=400, y=300)
    tkinter.Button(root, text="D. to", font=("Arial", 20), command=lambda: check_answer(False, info2)).place(x=800, y=300)

# Question 2
def info2():
    clear_screen()
    label_q2 = tkinter.Label(root, text="Question 2", font=("Arial", 35))
    label_q2.place(x=250, y=50)
    
    label2 = tkinter.Label(root, text="Which of the following is a built-in function in Python?", font=("Arial", 30))
    label2.place(x=100, y=100)

    tkinter.Button(root, text="A. factorial", font=("Arial", 20), command=lambda: check_answer(False, info3)).place(x=400, y=200)
    tkinter.Button(root, text="B. print", font=("Arial", 20), command=lambda: check_answer(True, info3)).place(x=800, y=200)
    tkinter.Button(root, text="C. seed", font=("Arial", 20), command=lambda: check_answer(False, info3)).place(x=400, y=300)
    tkinter.Button(root, text="D. sqrt", font=("Arial", 20), command=lambda: check_answer(False, info3)).place(x=800, y=300)

# Question 3
def info3():
    clear_screen()
    label_q3 = tkinter.Label(root, text="Question 3", font=("Arial", 35))
    label_q3.place(x=250, y=50)
    
    label3 = tkinter.Label(root, text="Which of these is not a core data type in Python?", font=("Arial", 30))
    label3.place(x=100, y=100)

    tkinter.Button(root, text="A. Tuple", font=("Arial", 20), command=lambda: check_answer(False, info4)).place(x=400, y=200)
    tkinter.Button(root, text="B. Dictionary", font=("Arial", 20), command=lambda: check_answer(False, info4)).place(x=800, y=200)
    tkinter.Button(root, text="C. Lists", font=("Arial", 20), command=lambda: check_answer(False, info4)).place(x=400, y=300)
    tkinter.Button(root, text="D. Class", font=("Arial", 20), command=lambda: check_answer(True, info4)).place(x=800, y=300)

# Question 4
def info4():
    clear_screen()
    label_q4 = tkinter.Label(root, text="Question 4", font=("Arial", 35))
    label_q4.place(x=250, y=50)
    
    label4 = tkinter.Label(root, text="Who developed Python programming language?", font=("Arial", 30))
    label4.place(x=100, y=100)

    tkinter.Button(root, text="A. Wick Van Rossum", font=("Arial", 20), command=lambda: check_answer(False, info5)).place(x=400, y=200)
    tkinter.Button(root, text="B. Rasmus Lerdorf", font=("Arial", 20), command=lambda: check_answer(False, info5)).place(x=800, y=200)
    tkinter.Button(root, text="C. Guido Van Rossum", font=("Arial", 20), command=lambda: check_answer(True, info5)).place(x=400, y=300)
    tkinter.Button(root, text="D. Niene Stom", font=("Arial", 20), command=lambda: check_answer(False, info5)).place(x=800, y=300)

# Final Score Display
def info5():
    clear_screen()
    global c
    label_q6 = tkinter.Label(root, text="QUIZ COMPLETED!", font=("Arial", 40))
    label_q6.place(x=250, y=50)

    label_score = tkinter.Label(root, text=f"Your Score: {c}/4", font=("Arial", 35))
    label_score.place(x=250, y=200)

    # Show result using a Label instead of messagebox
    if c >= 4:
        result_text = "Excellent! 🎉"
    elif c >= 2:
        result_text = "Good Job! 😊"
    else:
        result_text = "Better Luck Next Time! 😢"

    label_result = tkinter.Label(root, text=result_text, font=("Arial", 30), fg="blue")
    label_result.place(x=250, y=300)

# Start Button
button = tkinter.Button(root, text="START QUIZ", font=("Arial", 30), command=info1)
button.place(x=500, y=350)

# Run Application
root.mainloop()
