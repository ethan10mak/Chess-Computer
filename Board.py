import numpy as np
import chess
import tkinter as tk



board = chess.Board()
print(board)

window = tk.Tk()

window.title("Chess")
window.geometry("600x600")
window.mainloop()