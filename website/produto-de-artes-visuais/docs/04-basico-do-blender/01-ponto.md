# Ponto 3D no Blender

## Como Criar um Ponto no Blender (Vértice)

---

### **Método 1: Usando o Modo Edição (Criação Manual)**
1. **Abrir novo projeto**:
   - Inicie o Blender e selecione "General" ou pressione `Ctrl + N`

2. **Entrar no Modo Edição**:
   - Selecione o cubo padrão
   - Pressione `Tab` para alternar para o Modo Edição

3. **Criar um novo vértice**:
   - Pressione `Shift + A` > Mesh > Single Vert > Add Single Vert
   - OU use o atalho `Ctrl + LMB` para criar um vértice na posição do cursor 3D

4. **Posicionar o ponto**:
   - Selecione o vértice com `RMB`
   - Mova com a ferramenta Move (`G`)
   - Para precisão, digite as coordenadas no painel Item (N) > Transform

---

### **Método 2: Usando Partículas (Para Múltiplos Pontos)**
1. **Adicionar objeto base**:
   - `Shift + A` > Mesh > Plane
   - Reduza seu tamanho (`S` + valor pequeno como 0.01)

2. **Adicionar sistema de partículas**:
   - Na aba Particle Properties
   - Clique em `+` para adicionar novo sistema
   - Defina:
     - Emission > Number: 1
     - Render As > Object

3. **Configurar como ponto único**:
   - Em Render > Show Emitter: Desligado
   - Em Render > Scale: 0.1 (para tamanho pequeno)

---

### **Método 3: Usando Geometria de Pontos (Avançado)**
1. **Criar geometria de pontos**:
   - `Shift + A` > Mesh > Point Cloud
   - OU use Geometry Nodes para gerar pontos

2. **Ajustar visualização**:
   - No painel Viewport Display
   - Defina Display As > Points
   - Ajuste Size para valor pequeno (0.01)

---

### **Dicas Extras**
- **Visualização clara**:
  - No modo Object, selecione o vértice
  - Painel Viewport Display > ajuste Size para melhor visibilidade

- **Precisão absoluta**:
  - Use o painel Transform (N) para inserir coordenadas exatas (X,Y,Z)

- **Material para pontos**:
  - Crie material emissivo para melhor visualização
  - Base Color: Vermelho brilhante
  - Emission Strength: 5.0

---

### **Exemplo Prático**
1. `Tab` para entrar no Modo Edição
2. `Ctrl + LMB` para criar vértice na posição desejada
3. `G` + `Z` + `1` para mover exatamente 1 unidade no eixo Z
4. Painel Item (N) > Transform > Location: (0,0,0) para centralizar

**Resultado**: Ponto 3D preciso na cena!

Precisa de ajuda para conectar pontos ou criar formas complexas? Posso explicar como usar curvas ou geometria procedural no Blender!