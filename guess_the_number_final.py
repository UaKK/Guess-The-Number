from tkinter import *
from tkinter import messagebox
from random import randint
from tkinter.filedialog import *

def check_random():
    global difficulty,num_difficulty,right_answer

    if difficulty.get() == 1:
        num_difficulty = 50
    elif difficulty.get() == 2:
        num_difficulty = 100
    elif difficulty.get() == 3:
        num_difficulty = 200

    right_answer = randint(1,num_difficulty)
    print(right_answer)

    loading.config(text='Your number is ready!')

    easy_rbtn['state'] = DISABLED
    normal_rbtn['state'] = DISABLED
    hard_rbtn['state'] = DISABLED

    randomise['state'] = DISABLED
    guess['state'] = ACTIVE

def check_guess():
    global enter_num,right_answer,try_count,try_colour

    player_guess = int(enter_num.get())
    if player_guess == right_answer:
        win_message()
    elif player_guess > right_answer:
        imgs.config(image=dnarrow,background=None) 
        loading.config(text='Lower')
        try_count += 1
    elif player_guess < right_answer:
        imgs.config(image=uparrow,background=None)
        loading.config(text='Higher')
        try_count += 1

    if try_count < 3:
        try_colour = 'green'
    elif 3 <= try_count <= 6:
        try_colour = 'yellow'
    elif 5 <= try_count <= 9:
        try_colour = 'orange'
    elif try_count <= 10:
        try_colour = 'red'

    tries.config(text=f'Tries: {try_count}',foreground=try_colour)

def check_exit():
    exit()

def win_message():
    global try_count

    high_score()

    larry = messagebox.askyesno('Congratulations!',f'You guessed the number and it took you {(try_count+1)} tries! Do you wish to play again?')

    if larry:
        reset()
    elif not larry:
        garry = messagebox.askquestion('Exit','If you continue you will exit the program! Do you wish to proceed?')
        
        if garry == 'yes':
            check_exit()
        elif garry == 'no':
            reset()

def reset():
    global try_count,try_colour

    easy_rbtn['state'] = ACTIVE
    normal_rbtn['state'] = ACTIVE
    hard_rbtn['state'] = ACTIVE
    
    randomise['state'] = ACTIVE

    loading.config(text='Waiting to randomise...')
    enter_num.delete(0,END)
    imgs.config(image=dice)
    
    try_count = 0
    try_colour = 'green'

def high_score():
    global highest_score,high_score_lbl

    with open('highscore.txt', 'w') as output_file:
        text = str(try_count)
        output_file.write(text)

    if try_count < highest_score:
        highest_score = (try_count + 1)

    open_high_score()

    tries.config(text=f'Tries: {try_count}',foreground=try_colour)
    high_score_lbl.config(text=f'High Score: {highest_score}')

def open_high_score():
    global highest_score,high_score_lbl
    with open('highscore.txt', 'r') as input_file:
        text = input_file.read()
        high_score_lbl.config(text=f'High Score: {text}')


main_colour = '#2d162c'
sec_colour = '#9775a6'
btn_colour = '#683a68'
style = 'Helvetica 20 bold'
palette = 'https://lospec.com/palette-list/velvet-cherry-gb'

dir = 'C:/Users/User/Documents/VSCode/TKinter/Guess_The_Number'

screen = Tk()
screen.title('Guess The Number')
screen.geometry('300x250')
screen.resizable(False, False)
screen.configure(background=main_colour)

high_score_lbl = Label(screen,text='',font='Tahoma 10 bold',background=main_colour,foreground=sec_colour)

with open('highscore.txt', 'r') as input_file:
    text = input_file.read()
    high_score_lbl.config(text=f'High Score: {text}')

difficulty = IntVar()
highest_score = 200
num_difficulty = 0
try_count = 0
try_colour = 'green'

headline = Label(screen,text='Guess the Number',font=style,background=main_colour,foreground=sec_colour)
headline.grid(column=1,row=1,columnspan=3)

easy_rbtn = Radiobutton(screen,text='Easy(0-50)',variable=difficulty,value=1,bg=btn_colour,overrelief='sunken',offrelief='flat')
normal_rbtn = Radiobutton(screen,text='Medium(0-100)',variable=difficulty,value=2,bg=btn_colour,overrelief='sunken',offrelief='flat')
hard_rbtn = Radiobutton(screen,text='Hard(0-200)',variable=difficulty,value=3,bg=btn_colour,overrelief='sunken',offrelief='flat')
easy_rbtn.grid(column=1,row=2)
normal_rbtn.grid(column=2,row=2)
hard_rbtn.grid(column=3,row=2)

info = Label(screen,text='Try to guess the randomly generated number',font='Tahoma 10 bold',background=main_colour,foreground=sec_colour)
info.grid(column=1,row=3,columnspan=3)

enter_num = Entry(screen,width=5,justify=CENTER)
enter_num.grid(column=2,row=5)

tries = Label(screen,text=f'Tries: {try_count}',font='Tahoma 10 bold',background=main_colour,foreground=try_colour)
tries.grid(column=2,row=6)

high_score_lbl = Label(screen,text=f'High Score: {highest_score}',font='Tahoma 10 bold',background=main_colour,foreground=sec_colour)
high_score_lbl.grid(column=2, row=7)

uparrow = PhotoImage(file="uparrow_final.png")
dnarrow = PhotoImage(file="downarrow_final.png")
dice = PhotoImage(file="dice.png")

randomise = Button(screen,text='Randomise',background=btn_colour,command=check_random,width=10,height=1,overrelief='sunken')
guess = Button(screen,text='Guess',background=btn_colour,command=check_guess,width=10,height=1,overrelief='sunken')
exit_btn = Button(screen,text='Exit',background=btn_colour,command=check_exit,width=10,height=1,overrelief='sunken')
randomise.grid(column=3,row=5)
guess.grid(column=3,row=6)
exit_btn.grid(column=3,row=7)

guess['state'] = DISABLED

imgs = Label(screen,image=dice,background=main_colour)
imgs.grid(column=1,row=5,rowspan=3)

loading = Label(screen,text='Waiting to randomise...',background=main_colour,foreground=sec_colour,font='Helvetica 10 bold')
loading.grid(column=1,row=8,columnspan=3)

screen.mainloop()