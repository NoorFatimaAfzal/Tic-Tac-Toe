from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.title("Tic Tac Toe")
players=["X", "O"]
player=random.choice(players)

def create_label_frame():
    frame = Frame(root)
    frame.pack()

def create_button_frame():
    button_frame = Frame(root)
    button_frame.pack()

def create_topic_label():
    topic_Label = Label(frame, text="Welcome to Tic Tac Toe", font=("Arial", 20))
    topic_Label.pack()

# name
name_label = Label(frame, text="Name:", font=("Arial", 15))
name_label.pack()

name = StringVar()
name_entry = Entry(frame, textvariable=name, width=20)
name_entry.pack()

# pwd
pwd_label = Label(frame, text="Passward:", font=("Arial", 15))
pwd_label.pack()

pwd = StringVar()
pwd_entry = Entry(frame, textvariable=pwd, width=20)
pwd_entry.pack()

def create_player_label():
    player_Label = Label(frame, text="Player: " + player, font=("Arial", 20))
    player_Label.pack()

clicked=True
count=0

def reset():
    global clicked, count, player

    # Reset variables
    clicked = True
    count = 0
    player = random.choice(players)

    # Clear all buttons
    for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27]:
        button.config(text=" ", state=NORMAL, bg="SystemButtonFace")

    # Update player label
    player_Label.config(text="Player: " + player)

# Bind reset function to reset button
reset_button = Button(frame, text="Reset", font=("Arial", 20), command=reset)
reset_button.pack()


def disable_all_buttons():
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

