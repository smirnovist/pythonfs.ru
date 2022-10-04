// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Python From Scratch',
  tagline: 'Python с нуля',
  url: 'https://pythonfs.ru/',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'favicon.ico',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'smirnovist', // Usually your GitHub org/user name.
  projectName: 'pythonfs.ru', // Usually your repo name.

  // trailingSlash: false,

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'ru',
    locales: ['ru'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // sidebarCollapsed: false,
          showLastUpdateTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Python From Scratch',
        logo: {
          alt: 'Логотип',
          src: 'images/logo.svg',
        },
        items: [
          {
            label: 'Учебник',
            // type: 'doc',
            // docId: 'index',
            to: '/docs',
            position: 'left',
          },
          {
            label: 'Блог',
            to: '/blog',
            position: 'left',
          },
          {
            label: 'Примеры (.zip для Windows)',
            href: 'https://pythonfs.ru/archives/examples.zip',
            position: 'right',
          },
          {
            label: 'Примеры (.tar.gz для Unix)',
            href: 'https://pythonfs.ru/archives/examples.tar.gz',
            position: 'right',
          },
          {
            label: 'GitHub',
            href: 'https://github.com/smirnovist/pythonfs.ru',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Материалы',
            items: [
              {
                label: 'Учебник',
                to: '/docs',
              },
              {
                label: 'Блог',
                to: '/blog',
              },
            ],
          },
          {
            title: 'Архивы для скачивания',
            items: [
              {
                label: 'Примеры (.zip для Windows)',
                href: 'https://pythonfs.ru/archives/examples.zip',
              },
              {
                label: 'Примеры (.tar.gz для Unix)',
                href: 'https://pythonfs.ru/archives/examples.tar.gz',
              },
            ],
          },
          {
            title: 'Проект',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/smirnovist/pythonfs.ru',
              },
            ],
          },
        ],
        copyright: `&copy; Илья Смирнов, ${new Date().getFullYear()}<br>Материалы сайта доступны на условиях <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener noreferrer license">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License</a><br>Исходный код примеров доступен на условиях <a href="https://choosealicense.com/licenses/bsd-2-clause/" target="_blank" rel="noopener noreferrer license">BSD 2-Clause License</a><br>Python &reg; является зарегистрированным товарным знаком <a href="https://www.python.org/psf/" target="_blank" rel="noopener noreferrer">Python Software Foundation</a><br>Логотипы Python &trade; (в нескольких вариантах) являются товарными знаками <a href="https://www.python.org/psf/" target="_blank" rel="noopener noreferrer">Python Software Foundation</a><br><a href="https://www.python.org/psf/trademarks/" target="_blank" rel="noopener noreferrer">Политика использования товарных знаков Python Software Foundation</a><br>Сайт сделан на <a href="https://docusaurus.io/" target="_blank" rel="noopener noreferrer">Docusaurus</a><br>На сайте не используются файлы cookie`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
