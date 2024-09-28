from tkinter import *

# Define question dictionary with new GK questions
question = {
    "Who is known as the Father of the Nation in India?": ["Mahatma Gandhi", "Jawaharlal Nehru", "B. R. Ambedkar", "Sardar Vallabhbhai Patel"],
    "What is the capital of France?": ["Berlin", "Madrid", "Paris", "Lisbon"],
    "Which planet is known as the Red Planet?": ["Earth", "Venus", "Mars", "Jupiter"],
    "Who wrote the national anthem of India?": ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Lata Mangeshkar"],
    "Which is the largest ocean on Earth?": ["Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean"],
}

# Define answer list for the new questions
ans = ["Mahatma Gandhi", "Paris", "Mars", "Rabindranath Tagore", "Pacific Ocean"]

current_question = 0
time_left = 20  # Set timer to 20 seconds for each question

def start_quiz():
    start_button.forget()  # Hide the start button
    next_question()  # Display the first question

def next_question():
    global current_question, time_left
    # Check answer before moving to the next question, except for timeouts
    if time_left > 0:  # Only check the answer if time hasn't run out
        check_ans()  # Check answer if time hasn't expired
    user_ans.set('None')  # Reset the answer

    if current_question < len(question):
        c_question = list(question.keys())[current_question]
        clear_frame()

        # Display the current question
        Label(f1, text=f"Question : {c_question}", padx=15, font="calibre 14 bold", bg="#F7F7F7").pack(anchor=NW, pady=10)

        # Display answer options
        for option in question[c_question]:
            Radiobutton(f1, text=option, variable=user_ans,
                        value=option, padx=28, bg="#E0E0E0", font="calibre 12")\
            .pack(anchor=NW, pady=5)

        current_question += 1
        next_button.pack(pady=10)  # Show the "Next Question" button after displaying the question

        # Reset the timer to 20 seconds and update the timer label
        reset_timer()
    else:
        # Hide the next button when the quiz is finished
        next_button.forget()
        check_ans()  # Check answer for the last question
        clear_frame()
        output = f"Your Score is {user_score.get()} out of {len(question)}"
        Label(f1, text=output, font="calibre 20 bold", bg="#F7F7F7").pack(pady=10)
        Label(f1, text="Thanks for Participating", font="calibre 18 bold", bg="#F7F7F7").pack(pady=5)
        timer_label.pack_forget()  # Hide the timer label on the result sheet

def reset_timer():
    global time_left
    time_left = 20
    timer_label.config(text=f"Time left: {time_left} seconds")
    update_timer()

def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None' and temp_ans == ans[current_question-1]:
        user_score.set(user_score.get() + 1)

def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()

# Timer function
def update_timer():
    global time_left
    if time_left > 0:
        timer_label.config(text=f"Time left: {time_left} seconds")
        time_left -= 1
        root.after(1000, update_timer)  # Call this function every 1 second
    else:
        time_out()  # Call time out function if time runs out

def time_out():
    global current_question
    # Disable the radio buttons to prevent input
    user_ans.set('None')  # Reset the answer
    timer_label.config(text="Time Out!")  # Show time out message
    # Do not show any error message, just allow the user to proceed
    for widget in f1.winfo_children():
        if isinstance(widget, Radiobutton):
            widget.config(state=DISABLED)  # Disable the answer options
    root.after(2000, next_question)  # Automatically move to the next question after 2 seconds

if __name__ == "__main__":
    root = Tk()
    # Setup basic window
    root.title("GK Quiz App")
    root.geometry("850x520")
    root.minsize(800, 400)
    root.configure(bg="#D9E4F5")  # Soft blue background color

    user_ans = StringVar()
    user_ans.set('None')
    user_score = IntVar()
    user_score.set(0)

    Label(root, text="Quiz App", font="calibre 40 bold", bg="#D9E4F5", fg="#3B3B3B", padx=10, pady=10).pack()
    Label(root, text="", font="calibre 10 bold", bg="#D9E4F5").pack()

    start_button = Button(root, 
                          text="Start Quiz",
                          command=start_quiz, 
                          font="calibre 17 bold", bg="#4CAF50", fg="white", padx=10, pady=5)
    start_button.pack(pady=20)

    f1 = Frame(root, bg="#F7F7F7")  # Light background for question area
    f1.pack(side=TOP, fill=X, padx=20, pady=20)  # Adding padding around the frame

    timer_label = Label(root, text="", font="calibre 14 bold", bg="#D9E4F5")  # Timer label
    timer_label.pack(pady=5)

    next_button = Button(root, text="Next Question",
                         command=next_question, 
                         font="calibre 17 bold", bg="#2196F3", fg="white", padx=10, pady=5)
    
    next_button.pack_forget()  # Initially hide the next button

    # Adding hover effect for buttons
    start_button.bind("<Enter>", lambda e: start_button.config(bg="#45a049"))  # Darker green on hover
    start_button.bind("<Leave>", lambda e: start_button.config(bg="#4CAF50"))  # Original green

    next_button.bind("<Enter>", lambda e: next_button.config(bg="#1E88E5"))  # Darker blue on hover
    next_button.bind("<Leave>", lambda e: next_button.config(bg="#2196F3"))  # Original blue

    root.mainloop()
