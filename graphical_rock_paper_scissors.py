from tkinter import *
from random import randint
from tkinter import ttk

root =Tk()
#Change bg color
canvas=Canvas(root,width=200, height=200)
canvas.pack()
root.config(bg="black")


root.title("Rock-Paper-Scissor")


#Define images
rock = PhotoImage(file =r'rock.png')
paper = PhotoImage(file =r'paper.png')
scissors = PhotoImage(file =r'scissors.png')

#Add images to a list
image_list = [rock,paper,scissors]

#Score, Wins, Loses, Ties
Score = 0
Wins=0
Loses=0
Ties=0

#Pick random number between 1 and 2
pick_number = randint(0,2)

#Throw up an image when the program starts

image_label = Label(root, image=image_list[pick_number])
image_label.pack(pady=20)


J = canvas.create_text(100,30,text=("Score",Score), font=("Verdana",18))
wins = canvas.create_text(100,100,text=("Wins:",Wins), font=("Verdana",18))
loses = canvas.create_text(100,150,text=("Loses:",Loses), font=("Verdana",18))
ties = canvas.create_text(100,180,text=("Ties:",Ties), font=("Verdana",18))
#Create spin function
def spin():
    global Score
    global Wins
    global Loses
    global Ties
    #Pick random number
    pick_number = randint(0, 2)
    #Show image
    image_label.config(image=image_list[pick_number])

    #Convert dropdown choice to a number
    if (user_choice.get() == "Rock"):
        user_choice_value = 0
    elif (user_choice.get() =="Paper"):
        user_choice_value= 1
    elif (user_choice.get() =="Scissors"):
        user_choice_value= 2

    #Determine win or loss
    if (user_choice_value == 0): #Rock
        if (pick_number == 1):
            win_lose_label.config(text="Paper wins. You lose..")
            Score-=1
            Loses+=1
        elif (pick_number ==2):
            win_lose_label.config(text="Rock wins!!")
            Score+=1
            Wins+=1
        elif (pick_number ==0):
            win_lose_label.config(text="It's a tie. Spin again!")
            Ties+=1
    if (user_choice_value == 1): #Paper
        if (pick_number == 1):
            win_lose_label.config(text="It's a tie. Spin again!")
        elif (pick_number == 2):
            win_lose_label.config(text="Scissors wins. You lose..")
            Score-=1
            Loses+=1
        elif (pick_number == 0):
            win_lose_label.config(text="Paper wins!!")
            Score+=1
            Wins+=1
    if (user_choice_value == 2):  # Scissors
        if (pick_number == 1):
            win_lose_label.config(text="Scissors win!!")
            Score+=1
            Wins+=1
        elif (pick_number == 2):
            win_lose_label.config(text="It's a tie. Sping again!")
            Ties+=1

        elif (pick_number == 0):
            win_lose_label.config(text="Rock wins.You lose...")
            Score-=1
            Loses+=1

    canvas.itemconfig(J, text=("Score:",Score), font=("Verdana",18))
    canvas.itemconfig(wins, text=("Wins:", Wins), font=("Verdana", 18))
    canvas.itemconfig(loses, text=("Loses:", Loses), font=("Verdana", 18))
    canvas.itemconfig(ties, text=("Ties:", Ties), font=("Verdana", 18))


#Make choice
user_choice = ttk.Combobox(root,value=("Rock","Paper","Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)


#Create Spin Button
spin_button = Button(root,text="Spin!",command=spin)
spin_button.pack(pady=10)

#Label for showing if you won or not
win_lose_label = Label(root,text="",font=("Verdana",18))
win_lose_label.pack(pady=50)


root.mainloop()
