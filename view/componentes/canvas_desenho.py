from tkinter import *

from model.mao_livre import Mao_Livre
from model.reta import Reta
from model.retangulo import Retangulo
from model.oval import Oval
from model.circulo import Circulo
from model.quadrado import Quadrado
from model.pincel import Pincel

class CanvasDesenho(Canvas):
    def __init__(self, master, controller):
        super().__init__(master, bg="white", width=1024, height=576)
        self.controller = controller

        #mapeamento das figuras
        self.dicionario_figuras = {
            Mao_Livre : self.desenhar_mao_livre,
            Reta : self.desenhar_reta,
            Retangulo : self.desenhar_retangulo,
            Oval : self.desenhar_oval,
            Circulo: self.desenhar_circulo,
            Quadrado :self.desenhar_quadrado,
            Pincel: self.desenhar_pincel
            }

        self.bind("<Button-1>", self.controller.mouse_ini)    
        self.bind("<B1-Motion>", self.controller.mouse_movimentacao) 
        self.bind("<ButtonRelease-1>", self.controller.fim_mouse)

        self.bind("<Motion>", self.controller.rastrear_mouse)
        self.bind("<Leave>", self.controller.mouse_saiu)


    # metodo simplificado que desenha tudo direto
    def desenhar_figuras(self, lista_figuras, figura_selecionada=None):
        self.delete("all")
        if figura_selecionada is None:
            figura_selecionada = []

        #cria um loop que primeiro analisa qual o tipo de figura, olha se essa figura esta no dicionario e se estiver executa o metodo associado no dicionario
        for figura in lista_figuras:
            tipo_figura = type(figura)
            if tipo_figura in self.dicionario_figuras:
                metodo_figura = self.dicionario_figuras[tipo_figura]
                
                #se a figura tiver no método de seleção e for a selecionada, cria a figura com o dash
                if figura in figura_selecionada:
                    metodo_figura(figura, dash=(4,2))
                else:
                    metodo_figura(figura)


    #Criação de metodos para desenhar as figuras
    def desenhar_reta(self, figura, dash=None):
        ini_x, ini_y, posx, posy, cor, espessura = figura.pegar_dados()
        self.create_line(ini_x, ini_y, posx, posy, fill=cor, dash=dash, width=espessura)
    
    def desenhar_mao_livre(self, figura, dash=None):
        pontos, cor, espessura = figura.pegar_dados()
        self.create_line(pontos, fill=cor, dash=dash, width=espessura)
    
    def desenhar_retangulo(self,figura, dash=None):
        ini_x, ini_y, posx, posy, cor_borda, cor_preench, espessura = figura.pegar_dados()
        self.create_rectangle(ini_x, ini_y, posx, posy, outline=cor_borda, fill=cor_preench, dash=dash, width=espessura)

    def desenhar_oval(self,figura, dash=None):
        ini_x, ini_y, posx, posy, cor_borda, cor_preench, espessura = figura.pegar_dados()
        self.create_oval(ini_x, ini_y, posx, posy, outline=cor_borda, fill=cor_preench, dash=dash, width=espessura)

    def desenhar_circulo(self,figura, dash=None):
        ini_x, ini_y, posx, posy, cor_borda, cor_preench, espessura = figura.pegar_dados()
        self.create_oval(ini_x, ini_y, posx, posy, outline=cor_borda, fill=cor_preench, dash=dash, width=espessura)

    def desenhar_quadrado(self,figura, dash=None):
        ini_x, ini_y, posx, posy, cor_borda, cor_preench, espessura = figura.pegar_dados()
        self.create_rectangle(ini_x, ini_y, posx, posy, outline=cor_borda, fill=cor_preench, dash=dash, width=espessura)

    def desenhar_pincel(self, figura, dash=None):
        pontos, cor, espessura = figura.pegar_dados()
        self.create_line(pontos, fill=cor, dash=dash, width=espessura, capstyle=ROUND, joinstyle=ROUND, smooth=True)    
