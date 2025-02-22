import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '5ff'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '5ba'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'a2b'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'c3c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '156'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '88c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '000'),
    exact: true
  },
  {
    path: '/blog',
    component: ComponentCreator('/blog', '1d8'),
    exact: true
  },
  {
    path: '/blog/archive',
    component: ComponentCreator('/blog/archive', '182'),
    exact: true
  },
  {
    path: '/blog/first-blog-post',
    component: ComponentCreator('/blog/first-blog-post', '43a'),
    exact: true
  },
  {
    path: '/blog/tags',
    component: ComponentCreator('/blog/tags', '287'),
    exact: true
  },
  {
    path: '/blog/tags/hello',
    component: ComponentCreator('/blog/tags/hello', '9dc'),
    exact: true
  },
  {
    path: '/markdown-page',
    component: ComponentCreator('/markdown-page', '3d7'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', '1a8'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', '110'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', '36c'),
            routes: [
              {
                path: '/docs/ambiente-de-trabalho/installation',
                component: ComponentCreator('/docs/ambiente-de-trabalho/installation', '4fb'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ambiente-de-trabalho/preferences',
                component: ComponentCreator('/docs/ambiente-de-trabalho/preferences', '306'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ambiente-de-trabalho/user-interface',
                component: ComponentCreator('/docs/ambiente-de-trabalho/user-interface', '82f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/animating-and-rigging/etapa0-fluxo-de-trabalho',
                component: ComponentCreator('/docs/animating-and-rigging/etapa0-fluxo-de-trabalho', 'fb9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/animating-and-rigging/etapa1-pre-producao',
                component: ComponentCreator('/docs/animating-and-rigging/etapa1-pre-producao', '53e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/animating-and-rigging/etapa2-producao-insumos',
                component: ComponentCreator('/docs/animating-and-rigging/etapa2-producao-insumos', '965'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/animating-and-rigging/etapa3-producao',
                component: ComponentCreator('/docs/animating-and-rigging/etapa3-producao', '517'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/animating-and-rigging/etapa4-pos-producao',
                component: ComponentCreator('/docs/animating-and-rigging/etapa4-pos-producao', '7cf'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/arquitetura-do-aplicativo-blender/blender-file-structure',
                component: ComponentCreator('/docs/arquitetura-do-aplicativo-blender/blender-file-structure', 'f09'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/arquitetura-do-aplicativo-blender/context',
                component: ComponentCreator('/docs/arquitetura-do-aplicativo-blender/context', '61c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/arquitetura-do-aplicativo-blender/meshes',
                component: ComponentCreator('/docs/arquitetura-do-aplicativo-blender/meshes', '371'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/arquitetura-do-aplicativo-blender/referencias',
                component: ComponentCreator('/docs/arquitetura-do-aplicativo-blender/referencias', 'a3c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/arquitetura-do-aplicativo-blender/transformation',
                component: ComponentCreator('/docs/arquitetura-do-aplicativo-blender/transformation', 'f9c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/category/conceitos-gerais',
                component: ComponentCreator('/docs/category/conceitos-gerais', 'f74'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/characters-modeling/teoria',
                component: ComponentCreator('/docs/characters-modeling/teoria', 'e6f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/compositing/etapa0-fluxo-de-trabalho',
                component: ComponentCreator('/docs/compositing/etapa0-fluxo-de-trabalho', 'a50'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/compositing/etapa1-pre-producao',
                component: ComponentCreator('/docs/compositing/etapa1-pre-producao', '3aa'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/compositing/etapa2-producao-insumos',
                component: ComponentCreator('/docs/compositing/etapa2-producao-insumos', '0bb'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/compositing/etapa3-producao',
                component: ComponentCreator('/docs/compositing/etapa3-producao', '65f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/compositing/etapa4-pos-producao',
                component: ComponentCreator('/docs/compositing/etapa4-pos-producao', '529'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/conceitos-gerais/blender',
                component: ComponentCreator('/docs/conceitos-gerais/blender', '850'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/conceitos-gerais/source-code',
                component: ComponentCreator('/docs/conceitos-gerais/source-code', 'ea1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-cinematic/etapa0-fluxo-de-trabalho',
                component: ComponentCreator('/docs/concept-art-cinematic/etapa0-fluxo-de-trabalho', 'b5f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-cinematic/etapa1-pre-producao',
                component: ComponentCreator('/docs/concept-art-cinematic/etapa1-pre-producao', '96f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-cinematic/etapa2-producao-insumos',
                component: ComponentCreator('/docs/concept-art-cinematic/etapa2-producao-insumos', '249'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-cinematic/etapa3-producao',
                component: ComponentCreator('/docs/concept-art-cinematic/etapa3-producao', '756'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-cinematic/etapa4-pos-producao',
                component: ComponentCreator('/docs/concept-art-cinematic/etapa4-pos-producao', 'b70'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-storyboard-2d/blender-story-artist',
                component: ComponentCreator('/docs/concept-art-storyboard-2d/blender-story-artist', 'c96'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-storyboard-2d/etapa0-fluxo-de-trabalho',
                component: ComponentCreator('/docs/concept-art-storyboard-2d/etapa0-fluxo-de-trabalho', 'cc6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-storyboard-2d/etapa1-pre-producao',
                component: ComponentCreator('/docs/concept-art-storyboard-2d/etapa1-pre-producao', '133'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-storyboard-2d/etapa2-producao-insumos',
                component: ComponentCreator('/docs/concept-art-storyboard-2d/etapa2-producao-insumos', '2d4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-storyboard-2d/etapa3-producao',
                component: ComponentCreator('/docs/concept-art-storyboard-2d/etapa3-producao', 'a5a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-storyboard-2d/etapa4-pos-producao',
                component: ComponentCreator('/docs/concept-art-storyboard-2d/etapa4-pos-producao', 'f1c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-storyboard-3d/etapa1-pre-producao',
                component: ComponentCreator('/docs/concept-art-storyboard-3d/etapa1-pre-producao', '73d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-storyboard-3d/etapa2-producao-insumos',
                component: ComponentCreator('/docs/concept-art-storyboard-3d/etapa2-producao-insumos', 'c22'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-storyboard-3d/etapa3-producao',
                component: ComponentCreator('/docs/concept-art-storyboard-3d/etapa3-producao', 'caf'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/concept-art-storyboard-3d/etapa4-pos-producao',
                component: ComponentCreator('/docs/concept-art-storyboard-3d/etapa4-pos-producao', 'b36'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/effects/etapa0-fluxo-de-trabalho',
                component: ComponentCreator('/docs/effects/etapa0-fluxo-de-trabalho', 'e18'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/effects/etapa1-pre-producao',
                component: ComponentCreator('/docs/effects/etapa1-pre-producao', '6cc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/effects/etapa2-producao-insumos',
                component: ComponentCreator('/docs/effects/etapa2-producao-insumos', '95e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/effects/etapa3-producao',
                component: ComponentCreator('/docs/effects/etapa3-producao', '955'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/effects/etapa4-pos-producao',
                component: ComponentCreator('/docs/effects/etapa4-pos-producao', '31e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/environment-modeling/teoria',
                component: ComponentCreator('/docs/environment-modeling/teoria', '0c7'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/grading/etapa0-fluxo-de-trabalho',
                component: ComponentCreator('/docs/grading/etapa0-fluxo-de-trabalho', '79e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/grading/etapa1-pre-producao',
                component: ComponentCreator('/docs/grading/etapa1-pre-producao', '825'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/grading/etapa2-producao-insumos',
                component: ComponentCreator('/docs/grading/etapa2-producao-insumos', 'f1f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/grading/etapa3-producao',
                component: ComponentCreator('/docs/grading/etapa3-producao', 'd78'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/grading/etapa4-pos-producao',
                component: ComponentCreator('/docs/grading/etapa4-pos-producao', '6ee'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/layout/etapa0-fluxo-de-trabalho',
                component: ComponentCreator('/docs/layout/etapa0-fluxo-de-trabalho', '7b0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/layout/etapa1-pre-producao',
                component: ComponentCreator('/docs/layout/etapa1-pre-producao', '43b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/layout/etapa2-producao-insumos',
                component: ComponentCreator('/docs/layout/etapa2-producao-insumos', '623'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/layout/etapa3-producao',
                component: ComponentCreator('/docs/layout/etapa3-producao', '42e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/layout/etapa4-pos-producao',
                component: ComponentCreator('/docs/layout/etapa4-pos-producao', 'a63'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/lighting/etapa0-fluxo-de-trabalho',
                component: ComponentCreator('/docs/lighting/etapa0-fluxo-de-trabalho', '7e0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/lighting/etapa1-pre-producao',
                component: ComponentCreator('/docs/lighting/etapa1-pre-producao', 'ace'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/lighting/etapa2-producao-insumos',
                component: ComponentCreator('/docs/lighting/etapa2-producao-insumos', '1de'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/lighting/etapa3-producao',
                component: ComponentCreator('/docs/lighting/etapa3-producao', '40e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/lighting/etapa4-pos-producao',
                component: ComponentCreator('/docs/lighting/etapa4-pos-producao', '821'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/physics-and-scripting/building',
                component: ComponentCreator('/docs/physics-and-scripting/building', 'bfd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/physics-and-scripting/coding',
                component: ComponentCreator('/docs/physics-and-scripting/coding', '02b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/physics-and-scripting/scripting',
                component: ComponentCreator('/docs/physics-and-scripting/scripting', '450'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-animation-and-rigging',
                component: ComponentCreator('/docs/pipelines/pipeline-animation-and-rigging', 'f69'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-characters-modeling',
                component: ComponentCreator('/docs/pipelines/pipeline-characters-modeling', '963'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-compositing',
                component: ComponentCreator('/docs/pipelines/pipeline-compositing', 'f42'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-concept-art-cinematic',
                component: ComponentCreator('/docs/pipelines/pipeline-concept-art-cinematic', '2a0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-concept-art-storyboard-2D',
                component: ComponentCreator('/docs/pipelines/pipeline-concept-art-storyboard-2D', '4b3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-concept-art-storyboard-3D',
                component: ComponentCreator('/docs/pipelines/pipeline-concept-art-storyboard-3D', 'dce'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-effects',
                component: ComponentCreator('/docs/pipelines/pipeline-effects', '6ed'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-environments-modeling',
                component: ComponentCreator('/docs/pipelines/pipeline-environments-modeling', '61c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-grading',
                component: ComponentCreator('/docs/pipelines/pipeline-grading', '236'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-layout',
                component: ComponentCreator('/docs/pipelines/pipeline-layout', 'e09'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-lighting',
                component: ComponentCreator('/docs/pipelines/pipeline-lighting', '207'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-physics-and-scripting',
                component: ComponentCreator('/docs/pipelines/pipeline-physics-and-scripting', 'ffd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-props-modeling',
                component: ComponentCreator('/docs/pipelines/pipeline-props-modeling', '4c7'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-rendering',
                component: ComponentCreator('/docs/pipelines/pipeline-rendering', 'f25'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-sculpting-and-painting',
                component: ComponentCreator('/docs/pipelines/pipeline-sculpting-and-painting', '9bd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipeline-video-editing',
                component: ComponentCreator('/docs/pipelines/pipeline-video-editing', 'eba'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/pipelines',
                component: ComponentCreator('/docs/pipelines/pipelines', 'd14'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/pipelines/publicacao-web',
                component: ComponentCreator('/docs/pipelines/publicacao-web', '9ee'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/projects/Tutorial_Toon',
                component: ComponentCreator('/docs/projects/Tutorial_Toon', '67d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/props-modeling/teoria',
                component: ComponentCreator('/docs/props-modeling/teoria', '48b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/publicacao-web/etapa0-fluxo-de-trabalho',
                component: ComponentCreator('/docs/publicacao-web/etapa0-fluxo-de-trabalho', '260'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/publicacao-web/etapa1-pre-producao',
                component: ComponentCreator('/docs/publicacao-web/etapa1-pre-producao', 'f9c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/publicacao-web/etapa2-producao-insumos',
                component: ComponentCreator('/docs/publicacao-web/etapa2-producao-insumos', '9c3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/publicacao-web/etapa3-producao',
                component: ComponentCreator('/docs/publicacao-web/etapa3-producao', '956'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/publicacao-web/etapa4-pos-producao',
                component: ComponentCreator('/docs/publicacao-web/etapa4-pos-producao', '53c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/rendering/etapa0-fluxo-de-trabalho',
                component: ComponentCreator('/docs/rendering/etapa0-fluxo-de-trabalho', 'a6a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/rendering/etapa1-pre-producao',
                component: ComponentCreator('/docs/rendering/etapa1-pre-producao', '5fd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/rendering/etapa2-producao-insumos',
                component: ComponentCreator('/docs/rendering/etapa2-producao-insumos', '75c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/rendering/etapa3-producao',
                component: ComponentCreator('/docs/rendering/etapa3-producao', '4ab'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/rendering/etapa4-pos-producao',
                component: ComponentCreator('/docs/rendering/etapa4-pos-producao', '383'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/sculpting-and-painting/paleta-de-cores',
                component: ComponentCreator('/docs/sculpting-and-painting/paleta-de-cores', 'fa1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/sculpting-and-painting/processamento-de-cores',
                component: ComponentCreator('/docs/sculpting-and-painting/processamento-de-cores', '53a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/sculpting-and-painting/textura-de-cor',
                component: ComponentCreator('/docs/sculpting-and-painting/textura-de-cor', 'de6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uso-do-blender/editar',
                component: ComponentCreator('/docs/uso-do-blender/editar', '8c9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uso-do-blender/interface-de-comandos',
                component: ComponentCreator('/docs/uso-do-blender/interface-de-comandos', '939'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uso-do-blender/localizacao-para-transform',
                component: ComponentCreator('/docs/uso-do-blender/localizacao-para-transform', 'a2b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uso-do-blender/mover-e-alterar',
                component: ComponentCreator('/docs/uso-do-blender/mover-e-alterar', '87a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uso-do-blender/navegar',
                component: ComponentCreator('/docs/uso-do-blender/navegar', '4cc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uso-do-blender/selecionar',
                component: ComponentCreator('/docs/uso-do-blender/selecionar', '610'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uso-do-blender/textura-de-cor',
                component: ComponentCreator('/docs/uso-do-blender/textura-de-cor', '232'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uso-do-blender/toolset',
                component: ComponentCreator('/docs/uso-do-blender/toolset', '1ed'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uso-do-blender/visualizar',
                component: ComponentCreator('/docs/uso-do-blender/visualizar', '371'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/uso-do-blender/workspace',
                component: ComponentCreator('/docs/uso-do-blender/workspace', 'b56'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/video-editing/etapa0-fluxo-de-trabalho',
                component: ComponentCreator('/docs/video-editing/etapa0-fluxo-de-trabalho', 'cd7'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/video-editing/etapa1-pre-producao',
                component: ComponentCreator('/docs/video-editing/etapa1-pre-producao', '601'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/video-editing/etapa2-producao-insumos',
                component: ComponentCreator('/docs/video-editing/etapa2-producao-insumos', 'c12'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/video-editing/etapa3-producao',
                component: ComponentCreator('/docs/video-editing/etapa3-producao', '223'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/video-editing/etapa4-pos-producao',
                component: ComponentCreator('/docs/video-editing/etapa4-pos-producao', 'b4a'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/',
    component: ComponentCreator('/', 'e5f'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
