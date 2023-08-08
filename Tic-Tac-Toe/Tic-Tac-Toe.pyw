from tkinter import *
import tkinter.messagebox as tkm
from tkinter import font
import random

top = Tk()
top.title("TicTacToe")

frame = Frame(top)
frame.pack()

myFont = font.Font(family='Inlanders', size=40)
win = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 4, 8}, {2, 4, 6}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}]
num = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def IsWin():
    for i in range(0, 8):
        if win[i].issubset(player1):
            r = tkm.askyesno("Rematch", "player1 won\nDo you want Rematch?")
            if r:
                main()
            else:
                top.quit()
            break
        if win[i].issubset(player2):
            r = tkm.askyesno("Rematch", "player2 won\nDo you want Rematch?")
            if r:
                main()
            else:
                top.quit()
            break
    if t == 0:
        r = tkm.askyesno("Rematch", "ITS A TIE\nDo you want Rematch?")
        if r:
            main()
        else:
            top.quit()


'''def RandomPC():
    choice = random.choice(num)
    num.remove(choice)
    label(arr, choice)'''


def label(number, num):
    global t, player1, player2
    t = t - 1
    if t % 2 == 0:
        number[num] = 'X'
        player1.add(num)
    else:
        number[num] = 'O'
        player2.add(num)
    b[num]['text'] = f" {arr[num]}"
    b[num]['state'] = DISABLED
    if t <= 5:
        IsWin()


def game():
    b[0] = Button(frame, text=f" {arr[0]} ", font=myFont, padx=10, command=lambda: label(arr, 0), state=NORMAL)
    b[1] = Button(frame, text=f" {arr[1]} ", font=myFont, padx=10, command=lambda: label(arr, 1), state=NORMAL)
    b[2] = Button(frame, text=f" {arr[2]} ", font=myFont, padx=10, command=lambda: label(arr, 2), state=NORMAL)
    b[3] = Button(frame, text=f" {arr[3]} ", font=myFont, padx=10, command=lambda: label(arr, 3), state=NORMAL)
    b[4] = Button(frame, text=f" {arr[4]} ", font=myFont, padx=10, command=lambda: label(arr, 4), state=NORMAL)
    b[5] = Button(frame, text=f" {arr[5]} ", font=myFont, padx=10, command=lambda: label(arr, 5), state=NORMAL)
    b[6] = Button(frame, text=f" {arr[6]} ", font=myFont, padx=10, command=lambda: label(arr, 6), state=NORMAL)
    b[7] = Button(frame, text=f" {arr[7]} ", font=myFont, padx=10, command=lambda: label(arr, 7), state=NORMAL)
    b[8] = Button(frame, text=f" {arr[8]} ", font=myFont, padx=10, command=lambda: label(arr, 8), state=NORMAL)

    b[0].grid(row=1, column=1)
    b[1].grid(row=1, column=2)
    b[2].grid(row=1, column=3)
    b[3].grid(row=2, column=1)
    b[4].grid(row=2, column=2)
    b[5].grid(row=2, column=3)
    b[6].grid(row=3, column=1)
    b[7].grid(row=3, column=2)
    b[8].grid(row=3, column=3)


def main():
    global arr, b, player1, player2, t
    arr = [" "] * 9
    b = [''] * 9
    player1 = set()
    player2 = set()
    t = 9

    menubar = Menu(top)
    Game = Menu(menubar, tearoff=0)
    Game.add_command(label='Human Vs AI', command=game())
    Game.add_command(label='Human Vs AI', command=None)
    Game.add_command(label='HighScores', command=None)
    Game.add_separator()
    Game.add_command(label='Exit', command=top.destroy)

    menubar.add_cascade(label='Game', menu=Game)

    top.config(menu=menubar)


''' m1 = Button(frame, text=f" 1V1 ", font=myFont, padx=10, command=lambda: game(),state=NORMAL)
    m2 = Button(frame, text=f" vs AI ", font=myFont, padx=10, command=lambda: label(arr, 1),state=NORMAL)
    m3 = Button(frame, text=f" QUIT ", font=myFont, padx=10, command=lambda: label(arr, 2),state=NORMAL)
    m1.grid(row=1, column=2)
    m2.grid(row=2, column=2)
    m3.grid(row=3, column=2)
'''
main()

top.mainloop()
