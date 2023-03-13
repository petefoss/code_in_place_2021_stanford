import tkinter as tk
import random
import time
import PIL
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox

# Constants
CANVAS_WIDTH =800
CANVAS_HEIGHT = 550
CORRECT_PHRASES = ["YAY, well done!", "Woo Hoo!", "Go for it!", "You're doing well!", "Amazing!"]
WRONG_PHRASES = ["Not Quite", "Keep trying", "Almost there", "Nearly"]
NUM_OF_PAIRS = 4

# color palette
BG_COL = "#4B4453"
CARD_COL = "#C34A36"
# spare1 = "#FF8066"
# spare2 = "#B0A8B9"
# spare3 = "#845EC2"


def main():
    global canvas, card_back, result_label, ans_list, b_list, im_list
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'PAIRS MEMORY GAME', BG_COL)
    
    # Load all the amages
    card_back = ImageTk.PhotoImage(Image.open("images/stanford_s_logo.png"))

    im_bird = ImageTk.PhotoImage(Image.open("images/im_bird.png"))
    im_elephant = ImageTk.PhotoImage(Image.open("images/im_elephant.png"))
    im_chicken = ImageTk.PhotoImage(Image.open("images/im_chicken.png"))
    im_cow = ImageTk.PhotoImage(Image.open("images/im_cow.png"))
    im_deer = ImageTk.PhotoImage(Image.open("images/im_deer.png"))
    im_lion = ImageTk.PhotoImage(Image.open("images/im_lion.png"))
    im_racoon = ImageTk.PhotoImage(Image.open("images/im_racoon.png"))
    im_squirrel = ImageTk.PhotoImage(Image.open("images/im_squirrel.png"))

    # Put animal images in a list
    im_list = [im_lion, im_bird, im_elephant, im_cow, im_chicken, im_deer, im_racoon, im_squirrel]
    
    # random.shuffle(ans_list)

    # Make buttons
    b0 = tk.Button(canvas, bg=CARD_COL, image=card_back, width=166, height=230, command=lambda:card_click(b0, 0), relief="groove")
    b1 = tk.Button(canvas, bg=CARD_COL, image=card_back, width=166, height=230, command=lambda:card_click(b1, 1), relief="groove")
    b2 = tk.Button(canvas, bg=CARD_COL, image=card_back, width=166, height=230, command=lambda:card_click(b2, 2), relief="groove")
    b3 = tk.Button(canvas, bg=CARD_COL, image=card_back, width=166, height=230, command=lambda:card_click(b3, 3), relief="groove")
    b4 = tk.Button(canvas, bg=CARD_COL, image=card_back, width=166, height=230, command=lambda:card_click(b4, 4), relief="groove")
    b5 = tk.Button(canvas, bg=CARD_COL, image=card_back, width=166, height=230, command=lambda:card_click(b5, 5), relief="groove")
    b6 = tk.Button(canvas, bg=CARD_COL, image=card_back, width=166, height=230, command=lambda:card_click(b6, 6), relief="groove")
    b7 = tk.Button(canvas, bg=CARD_COL, image=card_back, width=166, height=230, command=lambda:card_click(b7, 7), relief="groove")
    
    # Position buttons in grid - 2 rows of 4 columns
    b0.grid(row=0, column=0, padx=10, pady=10)
    b1.grid(row=0, column=1, padx=10, pady=10)
    b2.grid(row=0, column=2, padx=10, pady=10)
    b3.grid(row=0, column=3, padx=10, pady=10)

    b4.grid(row=1, column=0, padx=10, pady=10)
    b5.grid(row=1, column=1, padx=10, pady=10)
    b6.grid(row=1, column=2, padx=10, pady=10)
    b7.grid(row=1, column=3, padx=10, pady=10)
    # Create a list of buttons - to be used when resetting
    b_list = [b0, b1, b2, b3, b4, b5, b6, b7]
    
    # Make Label for text and position in center under cards
    result_label = tk.Label(canvas, text = "Click 2 cards", font=("Helvetica", 20))
    result_label.grid(row=2, column=0, columnspan = 4, pady=10)

    start_game()

    #creates keyboard event that focuses the use of the keyboard to the canvas window
    canvas.focus_force()  # Canvas now has the keyboard focus
    canvas.bind("<Key>", easter_egg)
        

    canvas.mainloop()

def start_game():
    global ans_list, count, game_end, start, card_back
    # Make list of (4) random images and multiply to make pairs
    ans_list = (random.sample(im_list, NUM_OF_PAIRS))*2
    # Make ans_list random
    random.shuffle(ans_list)
    # Reset all counters to 0
    count = 0
    game_end = 0
    # Reset all the buttons back to starting state
    for button in b_list:
        button["image"] = card_back
        button["state"] = "normal"

    # Creates messagebox popup to start the game and the timer
    msg_box = messagebox.askquestion("PAIRS MEMORY GAME", "Do you want to play a game?")
    if msg_box == 'yes':
        start = time.time()
    else:
        top.destroy()

def card_click(b_num, cell_num):
    global count, ans_list, canvas, card_back, fst_click, scnd_click
    if count == 0: 
        # add 1 to counter
        count +=1
        fst_click = b_num
        b_num["image"] = ans_list[cell_num]
    if count == 1 and b_num!= fst_click:
        # add 1 to counter
        count +=1
        scnd_click = b_num
        b_num["image"] = ans_list[cell_num]
        canvas.after(500, check_same)
        # add 1 to counter

def check_same():
    global count, ans_list, game_end, top, start, fst_click, scnd_click 
    if fst_click["image"] != scnd_click["image"]:
        count = 0
        fst_click["image"] = card_back  
        scnd_click["image"] = card_back  
        result_label["text"] = random.choice(WRONG_PHRASES)
        
    else:
        fst_click["state"] = "disabled"
        scnd_click["state"] = "disabled"
        count = 0
        result_label["text"] = random.choice(CORRECT_PHRASES)
        game_end += 1
    
    if game_end == NUM_OF_PAIRS:
        msg_box = messagebox.askquestion("PAIRS MEMORY GAME", "Yay, you win, it took you " + str(int(time.time() - start)) + " seconds!    Do you want to play again?") 
        if msg_box == 'yes':
            start_game()
        else:
            top.destroy()

# Cheat Mode - function sets all the cards to a certain order
def easter_egg(event):
    global ans_list
    ans_list = []
    for i in range(4):
        ans_list.append(im_list[0])     # change the im_list value to i or 0 for diffeerent set results
    ans_list *=2


def make_canvas(width, height, title=None, col=None):
    
    # Creates and returns a canvas of the given int size with a blue border,
    
    objects = {}
    global top
    top = tk.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tk.Canvas(top, width=width + 1, height=height + 1, highlightthickness=0)
    if col:
        top.configure(background=col)
        canvas.configure(background=col)
    
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas




if __name__ == '__main__':
    main()
