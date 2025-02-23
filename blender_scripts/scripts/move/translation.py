# <pep8-80 compliant>
import bpy
import mathutils


# Class
class Translation:
    """Translation of Vector"""

    # Class execution 1
    @classmethod
    def translate(cls):
        _translate_vector()
        return {'FINISHED'}


# non-public method
def _translate_vector():
    bpy.context.scene.cursor.rotation_mode = 'XYZ'
    bpy.context.scene.cursor.location = Vector((0.0, 0.0, 0.0))
    bpy.context.scene.cursor.rotation_euler = Vector((0.0, 0.0, 0.0))


# Unregister
def unregister():
    bpy.utils.unregister_class(MoveEntryPoint)


# Register
def register():
    bpy.utils.register_class(MoveEntryPoint)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
