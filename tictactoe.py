import tkinter
from tkinter import messagebox

from tictactoe_game_engine import TictactoeGameEngine

class Tictactoe:
    def __init__(self):
        self.tictactoe_game_engine = TictactoeGameEngine()
        
    def play(self):
        #show board
        print(self.tictactoe_game_engine)
        #무한반복
        while True:
            #row, col 입력받자
            row = int(input('row: '))
            col = int(input('col: '))
            #말을 놓자
            self.tictactoe_game_engine.set(row, col)
            #show board
            print(self.tictactoe_game_engine)
            #만약에 승자가 있으면, 무승부이면 끝
            result = self.tictactoe_game_engine.check_winner()
            if result != None:
                break
        if result == 'O':
            print('O승리')
        elif result == 'X':
            print('X승리')
        elif result == 'd':
            print('무승부')

class TictacToeGUI:
    def __init__(self):
        CANCAS_SIZE = 300
        self.TILE_SIZE = CANCAS_SIZE / 3
        self.tictactoe_game_engine = TictactoeGameEngine()

        self.root = tkinter.Tk()
        self.root.title('틱 택 토')
        self.root.geometry(str(CANCAS_SIZE) + 'x' + str(CANCAS_SIZE))
        self.root.resizable(width=False, height=False)
        self.canvas = tkinter.Canvas(self.root, bg='white', width=CANCAS_SIZE, height=CANCAS_SIZE)
        self.canvas.pack()

        self.images = {}
        self.images['X'] = tkinter.PhotoImage(file='X.gif')
        self.images['O'] = tkinter.PhotoImage(file='O.gif')

        self.canvas.bind('<Button-1>', self.click_handler)

    def click_handler(self, event):
        x = event.x
        y = event.y
        col = x//100 + 1
        row = y//100 + 1
        self.tictactoe_game_engine.set(row, col)
        self.draw_board()
        #check_winner
        result = self.tictactoe_game_engine.check_winner()
        if result == 'O':
            messagebox.showinfo("GAME OVER!", "O win!")
            self.root.quit()
        elif result == 'X':
            messagebox.showinfo("GAME OVER!", "X win!")
            self.root.quit()
        elif result == 'd':
            messagebox.showinfo("GAME OVER!", "무승부.")
            self.root.quit()

    def draw_board(self):
        self.canvas.delete('all')
        x=0
        y=0
        for i, v in enumerate(self.tictactoe_game_engine.board):
            if v == 'X':
                self.canvas.create_image(x, y, anchor='nw', image=self.images['X'])
            elif v == 'O':
                self.canvas.create_image(x, y, anchor='nw', image=self.images['O'])
            x += self.TILE_SIZE
            if i % 3 == 2:
                x = 0
                y += self.TILE_SIZE




    def play(self):
        # self.canvas.create_image(200, 100, anchor='nw', image=self.images['O'])
        # self.canvas.create_image(200, 0, anchor='nw', image=self.images['X'])
        # self.canvas.create_image(0, 100, anchor='nw', image=self.images['O'])
        # self.canvas.create_image(0, 0, anchor='nw', image=self.images['X'])
        # self.canvas.create_image(100, 200, anchor='nw', image=self.images['O'])
        self.root.mainloop()

if __name__ == '__main__':
    ttt = TictacToeGUI()
    ttt.play()