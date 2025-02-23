# <pep8-80 compliant>
import argparse
import bpy
import os
import sys
import unittest

# from add_curve import AddCurve
# from add_surface import AddSurface
# from add_metaball import AddMetaball
# from add_text import AddText
# from add_grease_pencil import AddGreasePencil
# from add_armature import AddArmature
# from add_lattice import AddLattice
# from add_empty import AddEmpty
# from add_image import AddImage
# from add_light import AddLight
# from add_light_probe import AddLightProbe
# from add_camera import AddCamera
# from add_speaker import AddSpeaker
# from add_force_field import AddForceField
# from save_blender_file import SaveBlenderFile
# from save_rendering import SaveRendering
# from input_planta_structure import InputPlantaStruture
# from input_lighting_positions import t_lighting
# from list_objects import ListObjects
# from list_scenes import ListScenes
# from list_materials import ListMaterials
# from evaluate_time import EvaluateTime

# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name", 
#   executa-se apenas a função AddObjetcsFromInputData.add().
if __name__ == "__main__":
    # to get AddPath from file add_path.py in current working directory
    current_directory = os.getcwd()
    if current_directory not in sys.path:
        sys.path.append(current_directory)
    #to get all paths of this python program
    from add_path import AddPath
    AddPath.add()
    from add_objects_from_input_data import AddObjetcsFromInputData
    from add_mesh import AddMesh
    if current_directory in sys.path:
        sys.path.remove(current_directory)
    unittest.main()
