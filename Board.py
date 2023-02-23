import numpy as np
import chess
from tkinter import *

black = ["r", "n", "b", "q", "k", "p"]
white = ["R", "N", "B", "Q", "K", "P"]

def drawBoard(x, y):
    color = "white"
    while y < 400:
        while x < 400:
            canvas.create_rectangle(x, y, x+50, y+50,
             outline="black", fill=color)
            if color == "white":
                color = "black"
            else:
                color = "white"
            x = x + 50
        x = 0
        y = y + 50
        if color == "white":
            color = "black"
        else:
            color = "white"

def updateBoard():
    def drawImage(piece, pos, row, col):
        x = row * 50
        y = col * 50
        print(piece)
        if piece in black:
            canvas.create_rectangle(x+20, y+20, x+30, y+30,
            outline="white", fill="black")
            print("black")
        elif piece in white:
            canvas.create_rectangle(x+20, y+20, x+30, y+30,
            outline="black", fill="white")
            print("white")
           

    pos = 0
    while pos < 64:
        piece = board.piece_at(pos)
        col = chess.square_file(pos)
        row = chess.square_rank(pos)
        drawImage(piece, pos, row, col)
        pos += 1



board = chess.Board()
print(board)

window = Tk()

window.title("Chess")
window.geometry("800x600")
canvas = Canvas(height = 801, width = 601)
drawBoard(0,0)
canvas.pack()

updateBoard()
canvas.pack()

window.mainloop()

