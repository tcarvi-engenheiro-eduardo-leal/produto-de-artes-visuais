import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

const config: Config = {
  title: 'Tutoriais de Artes Visuais com Aplicativos Open Source',
  tagline: 'produto-de-artes-visuais',
  favicon: 'img/favicon.ico',
  url: 'https://projeto-de-artes-visuais.web.app/',
  baseUrl: '/',
  organizationName: 'tcarvi-engenheiro-eduardo-leal',
  projectName: 'produto-de-artes-visuais',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  i18n: {
    defaultLocale: 'pt-br',
    locales: ['pt-br'],
  },
  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css',
      type: 'text/css',
      integrity:
        'sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM',
      crossorigin: 'anonymous',
    },
  ],
  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
          sidebarPath: './sidebars.ts',
          editUrl:
            'https://github.com/tcarvi-engenheiro-eduardo-leal/produto-de-artes-visuais/edit/main/tutorial/',
        },
        blog: {
          showReadingTime: true,
          editUrl:
            'https://github.com/tcarvi-engenheiro-eduardo-leal/produto-de-artes-visuais/edit/main/tutorial/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],
  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'produto-de-artes-visuais',
      logo: {
        alt: 'produto-de-artes-visuais',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Tutoriais',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/tcarvi-engenheiro-eduardo-leal/produto-de-artes-visuais',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Tutorial',
              to: '/docs/conceitos-gerais/teoria-das-artes-visuais',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/users/26135239/tcarvi-engenheiro-eduardo-leal?tab=questions',
            },
            {
              label: 'YouTube',
              href: 'https://www.youtube.com/channel/UCWA39JV7f68QQ6lZEpMOqIA',
            },
            {
              label: 'X',
              href: 'https://x.com/tcarvi_eduardo',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/tcarvi-engenheiro-eduardo-leal/produto-de-artes-visuais',
            },
          ],
        },
      ],
      copyright: `atualizado em  ${new Date().toLocaleDateString("pt-BR")} ©TCARVI`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
