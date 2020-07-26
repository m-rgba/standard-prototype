module.exports = {
  stories: ['../stories/**/*.stories.js'],
  addons: [
    '@storybook/addon-actions', 
    '@storybook/addon-links', 
    '@storybook/addon-knobs',
    '@storybook/addon-notes/register',
    // { 
    //   name: '@storybook/addon-docs',
    //   options: {
    //     configureJSX: true,
    //   },
    // }
  ],
};