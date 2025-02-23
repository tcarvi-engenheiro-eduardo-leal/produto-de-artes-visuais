# <pep8-80 compliant>
import bpy
import time


# Class
class EvaluateTime:
    """Evaluate time of script execution"""

    # Class execution 1
    @classmethod
    def init(cls, t_time):
        _init_time_counter(t_time)
        return {'FINISHED'}

    # Class execution 2
    @classmethod
    def evaluate_time(cls, t_time_started):
        _evaluate_time(t_time_started)
        return {'FINISHED'}


# non-public method
def _init_time_counter(t_time_start):
    t_time_start = time.time()


# non-public method
def _evaluate_time(t_time_started):
    print("Script terminado em: %.4f sec" % (time.time() - t_time_started))


# To register
def register():
    bpy.utils.register_class(EvaluateTime)


# To unregister
def unregister():
    bpy.utils.unregister_class(EvaluateTime)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register().
if __name__ == "__main__":
    register()
