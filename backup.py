from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Tic Tac Toe")
root.configure(background="#82D5A5")

def login():
    global label1, label2, label3, entry1, entry2, button, player1, player2, player, players
    player1 = entry1.get()
    player2 = entry2.get()
    if player1 == "" and player2 == "":
        messagebox.showerror("names", "Please enter player names!")
    else:
        messagebox.showinfo("Login", "Login successful")
        player = player1
        players = [player1, player2]
        label1.destroy()
        label2.destroy()
        label3.destroy()
        entry1.destroy()
        entry2.destroy()
        button.destroy()
        #show 2nd page
        create_widgets()      

# labels mai user interaction include nahi hota widgets mai hota hai        

label1 = Label(
    root, 
    text="Tic Tac Toe Game", 
    font=("Comic Sans MS", 30), 
    background="white", 
    fg="black"
)
label1.place(x=500, y=20)    

label2 = Label(
    root, 
    text="Player1: ", 
    font=("Comic Sans MS", 20), 
    background="white", 
    fg="black"
)
label2.place(x=400, y=190)

label3 = Label(
    root, 
    text="Player2: ", 
    font=("Comic Sans MS", 20), 
    background="white", 
    fg="black"
)
label3.place(x=400, y=340)

entry1 = Entry(
    root, 
    font=("Comic Sans MS", 20), 
    background="white", 
    fg="black"
)
entry1.place(x=600, y=200)

entry2 = Entry(
    root, 
    font=("Comic Sans MS", 20), 
    background="white", 
    fg="black",
)
entry2.place(x=600, y=350)

button = Button(
    root, 
    text="Login", 
    font=("Comic Sans MS", 20), 
    background="white", 
    fg="black",
    command=login
)
button.place(x=550, y=500)

# making 2nd page
def create_widgets():
    create_label_frame()
    create_button_frame()
    create_topic_label()
    create_player_label()
    create_reset_button()
    create_buttons()


# making things used in 2nd page
    
def create_label_frame():
    global frame
    frame = Frame(
        root,
        background="#82D5A5",
        )
    frame.pack(padx=10, pady=10)

def create_button_frame():
    global button_frame
    button_frame = Frame(
        root,
        background="#82D5A5",
        )
    button_frame.pack(padx=10, pady=10)

def create_topic_label():
    global frame, topic_Label
    topic_Label = Label(
            frame, 
            text="Welcome to Tic Tac Toe", 
            font=("Arial", 20), 
            background="white", 
            fg="black"
            )
    topic_Label.pack(pady=10)

def create_player_label():
    global frame, player, players, player_Label
    player_Label = Label(
            frame, 
            text="Player: " + player, 
            font=("Arial", 20), 
            background="white", 
            fg="black"
            )
    player_Label.pack(pady=10)

def create_reset_button():
    global frame, reset_button
    reset_button = Button(
            frame, 
            text="Reset", 
            font=("Arial", 20), 
            command=reset,
            background="white",
            fg="black"
            )
    reset_button.pack(pady=10)
clicked=True
count=0

def reset():
    global clicked, count, player, players, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27,frame

    # Reset variables
    clicked = True
    count = 0
    player = random.choice(players)

    # Clear all buttons
    for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27]:
        button.config(text=" ", state=NORMAL, bg="SystemButtonFace")

    # Update player label
    player_Label.config(
            text="Player: " + player,
            background="white",
            fg="black"
            )

    disable_all_buttons()
    

def disable_all_buttons():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)
    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)
    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)
    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)

def b_click(b):
    global clicked, count, player

    if b['text'] == " " and clicked == True:
        b['text'] = players[0][0][0]
        clicked = False
        player = players[0]  # Change player to O
    elif b['text'] == " " and clicked == False:
        b['text'] = players[1][0]
        clicked = True
        player = players[1]  # Change player to X
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected\nPick another box...")
    
    player_Label.config(
            text="Player: " + player,
            background="white",
            fg=
                    "black"
            )  # Update label text
    checkifwon()

