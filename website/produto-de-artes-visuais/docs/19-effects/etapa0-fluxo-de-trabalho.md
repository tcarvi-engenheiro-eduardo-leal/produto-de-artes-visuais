---
title: Fluxo de Trabalho
sidebar_position: 0
---

### Pensar nos cenários e nos objetos
- Criar roteiro do enredo, com desenho de cenas e com detalhamentos necessários.
- Compilar o roteiro com definição de cenas: objetos e posição geométrica.

### Automatizar criação de cenários e objetos Low Poly
- Identificar comandos a serem passados para engine tcarviAI
- Manipular arquivos de input
- Enviar comandos para engine tcarviAI
- Avaliar produtos *Low Poly* gerados
    - Quantificar vertex, edges e faces
    - Corrigir, no arquivo de input, a qualidade dos objetos, buscando superfícies com poucos quadrados.
    - Corrigir, no arquivo de input, a disposição dos objetos gerados.
- Renviar comandos para geração de cenas ***Low Poly***

#### Sobre técnica "Low Poly"
- Objetos iniciais da manipulação devem ter poucos polígonos
- Ondulações da borda de superfícies devem ser feitas com:
    - Novos ***edges*** próximo da curvatura, através de ***Loop Cut Slide*** ou de ***Knife***.
    - ***Extrude*** dos novos quadrados
- Visualização aproximada com o *preview* de "Shade Smooth"

#### Refactor contínuo da "blocagem" das cenas ***Low Poly*** geradas automaticamente
- Sem alterar a posição e a topologia dos objetos Low Poly já gerados, acrescentar outros objetos 3D necessários.
- Identificar comandos e incluí-los no arquivo de input, com a repetição da geração automática das cenas "Low Poly".
- Concluir blocagem quando não houver mais objetos e serem incluídos.

#### Vincular UVs nos objetos da cena
. . .

#### Incluir textura nos objetos
. . .

#### Lógica da automação:
- **Sempre buscar automatizar processos anteriores.**
- Apenas a parte artística, que não segue padronização de tamanhos e de simetria, não deve ser automatizada.
- O trabalho não-automatizado da criação artística deve se restringir à:
    - Acréscimo de objetos 3D no arquivo textual de *inputs*:
        - Escolha dos objetos a serem incluídos nas cenas
        - Identificação de tamanhos, distâncias e disposição destes objetos
        - Organização dos comandos a serem passados para a engine tcarviIAI
    - Correção e melhoria das texturas dos objetos "Low Poly" gerados automaticamente.
        - Documentar o trabalho artístico, para possível reexecução em cenas "Low Poly" geradas novamente.

---

#### Animação de Movimentos 
- Modelo:
    - ["Alita: Battle Angel", cena de Luta (1)](https://www.youtube.com/watch?v=Um8i-glXSzY&list=PLHZr_2UlXu7DQGrSztRSCzNEYpk6Nso4f&index=34&t=10s)
    - ["Alita: Battle Angel", cena de Luta (2)](https://www.youtube.com/watch?v=G95jgdwyq_Q&list=PLHZr_2UlXu7DQGrSztRSCzNEYpk6Nso4f&index=35)
    - ["Alita: Battle Angel", cena de Luta (3)](https://www.youtube.com/watch?v=Q0mNooEcpk0&list=PLHZr_2UlXu7DQGrSztRSCzNEYpk6Nso4f&index=36)
- Tecnologias: 
    - Live-action com imagens geradas por computador
    - Fusion Camera System, performance de captura facial
    - Simulcam
    - Pintura, modelagem, fotografia, texturização, animação e vídeo digital 
    - Efeitos visuais de pós-produção

---

#### Renderização do Visual
- Modelo:
    - ["Alita: Battle Angel", análise dos criadores](https://www.youtube.com/watch?v=J1SO6tOBA8Y&list=PLfPBohF1uFwrLlEa2PG097NzK9Om0ywft&index=12)
    - ["Alita: Battle Angel", cenários](https://www.youtube.com/watch?v=U3D2vmWD88w&list=PLfPBohF1uFwrLlEa2PG097NzK9Om0ywft&index=8)
    - ["Alita: Battle Angel", photorealism](https://www.youtube.com/watch?v=hOMuRopLgxg&list=PLfPBohF1uFwrLlEa2PG097NzK9Om0ywft&index=15)
    - ["Alita: Battle Angel", character and behaviour realism](https://www.youtube.com/watch?v=e3xdGx7Xa4w&list=PLfPBohF1uFwrLlEa2PG097NzK9Om0ywft&index=22)
    - ["Alita: Battle Angel", expression of emotion](https://www.youtube.com/watch?v=1AKW2aNSRs8&list=PLfPBohF1uFwrLlEa2PG097NzK9Om0ywft&index=13)
    - ["Alita: Battle Angel", expression of hero morality](https://www.youtube.com/watch?v=6PPTM1zRTy4&list=PLfPBohF1uFwrLlEa2PG097NzK9Om0ywft&index=21)

---

#### Edição do áudio: falas e soundtrack
- Modelo:
    - ["Alita: Battle Angel", cena com falas](https://www.youtube.com/watch?v=hZi3Jx2EZFU&list=PLfPBohF1uFwrLlEa2PG097NzK9Om0ywft&index=17)
    - ["Alita: Battle Angel", soundtrack - análise dos criadores](https://www.youtube.com/watch?v=5yBV0Fjtma8&list=PLfPBohF1uFwrLlEa2PG097NzK9Om0ywft&index=10)
    - ["Alita: Battle Angel", trailer](https://www.youtube.com/watch?v=w7pYhpJaJW8&list=PLfPBohF1uFwrLlEa2PG097NzK9Om0ywft&index=24)

---

#### Edição de áudio: música
- Modelo:
    - ["Alita: Battle Angel", com música empolgante (1)](https://www.youtube.com/watch?v=l264SGk15O0&list=PLHZr_2UlXu7DQGrSztRSCzNEYpk6Nso4f&index=37)
    - ["Alita: Battle Angel", com música empolgante (2)](https://www.youtube.com/watch?v=ZKkzEBtIoH8&list=PLHZr_2UlXu7DQGrSztRSCzNEYpk6Nso4f&index=38)

#### Referência de Excelente Qualidade
- ["Alita: Battle Angel", the creators](https://www.youtube.com/watch?v=pYwjokFLKx4&list=PLfPBohF1uFwrLlEa2PG097NzK9Om0ywft&index=26)
