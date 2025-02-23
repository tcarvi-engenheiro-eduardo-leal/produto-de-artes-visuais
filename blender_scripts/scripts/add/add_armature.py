# <pep8-80 compliant>
import bpy


# Class
class AddArmature:
    """Create a new Armature Object from data: bones"""

    # Class execution
    @classmethod
    def add(cls):
        _add_object()
        return {'FINISHED'}


# non-public method
def _add_object():
    # TODO - To define input
    # Armatures can get confusing, there are bones
    # as well as edit bones that contain the basic armature structure
    # and properties
    # and then there are pose bones that stores constraints
    # and animation data for all the action.
    # TODO - To define input
    # obj.data.edit_bones # adding, deleting, positioning bones
    # obj.data.bones # adjusting bone properties
    # obj.pose.bones # adding constraints, custom shapes...
    # TODO - To define input
    # bone1 = armature_data.edit_bones.new('bone1')
    # a new bone will have zero length and not be kept
    # move the head/tail to keep the bone
    # bone1.head = (1.0, 1.0, 0.0)
    # bone1.tail = (1.0, 1.0, 1.0)
    # bone2 = armature_data.edit_bones.new('bone2')
    # a new bone will have zero length and not be kept
    # move the head/tail to keep the bone
    # bone2.head = (1.0, 1.0, 0.0)
    # bone2.tail = (1.0, 1.0, 1.0)
    # TODO - To define input
    # make the custom bone shape
    # bm = bmesh.new()
    # bmesh.ops.create_circle(bm, cap_ends=False, diameter=0.2, segments=8)
    # me = bpy.data.meshes.new("Mesh")
    # bm.to_mesh(me)
    # bm.free()
    # b2_shape = bpy.data.objects.new("bone2_shape", me)
    # bpy.context.scene.objects.link(b2_shape)
    # b2_shape.layers = [False]*19+[True]
    # TODO - To define input
    # use pose.bones for custom shape
    # arm_obj.pose.bones['bone2'].custom_shape = b2_shape
    # use data.bones for show_wire
    # arm_obj.data.bones['bone2'].show_wire = True
    t_data = bpy.data.armatures.new(name="armatureData")
    t_object = bpy.data.objects.new(name="armatureObject", object_data=t_data)
    bpy.context.scene.collection.objects.link(t_object)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)


# To register
def register():
    bpy.utils.register_class(AddArmature)


# To unregister
def unregister():
    bpy.utils.unregister_class(AddArmature)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
