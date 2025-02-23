# <pep8-80 compliant>
import bpy
import os


# Class
class SaveBlenderFile:
    """Save blender file"""

    # Class execution
    @classmethod
    def save(cls, t_blender_file_name):
        _save_blender_file(t_blender_file_name)
        return {'FINISHED'}


# non-public method
def _save_blender_file(blender_file_name):
    save_dir = os.path.join(
        os.path.abspath("."),
        "blender_projects"
        )
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    save_path = os.path.join(
        os.path.abspath("."),
        "blender_projects\\" + blender_file_name
        )
    if os.path.exists(save_path):
        os.remove(save_path)
    bpy.ops.wm.save_as_mainfile(filepath=save_path)


# To register
def register():
    bpy.utils.register_class(SaveBlenderFile)


# To unregister
def unregister():
    bpy.utils.unregister_class(SaveBlenderFile)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
