import numpy as np
import chess
from tkinter import *

def drawBoard(x, y):
    color = "white"
    while x <= 400:
        while y <= 400:
            canvas.create_rectangle(x, y, x+50, y+50,
             outline="black", fill=color)
            if color == "white":
                color = "black"
            else:
                color = "white"
            y = y + 50
        y = 0
        x = x + 50
    



board = chess.Board()
print(board)

window = Tk()
canvas = Canvas(height = 800, width = 600)
window.title("Chess")
window.geometry("800x600")

drawBoard(0,0)
canvas.pack()


window.mainloop()

