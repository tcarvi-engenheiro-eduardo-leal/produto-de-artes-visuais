# <pep8-80 compliant>
import sys

# Class
class AddPath:
    """Add paths for the program"""

    # Class execution
    @classmethod
    def add(cls):
        _dir_src_add()
        _dir_src_evaluate()
        _dir_src_geometry()
        _dir_src_io()
        _dir_src_list()
        _dir_src_model()
        _dir_src_move()
        _dir_src_input_data()
        print("Python sys.path:")
        for path in sys.path:
            print(path)
        return {'FINISHED'}

# non-public method
def _update_path_to_unix(windows_path):
    windows_path = windows_path.replace('C:\\libs\\python\\src\\', '/Users/eduardosantosleal/src/')
    windows_path = windows_path.replace('\\', '/')
    return windows_path


# non-public method
def _dir_src_add():
    t_dir_src_add = \
        'C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\add'
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        t_dir_src_add = _update_path_to_unix(t_dir_src_add)
    if t_dir_src_add not in sys.path:
        sys.path.append(t_dir_src_add)

# non-public method
def _dir_src_evaluate():
    t_dir_src_evaluate = \
        'C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\evaluate'
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        t_dir_src_evaluate = _update_path_to_unix(t_dir_src_evaluate)
    if t_dir_src_evaluate not in sys.path:
        sys.path.append(t_dir_src_evaluate)

# non-public method
def _dir_src_geometry():
    t_dir_src_geometry = \
        'C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\geometry'
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        t_dir_src_geometry = _update_path_to_unix(t_dir_src_geometry)
    if t_dir_src_geometry not in sys.path:
        sys.path.append(t_dir_src_geometry)

# non-public method
def _dir_src_io():
    t_dir_src_io = \
        'C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\io'
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        t_dir_src_io = _update_path_to_unix(t_dir_src_io)
    if t_dir_src_io not in sys.path:
        sys.path.append(t_dir_src_io)


# non-public method
def _dir_src_list():
    t_dir_src_list = \
        'C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\list'
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        t_dir_src_list = _update_path_to_unix(t_dir_src_list)
    if t_dir_src_list not in sys.path:
        sys.path.append(t_dir_src_list)


# non-public method
def _dir_src_model():
    t_dir_src_model = \
        'C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\model'
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        t_dir_src_model = _update_path_to_unix(t_dir_src_model)
    if t_dir_src_model not in sys.path:
        sys.path.append(t_dir_src_model)


# non-public method
def _dir_src_move():
    t_dir_src_move = \
        'C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\scripts\\move'
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        t_dir_src_move = _update_path_to_unix(t_dir_src_move)
    if t_dir_src_move not in sys.path:
        sys.path.append(t_dir_src_move)


# non-public method
def _dir_src_input_data():
    t_dir_src_input_data = \
        'C:\\libs\\python\\src\\github.com\\tcarvi-engenheiro-eduardo-leal\\produto-de-artes-visuais\\blender_scripts\\input_data'
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        t_dir_src_input_data = _update_path_to_unix(t_dir_src_input_data)
    if t_dir_src_input_data not in sys.path:
        sys.path.append(t_dir_src_input_data)

# Se este script for chamado pelo próprio arquivo, 
#   como fluxo de execução "$ python file_name", 
#   executa-se apenas a função AddPath.add().
if __name__ == "__main__":
    AddPath.add()
