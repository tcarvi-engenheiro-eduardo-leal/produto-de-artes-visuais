# <pep8-80 compliant>
import sys
import os
import unittest

# to get AddPath from file add_path.py in current working directory
current_directory = os.getcwd()
if current_directory not in sys.path:
    sys.path.append(current_directory)
from add_path import AddPath
if current_directory in sys.path:
    sys.path.remove(current_directory)

def _get_lista_de_diretorios():
    lista = []
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        lista.append('/Users/eduardosantosleal/src/github.com/tcarvi-engenheiro-eduardo-leal/produto-de-artes-visuais/blender_scripts/scripts/add')
        lista.append("/Users/eduardosantosleal/src/github.com/tcarvi-engenheiro-eduardo-leal/produto-de-artes-visuais/blender_scripts/scripts/evaluate")
        lista.append("/Users/eduardosantosleal/src/github.com/tcarvi-engenheiro-eduardo-leal/produto-de-artes-visuais/blender_scripts/scripts/geometry")
        lista.append('/Users/eduardosantosleal/src/github.com/tcarvi-engenheiro-eduardo-leal/produto-de-artes-visuais/blender_scripts/scripts/io')
        lista.append("/Users/eduardosantosleal/src/github.com/tcarvi-engenheiro-eduardo-leal/produto-de-artes-visuais/blender_scripts/scripts/list")
        lista.append("/Users/eduardosantosleal/src/github.com/tcarvi-engenheiro-eduardo-leal/produto-de-artes-visuais/blender_scripts/scripts/model")
        lista.append("/Users/eduardosantosleal/src/github.com/tcarvi-engenheiro-eduardo-leal/produto-de-artes-visuais/blender_scripts/scripts/move")
        lista.append("/Users/eduardosantosleal/src/github.com/tcarvi-engenheiro-eduardo-leal/produto-de-artes-visuais/blender_scripts/input_data")
    else:
        lista.append('C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\add')
        lista.append("C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\evaluate")
        lista.append("C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\geometry")
        lista.append('C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\io')
        lista.append("C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\list")
        lista.append("C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\model")
        lista.append("C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\move")
        lista.append("C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\input_data")
    return lista

class TestInclusaoDePaths(unittest.TestCase):
    def test_inclusao_de_paths(self):
        lista = _get_lista_de_diretorios()
        for diretorio in lista:
            self.assertIn(diretorio, sys.path, "Problema na inclusão de " + diretorio + ". Verifique!")
            print("Verificado: " + diretorio)

if __name__ == "__main__":
    AddPath.add()
    unittest.main()
