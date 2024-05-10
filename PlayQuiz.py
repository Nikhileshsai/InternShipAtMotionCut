import tkinter as tk
from tkinter import messagebox
import json

class QuizApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz App")
        self.window.config(padx=100, pady=100, bg="#40E0D0")
        self.start_frame = tk.Frame(self.window, bg="#40E0D0")
        self.start_frame.pack(expand=True)  
        self.start_button = tk.Button(self.start_frame, text="Start Quiz", font=("Arial", 16), command=self.start_quiz)
        self.start_button.pack(expand=True)
        self.quiz_frame = None
        self.load_questions()
        self.window.mainloop()

    def start_quiz(self):
        self.start_frame.pack_forget()  # Hide the start frame
        self.quiz_frame = tk.Frame(self.window, bg="#40E0D0")
        self.quiz_frame.pack(expand=True)
        self.create_widgets()
        self.display_question()

    def load_questions(self):
        with open("QuizData.json", "r") as f:
            self.questions = json.load(f)
        self.current_question_index = 0
        self.score = 0

    def create_widgets(self):
        self.question_label = tk.Label(self.quiz_frame, text="", font=("Arial", 16), wraplength=500)
        self.question_label.pack(pady=10)
        self.option_buttons = []
        for i in range(3):
            button = tk.Button(self.quiz_frame, text="", font=("Arial", 12), command=lambda opt=i: self.check_answer(opt))
            button.pack(pady=10)
            self.option_buttons.append(button)
        self.next_button = tk.Button(self.quiz_frame, text="Next Question", font=("Arial", 12), command=self.next_question)
        self.next_button.pack(pady=20)
        self.next_button.state = tk.DISABLED
        self.score_label = tk.Label(self.quiz_frame, text="Score:", font=("Arial", 12))
        self.score_label.pack(pady=10)

    def display_question(self):
        question = self.questions[self.current_question_index]
        self.question_label.config(text=question["question"])
        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=option)

        self.next_button.state = tk.NORMAL

    def check_answer(self, option_index):
        selected_option = self.option_buttons[option_index]["text"]
        correct_answer = self.questions[self.current_question_index]["answer"]
        if selected_option == correct_answer:
            self.score += 1
        else:
            # Display feedback with correct answer
            feedback = f"Oops! That's incorrect. The correct answer is: {correct_answer}"
            messagebox.showinfo("Feedback", feedback)
        self.score_label.config(text=f"Score: {self.score}")
        self.next_button.invoke()

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index == len(self.questions):
            self.display_result()
        else:
            self.display_question()
            self.next_button.state = tk.DISABLED

    def display_result(self):
        for button in self.option_buttons:
            button.pack_forget()
        self.question_label.config(text=f"You scored {self.score} out of {len(self.questions)}!")
        self.next_button.config(text="Back To Start", command=self.restart_quiz)
        self.next_button.pack(pady=20)
        for button in self.option_buttons:
            button.state = tk.DISABLED

    def restart_quiz(self):
        self.current_question_index = 0
        self.score = 0
        self.display_question()
        self.next_button.state = tk.DISABLED
        self.score_label.config(text="Score: 0")
        self.quiz_frame.pack_forget()
        self.start_frame.pack()

app = QuizApp()
