# <pep8-80 compliant>
import bpy
import math
from mathutils import Vector, Matrix

class Deslocar:

    def deslocar_reto(d):
        if(d[0] == 0):
            # 0 Deslocamento ortogonal em X
            # print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
            bpy.context.scene.cursor.location[0] += d[1]
            bpy.context.view_layer.update()
        elif(d[0] == 1):
            # 1 Deslocamento ortogonal em Y
            # print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
            bpy.context.scene.cursor.location[1] += d[1]
            bpy.context.view_layer.update()
        elif(d[0] == 2):
            # 2 Deslocamento ortogonal em Z
            # print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
            bpy.context.scene.cursor.location[2] += d[1]
            bpy.context.view_layer.update()
        elif(d[0] == 3):
            # Atualiza posição XY
            # print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
            bpy.context.scene.cursor.location[0] += d[1]
            bpy.context.scene.cursor.location[1] += d[2]
            bpy.context.view_layer.update()

    def deslocar_inclinado(d):
        if(d[0] == 10):
            # 10 Deslocamento inclinado em X
            # print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
            t_medida_deslocamentoX = d[1]
            t_inclinação_deslocamento_graus = d[2]
            t_inclinação_deslocamento_radianos = math.radians(t_inclinação_deslocamento_graus)
            bpy.context.scene.cursor.location[0] = bpy.context.scene.cursor.location[0] + t_medida_deslocamentoX * math.cos(t_inclinação_deslocamento_radianos)
            bpy.context.scene.cursor.location[1] = bpy.context.scene.cursor.location[1] + t_medida_deslocamentoX * math.sin(t_inclinação_deslocamento_radianos)
            bpy.context.view_layer.update()
            print("changed bpy.context.scene.cursor.location[0] = ", bpy.context.scene.cursor.location[0])
            print("changed bpy.context.scene.cursor.location[1] = ", bpy.context.scene.cursor.location[1])
        elif(d[0] == 11):
            # 10 Deslocamento inclinado em Y
            # print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
            bpy.context.scene.cursor.rotation_euler[1] += math.radians(d[1])
            bpy.context.view_layer.update()
        elif(d[0] == 12):
            # 10 Deslocamento inclinado em Z
            # print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
            bpy.context.scene.cursor.rotation_euler[2] += math.radians(d[1])
            bpy.context.view_layer.update()
        elif(d[0] == 13):
            # 10 Deslocamento inclinado em XZ
            # print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
            bpy.context.scene.cursor.rotation_euler[0] += math.radians(d[1])
            bpy.context.scene.cursor.rotation_euler[1] += math.radians(d[1])
            bpy.context.view_layer.update()


# To register
def register():
    bpy.utils.register_class(Deslocar)


# To unregister
def unregister():
    bpy.utils.unregister_class(Deslocar)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()