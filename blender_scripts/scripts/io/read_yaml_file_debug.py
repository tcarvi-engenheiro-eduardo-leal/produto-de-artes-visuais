# <pep8-80 compliant>
# CLI: Blender -b --python-expr "import pdb; pdb.run('exec(open(\"./scripts/io/read_yaml_file.py\").read())')"
# Parada: pdb.set_trace()
import sys
import bpy
import unittest

print("Versão do Blender:", bpy.app.version_string)
print("Versão do bpy:", bpy.app.version_string.split(' ')[0])

dependency_path = '/Users/eduardosantosleal/.local/lib/python3.10/site-packages'
if dependency_path not in sys.path:
    sys.path.append(dependency_path)
# Dependência pyaml-21.10.1
import yaml

class TestYamlFile(unittest.TestCase):
    def test(self):
        with open("./scripts/io/testeFile.yaml", "r") as f:
            dados = yaml.load(f, Loader=yaml.FullLoader)
            comandos = dados.get("comandos")
            self.assertEqual(len(comandos), 7)
            self.assertEqual(comandos[0].get("name"), "DesenharRetoLinhaEmX")
            self.assertEqual(comandos[0].get("deslocamento"), "8.5")
            self.assertEqual(comandos[1].get("name"), "DeslocarRetoEmX")
            self.assertEqual(comandos[1].get("deslocamento"), "3")


# Class
class ReadYamlFile(bpy.types.Operator):
    """READ yaml file"""
    bl_idname = "my_category.read_yaml_file"
    bl_label = "Read Yaml File"
    bl_options = {'REGISTER', 'UNDO'}

    # Importar bpy.types.Operator localmente para evitar referência circular
    from bpy.types import Operator

    def execute(self, context):
        pdb.set_trace()
        estrutura = _read_yaml_file("inputPlantaBaixa.yaml")
        return {'FINISHED'}

# non-public method
def _read_yaml_file(yaml_file_name):
    with open(yaml_file_name, 'r') as stream:
        try:
            yaml_contents = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return yaml_contents


# To register
def register():
    bpy.utils.register_class(ReadYamlFile)


# To unregister
def unregister():
    bpy.utils.unregister_class(ReadYamlFile)


if __name__ == "__main__":
    unittest.main()
