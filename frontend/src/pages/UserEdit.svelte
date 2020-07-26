<script>
    import { handleErrors } from "../shared.js";
    import { onMount } from "svelte";
	import { navigate } from "svelte-routing";
    import SidebarNav from "../components/SidebarNav.svelte";

    let localToken = localStorage.getItem("token")
    export let id;

    let email = "";
    let is_active;
    let is_administrator;

    onMount(() => {
        getUser();
    });

    async function getUser() {
        await fetch(`http://localhost:8000/api/users/${id}/`, {
            method: "GET",
            headers: {
                Authorization: `JWT ${localToken}`
            }})
        .then(handleErrors)
        .then(response => response.json())
        .then(data => {
            email = data.email;
            is_active = data.is_active;
            is_administrator = data.is_administrator;
        });
    }

    async function editUser() {
        let postObj = {
            "email": email,
            "username": email,
            "is_active": is_active,
            "is_administrator": is_administrator
        };
        await fetch(`http://localhost:8000/api/users/${id}/`, {
            method: "PUT",
            headers: {
                Authorization: `JWT ${localToken}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(postObj)
        })
        .then(handleErrors)
        .then(response => response.json())
        .then(response => navigate(`/users/?updated=true`, { replace: true }))
    }
</script>

<SidebarNav />

<div class="content-expanded">
    <div class="page-top container-fluid">

        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <div class="page-top mb-lg">

                    <h2 class="mb-xs black"> 
                        Edit User: 
                        {#if email}
                            {email}
                        {:else}
                            <span class="placeholder">***************</span> 
                        {/if}
                    </h2>

                    <div class="card mb-xs"> 
                        <label>User Email</label>
                        <input value="{email}" disabled class="w-100 mb-xs" />
            
                        <label>User Type</label>
                        <select bind:value="{is_administrator}" class="w-100 mb-xs">
                            {#if is_administrator == true}
                                <option selected value="true">Administrator</option>
                                <option value="false">User</option>
                            {:else}
                                <option selected value="false">User</option>
                                <option value="true">Administrator</option>
                            {/if}
                        </select>

                        <label>Status</label>
                        <select bind:value="{is_active}" class="w-100 mb-xs">
                            {#if is_active == true}
                                <option selected value="true">Active</option>
                                <option value="false">Deactivated</option>
                            {:else}
                                <option selected value="false">Deactivated</option>
                                <option value="true">Active</option>
                            {/if}
                        </select>
                    
                        <button on:click="{editUser}" class="primary mb-xs w-100">Modify User</button>
                        <a href="/users"><button class="default w-100">Cancel</button></a>
                    </div>
                </div>
            </div>
        </div>

    </div>
</div>