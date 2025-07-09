# Teoria

- Blender’s comprehensive array of modeling tools make creating, transforming, sculpting and editing your models a breeze.
- Blender's modeling tools include:
    - Keyboard shortcuts for a fast workflow
    - N-Gon support
    - Edge slide, collapse and dissolve
    - Grid and Bridge fill
    - Python scripting for custom tools and add-ons

### Tipos de Modelagem:
- Orgânica
- Hardsurface
- Orgânica hardsurface

### Modificadores
- Generate
    - Array
        - Replicar Objetos
        - Pode-se aplicar mais de uma vez este modificador
        - Pode-se usar um objeto vazio para descrever diferença usada na replicação do modificador
    - Bevel
        - Pode ser relevante usar apply antes deste modificador 
        - Aplicação em todo o objeto.
        - Adiciona detalhes na malha sem processos destrutivos.
        - Principais termos: width, segments
    - Bolean
        - Adicionar ou remover malha
        - Uso em último caso, para não gerar complexidade no começo da modelagem
        - Depois deve ser aplicado
    - Mirror
        - Pode ser relevante usar apply antes deste modificador 
        - Pode-se escolhar base de espelhamento
        - E pode-se escolher eixos de espelhamento
    - Solidify
        - Para gerar espessura em objetos
    - Subdivision Surface
        - Para criar formas mais orgânicas
            - Simple: apenas divisão de polígonos
            - Catmull-Clark: Arredonda a malha
        - Subdivision: 
            - Viewport: número subdivisoes de cubo, por exemplo
            - Render: número de subdivisioes para o render.
            - Número 4 ou 5 já são pesados para  processamento do render. Para a modelagem, usa-se o viewport com 2.
            - Pode ser necessário uma edge de contenção para que as "quinas" que sejam suaves, e não a forma em si.
- Deform
    - Curve
        - Deformação de acordo com uma curva
        - Deve-se escolher o eixo correto.
        - Depois deve-se alterar o modelo para melhor resultado

### Problemas de Malha:
- 
