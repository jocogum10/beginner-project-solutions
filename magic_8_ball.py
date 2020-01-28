"""
Magic 8 Ball
- Simulate a magic 8-ball.
- Allow the user to enter their question.
- Display an in progress message(i.e. "thinking").
- Create 20 responses, and show a random response.
- Allow the user to ask another question or quit.
- Bonus:
  - Add a gui.
  - It must have box for users to enter the question.
  - It must have at least 4 buttons:
    - ask
    - clear (the text box)
    - play again
    - quit (this must close the window)
"""
import random, tkinter, time

answers = ['It is certain.', 
           'It is decidedly so.',
           'Without a doubt.',
           'Yes - definitely.',
           'You may rely on it.',
           'As I see it, yes.',
           'Most likely.',
           'Outlook good.',
           'Yes.',
           'Signs point to yes.',
           'Reply hazy, try again.',
           'Ask again later.',
           'Better not tell you now.',
           'Cannot predict now.',
           'Concentrate and ask again.',
           "Don't count on it.",
           'My reply is no.',
           'My sources say no.',
           'Outlook not so good.',
           'Very doubtful.',]

def magic_8_ball(ask):
    global answer, question, button1
    i = random.randrange(20)
    if '?' in ask:
        answer.delete("1.0", "end")
        answer.insert("end", "thinking...")
        answer.update()
        time.sleep(random.randrange(5))
        answer.delete("1.0", "end")
        answer.insert("end", answers[i])
        answer.see("end")
        answer.update()
        button1.config(state="disabled")
    else:
        answer.delete("1.0", "end")
        answer.insert("end", "Ask a question. Put a '?'.")
        answer.see("end")
        answer.update()
        
def clear():
    global answer
    answer.delete("1.0", "end")
    answer.update()

def play_again():
    global question
    question.delete(0, "end")
    question.insert(0, "Ask again... ")
    question.focus()
    button1.config(state="normal")
    
if __name__ == '__main__':
    
    root = tkinter.Tk()
    root.title("Magic 8 ball")
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    
    answer = tkinter.Text(root, height=5, width=30)
    answer.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    
    question = tkinter.Entry(root, width=30)
    question.insert(0, "Type your question here.. ")
    question.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    question.focus()
    
    button1 = tkinter.Button(root, text="magic 8 ball", bg="grey",command=(lambda: magic_8_ball(question.get())))
    button1.grid(row=1,columnspan=2, sticky="ew", padx=10, pady=10)
    button2 = tkinter.Button(root, text="play again", bg="grey",command=(lambda: play_again()))
    button2.grid(row=2,columnspan=2, sticky="ew", padx=10, pady=10)
    button3 = tkinter.Button(root, text="clear", bg="grey",command=(lambda: clear()))
    button3.grid(row=3,columnspan=2, sticky="ew", padx=10, pady=10)
    button4 = tkinter.Button(root, text="quit", bg="grey",command=(lambda: root.destroy()))
    button4.grid(row=4,columnspan=2, sticky="ew", padx=10, pady=10)
    
    
    root.mainloop()
    
    