def checkifwon():
    global winner, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, count, player, player_Label, players, frame, button_frame, topic_Label, reset_button, label1, label2, label3, entry1, entry2, button
    winner=False

    if b1['text']==players[0][0] and b2['text']==players[0][0] and b3['text']==players[0][0]:
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b4['text']==players[0][0] and b5['text']==players[0][0] and b6['text']==players[0][0]:
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b7['text']==players[0][0] and b8['text']==players[0][0] and b9['text']==players[0][0]:
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b1['text']==players[0][0] and b4['text']==players[0][0] and b7['text']==players[0][0]:
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()
    
    elif b2['text']==players[0][0] and b5['text']==players[0][0] and b8['text']==players[0][0]:
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b3['text']==players[0][0] and b6['text']==players[0][0] and b9['text']==players[0][0]:
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b1['text']==players[0][0] and b5['text']==players[0][0] and b9['text']==players[0][0]:
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b3['text']==players[0][0] and b5['text']==players[0][0] and b7['text']==players[0][0]:
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b1['text']==players[0][0] and b10['text']==players[0][0] and b19['text']==players[0][0]:
        b1.config(bg="green")
        b10.config(bg="green")
        b19.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b2['text']==players[0][0] and b11['text']==players[0][0] and b20['text']==players[0][0]:
        b2.config(bg="green")
        b11.config(bg="green")
        b20.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b3['text']==players[0][0] and b12['text']==players[0][0] and b21['text']==players[0][0]:
        b3.config(bg="green")
        b12.config(bg="green")
        b21.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b4['text']==players[0][0] and b13['text']==players[0][0] and b22['text']==players[0][0]:
        b4.config(bg="green")
        b13.config(bg="green")
        b22.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b5['text']==players[0][0] and b14['text']==players[0][0] and b23['text']==players[0][0]:
        b5.config(bg="green")
        b14.config(bg="green")
        b23.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b6['text']==players[0][0] and b15['text']==players[0][0] and b24['text']==players[0][0]:
        b6.config(bg="green")
        b15.config(bg="green")
        b24.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b7['text']==players[0][0] and b16['text']==players[0][0] and b25['text']==players[0][0]:
        b7.config(bg="green")
        b16.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b8['text']==players[0][0] and b17['text']==players[0][0] and b26['text']==players[0][0]:
        b8.config(bg="green")
        b17.config(bg="green")
        b26.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b9['text']==players[0][0] and b18['text']==players[0][0] and b27['text']==players[0][0]:
        b9.config(bg="green")
        b18.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()
    
    elif b1['text']==players[0][0] and b14['text']==players[0][0] and b27['text']==players[0][0]:
        b1.config(bg="green")
        b14.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b3['text']==players[0][0] and b14['text']==players[0][0] and b25['text']==players[0][0]:
        b3.config(bg="green")
        b14.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b10['text']==players[0][0] and b11['text']==players[0][0] and b12['text']==players[0][0]:
        b10.config(bg="green")
        b11.config(bg="green")
        b12.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b13['text']==players[0][0] and b14['text']==players[0][0] and b15['text']==players[0][0]:
        b13.config(bg="green")
        b14.config(bg="green")
        b15.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b16['text']==players[0][0] and b17['text']==players[0][0] and b18['text']==players[0][0]:
        b16.config(bg="green")
        b17.config(bg="green")
        b18.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b19['text']==players[0][0] and b20['text']==players[0][0] and b21['text']==players[0][0]:
        b19.config(bg="green")
        b20.config(bg="green")
        b21.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b22['text']==players[0][0] and b23['text']==players[0][0] and b24['text']==players[0][0]:
        b22.config(bg="green")
        b23.config(bg="green")
        b24.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b25['text']==players[0][0] and b26['text']==players[0][0] and b27['text']==players[0][0]:
        b25.config(bg="green")
        b26.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b3['text']==players[0][0] and b14['text']==players[0][0] and b25['text']==players[0][0]:
        b3.config(bg="green")
        b14.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    elif b1['text']==players[0][0] and b14['text']==players[0][0] and b27['text']==players[0][0]:
        b1.config(bg="green")
        b14.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[0]} wins")
        disable_all_buttons()

    # check for O win
        
    if b1['text']==players[1][0] and b2['text']==players[1][0] and b3['text']==players[1][0]:
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b4['text']==players[1][0] and b5['text']==players[1][0] and b6['text']==players[1][0]:
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b7['text']==players[1][0] and b8['text']==players[1][0] and b9['text']==players[1][0]:
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b1['text']==players[1][0] and b4['text']==players[1][0] and b7['text']==players[1][0]:
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b2['text']==players[1][0] and b5['text']==players[1][0] and b8['text']==players[1][0]:
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b3['text']==players[1][0] and b6['text']==players[1][0] and b9['text']==players[1][0]:
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b1['text']==players[1][0] and b5['text']==players[1][0] and b9['text']==players[1][0]:
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b3['text']==players[1][0] and b5['text']==players[1][0] and b7['text']==players[1][0]:
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b1['text']==players[1][0] and b10['text']==players[1][0] and b19['text']==players[1][0]:
        b1.config(bg="green")
        b10.config(bg="green")
        b19.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b2['text']==players[1][0] and b11['text']==players[1][0] and b20['text']==players[1][0]:
        b2.config(bg="green")
        b11.config(bg="green")
        b20.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b3['text']==players[1][0] and b12['text']==players[1][0] and b21['text']==players[1][0]:
        b3.config(bg="green")
        b12.config(bg="green")
        b21.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b4['text']==players[1][0] and b13['text']==players[1][0] and b22['text']==players[1][0]:
        b4.config(bg="green")
        b13.config(bg="green")
        b22.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b5['text']==players[1][0] and b14['text']==players[1][0] and b23['text']==players[1][0]:
        b5.config(bg="green")
        b14.config(bg="green")
        b23.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b6['text']==players[1][0] and b15['text']==players[1][0] and b24['text']==players[1][0]:
        b6.config(bg="green")
        b15.config(bg="green")
        b24.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b7['text']==players[1][0] and b16['text']==players[1][0] and b25['text']==players[1][0]:
        b7.config(bg="green")
        b16.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b8['text']==players[1][0] and b17['text']==players[1][0] and b26['text']==players[1][0]:
        b8.config(bg="green")
        b17.config(bg="green")
        b26.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b9['text']==players[1][0] and b18['text']==players[1][0] and b27['text']==players[1][0]:
        b9.config(bg="green")
        b18.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b1['text']==players[1][0] and b14['text']==players[1][0] and b27['text']==players[1][0]:
        b1.config(bg="green")
        b14.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b3['text']==players[1][0] and b14['text']==players[1][0] and b25['text']==players[1][0]:
        b3.config(bg="green")
        b14.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b10['text']==players[1][0] and b11['text']==players[1][0] and b12['text']==players[1][0]:
        b10.config(bg="green")
        b11.config(bg="green")
        b12.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b13['text']==players[1][0] and b14['text']==players[1][0] and b15['text']==players[1][0]:
        b13.config(bg="green")
        b14.config(bg="green")
        b15.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b16["text"]==players[1][0] and b17["text"]==players[1][0] and b18["text"]==players[1][0]:
        b16.config(bg="green")
        b17.config(bg="green")
        b18.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b19["text"]==players[1][0] and b20["text"]==players[1][0] and b21["text"]==players[1][0]:
        b19.config(bg="green")
        b20.config(bg="green")
        b21.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b22["text"]==players[1][0] and b23["text"]==players[1][0] and b24["text"]==players[1][0]:
        b22.config(bg="green")
        b23.config(bg="green")
        b24.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b25["text"]==players[1][0] and b26["text"]==players[1][0] and b27["text"]==players[1][0]:
        b25.config(bg="green")
        b26.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b3['text']==players[1][0] and b14['text']==players[1][0] and b25['text']==players[1][0]:
        b3.config(bg="green")
        b14.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b1['text']==players[1][0] and b14['text']==players[1][0] and b27['text']==players[1][0]:
        b1.config(bg="green")
        b14.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b1["text"]==players[1][0] and b10["text"]==players[1][0] and b19["text"]==players[1][0]:
        b1.config(bg="green")
        b10.config(bg="green")
        b19.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b2["text"]==players[1][0] and b11["text"]==players[1][0] and b20["text"]==players[1][0]:
        b2.config(bg="green")
        b11.config(bg="green")
        b20.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b3["text"]==players[1][0] and b12["text"]==players[1][0] and b21["text"]==players[1][0]:
        b3.config(bg="green")
        b12.config(bg="green")
        b21.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b4["text"]==players[1][0] and b13["text"]==players[1][0] and b22["text"]==players[1][0]:
        b4.config(bg="green")
        b13.config(bg="green")
        b22.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b5["text"]==players[1][0] and b14["text"]==players[1][0] and b23["text"]==players[1][0]:
        b5.config(bg="green")
        b14.config(bg="green")
        b23.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b6["text"]==players[1][0] and b15["text"]==players[1][0] and b24["text"]==players[1][0]:
        b6.config(bg="green")
        b15.config(bg="green")
        b24.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b7["text"]==players[1][0] and b16["text"]==players[1][0] and b25["text"]==players[1][0]:
        b7.config(bg="green")
        b16.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b8["text"]==players[1][0] and b17["text"]==players[1][0] and b26["text"]==players[1][0]:
        b8.config(bg="green")
        b17.config(bg="green")
        b26.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    elif b9["text"]==players[1][0] and b18["text"]==players[1][0] and b27["text"]==players[1][0]:
        b9.config(bg="green")
        b18.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo(f"Tic Tac Toe", f"Congratulations! {players[1]} wins")
        disable_all_buttons()

    if count==27 and winner==False:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!\nNo one wins")
        disable_all_buttons()

