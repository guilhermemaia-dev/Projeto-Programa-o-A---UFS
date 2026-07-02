from figuras import Figuras
from tkinter import *
class Mao_Livre(Figuras):
    def desenhar(self, canvas):
        canvas.create_line(self.ini_x, self.ini_y, self.posx, self.posy, fill="Yellow")

root = Tk()
canvas = Canvas(root, bg="Grey")
canvas.pack()
figura = None
ferramenta = "mao_livre"
def clicar(event):
    global figura
    if ferramenta == "mao_livre":
        figura = Mao_Livre(event.x, event.y, event.x, event.y)
def arrastar(event):
    global figura
    if ferramenta == "mao_livre":
        figura.posx = event.x
        figura.posy = event.y
        figura.desenhar(canvas)
        figura.ini_x = event.x
        figura.ini_y = event.y
canvas.bind("<Button-1>", clicar)
canvas.bind("<B1-Motion>", arrastar)
root.mainloop()