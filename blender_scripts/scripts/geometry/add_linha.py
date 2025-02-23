# <pep8-80 compliant>
import sys
import bpy
import json
import math
import bmesh
from mathutils import Vector, Matrix
from add_material import AddMaterial
from move_entry_point import MoveEntryPoint

class Linha:

    def desenhar_reto(d):
        if(d[0] == 20):
            # DesenharLinhaRetaEmX
            t_comprimento_linha = d[1]
            print("DesenharLinhaRetaEmX - Comprimento = ", t_comprimento_linha)
            _add_linha_15_centimetros_em_X(d[1])
            bpy.context.scene.cursor.location[0] += t_comprimento_linha
            # [NÃO MUDA] bpy.context.scene.cursor.location[1] = bpy.context.scene.cursor.location[1]
            bpy.context.view_layer.update()
            print("[Nova] Location do cursor: ", bpy.context.scene.cursor.location)
            print("\n")
        elif(d[0] == 21):
            # DesenharLinhaRetaEmY
            t_comprimento_linha = d[1]
            print("DesenharLinhaRetaEmY - Comprimento = ", t_comprimento_linha)
            _add_linha_15_centimetros_em_Y(d[1])
            bpy.context.scene.cursor.location[1] += t_comprimento_linha
            bpy.context.view_layer.update()
            print("[Nova] Location do cursor: ", bpy.context.scene.cursor.location)
            print("\n")
    
    def desenhar_inclinado(d):
        if(d[0] == 30):
            # print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
            # 30 Linha inclinado de 0.15 em X
            t_comprimento_retangulo = d[1]
            print("Comprimento da linha inclinada = ", t_comprimento_retangulo)
            t_inclinação_retangulo_graus = d[2]
            t_inclinação_retangulo_radianos = math.radians(t_inclinação_retangulo_graus)
            print("Inclinacao da retangulo em radianos = ", t_inclinação_retangulo_radianos)
            _add_retangulo_15_centimetros_inclinado_em_x(t_comprimento_retangulo, t_inclinação_retangulo_radianos)
            bpy.context.scene.cursor.location[0] += t_comprimento_retangulo * math.cos(t_inclinação_retangulo_radianos)
            bpy.context.scene.cursor.location[1] += t_comprimento_retangulo * math.sin(t_inclinação_retangulo_radianos)
            bpy.context.view_layer.update()
            print("[Nova] Location do cursor: ", bpy.context.scene.cursor.location)
            print("\n")
        elif(d[0] == 31):
            # print("Comando d[0] = {} - {}".format(d[0],EnumComandoDesenho(d[0]).name))
            # 30 LInha inclinado de 0.15 em Y
            t_comprimento_retangulo = d[1]
            print("Comprimento da linha inclinada = ", t_comprimento_retangulo)
            t_value_inclinacao = d[2]
            _add_retangulo_15_centimetros_inclinado_em_x(t_comprimento_retangulo, t_value_inclinacao)
            bpy.context.scene.cursor.location[1] += t_comprimento_retangulo
            bpy.context.view_layer.update()
            print("[Nova] Location do cursor: ", bpy.context.scene.cursor.location)
            print("\n")


# non-public method
def _add_linha_15_centimetros_em_X(t_value_x: float):
    t_value_y = 0.00
    t_value_inclinacaoX = 0.00
    t_value_inclinacaoY = 0.00
    _add_linha(t_value_x, t_value_y, t_value_inclinacaoX, t_value_inclinacaoY)


# non-public method
def _add_linha_15_centimetros_em_Y(t_value_y: float):
    t_value_x = 0.00
    t_value_inclinacaoX = 0
    t_value_inclinacaoY = math.radians(90)
    _add_linha(t_value_x, t_value_y, t_value_inclinacaoX, t_value_inclinacaoY)


# non-public method
def _add_linha(t_value_x: float, t_value_y: float, t_value_inclinacaoX: float, t_value_inclinacaoY: float):
    # if t_value_x < 0:
    #     t_value_y *= -1
    t_data_MeshesInitial = bpy.data.meshes.new(name="t_data_MeshesInitial")
    t_data_MeshesInitial.from_pydata(
        [
            Vector(
                (
                    bpy.context.scene.cursor.location[0],
                    bpy.context.scene.cursor.location[1],
                    bpy.context.scene.cursor.location[2]
                )
            ),
            Vector(
                (
                    bpy.context.scene.cursor.location[0] + t_value_x * math.cos(t_value_inclinacaoX),
                    bpy.context.scene.cursor.location[1] + t_value_y * math.sin(t_value_inclinacaoY),
                    bpy.context.scene.cursor.location[2]
                )
            )
        ],
        [
            (0,1)
        ],
        [
            
        ]
    )
    
    t_bmesh = bmesh.new(use_operators=True)
    t_bmesh.from_mesh(t_data_MeshesInitial)

    #
    # Operações no BMESH
    #

    bmesh.ops.extrude_edge_only(t_bmesh)
    # t_bmesh.from_object(object=t_object, depsgraph=bpy.context.evaluated_depsgraph_get())
    # modifier = t_object.modifiers.new(name="Skin", type='SKIN')

    # Finish up, write the bmesh into a new mesh and free the bmesh
    t_data_meshe = bpy.data.meshes.new("t_data_Meshe")
    t_bmesh.to_mesh(t_data_meshe)
    t_bmesh.free()
    
    t_data_object = bpy.data.objects.new(
        name="t_data_object",
        object_data=t_data_meshe
    )
    print(t_data_object)
    print("verts0 = ", t_data_meshe.vertices[0].co)
    print("verts1 = ", t_data_meshe.vertices[1].co)
    AddMaterial.add(t_data_object, "MaterialretanguloBranca")
    bpy.context.scene.collection.objects.link(t_data_object)


# To register
def register():
    bpy.utils.register_class(Linha)


# To unregister
def unregister():
    bpy.utils.unregister_class(Linha)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()