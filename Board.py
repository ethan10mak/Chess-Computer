import numpy as np
import chess
from tkinter import *

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
            print(x, y)
            x = x + 50
        x = 0
        y = y + 50
        if color == "white":
            color = "black"
        else:
            color = "white"
    



board = chess.Board()
print(board)

window = Tk()

window.title("Chess")
window.geometry("800x600")
canvas = Canvas(height = 800, width = 600)
drawBoard(0,0)
canvas.pack()


window.mainloop()

