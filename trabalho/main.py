import estado
import ferramentas

import config
from tkinter import *

#BASE DA JANELA
estado.root = Tk()
estado.root.geometry(config.geometria_janela)
estado.root.title(config.titulo)

estado.canva = Canvas(estado.root, bg=config.fundo_canvas, width=config.largura_canvas, height=config.altura_canvas)
estado.canva.pack()

import interface

estado.canva.bind('<ButtonPress-1>', ferramentas.mouse_ini)
ferramentas.livre()
estado.root.mainloop()