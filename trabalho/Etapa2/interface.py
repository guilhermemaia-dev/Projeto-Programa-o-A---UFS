from dataclasses import dataclass
from tkinter import *

from retangulo import Retangulo
from mao_livre import Mao_Livre
from reta import Reta
from oval import Oval
from circulo import Circulo


# Cria interface usando dataclass para reduzir o tamanho
@dataclass
class Interface:
    janela: Tk
    canvas: Canvas
    estado_marcador: int
    cores: list[str]
    cor_selecionada_borda: str
    cor_selecionada_preenchimento: str
    figuras: list
    ferramenta_atual: str = 'Mao_Livre'
    ferramentas_traduzidas = {"Mao_Livre": Mao_Livre, "Reta": Reta, "Retangulo": Retangulo, "Oval": Oval, "Circulo": Circulo}


    def criar_interface(self):
        #criar o canvas e label do seletor de cores e marcador de preenchimento
        self.canvas.pack()

        # MARCADOR DE PREENCHIMENTO: Se ativo, seletor de cores escolhe o preenchimento, caso contrário serve apenas para a borda
        marcador = Checkbutton(self.janela, text="Escolher preenchimento", variable=self.estado_marcador)
        marcador.pack(side=LEFT, padx=10)

        label_seletor_cor = Label(self.janela, text="SELETOR DE CORES")
        label_seletor_cor.pack(side=LEFT, padx=10)

        #cria os botões do seletor de cores
        for cor in self.cores:
            if cor == "#E7E7E7":
                bot_cor = Button(self.janela, width=2, height=1, highlightbackground="black", command=lambda COR='': self.receberAcor(COR))
            else:
                bot_cor = Button(self.janela, width=2, height=1,bg=cor, command=lambda COR=cor: self.receberAcor(COR))

            bot_cor.pack(side=LEFT, pady=1)
            
        #criar os botoes do seletor de figuras
        bot_livre = Button(self.janela, text="MÃO LIVRE", command=self.selecionar_livre)
        bot_reta = Button(self.janela, text="RETA", command=self.selecionar_reta)
        bot_retangulo = Button(self.janela, text="RETANGULAR", command=self.selecionar_retangulo)
        bot_oval = Button(self.janela, text="OVAL", command=self.selecionar_oval)
        bot_circulo = Button(self.janela, text="CIRCULAR", command=self.selecionar_circulo)

        #Coloca os botões na janela
        bot_livre.pack(side=LEFT)
        bot_reta.pack(side=LEFT)
        bot_retangulo.pack(side=LEFT)
        bot_oval.pack(side=LEFT)
        bot_circulo.pack(side=LEFT)

        # mostra a cor da borda atual na interface
        label_indicar_cor_borda = Label(self.janela, text="BORDA:")
        label_indicar_cor_borda.pack(side=LEFT, padx=10)
        self.label_cor_selecionadaBorda = Label(self.janela, bg=self.cor_selecionada_borda, width=2, height=1)
        self.label_cor_selecionadaBorda.pack(side=LEFT, padx=10)

        # mostra a cor do preenchimento atual
        label_indicar_cor_preenchimento = Label(self.janela, text="PREENCHIMENTO:")
        label_indicar_cor_preenchimento.pack(side=LEFT, padx=10)
        self.label_corPreench_selecionada = Label(self.janela, bg="#E7E7E7", width=2, height=1)
        self.label_corPreench_selecionada.pack(side=LEFT, padx=10)

        #Capta os cliques do mouse
        self.canvas.bind("<Button-1>", self.mouse_ini)
        self.canvas.bind("<B1-Motion>", self.mouse_movimentacao)
        self.canvas.bind("<ButtonRelease-1>", self.fim_mouse)

        #abrir a janela (iniciando o mainloop)
        self.janela.mainloop()
        
    #recebe a cor clicada e faz a "tradução" dela
    def receberAcor(self, cor_clicada):
        # se for 1, ou seja, escolher preenchimento está marcada, atualiza a cor do tipo preenchimento mostrada na interface e a variavel que guarda a cor
        if self.estado_marcador.get() == 1: 
            self.cor_selecionada_preenchimento = cor_clicada
            if self.cor_selecionada_preenchimento != "":
                self.label_corPreench_selecionada.configure(bg=self.cor_selecionada_preenchimento)
            else:
                self.label_corPreench_selecionada.configure(bg="#E7E7E7")
        
        #atualiza a cor do tipo borda mostrada na interface e a variavel que guarda a cor 
        else:
            if cor_clicada == "":
                self.cor_selecionada_borda = "#000000"
            else:
                self.cor_selecionada_borda = cor_clicada

        self.label_cor_selecionadaBorda.configure(bg=self.cor_selecionada_borda)



    #captar os eventos do mouse e guardar coordenadas
    def mouse_ini(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

    # metodo que capta as coordenadas enquanto movimenta o mouse e continua criando a figura (fazendo o preview)
    def mouse_movimentacao(self, event):
        self.x1 = event.x
        self.y1 = event.y

        preview = self.criar_figura(self.x1, self.y1)
        
        # se for mao_livre então vai adicionando na hora do movimento todos os previews e desenhando a figura, ou seja, desenhando o preview
        if self.ferramenta_atual == "Mao_Livre":
            self.figuras.append(preview)
            self.desenhar_figuras()
            self.ini_x = self.x1
            self.ini_y = self.y1
        # se for as outras figuras, apenas desenha o preview da figura
        else:
            self.desenhar_figuras()
            preview.desenhar(self.canvas)

    #quando solta o mouse pega as coordenadas finais (x2,y2) e cria a figura final com essas coordenadas
    def fim_mouse(self, event):
        self.x2 = event.x
        self.y2 = event.y

        figura = self.criar_figura(self.x2, self.y2)

        #garante que não seja criada figuras com apenas um clique, ou seja, figuras que a posição inicial for igual a final (sem movimentação)
        if self.ini_x != self.x2 and self.ini_y != self.y2:
            self.figuras.append(figura)


        if self.ferramenta_atual == "Oval":
            #          10         -70    80
            if -50000 > self.ini_x - self.x2 > 50000 or -50000 > self.ini_y - self.y2 > 50000:
                self.figuras.append(figura)

        self.desenhar_figuras()
            




    # metodo para criar a figura
    # os parâmetros x,y dependem do que for, por exemplo, se for o mouse_movimentacao (preview) que chama o metodo, então será passado x1,y1
    # caso for fim_mouse será passado x2,y2
    def criar_figura(self,x,y):

        # busca no dicionário "ferramentas_traduzidas" para evitar repetição de codigo, evitando comparações desnecessárias como por exemplo: elif ferramenta_atual == "circulo, oval..."
        classe_da_figura = self.ferramentas_traduzidas.get(self.ferramenta_atual)
        
        if self.ferramenta_atual in ["Mao_Livre", "Reta"]:
            return classe_da_figura(self.ini_x, self.ini_y, x, y,self.cor_selecionada_borda)
        else:
            return classe_da_figura(self.ini_x, self.ini_y, x, y, self.cor_selecionada_borda, self.cor_selecionada_preenchimento)


    # método para desenhar as figuras (polimorfismo)
    def desenhar_figuras(self):
        self.canvas.delete('all')
        for figura in self.figuras:
            figura.desenhar(self.canvas)

    #métodos para selecionar as ferramentas e deixar guardado nas variáveis
    def selecionar_livre(self):
        self.ferramenta_atual = "Mao_Livre"

    def selecionar_reta(self):
        self.ferramenta_atual = "Reta"

    def selecionar_retangulo(self):
        self.ferramenta_atual = "Retangulo"

    def selecionar_oval(self):
        self.ferramenta_atual = "Oval"

    def selecionar_circulo(self):
        self.ferramenta_atual = "Circulo"