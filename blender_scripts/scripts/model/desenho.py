# <pep8-80 compliant>
import io
from enum import Enum

# from comando_desenho import EnumComandoDesenho

# Class
class Desenho(object):
    """Estrutura de Desenho"""

    def __init__(self, json_estrutura):
        self.__estrutura = self.__gera_estrutura(json_estrutura)

    def __gera_estrutura(self, json_estrutura):
        estrutura_em_processamento = []
        for obj in json_estrutura["comandos"]:
            anguloReto = 0
            if obj["comando"].endswith("Y"):
                anguloReto = 90
            print("anguloReto = ", anguloReto)
            estrutura_em_processamento.append(
                [
                    EnumComandoDesenho[obj["comando"]].value,
                    float(obj.get("deslocamento", 0)),
                    float(obj.get("angulo", anguloReto))
                ]
            )
        return estrutura_em_processamento

    @property
    def estrutura(self):
        return self.__estrutura


# Class
class EnumComandoDesenho(Enum):
    DeslocarRetoEmX = 0
    DeslocarRetoEmY = 1
    DeslocarRetoEmZ = 2
    DeslocarInclinadoEmX = 10
    DeslocarInclinadoEmY = 11
    DeslocarInclinadoEmZ = 12
    DesenharRetoLinhaEmX = 20
    DesenharRetoLinhaEmY = 21
    DesenharRetoLinhaEmZ = 22
    DesenharInclinadoLinhaEmX = 30
    DesenharInclinadoLinhaEmY = 31
    DesenharInclinadoLinhaEmZ = 32
    DesenharRetanguloEmX = 40
    DesenharRetanguloEmY = 41
    DesenharRetanguloEmZ = 42
    DesenharParalelogramoEmX = 50
    DesenharParalelogramoEmY = 51
    DesenharParalelogramoEmZ = 52

# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name", 
#   executa-se a função AddPath.add()
#   e depois se executa o teste desta classe
if __name__ == "__main__":
    import sys
    
    t_adding_paths = \
        'C:\\libs\\python\\src\\github.com\\tgraphics\\scripts\\background_jobs'
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        t_adding_paths = t_adding_paths.replace('C:', '')
        t_adding_paths = t_adding_paths.replace('\\', '/')
    if t_adding_paths not in sys.path:
        sys.path.append(t_adding_paths)
    from add_path import AddPath
    AddPath.add()
    
    import json
    with open('C:\\libs\\python\\src\\github.com\\tgraphics\\input_data\\input_planta_structure.json') as json_data_file:
        t_json_structure = json.load(json_data_file)
        print(t_json_structure)
        desenho = Desenho(t_json_structure)
        print(desenho.estrutura)