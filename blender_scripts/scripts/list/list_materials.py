# <pep8-80 compliant>
import bpy


# Class
class ListMaterials:
    """List all data materials"""

    # Class execution
    @classmethod
    def list(cls):
        _list_materials()
        return {'FINISHED'}


# non-public method
def _list_materials():
    # print all materials
    for t_material in bpy.data.materials:
        print("Name = ", t_material.name)


# To register
def register():
    bpy.utils.register_class(ListMaterials)


# To unregister
def unregister():
    bpy.utils.unregister_class(ListMaterials)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
