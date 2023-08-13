from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    
    # Make a new window variable, window = Tk()
    window = Tk()

    
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    
    # 1. Create a variable to hold the user's score. Set it equal to zero.
    score = 0

    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question
    question = simpledialog.askstring(title='question', prompt="What is 4x4")

    #      // 3.  Use an if statement to check if their answer is correct
    if question == "16":
        score = score + 1
        messagebox.showinfo(title='question', message="correct!")


    #      // 4.  if the user's answer was correct, add one to their score
    question = simpledialog.askstring(title='question', prompt="What is 2x9")
    if question == "18":
        score = score + 1
        messagebox.showinfo(title='question', message="correct!")
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    question = simpledialog.askstring(title='question', prompt="What is 9x9")
    if question == "81":
        score = score + 1
        messagebox.showinfo(title='question', message="correct!")
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function
    messagebox.showinfo(title='final score',message="your final score is "+str(score))
    
    # Run the window's .mainloop() method
    window.mainloop()
