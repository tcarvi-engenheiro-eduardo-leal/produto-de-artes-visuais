# <pep8-80 compliant>
import sys
import json

t_adding_paths = \
    'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\background_jobs'
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    t_adding_paths = t_adding_paths.replace('C:', '')
    t_adding_paths = t_adding_paths.replace('\\', '/')
if t_adding_paths not in sys.path:
    sys.path.append(t_adding_paths)
from add_path import AddPath
AddPath.add()

from desenho import Desenho

# Class
class InputPlantaStruture:
    """Add paths for the program"""

    # Class execution
    @classmethod
    def receive(cls):
        t_diretorio_input_planta = 'C:\\libs\\python\\src\\github.com\\tgraphics\\input_data'
        if(sys.platform.startswith('linux') or sys.platform.startswith('darwin')):
            t_diretorio_input_planta = _update_path_to_unix(t_diretorio_input_planta)
        estrutura = []
        with open('C:\\libs\\python\\src\\github.com\\tgraphics\\input_data\\input_planta_structure.json') as json_data_file:
            t_json_structure = json.load(json_data_file)
            desenho = Desenho(t_json_structure)
            estrutura = desenho.estrutura
        return estrutura


# non-public method
def _update_path_to_unix(windows_path):
    windows_path = windows_path.replace('C:', '')
    windows_path = windows_path.replace('\\', '/')
    return windows_path


# To register
def register():
    bpy.utils.register_class(InputPlantaStruture)


# To unregister
def unregister():
    bpy.utils.unregister_class(InputPlantaStruture)


# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name",
#   executa-se apenas a função register()
# Pode-se também incluir testes neste método
if __name__ == "__main__":
    # register()
    input = InputPlantaStruture()
    print(input.receive())