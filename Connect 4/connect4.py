import customtkinter as ctk
from tkinter import PhotoImage,messagebox
import sys
import warnings
warnings.filterwarnings('ignore')

global cell,buttons,Turn,player1,player2,title,board

class Player:
    def __init__(self, name, marker):
        self.name = name
        self.move = set()
        self.marker = marker
    def add_move(self,coords):
        self.move.add(coords)


def is_win(player):
    for row,col in player.move:
        if {(row+1,col+1),(row+2,col+2),(row+3,col+3)}.issubset(player.move):
            return True
        if {(row-1,col-1),(row-2,col-2),(row-3,col-3)}.issubset(player.move):
            return True
        if {(row-1,col+1),(row-2,col+2),(row-3,col+3)}.issubset(player.move):
            return True
        if {(row+1,col-1),(row+2,col-2),(row+3,col-3)}.issubset(player.move):
            return True

        if {(row+1,col),(row+2,col),(row+3,col)}.issubset(player.move):
            return True
        if {(row-1,col),(row-2,col),(row-3,col)}.issubset(player.move):
            return True
        if {(row,col+1),(row,col+2),(row,col+3)}.issubset(player.move):
            return True
        if {(row,col-1),(row,col-2),(row,col-3)}.issubset(player.move):
            return True

def update_board(board, move):
    global Turn, player1, player2
    if board[0][move] != ' ':
        return
    player = player1 if Turn else player2
    Turn = not Turn

    for row in range(len(board)):
        if board[row][move] != ' ':
            board[row - 1][move] = player.marker
            cell[row-1][move].configure(image=player.marker)
            player.add_move((row-1, move))
            if is_win(player):
                if messagebox.askyesno(message = ('Yellow Wins' if Turn else 'Red Wins')+'\nDo you Want to Play Again' ,title='Game OVER',icon='info'):
                    reset()
                else:
                    sys.exit(0)

            title.configure(text='Red\'s Turn' if Turn else 'Yellow\'s Turn')
            return
    else:
        board[5][move] = player.marker
        cell[5][move].configure(image=player.marker)
        player.add_move((5, move))
        if is_win(player):
            if messagebox.askyesno(message=('Yellow Wins' if Turn else 'Red Wins')+'\nDo you Want to Play Again' , title='Game OVER',icon='info'):
                reset()
            else:
                sys.exit(0)
            return
        title.configure(text='Red\'s Turn' if Turn else 'Yellow\'s Turn')
        return


def reset():
    global player2,player1,Turn,cell,buttons,title,board
    player1.move = set()
    player2.move = set()
    board = [[' ' for i in range(7)] for j in range(6)]
    Turn = False
    for row in range(6):
        for col in range(7):
            cell[row][col].configure(image=PhotoImage(file='assets/empty.png'))


def initialize(game):
    global cell,board,Turn,title,buttons,player1,player2
    rows, cols = 6, 7
    board = [[' ' for i in range(cols)] for j in range(rows)]

    player1 = Player('Red', PhotoImage(file='assets/red.png'))
    player2 = Player('Yellow', PhotoImage(file='assets/yellow.png'))

    Turn = True

    #UI
    cell = [[ctk.CTkLabel(game, image=PhotoImage(file='assets/empty.png'), text='', ) for col in range(7)] for row in range(6)]
    buttons = [
        ctk.CTkButton(game, width=100, height=60, image=PhotoImage(file='assets/down.png'), text='',
                      command=lambda: update_board(board, move=0)),
        ctk.CTkButton(game, width=100, height=60, image=PhotoImage(file='assets/down.png'), text='',
                      command=lambda: update_board(board, move=1)),
        ctk.CTkButton(game, width=100, height=60, image=PhotoImage(file='assets/down.png'), text='',
                      command=lambda: update_board(board, move=2)),
        ctk.CTkButton(game, width=100, height=60, image=PhotoImage(file='assets/down.png'), text='',
                      command=lambda: update_board(board, move=3)),
        ctk.CTkButton(game, width=100, height=60, image=PhotoImage(file='assets/down.png'), text='',
                      command=lambda: update_board(board, move=4)),
        ctk.CTkButton(game, width=100, height=60, image=PhotoImage(file='assets/down.png'), text='',
                      command=lambda: update_board(board, move=5)),
        ctk.CTkButton(game, width=100, height=60, image=PhotoImage(file='assets/down.png'), text='',
                      command=lambda: update_board(board, move=6)),
    ]
    title = ctk.CTkLabel(game, text='Red\'s Turn', height=20, font=('Arial', 20))


    #GRID
    title.grid(row=0, column=2, columnspan=2)

    for col in range(cols):
        buttons[col].grid(row=1, column=col)

    for row in range(rows):
        for col in range(cols):
            cell[row][col].grid(row=row + 2, column=col)


 
def main():
    global cell,Turn, player1,player2,buttons,title,board

    game = ctk.CTk()
    game.geometry('700x680')
    game.title('Connect4')

    initialize(game)

    game.resizable(False,False)
    game.mainloop()




if __name__ == '__main__':
    main()
