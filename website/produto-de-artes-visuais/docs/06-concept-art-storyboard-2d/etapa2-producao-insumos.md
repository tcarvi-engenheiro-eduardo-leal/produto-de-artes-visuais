# Etapa 2 - Produção (Insumos para Modelagem)

### Cadastramento do Cenário
- Ambiente geométrico a ser pensado:
    - Eixo tridimensional X que segue positivo da sua frente para posição direita ortogonal.
    - Eixo tridimensional Y que segue positivo da sua frente para posição mais em frente, seguindo em reta.
    - Eixo tridimensional Z que segue positivo da sua frente para posição acima (superior) ortogonal.
    - O deslocamento pode ser informado tanto nos eixos X,Y e Z quanto no próprio eixo do desenho. É obrigatório informar o ângulo da sequência do desenho. O aplicativo calculará o deslocamento real nos eixos ortogonais e criará o desenho inclinado. 
        - Exemplo de instrução:
            - comando:  `DeslocarEmX`, 
            - deslocamento: `3 metros`,
            - anguloRadiano: `4/3`
        - É igual à instrução:
            - comando: `DeslocarEmXInclinado`,
            - deslocamento: `5 metros`,
            - anguloRadiano: `4/3`
        - No primeiro caso, o ângulo serve para calcular o **REAL DeslocamentoEmY**, considerando como fixo o **DeslocamentoEmX que já é o REAL**. Assim se produzirá um desenho inclinado.
        - No segundo caso, serve tanto par calcular o **REAL DeslocamentoEmY** quanto o **REAL DeslocamentoEmX**. Foi passado para o aplicativo apenas o comprimento do eixo do desenho, mas não suas medidas globais de "deslocamento". O app faz tal cálculo.
        - Por trigonometria básica, considera-se:
            - deslocamentoX =  deslocamentoLogitudinal multiplicado por coseno(ângulo de inclinação).
            - Mas, depois de localizar o *script* em uma estrutura de boa legibilidade em projeto Python, o *script* deve ser melhorado com o uso de:
                - https://en.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions#Quaternions
                - https://docs.blender.org/api/249PythonDoc/Mathutils.Quaternion-class.html
    - Todos os comandos refletem a realidade do trabalho de cadastramento arquitetônico e faz os cálculos necesssários para o processamento da computação gráfica do Blender.
    - Assim como o comando DeslocamentoEmX, todos os demais comandos devem ser informados de forma intuitiva e sintética. A *engine* tcarviAI terá condições de processar a entrada de dados e gerar imagens, animações, vídeos e interatividades.
- Começo do cadastramento:
    - Escolhe-se posição esquerda na frente, onde estará o centro do eixo tridimensional.
        - Medidas positivas para direira e para cima. 
        - E **também positiva entrando no espaço do desenho, seguindo para o fundo do mesmo**.
- Fluxo de desenho:
    - Informa-se o comando a ser passado para a solução de AI (tcarviAI):
    - `Comando`: `text`
        - DeslocarRetoEmX
        - DeslocarRetoEmY
        - DeslocarRetoEmZ
        - DeslocarInclinadoEmX
        - DeslocarInclinadoEmY
        - DeslocarInclinadoEmZ
        - DesenharRetoLinhaEmX
        - DesenharRetoLinhaEmY
        - DesenharRetoLinhaEmZ
        - DesenharInclinadoLinhaEmX
        - DesenharInclinadoLinhaEmY
        - DesenharInclinadoLinhaEmZ
        - DesenharRetanguloEmX
        - DesenharRetanguloEmY
        - DesenharRetanguloEmZ
        - DesenharParalelogramoEmX
        - DesenharParalelogramoEmY
        - DesenharParalelogramoEmZ
    - `SubcomandoNecessário`: `value`
        - Sendo `SubcomandoNecessário`
            - Nome de subcomando necessário para processamento do comando pai indicado. 
        - Sendo `value`
            - Número inteiro ou float

# tgraphics  

- Requirements: 
    - `install blender`
    - `install python`
    - `install git`
- Installation:
    - ``` console
    mkdir C:\libs\python\src\github.com\
    ```
    - ``` console
    cd C:\libs\python\src\github.com\
    ```
    - ``` console
    git clone https://github.com/tcarvi/tgraphics.git
    ```
    - ``` console
    cd tgraphics
    ```
    - ``` console
    pip install --upgrade pip
    ```
    - ``` console
    pip install -r requirements.txt
    ```
- Default output folders: 
    - rendering output: `render_output/`
    - saving blender file:  `blender_projects/`

#### Windows - CLI (Command Line Interface):
###### Se utilizados, os parâmetros -s e -r devem seguir a ordem definida.
```console
blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_objects_from_input_data.py
```  
``` console
blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_objects_from_input_data.py -- -s="blenderFileName.blend" -r="renderFileName"
```  
``` console
blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_objects_from_input_data.py -- -s="blenderFileName.blend"
```  
``` console
blender --background --factory-startup --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_path.py --python C:\libs\python\src\github.com\tgraphics\scripts\background_jobs\add_objects_from_input_data.py -- -r="renderFileName"
```  

#### Linux - CLI (Command Line Interface)
``` console
blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data.py
```  

###### Se utilizados, os parâmetros -s e -r devem seguir a ordem definida.
``` console
blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data
```  
``` console
blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data -- -s="blenderFileName.blend" -r="renderFileName"
```
``` console
blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data -- -s="blenderFileName.blend"
```  
``` console
blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data -- -r="renderFileName"
```  

#### MAC OSX - CLI (Command Line Interface)
``` console
/Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_path.py --python /libs/python/src/github.com/tgraphics/scripts/background_jobs/add_objects_from_input_data.py
```  

###### Se utilizados, os parâmetros -s e -r devem seguir a ordem definida.

###### Notice:
- `--factory-startup` is used to avoid the user default settings from interfering with automated scene generation.
- `--` causes blender to ignore all following arguments so python can use them.
- See blender --help for details.