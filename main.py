from view.janela_Paint import *
from model.model_Interface import *
from controller.controller_Paint import *

#cria a view, o model, o controller e inicia o mainloop

view = JanelaPaint()
model = ModelInterface()
controller = ControllerPaint(model, view)
view.janela.mainloop()