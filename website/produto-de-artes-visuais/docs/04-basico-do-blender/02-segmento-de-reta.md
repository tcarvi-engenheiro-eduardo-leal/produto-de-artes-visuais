# Segmento de Reta 3D no Blender

## Como Criar uma Linha Reta no Blender

---

### **Método 1: Usando a Ferramenta de Vértices (Modo Edição)**
1. **Preparação inicial**:
   - Abra o Blender e delete o cubo padrão (`X` ou `Delete`)
   - Pressione `Shift + A` > Mesh > Plane para criar um objeto base

2. **Entrar no Modo Edição**:
   - Selecione o plano e pressione `Tab`
   - Delete todos os vértices existentes (`X` > Vertices)

3. **Criar a linha reta**:
   - Pressione `Ctrl + LMB` para criar o primeiro vértice (ponto inicial)
   - Mova o cursor e `Ctrl + LMB` novamente para o ponto final
   - Pressione `F` para criar uma aresta conectando os vértices

4. **Ajustes finais**:
   - Selecione a aresta com `RMB`
   - No painel Item (`N`), ajuste as coordenadas dos vértices para precisão

---

### **Método 2: Usando Curvas Bézier**
1. **Criar curva Bézier**:
   - `Shift + A` > Curve > Bézier
   - No Modo Edição (`Tab`), delete todos os pontos existentes

2. **Desenhar a linha**:
   - `Ctrl + LMB` para o ponto inicial
   - `Ctrl + LMB` para o ponto final
   - Pressione `Escape` para finalizar

3. **Converter para Mesh (opcional)**:
   - Com a curva selecionada: `Alt + C` > Mesh from Curve

---

### **Método 3: Usando Grease Pencil (Para Anotações)**
1. **Ativar Grease Pencil**:
   - Pressione `Shift + F` ou selecione a ferramenta na barra
   - Escolha "Line" no painel de opções

2. **Desenhar a linha**:
   - Clique e arraste mantendo `Shift` pressionado
   - Solte para finalizar

3. **Converter para Mesh 3D**:
   - Selecione o traço Grease Pencil
   - `Alt + C` > Convert to Mesh

---

### **Dicas Profissionais**:
- **Precisão absoluta**:
  - Use `Shift + S` para snap (ímã) a vértices/grid
  - Digite coordenadas exatas no painel Transform (`N`)

- **Visualização melhorada**:
  - No Modo Edição, ative "Draw All Edges" nas opções de visualização
  - Aumente o "Line Width" nas preferências do Viewport

- **Múltiplas linhas**:
  - Use `Shift + D` para duplicar arestas selecionadas
  - Para linhas paralelas perfeitas, use o modificador Array

---

### **Exemplo Prático**:
1. Crie um novo projeto (`Ctrl + N`)
2. `Shift + A` > Mesh > Plane
3. `Tab` > `X` > Delete Vertices
4. `Ctrl + LMB` em (0,0,0) e depois em (2,0,0)
5. `F` para criar a aresta
6. No painel Transform (`N`), defina:
   - Vértice 1: (0,0,0)
   - Vértice 2: (2,0,0)

**Resultado**: Segmento de reta 3D perfeito ao longo do eixo X!

Precisa criar linhas curvas ou formas mais complexas? Posso mostrar como usar ferramentas como Skin, Screw ou Geometry Nodes no Blender!