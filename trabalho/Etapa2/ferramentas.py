import estado
from oval import Oval
from retangulo import Retangulo
from circulo import Circulo
from mao_livre import Mao_Livre
from reta import Reta


def redesenhar():
    for forma in estado.formas:
        forma.desenhar(estado.canva)  

#FUNCIONAMENTO QUANDO O USUARIO CLICA O MOUSE
def clicar(event):
    if estado.ferramenta == "retangulo":
        estado.figura = Retangulo(event.x, event.y, event.x, event.y, estado.cor_selecionadaBorda, estado.cor_Dopreenchimento)
    elif estado.ferramenta == "oval":
        estado.figura = Oval(event.x, event.y, event.x, event.y, estado.cor_selecionadaBorda, estado.cor_Dopreenchimento)
    elif estado.ferramenta == "circulo":
        estado.figura = Circulo(event.x, event.y, 0, estado.cor_selecionadaBorda, estado.cor_Dopreenchimento)
    elif estado.ferramenta == "maolivre":
        estado.figura = Mao_Livre(event.x, event.y, event.x, event.y)
    elif estado.ferramenta == "reta":
        estado.figura = Reta(event.x, event.y, event.x, event.y)

#FUNCIONAMENTO QUANDO O USUARIO ARRASTA O MOUSE
def arrastar(event):
    if estado.ferramenta == "retangulo":
        estado.figura.posx = event.x
        estado.figura.posy = event.y
    elif estado.ferramenta == "oval":
        estado.figura.posx = event.x
        estado.figura.posy = event.y
    elif estado.ferramenta == "circulo":
        estado.figura.raio = (((estado.figura.ini_x - event.x)**2 + (estado.figura.ini_y - event.y)**2) ** 0.5)
    elif estado.ferramenta == "maolivre":
        estado.figura.posx = event.x
        estado.figura.posy = event.y
        estado.figura.desenhar(estado.canva)
        estado.figura.ini_x = event.x
        estado.figura.ini_y = event.y
        return  # MAO LIVRE NÃO PRECISA DO REDESENHAR
    elif estado.ferramenta == "reta":
        estado.figura.posx = event.x
        estado.figura.posy = event.y
    estado.canva.delete("all")
    redesenhar()
    estado.figura.desenhar(estado.canva)

#FUNCIONAMENTO QUANDO O USUARIO SOLTA O MOUSE
def soltar(event):
    estado.formas.append(estado.figura)  
    redesenhar()