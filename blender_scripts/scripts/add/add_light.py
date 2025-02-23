# <pep8-80 compliant>
import bpy


# Class
class AddLight:
    """ADD light with input location"""

    # Class execution
    @classmethod
    def add(cls, t_initial_position):
        _add_light(t_initial_position)
        return {'FINISHED'}


# non-public method
def _add_light(t_initial_position):
    t_data = bpy.data.lights.new("lightData", 'POINT')
    t_object = bpy.data.objects.new(name="lightObject", object_data=t_data)
    t_object.location = t_initial_position
    bpy.context.scene.collection.objects.link(t_object)


# To register
def register():
    bpy.utils.register_class(AddLight)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddLight)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
