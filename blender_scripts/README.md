# Blender Scripts

## Script básico de Verificação do Ambiente, em Background
/Applications/Blender.app/Contents/MacOS/Blender --background --python ./scripts/verificar_ambiente.py

## Init Background Jobs
/Applications/Blender.app/Contents/MacOS/Blender --background --python blender_scripts/scripts/init_background_jobs/add_path.py

Python3.11

#### Blender library modules:
- `\_bpy`
- `bl\_operators`
- `cycles`

## Execução de Scripts


cd nao_enviar



- Requirements: 
    - `install blender` ( https://www.blender.org/ )
    - `install python` ( https://www.python.org/downloads/ )
    - `install git`
- Installation Windows:
    - `mkdir C:\libs\python\src\github.com\`
    - `cd C:\libs\python\src\github.com\`
    - `git clone https://github.com/tcarvi/tgraphics.git`
    - `cd tgraphics`
    - `pip install --upgrade pip`
    - `pip install -r requirements.txt`
- Installation MAC:
    - Python Installation:
        - /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        - (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/eduardosantosleal/.zprofile
        - eval "$(/opt/homebrew/bin/brew shellenv)"
        - source ~/.zprofile
        - brew update
        - Brew installation:
            - Example usage:
                - brew search TEXT|/REGEX/
                - brew info [FORMULA|CASK...]
                - brew install FORMULA|CASK...
                - brew update
                - brew upgrade [FORMULA|CASK...]
                - brew uninstall FORMULA|CASK...
                - brew list [FORMULA|CASK...]
            - Troubleshooting:
                - brew config
                - brew doctor
                - brew install --verbose --debug FORMULA|CASK
            - Contributing:
                - brew create URL [--no-fetch]
                - brew edit [FORMULA|CASK...]
            - Further help:
                - brew commands
                - brew help [COMMAND]
                - man brew
                - https://docs.brew.sh
        - brew install python@3.9
        - python3.9 --version
            - Python has been installed as /opt/homebrew/bin/python3.9 
            - Unversioned and major-versioned symlinks `python`, `python3`, `python-config`, `python3-config`, `pip`, `pip3`, etc. pointing to `python3.9`, `python3.9-config`, `pip3.9` etc., respectively, have been installed into /opt/homebrew/opt/python@3.9/libexec/bin
            - You can install Python packages with `pip3.9 install <package>`. They will install into the site-package directory /opt/homebrew/lib/python3.9/site-packages
            - tkinter is no longer included with this formula, but it is available separately: `brew install python-tk@3.9`
            - If you do not need a specific version of Python, and always want Homebrew's `python3` in your PATH: `brew install python3`
    - `mkdir ~/src/github.com/tcarvi`
    - `cd ~/src/github.com/tcarvi`
    - `git clone https://github.com/tcarvi/tgraphics.git`
    - `cd tgraphics`
    - Blender Installation:
        - Instalar Aplicação Blender do site oficial
        - Acrescente binário do executor no path do MAC:
            - (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/eduardosantosleal/.zprofile
            - eval "$(/opt/homebrew/bin/brew shellenv)"
            - source ~/.zprofile
    - `/Applications/Blender.app/Contents/MacOS\Blender --background --python-use-system-env`
- Default output folders: 
    - rendering output: `render_output/`
    - saving blender file:  `blender_projects/`

/Applications/Blender.app/Contents/MacOS/Blender --background --python-use-system-env -b -- -P scripts/background_jobs/add_path.py -P scripts/background_jobs/add_objects_from_input_data.py
- Ver linhas de comando para geração automatizada do projeto blender em:
    - /Applications/Blender.app/Contents/MacOS/Blender -b -- -P scripts/background_jobs/add_path.py -P scripts/b
ackground_jobs/add_objects_from_input_data.py
    - ``` console
    http://localhost:3000/docs/processos/etapa2-producao-insumos
    ```  
