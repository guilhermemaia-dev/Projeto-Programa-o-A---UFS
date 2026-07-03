from tkinter import *
from interface import Interface

# Criar janela principal

root = Tk()
root.geometry("1280x720")
root.title("PAINT 2.0")

canva = Canvas(root, width=1024, height=576, bg="white")

lista_cores = ["#00a8ff", "#c01414", "#10eb09", "#000000", "#ffffff", "#d9ff00", "#a200ff", "#ff5e00", "#858585", "#E7E7E7"]

paint = Interface(janela=root, canvas=canva, estado_marcador=IntVar(value=0), cores=lista_cores, cor_selecionada_borda="black", cor_selecionada_preenchimento='', figuras=[])

paint.criar_interface()