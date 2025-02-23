# <pep8-80 compliant>
# CLI: Blender --factory-startup --background -noaudio --python ./scripts/io/read_yaml_file_test.py -- --verbose
import sys
import os
import unittest
read_yaml_file_directory = os.getcwd()+"/scripts/io"
if read_yaml_file_directory not in sys.path:
    sys.path.append(read_yaml_file_directory)
from read_yaml_file import ReadYamlFile

class TestYamlFile(unittest.TestCase):
    def test(self):
        dados = ReadYamlFile.execute("./input_data/input_planta_structure.yaml")
        print("dados=" + dados)
        comandos = dados.get("comandos")
        print("dados['comandos']=" + dados['comandos'])
        self.assertEqual(len(comandos), 7)
        self.assertEqual(comandos[0].get("comando"), "DesenharRetoLinhaEmX")
        self.assertEqual(comandos[0].get("deslocamento"), "8.5")
        self.assertEqual(comandos[1].get("comando"), "DeslocarRetoEmX")
        self.assertEqual(comandos[1].get("deslocamento"), "3")

if __name__ == "__main__":
    unittest.main()
