# <pep8-80 compliant>
# CLI: Blender --factory-startup -b -P ./scripts/io/read_yaml_file.py

import sys
import bpy
dependency_for_yaml_path = '/Users/eduardosantosleal/.local/lib/python3.10/site-packages'
if dependency_for_yaml_path not in sys.path:
    sys.path.append(dependency_for_yaml_path)
import yaml

class ReadYamlFile():
    """READ yaml file"""
    bl_idname = "my_category.read_yaml_file"
    bl_label = "Read Yaml File"
    bl_rna = "bl rna"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def execute(cls, t_blender_yaml_file_name):
        estrutura = _read_yaml_file(t_blender_yaml_file_name)
        return estrutura

def _read_yaml_file(yaml_file_name):
    with open(yaml_file_name, 'r') as stream:
        try:
            yaml_contents = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return yaml_contents

def register():
    bpy.utils.register_class(ReadYamlFile)

def unregister():
    bpy.utils.unregister_class(ReadYamlFile)

if __name__ == "__main__":
    estruturaASerRecebida = ReadYamlFile.execute("input_data/input_planta_structure.yaml")
