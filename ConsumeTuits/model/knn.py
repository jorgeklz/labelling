import iniciador as model

from os.path import exists

"""
This is the model generated by Jandry, this will change in the future
"""
class KNNModel:
    def __init__(self):
        pass

    def predict_label(self, text):
        return  model.EtiquetaEnTexto(model.EtiquetarModelLSI(text))