def create_buttons():
    global button_frame, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27
    b1=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b1)
    )

    b2=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b2)
    )

    b3=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b3)
    )

    b4=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b4)
    )

    b5=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b5)
    )

    b6=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b6)
    )

    b7=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b7)
    )

    b8=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b8)
    )

    b9=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b9)
    )

    b10=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b10)
    )

    b11=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b11)
    )

    b12=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b12)
    )

    b13=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b13)
    )

    b14=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) , 
        bg="white" ,
        height=2, 
        width=5,
        command=lambda: b_click(b14)
    )

    b15=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b15)
    )

    b16=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b16)
    )

    b17=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b17)
    )

    b18=Button( 
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b18)
    )

    b19=Button( 
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b19)
    )

    b20=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b20)
    )

    b21=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b21)
    )

    b22=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b22)
    )

    b23=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b23)
    )

    b24=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b24)
    )

    b25=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b25)
    )

    b26=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b26)
    )

    b27=Button(
        button_frame,
        text=" " ,
        font=("Arial" , 30) ,
        bg="white" ,
        height=2,
        width=5,
        command=lambda: b_click(b27)
    )

    # grid the buttons
    b1.grid(row=6, column=0, sticky='ew')
    b2.grid(row=6, column=1, sticky='ew')
    b3.grid(row=6, column=2, sticky='ew')
    b10.grid(row=6, column=4, sticky='ew')
    b11.grid(row=6, column=5, sticky='ew')
    b12.grid(row=6, column=6, sticky='ew')
    b19.grid(row=6, column=8, sticky='ew')
    b20.grid(row=6, column=9, sticky='ew')
    b21.grid(row=6, column=10, sticky='ew')

    b4.grid(row=7, column=0, sticky='ew')
    b5.grid(row=7, column=1, sticky='ew')
    b6.grid(row=7, column=2, sticky='ew')
    b13.grid(row=7, column=4, sticky='ew')
    b14.grid(row=7, column=5, sticky='ew')
    b15.grid(row=7, column=6, sticky='ew')
    b22.grid(row=7, column=8, sticky='ew')
    b23.grid(row=7, column=9, sticky='ew')
    b24.grid(row=7, column=10, sticky='ew')


    b7.grid(row=8, column=0 , sticky='ew')
    b8.grid(row=8, column=1, sticky='ew')
    b9.grid(row=8, column=2, sticky='ew')
    b16.grid(row=8, column=4, sticky='ew')
    b17.grid(row=8, column=5, sticky='ew')
    b18.grid(row=8, column=6, sticky='ew')
    b25.grid(row=8, column=8, sticky='ew')
    b26.grid(row=8, column=9, sticky='ew')
    b27.grid(row=8, column=10, sticky='ew')

    # Add padding after every 3 columns
    padding1 = Label(button_frame, width=10)
    padding1.grid(row=6, column=3)

    padding2 = Label(button_frame, width=10)
    padding2.grid(row=7, column=3)

    padding3 = Label(button_frame, width=10)
    padding3.grid(row=8, column=3)

    padding4 = Label(button_frame, width=10)
    padding4.grid(row=6, column=7)

    padding5 = Label(button_frame, width=10)
    padding5.grid(row=7, column=7)

    padding6 = Label(button_frame, width=10)
    padding6.grid(row=8, column=7)

    return [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27]

root.mainloop()