# <pep8-80 compliant>
import bpy


# Class
class AddMaterial:
    """Add material to an object"""

    # Class execution
    @classmethod
    def add(cls, t_object, t_material_name):
        _add_material(t_object, t_material_name)
        return {'FINISHED'}


# non-public method
def _add_material(t_object, t_material_name):
    # print("Adding material ...")
    # Get material
    t_material = bpy.data.materials.get(t_material_name)
    if t_material is None:
        # create and define material
        t_material = bpy.data.materials.new(name=t_material_name)
        t_material.diffuse_color = (0.0, 0.502, 0.6863, 1)
        # print(t_material_name)
    # Assign a material to an object
    if t_object.data.materials:
        # assign to 1st material slot
        t_object.data.materials[0] = t_material
    else:
        # no slots. Append to 1st material slot
        t_object.data.materials.append(t_material)
    # print("Added material")


# To register
def register():
    bpy.utils.register_class(AddMaterial)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddMaterial)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
