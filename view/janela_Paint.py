from tkinter import *
from tkinter import colorchooser
import os
from tkinter import filedialog

from model.mao_livre import Mao_Livre
from model.reta import Reta
from model.retangulo import Retangulo
from model.oval import Oval
from model.circulo import Circulo
from model.borracha import Borracha
from model.quadrado import Quadrado


class JanelaPaint:
    def __init__(self):
        self.janela = Tk()
        self.configuracao_janela()
        #obs: o controlador ainda n foi criado (apenas é criado na proxima linha do main)
        self.controller = None
        
        #cria um dicionario com as figuras existentes no programa e relacionando as figuras com os metodos
        self.dicionario_figuras = {
            Mao_Livre : self.desenhar_mao_livre,
            Reta : self.desenhar_reta,
            Borracha : self.desenhar_borracha,
            Retangulo : self.desenhar_retangulo,
            Oval : self.desenhar_oval,
            Circulo: self.desenhar_circulo,
            Quadrado :self.desenhar_quadrado
         }

    def configuracao_janela(self):
        self.janela.title("PAINT 2.1")
        self.janela.geometry("1600x900")


    def criar_elementos(self):
        self.canvas = Canvas(self.janela, width=1024, height=576, bg="white")
        self.canvas.pack(pady=20)

        #cria o frame para armazenar melhor os botoes e labels
        frame_linha1 = Frame(self.janela)
        frame_linha1.pack()
        frame_linha2 = Frame(self.janela)
        frame_linha2.pack()
        frame_linha3 = Frame(self.janela)
        frame_linha3.pack()

        self.estado_marcador = IntVar(value=0)
        self.marcador = Checkbutton(frame_linha1, text="Escolher preenchimento", variable=self.estado_marcador)
        self.marcador.pack(side=LEFT, padx=10)

        label_seletor_cor = Label(frame_linha1, text="SELETOR DE CORES")
        label_seletor_cor.pack(side=LEFT, padx=10)

        self.canvas.bind("<Button-1>", self.controller.mouse_ini)    
        self.canvas.bind("<B1-Motion>", self.controller.mouse_movimentacao) 
        self.canvas.bind("<ButtonRelease-1>", self.controller.fim_mouse)

        # criação da bind para Ctrl C e Ctrl V
        self.janela.bind("<Control-c>", self.controller.control_c)
        self.janela.bind("<Control-v>", self.controller.control_v)

        #cria uma bind para crtl+z apagar a ultima figura desenhada
        self.janela.bind("<Control-z>", self.controller.ctrl_z)   

        #atribuição das teclas das setas para manipulação das figuras#
        self.janela.bind("<Up>", self.controller.camada_frontal)
        self.janela.bind("<Down>", self.controller.camada_traseira)
        #terminar após a pausa#
        self.janela.bind("<Left>", self.controller.camada_traseira)
        self.janela.bind("<Right>", self.controller.camada_traseira)
        # pede ao controlador para obter a lista de cores, ele pede para o model, o model devolve a ele, e ele devolve para o view
        cores = self.controller.obter_cor()
        
        #cria os botões do seletor de cores e quando clica, manda uma mensagem para o controller para informar a cor clicada e o estado do marcador
        for cor in cores:
            if cor == "#E7E7E7":
                bot_cor = Button(frame_linha1, width=2, height=1, highlightbackground="black", command=lambda COR='': self.controller.receberAcor(COR, self.estado_marcador.get()))
            else:
                bot_cor = Button(frame_linha1, width=2, height=1,bg=cor, command=lambda COR=cor: self.controller.receberAcor(COR, self.estado_marcador.get()))

            bot_cor.pack(side=LEFT, pady=1)

        #criar botão para escolher mais cores
        caminho = os.path.join(os.path.dirname(__file__), "maiscores.png")
        self.imagem = PhotoImage(file=caminho)
        self.imagem = self.imagem.subsample(10, 11)
        bot_mais_cores = Button(frame_linha1, image=self.imagem,command=self.abrir_seletor_cor)
        bot_mais_cores.pack(side=LEFT)

        #criar os botões do seletor de figuras e colocar na janela logo
        bot_livre = Button(frame_linha2, text="MÃO LIVRE", command=lambda: self.controller.selecionar_ferramenta("Mao_Livre"))
        bot_reta = Button(frame_linha2, text="RETA", command=lambda: self.controller.selecionar_ferramenta("Reta"))
        bot_retangulo = Button(frame_linha2, text="RETANGULAR", command=lambda: self.controller.selecionar_ferramenta("Retangulo"))
        bot_oval = Button(frame_linha2, text="OVAL", command=lambda: self.controller.selecionar_ferramenta("Oval"))
        bot_circulo = Button(frame_linha2, text="CIRCULAR", command=lambda: self.controller.selecionar_ferramenta("Circulo"))
        bot_quadrado = Button(frame_linha2,text="QUADRADO",command=lambda:self.controller.selecionar_ferramenta("Quadrado"))
        bot_borracha = Button(frame_linha2, text="BORRACHA", command=lambda: self.controller.selecionar_ferramenta("Borracha"))
        bot_selecao = Button(frame_linha2, text="SELEÇÃO",command=lambda: self.controller.selecionar_ferramenta("Seleção"))
        bot_limpar = Button(frame_linha2, text="LIMPAR", bg="#9c5b56", fg="white" ,command=self.controller.limpar_tela)

        #Coloca os botões na janela
        bot_livre.pack(side=LEFT, padx=1)
        bot_reta.pack(side=LEFT, padx=1)
        bot_retangulo.pack(side=LEFT, padx=1)
        bot_oval.pack(side=LEFT, padx=1)
        bot_circulo.pack(side=LEFT, padx=1)
        bot_quadrado.pack(side=LEFT, padx=1)
        bot_borracha.pack(side=LEFT, padx=1)
        bot_selecao.pack(side=LEFT,padx=1)
        bot_limpar.pack(side=LEFT)

        # mostra a cor da borda atual na interface
        label_indicar_cor_borda = Label(frame_linha1, text="BORDA:")
        label_indicar_cor_borda.pack(side=LEFT, padx=10)
        self.label_cor_selecionadaBorda = Label(frame_linha1, bg=self.controller.model.cor_selecionada_borda, width=2, height=1)
        self.label_cor_selecionadaBorda.pack(side=LEFT, padx=10)

        # mostra a cor do preenchimento atual
        cor_preenc_default = self.controller.model.cor_selecionada_preenchimento
        if cor_preenc_default == "":
            cor_preenc_default = "#E7E7E7"
        label_indicar_cor_preenchimento = Label(frame_linha1, text="PREENCHIMENTO:")
        label_indicar_cor_preenchimento.pack(side=LEFT, padx=10)
        self.label_corPreench_selecionada = Label(frame_linha1, bg=cor_preenc_default, width=2, height=1)
        self.label_corPreench_selecionada.pack(side=LEFT, padx=10)

        # mostrar a ferramenta selecionada atualmente
        label_indicar_ferramenta_atual = Label(frame_linha2, text="Ferramenta selecionada:")
        label_indicar_ferramenta_atual.pack(side=LEFT, padx=10)
        self.mostrar_ferramenta_atual = Label(frame_linha2, text=self.controller.model.ferramenta_atual)
        self.mostrar_ferramenta_atual.pack(side=LEFT,padx=10)

        #criar um menu para conseguir implementar os botões de salvar e abrir arquivo
        menu = Menu(self.janela)
        self.janela.config(menu=menu)
        menu_arquivo = Menu(menu, tearoff= 0)
        menu.add_cascade(label="Arquivo",menu=menu_arquivo)
        menu_arquivo.add_command(label="Salvar",command=self.controller.salvar_desenho)
        menu_arquivo.add_command(label="Abrir",command=self.controller.abrir_desenho)

       
        

    #metodo para o próprio view atualizar as cores do preview na tela
    def alterar_cor_preview(self, cor_borda, cor_preenchimento):
        self.label_cor_selecionadaBorda.configure(bg=cor_borda)
        if cor_preenchimento != "":
            self.label_corPreench_selecionada.configure(bg=cor_preenchimento)
        else:
            self.label_corPreench_selecionada.configure(bg="#E7E7E7")

    # metodo para alterar a ferramenta atual mostrada na tela
    def alterar_ferramenta_preview(self, ferramenta_atual):
        self.mostrar_ferramenta_atual.configure(text=ferramenta_atual)


    #abre o seletor e manda pro controller a cor escolhida pelo usuario
    def abrir_seletor_cor(self):
        cor = colorchooser.askcolor()[1]
        if cor:
            self.controller.receberAcor(cor, self.estado_marcador.get())




    #Criação de metodos para desenhar as figuras
    def desenhar_reta(self, figura, dash=None):
        ini_x, ini_y, posx, posy, cor = figura.pegar_dados()
        self.canvas.create_line(ini_x, ini_y, posx, posy, fill=cor, dash=dash)
    
    def desenhar_mao_livre(self, figura, dash=None):
        pontos, cor = figura.pegar_dados()
        self.canvas.create_line(pontos, fill=cor, dash=dash)
        
    def desenhar_borracha(self,figura, dash=None):
        pontos, cor, tamanho = figura.pegar_dados()
        self.canvas.create_line(pontos, fill=cor, width=tamanho, dash=dash)
    
    def desenhar_retangulo(self,figura, dash=None):
        ini_x, ini_y, posx, posy, cor_borda, cor_preench = figura.pegar_dados()
        self.canvas.create_rectangle(ini_x, ini_y, posx, posy, outline=cor_borda, fill=cor_preench, dash=dash)

    def desenhar_oval(self,figura, dash=None):
        ini_x, ini_y, posx, posy, cor_borda, cor_preench = figura.pegar_dados()
        self.canvas.create_oval(ini_x, ini_y, posx, posy, outline=cor_borda, fill=cor_preench, dash=dash)

    def desenhar_circulo(self,figura, dash=None):
        ini_x, ini_y, posx, posy, cor_borda, cor_preench = figura.pegar_dados()
        self.canvas.create_oval(ini_x, ini_y, posx, posy, outline=cor_borda, fill=cor_preench, dash=dash)

    def desenhar_quadrado(self,figura, dash=None):
        ini_x, ini_y, posx, posy, cor_borda, cor_preench = figura.pegar_dados()
        self.canvas.create_rectangle(ini_x, ini_y, posx, posy, outline=cor_borda, fill=cor_preench, dash=dash)


    # metodo simplificado que desenha tudo direto
    def desenhar_figuras(self, lista_figuras, figura_selecionada=None):
        self.canvas.delete("all")

        #cria um loop que primeiro analisa qual o tipo de figura, olha se essa figura esta no dicionario e se estiver executa o metodo associado no dicionario
        for figura in lista_figuras:
            tipo_figura = type(figura)
            if tipo_figura in self.dicionario_figuras:
                metodo_figura = self.dicionario_figuras[tipo_figura]
                
                #se a figura tiver no método de seleção e for a selecionada, cria a figura com o dash
                if figura == figura_selecionada:
                    metodo_figura(figura, dash=(4,2))
                else:
                    metodo_figura(figura)



#Janela de pedir arquivo/caminho#
    def pedir_caminho_salvar(self):
        return filedialog.asksaveasfilename(
            title="Salvar Arquivo",
            defaultextension=".paint",
            filetypes=[("Arquivos Paint", "*.paint"), ("Todos os Arquivos", "*.*")])

    def pedir_caminho_abrir(self):
        return filedialog.askopenfilename(
            title="Abrir Arquivo",
            filetypes=[("Arquivos Paint", "*.paint"), ("Todos os Arquivos", "*.*")])
#Método de colocar a figura acima das outras#
    def camada_acima(figuras):
        figuras.remove(figSel)