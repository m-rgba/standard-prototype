import Sidebar from './sidebar.svelte';
  
export default {
  title: 'Layouts|Sidebar'
};

export const Default = () => ({
  Component: Sidebar,
  props: { 
  }
});
Default.story = {
  parameters: {
    notes: `
      # Sidebar
      This is the sidebar component found inside all the page components as standard navigation.
    `},
};