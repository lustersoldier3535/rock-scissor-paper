from tkinter import *
from PIL import Image,ImageTk

# main window
root = Tk()
root.title("Rock,Paper,Scissors")
root.configure(background="blue")

#picture
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

#insert Picture
user_label = Label(root, image=scissors_img, bg="#9b59b6")
comp_label = Label(root, image=scissors_img, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)


#scores
playerScore = Label(root, text=0 ,font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

#indicators
user_indicator = Label(root, font=50, text="PLAYER")
comp_indicater = Label(root, font=50, text="COMPUTER")
user_indicator.grid(row=0, column=3)
comuter_indicator.grid(row=0, column=1)

#buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FFFFFF", fg="white").grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FFFFFFF", fg="white").grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#FFFFFF", fg="white").grid(row=2, column=3)


root.mainloop() 
