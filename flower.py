from tkinter import *
from PIL import Image, ImageTk
import random

def create_flower_animation():
    global canvas, flower_photo, flowers

    # Create a canvas
    canvas = Canvas(root, width=500, height=500)
    canvas.pack()

    # Load a flower image
    flower_image = Image.open("flower.jpg")  # Replace with your flower image path
    flower_photo = ImageTk.PhotoImage(flower_image)

    # Create several flowers at random x positions
    flowers = [canvas.create_image(random.randint(0, 500), -i*100, image=flower_photo) for i in range(20)]

    # Start the animation
    move_flowers()

def move_flowers():
    for flower in flowers:
        canvas.move(flower, 0, 5)
    root.after(100, move_flowers)  # Move the flowers every 100 ms

root = Tk()
create_flower_animation()
root.mainloop()