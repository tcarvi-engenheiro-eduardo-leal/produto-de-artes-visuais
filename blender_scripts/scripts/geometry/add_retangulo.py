# <pep8-80 compliant>
import bpy
import math
from mathutils import Vector, Matrix

class Retangulo:

    def desenhar_reto(d):
        print("desenhar reto")

    def desenhar_inclinado(d):
        print("Desenhar inclinado")

# To register
def register():
    bpy.utils.register_class(Retangulo)


# To unregister
def unregister():
    bpy.utils.unregister_class(Retangulo)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()