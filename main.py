import random
from tkinter import*
from PIL import Image, ImageTk

#Dictionary and vars
schema = {
    "rock":{"rock":1,"paper":0,"scissors":2},
    "paper":{"rock":2,"paper":1,"scissors":0},
    "scissors":{"rock":0,"paper":2,"scissors":1},
}
comp_score = 0
player_score = 0
#Function
def outcome_handler(user_choice):
    global comp_score
    global player_score
    outcomes = ("rock","paper","scissors")
    random_number= random.randint(0,2)
    computer_choice = outcomes[random_number]
    result  = schema[user_choice][computer_choice]

    player_choice_label.config(fg="red",text="Player Choice :"+str(user_choice))
    computer_choice_label.config(fg="purple",text="Computer Choice :"+str(computer_choice))

    if result == 2:
        player_score = player_score +2
        player_score_label.config(text="Player :"+str(player_score))
        outcome_label.config(fg="blue",text="Outcome:Player won")
    elif result == 1:
        player_score = player_score + 1
        comp_score = player_score + 1
        player_score_label.config(text="Player :"+str(player_score)) 
        computer_score_label.config(text="Computer :"+str(comp_score))
        outcome_label.config(fg="blue",text="Outcome : Computer won")
    elif result == 0:
        comp_score = comp_score +2
#main screen
root = Tk()
root.title("RPS")

#labels
label=Label(root,text="Rock , Paper, Scissors",font=("Calibri",14)).grid(row=0,sticky=N,pady=10,padx=200)
label=Label(root,text="Please select an option",font=("Calibri",12)).grid(row=1,stick=N)
player_score_label=Label(root,text="Player : 0",font=("Calibri",12))
player_score_label.grid(row=2,sticky=W)
computer_score_label = Label(root,text="Computer :0",font=("Calibri",12))
computer_score_label.grid(row=2,sticky=E)
player_choice_label = label=Label(root,font=("Calibri",12))
player_choice_label.grid(row=3,sticky=W)
computer_choice_label=Label(root,font=("calibri",12))
computer_choice_label.grid(row=3,sticky=E)
outcome_label = Label(root,font=("Calibri",12))
outcome_label.grid(row=3,sticky=N)
#Button
Button(root,text="Rock",width=15,command=lambda:outcome_handler("rock")).grid(row=4,sticky=W,padx=5,pady=5)
Button(root,text="Paper",width=15,command=lambda:outcome_handler("paper")).grid(row=4,sticky=N,padx=5,pady=5)
Button(root,text="Scissors",width=15,command=lambda:outcome_handler("scissors")).grid(row=4,sticky=E,padx=5,pady=5)
#Dummy label
Label(root).grid(row=5)

root.mainloop()