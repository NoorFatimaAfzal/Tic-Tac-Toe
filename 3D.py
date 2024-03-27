from tkinter import *
import random

root = Tk()
root.title("3D Tic Tac Toe")

# Create three frames for the three boards
frame1 = Frame(root)
frame1.grid(row=0, column=0, padx=10, pady=10)

frame2 = Frame(root)
frame2.grid(row=0, column=1, padx=10, pady=10)

frame3 = Frame(root)
frame3.grid(row=0, column=2, padx=10, pady=10)

# Create the buttons for each board
for frame in [frame1, frame2, frame3]:
    for i in range(3):
        for j in range(3):
            button = Button(frame, text=" ", font=("Arial", 30), bg="white", height=2, width=5)
            button.grid(row=i, column=j)

root.mainloop()