def checkifwon():
    global winner
    winner=False

    if b1['text']=="X" and b2['text']=="X" and b3['text']=="X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b4['text']=="X" and b5['text']=="X" and b6['text']=="X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b7['text']=="X" and b8['text']=="X" and b9['text']=="X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b1['text']=="X" and b4['text']=="X" and b7['text']=="X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()
    
    elif b2['text']=="X" and b5['text']=="X" and b8['text']=="X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b3['text']=="X" and b6['text']=="X" and b9['text']=="X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b1['text']=="X" and b5['text']=="X" and b9['text']=="X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b3['text']=="X" and b5['text']=="X" and b7['text']=="X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b1['text']=="X" and b10['text']=="X" and b19['text']=="X":
        b1.config(bg="green")
        b10.config(bg="green")
        b19.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b2['text']=="X" and b11['text']=="X" and b20['text']=="X":
        b2.config(bg="green")
        b11.config(bg="green")
        b20.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b3['text']=="X" and b12['text']=="X" and b21['text']=="X":
        b3.config(bg="green")
        b12.config(bg="green")
        b21.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b4['text']=="X" and b13['text']=="X" and b22['text']=="X":
        b4.config(bg="green")
        b13.config(bg="green")
        b22.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b5['text']=="X" and b14['text']=="X" and b23['text']=="X":
        b5.config(bg="green")
        b14.config(bg="green")
        b23.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b6['text']=="X" and b15['text']=="X" and b24['text']=="X":
        b6.config(bg="green")
        b15.config(bg="green")
        b24.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b7['text']=="X" and b16['text']=="X" and b25['text']=="X":
        b7.config(bg="green")
        b16.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b8['text']=="X" and b17['text']=="X" and b26['text']=="X":
        b8.config(bg="green")
        b17.config(bg="green")
        b26.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b9['text']=="X" and b18['text']=="X" and b27['text']=="X":
        b9.config(bg="green")
        b18.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()
    
    elif b1['text']=="X" and b14['text']=="X" and b27['text']=="X":
        b1.config(bg="green")
        b14.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b3['text']=="X" and b14['text']=="X" and b25['text']=="X":
        b3.config(bg="green")
        b14.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b10['text']=="X" and b11['text']=="X" and b12['text']=="X":
        b10.config(bg="green")
        b11.config(bg="green")
        b12.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b13['text']=="X" and b14['text']=="X" and b15['text']=="X":
        b13.config(bg="green")
        b14.config(bg="green")
        b15.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b16['text']=="X" and b17['text']=="X" and b18['text']=="X":
        b16.config(bg="green")
        b17.config(bg="green")
        b18.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b19['text']=="X" and b20['text']=="X" and b21['text']=="X":
        b19.config(bg="green")
        b20.config(bg="green")
        b21.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b22['text']=="X" and b23['text']=="X" and b24['text']=="X":
        b22.config(bg="green")
        b23.config(bg="green")
        b24.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b25['text']=="X" and b26['text']=="X" and b27['text']=="X":
        b25.config(bg="green")
        b26.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b3['text']=="X" and b14['text']=="X" and b25['text']=="X":
        b3.config(bg="green")
        b14.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    elif b1['text']=="X" and b14['text']=="X" and b27['text']=="X":
        b1.config(bg="green")
        b14.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins")
        disable_all_buttons()

    

    

    # check for O win
        
    if b1['text']=="O" and b2['text']=="O" and b3['text']=="O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b4['text']=="O" and b5['text']=="O" and b6['text']=="O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b7['text']=="O" and b8['text']=="O" and b9['text']=="O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b1['text']=="O" and b4['text']=="O" and b7['text']=="O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b2['text']=="O" and b5['text']=="O" and b8['text']=="O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b3['text']=="O" and b6['text']=="O" and b9['text']=="O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b1['text']=="O" and b5['text']=="O" and b9['text']=="O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b3['text']=="O" and b5['text']=="O" and b7['text']=="O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b1['text']=="O" and b10['text']=="O" and b19['text']=="O":
        b1.config(bg="green")
        b10.config(bg="green")
        b19.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b2['text']=="O" and b11['text']=="O" and b20['text']=="O":
        b2.config(bg="green")
        b11.config(bg="green")
        b20.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b3['text']=="O" and b12['text']=="O" and b21['text']=="O":
        b3.config(bg="green")
        b12.config(bg="green")
        b21.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b4['text']=="O" and b13['text']=="O" and b22['text']=="O":
        b4.config(bg="green")
        b13.config(bg="green")
        b22.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b5['text']=="O" and b14['text']=="O" and b23['text']=="O":
        b5.config(bg="green")
        b14.config(bg="green")
        b23.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b6['text']=="O" and b15['text']=="O" and b24['text']=="O":
        b6.config(bg="green")
        b15.config(bg="green")
        b24.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b7['text']=="O" and b16['text']=="O" and b25['text']=="O":
        b7.config(bg="green")
        b16.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b8['text']=="O" and b17['text']=="O" and b26['text']=="O":
        b8.config(bg="green")
        b17.config(bg="green")
        b26.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b9['text']=="O" and b18['text']=="O" and b27['text']=="O":
        b9.config(bg="green")
        b18.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b1['text']=="O" and b14['text']=="O" and b27['text']=="O":
        b1.config(bg="green")
        b14.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b3['text']=="O" and b14['text']=="O" and b25['text']=="O":
        b3.config(bg="green")
        b14.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b10['text']=="O" and b11['text']=="O" and b12['text']=="O":
        b10.config(bg="green")
        b11.config(bg="green")
        b12.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b13['text']=="O" and b14['text']=="O" and b15['text']=="O":
        b13.config(bg="green")
        b14.config(bg="green")
        b15.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b16["text"]=="O" and b17["text"]=="O" and b18["text"]=="O":
        b16.config(bg="green")
        b17.config(bg="green")
        b18.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b19["text"]=="O" and b20["text"]=="O" and b21["text"]=="O":
        b19.config(bg="green")
        b20.config(bg="green")
        b21.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b22["text"]=="O" and b23["text"]=="O" and b24["text"]=="O":
        b22.config(bg="green")
        b23.config(bg="green")
        b24.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b25["text"]=="O" and b26["text"]=="O" and b27["text"]=="O":
        b25.config(bg="green")
        b26.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b3['text']=="O" and b14['text']=="O" and b25['text']=="O":
        b3.config(bg="green")
        b14.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b1['text']=="O" and b14['text']=="O" and b27['text']=="O":
        b1.config(bg="green")
        b14.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b1["text"]=="O" and b10["text"]=="O" and b19["text"]=="O":
        b1.config(bg="green")
        b10.config(bg="green")
        b19.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b2["text"]=="O" and b11["text"]=="O" and b20["text"]=="O":
        b2.config(bg="green")
        b11.config(bg="green")
        b20.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b3["text"]=="O" and b12["text"]=="O" and b21["text"]=="O":
        b3.config(bg="green")
        b12.config(bg="green")
        b21.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b4["text"]=="O" and b13["text"]=="O" and b22["text"]=="O":
        b4.config(bg="green")
        b13.config(bg="green")
        b22.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b5["text"]=="O" and b14["text"]=="O" and b23["text"]=="O":
        b5.config(bg="green")
        b14.config(bg="green")
        b23.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b6["text"]=="O" and b15["text"]=="O" and b24["text"]=="O":
        b6.config(bg="green")
        b15.config(bg="green")
        b24.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b7["text"]=="O" and b16["text"]=="O" and b25["text"]=="O":
        b7.config(bg="green")
        b16.config(bg="green")
        b25.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b8["text"]=="O" and b17["text"]=="O" and b26["text"]=="O":
        b8.config(bg="green")
        b17.config(bg="green")
        b26.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()

    elif b9["text"]=="O" and b18["text"]=="O" and b27["text"]=="O":
        b9.config(bg="green")
        b18.config(bg="green")
        b27.config(bg="green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins")
        disable_all_buttons()


    if count==27 and winner==False:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!\nNo one wins")
        disable_all_buttons()

def b_click(b):
    global clicked, count, player

    if b['text'] == " " and clicked == True:
        b['text'] = "X"
        clicked = False
        player = "O"  # Change player to O
    elif b['text'] == " " and clicked == False:
        b['text'] = "O"
        clicked = True
        player = "X"  # Change player to X
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected\nPick another box...")
    
    player_Label.config(text="Player: " + player)  # Update label text
    checkifwon()
    
def create_buttons():
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

    return [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27]

buttons = create_buttons()

# grid the buttons
for i, button in enumerate(buttons):
    button.grid(row=6 + i // 3, column=(i % 3) * 3, sticky='ew')


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






root.mainloop()
