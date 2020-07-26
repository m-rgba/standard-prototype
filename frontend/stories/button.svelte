<script>
  import { createEventDispatcher } from 'svelte';
  export let content = '';
  export let type = 'default';

  const dispatch = createEventDispatcher();
  function onClick(event) {
    dispatch('click', event)
  }
</script>

<button class="{type}" on:click={onClick}>
  {content}
</button>

<style>  
  button{
      color: #4D5362;
      font-size: 14px;
      font-family: -apple-system, 'Inter', sans-serif;
      font-weight: 400;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
  }
  
  button.default {
      font-size:12px;
      padding:8px 16px;
      background: #f5f8fa;
      font-weight: 600;
      border-radius: 4px;
      background-image: linear-gradient(180deg,rgba(255, 255, 255, 0.5),rgba(255, 255, 255, 0));
      border: 1px solid #cbd0d5;
      transition: all 0.15s ease-in-out;
  }
  button.default:hover {
      background: #e9ebf1;
  }
  button.default:active{
      background: #e3e8ea;
      background-image: none;
      box-shadow: inset 0 0px 1px 2px rgba(0, 0, 0, 0.1);
  }

  button.blank {
      border: 0;
      background: transparent;
      font-size: 12px;
      font-weight: 600;
  }
  
  button.primary{
      font-size:12px;
      border-radius: 4px;
      color: #fff;
      font-weight: 600;
      background: #1E81F6;
      border: 0;
      padding: 8px 16px;   
      transition: all 0.15s ease-in-out;
  }
  button.primary:hover{
      background: #1f6ecc;
  }
  button.primary:active{
      background: #1f6ecc;
      box-shadow: inset 0 0px 1px 2px rgba(0, 0, 0, 0.2);
  }
  button.primary.sm, button.default.sm{
      font-size:12px;
  }
</style>