# <pep8-80 compliant>
import bpy


# Class
class AddCollectionsInstance:
    """ADD collectioninstance"""

    # Class execution
    @classmethod
    def add(cls):
        _add_object()
        return {'FINISHED'}


# non-public method
def _add_object():
    # TODO - To define input
    # TODO - To add
    print("TODO")


# To register
def register():
    bpy.utils.register_class(AddCollectionsInstance)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddCollectionsInstance)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
