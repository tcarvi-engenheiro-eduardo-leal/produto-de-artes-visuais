# <pep8-80 compliant>
import bpy
import os


# Class
class SaveRendering:
    """Save rendering file"""

    # Class execution
    @classmethod
    def save(cls, t_rendering_file_name):
        _save_rendering(t_rendering_file_name)
        return {'FINISHED'}


# non-public method
def _save_rendering(t_rendering_file_name):
    t_save_dir = os.path.join(
        os.path.abspath("."),
        "render_output"
        )
    if not os.path.exists(t_save_dir):
        os.mkdir(t_save_dir)
    t_save_path = os.path.join(
        os.path.abspath("."),
        "render_output\\" + t_rendering_file_name
        )
    # TODO - To define input
    # TODO - To add
    t_render = bpy.context.scene.render
    t_render.use_file_extension = True
    t_render.filepath = t_save_path
    bpy.ops.render.render(write_still=True)


# To register
def register():
    bpy.utils.register_class(SaveRendering)


# To unregister
def unregister():
    bpy.utils.unregister_class(SaveRendering)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
