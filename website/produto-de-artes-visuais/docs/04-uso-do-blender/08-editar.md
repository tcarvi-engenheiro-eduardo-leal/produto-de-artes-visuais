# editar

## Delete
- `SELECT` `X` `D` -- Delete selection

## Extrude em X, Y ou Z
- Extrude EDGE:
    - `Tab Edit Mode` `2` `SELECT EDGE` `E` `X` -- Extrude Edge em X
    - `Tab Edit Mode` `2` `SELECT EDGE` `E` `Y` -- Extrude Edge em Y
    - `Tab Edit Mode` `2` `SELECT EDGE` `E` `Z` -- Extrude Edge em Z
- Extrude FACE:
    - `Tab Edit Mode` `3` `SELECT FACE` `E` `X` -- Extrude Face em X
    - `Tab Edit Mode` `3` `SELECT FACE` `E` `Y` -- Extrude Face em Y
    - `Tab Edit Mode` `3` `SELECT FACE` `E` `Z` -- Extrude Face em Z

## Inset Face
- Cria polígono interno
- Polígono sem profundidade
- Polígono com ligação apenas nos cantos da seleção inicial de faces. 
    - `Tab Edit Mode` `3` `SELECT FACE` `I`

## Criar edge com knife
- `Tab Edit Mode` `1` `K` `SELECT VERTEX origem` `SELECT VERTEX fim`
- `Tab Edit Mode` `1` `K` `SELECT EDGE Ponto origem` `SELECT EDGE Ponto fim`

## Loop Cut and Slide
- Criar Edges em um Loop do objeto.
- Posição do loop é escolhida com arrasto do mouse.
    - `Tab Edit Mode` `CTRL` `R` `Slide`

## Bevel
- Pode ser aplicado sobre Edges e sobre Faces
- `Tab Edit Mode` `2` `SELECT EDGE` `CRTL` `B` -- Criação paralela de Bevel
    - Depois abrir janela de configuração do bevel com `F6`.
- `Tab Edit Mode` `3` `SELECT FACE` `CRTL` `B` -- Criação menor de Bevel, para fora ou para dentro.

## Bridge Edge Loop
- `Tab Edit Mode` `2` `SELECT EDGE` `SHIFT` `SELECT-SECOND-EDGE` `CRTL` `E` `OPTION BRIDGE EDGE LOOP` -- Select edges paralelos, depois cria bridge com limite dos edges selecionados.

## Make Edge Face
- `TAB Edit Mode` `2` `LMB-CLICK em EDGE 1` `SHIFT` `LMB-CLICK em EDGE 2` `F` -- Select edge loop, depois cria face com limite dos edges.

## Proportional Editing
- 