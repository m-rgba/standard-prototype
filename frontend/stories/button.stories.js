import { action } from '@storybook/addon-actions';
import { withKnobs, text } from '@storybook/addon-knobs';
import Button from './button.svelte';

export default {
  title: 'Components|Buttons',
  decorators: [withKnobs]
};

export const Default = () => ({
  Component: Button,
  props: { 
    content: text('content', 'This is a default styled button'),
    type: 'default' 
  },
  on: { click: action('clicked') },
});
/* Add a description... */
Default.story = {
  parameters: {
    notes: `
      # Default Button
      Default button used for most instances.
    `},
};

export const Primary = () => ({
  Component: Button,
  props: {
    content: text('content', 'This is a primary styled button'),
    type: 'primary' 
  },
  on: { click: action('clicked') },
});
Primary.story = {
  parameters: {
    notes: `
      # Primary Button
      Primary button which can be used for taking action. 

      Usually you would just have **one** of these per page.
    `},
};