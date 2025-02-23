# <pep8-80 compliant>
import bpy
import mathutils


# Class
class MoveEntryPoint:
    """Move entry point"""

    # Class execution 1
    @classmethod
    def centralizar(cls):
        _center_entry_point()
        return {'FINISHED'}

    # Class execution 2
    @classmethod
    def mover(cls, t_plus_x, t_plus_y, t_plus_z):
        _increment_position_entry_point(
            t_plus_x,
            t_plus_y,
            t_plus_z
            )
        return {'FINISHED'}

    # Class execution 3
    @classmethod
    def rotacionar(cls, t_rot_plus_x, t_rot_plus_y, t_rot_plus_z):
        _increment_rot_euler_entry_point(
            t_rot_plus_x,
            t_rot_plus_y,
            t_rot_plus_z
            )
        return {'FINISHED'}


# non-public method
def _center_entry_point():
    bpy.context.scene.cursor.rotation_mode = 'XYZ'
    bpy.context.scene.cursor.location = Vector((0.0, 0.0, 0.0))
    bpy.context.scene.cursor.rotation_euler = Vector((0.0, 0.0, 0.0))


# non-public method
def _increment_position_entry_point(t_plus_x, t_plus_y, t_plus_z):
    bpy.context.scene.cursor.location[0] += t_plus_x
    bpy.context.scene.cursor.location[1] += t_plus_y
    bpy.context.scene.cursor.location[2] += t_plus_z


# non-public method
def _increment_rot_euler_entry_point(t_rot_plus_x, t_rot_plus_y, t_rot_plus_z):
    bpy.context.scene.cursor.rotation_euler[0] += t_rot_plus_x
    bpy.context.scene.cursor.rotation_euler[1] += t_rot_plus_y
    bpy.context.scene.cursor.rotation_euler[2] += t_rot_plus_z


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
