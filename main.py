from tkinter import *

import pandas

from tester import processsed_list

with open("data/words_to_learn.csv", "w") as unlearned:
    unlearned.write("")

bg = "#B1DDC6"
window = Tk()
window.title("Learn French with tkinter")
window.config(background="#B1DDC6")
canvas = Canvas(width=800,height=526, background=bg, highlightthickness=0)
back = PhotoImage(file="card_back.png")
front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
canvas.grid(column=0, row=0, columnspan=2)
rbutton = Button(width=200, height=100, image=right, background=bg, highlightthickness=0)
wbutton = Button(width=200, height=100, image=wrong, background=bg, highlightthickness=0)
rbutton.grid(column=0, row=1)
wbutton.grid(column=1, row=1)
word_index = 0
active_card = None
active_text = None
language = None
timer = None

french_words = []
english_words = []
n = 0
for french in processsed_list:
    french_words += french
for fr in french_words:
    english_words.append(processsed_list[n][fr])
    n += 1
n = 0

def turn_back(en):
    global canvas
    global active_card
    global active_text
    global language
    global timer
    global word_index
    active_card = canvas.create_image(800/2, 526/2, image=back)
    active_text = canvas.create_text(400, 526/2, text=en, font=("italic", 40, "bold"))
    language = canvas.create_text(400, 200, text="English", font=("courier", 20, "bold"))
    canvas.after_cancel(timer)
    word_index += 1

def createimg():
    global timer
    global language
    global canvas
    global active_card
    global active_text
    global word_index
    active_card = canvas.create_image(800/2, 526/2, image=front)
    active_text = canvas.create_text(400, 526/2, text=str(french_words[word_index]), font=("italic", 40, "bold"))
    language = canvas.create_text(400, 200, text="French", font=("courier", 20, "bold"))
    timer = canvas.after(4000, turn_back, english_words[word_index])

    if word_index != 0:
        with open("data/words_to_learn.csv", "a") as unlearned:
            unlearned.write(f"french: {french_words[word_index]} - english: {english_words[word_index]}\n")

def reset_timer():
    global timer
    global canvas
    canvas.after_cancel(timer)
    createimg(french)

window.config(pady=70, padx=70)
word_index = 0
active_card = canvas.create_image(800/2, 526/2, image=front)
active_text = canvas.create_text(400, (526/2)-100, text="LEARN FRENCH", font=("italic", 40, "bold"))
active_text_instructions = canvas.create_text(400, (526/2) + 80, text="A french word will appear,\nand you will have 4 seconds to translate it to english before the correct answer pops up.", font=("mono", 12, "bold"), justify=['center'])
active_subtext = canvas.create_text(400, (526/2)+150, text="\nClick on the green button if you get the word right.\nClick on the red button when if you get the word wrong.\nYou can review failures for later studies", font=("italic", 10, "bold"), justify=['center'])
rbutton.config(command=createimg)
wbutton.config(command=createimg)

window.mainloop()