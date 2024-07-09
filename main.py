import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("600x450")
window.title("Dice Roll")

dice = ["C:/Users/pradu/OneDrive/Documents/Project/Python/Dice Simulator/images/dice1.png", "C:/Users/pradu/OneDrive/Documents/Project/Python/Dice Simulator/images/dice2.png", "C:/Users/pradu/OneDrive/Documents/Project/Python/Dice Simulator/images/dice3.png", "C:/Users/pradu/OneDrive/Documents/Project/Python/Dice Simulator/images/dice4.png", "C:/Users/pradu/OneDrive/Documents/Project/Python/Dice Simulator/images/dice5.png", "C:/Users/pradu/OneDrive/Documents/Project/Python/Dice Simulator/images/dice6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window, image=image1)
label2 = tk.Label(window, image=image2)

label1.image = image1
label2.image = image2

label1.place(x=30, y=100)
label2.place(x=300, y=100)

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2

button = tk.Button(window, text="ROLL", bg="green", fg="aqua", font="Times 20 bold", command=dice_roll)
button.place(x=250, y=0)

window.mainloop()
