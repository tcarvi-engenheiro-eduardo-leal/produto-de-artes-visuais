# <pep8-80 compliant>
import bpy


# Class
class ListScenes:
    """List all data scenes"""

    # Class execution
    @classmethod
    def list(cls):
        _list_scenes()
        return {'FINISHED'}


# non-public method
def _list_scenes():
    # print all scenes
    for t_scene in bpy.data.scenes:
        print("Name = ", t_scene.name)


# To register
def register():
    bpy.utils.register_class(ListScenes)


# To unregister
def unregister():
    bpy.utils.unregister_class(ListScenes)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
