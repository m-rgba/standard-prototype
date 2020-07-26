<script>
  import {auth} from '../auth/firebase.js'
  import { navigate } from "svelte-routing";

  let is_administrator = localStorage.getItem("is_administrator")

  function handleLogout(){
    auth.signOut();
    localStorage.clear();
    navigate("/login", { replace: true });
  };
</script>

<div class="sidebar">
    <a href="/">
      <button class="nav logo mb-xs">
          <img style="width:36px;" alt="Home Logo" src="/logo.svg" />
      </button>
    </a>

    <a href="/tickets">
      <button class="nav mb-xs">
        <i class="fas fa-inbox"></i>
      </button>
    </a>

    <a href="/profile">
      <button class="nav mb-xs">
        <i class="fas fa-user"></i>
      </button>
    </a>

    {#if is_administrator == "true"}
      <a href="/users">
        <button class="nav mb-xs">
          <i class="fas fa-users"></i>
        </button>
      </a>
    {/if}
    
    <button on:click={handleLogout} class="nav settings mb-xs">
        <i class="fas fa-door-open"></i>
    </button>
</div>
