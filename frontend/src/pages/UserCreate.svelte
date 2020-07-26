<script>
    import { handleErrors } from "../shared.js";
    import { onMount } from "svelte";
	import { navigate } from "svelte-routing";
    import SidebarNav from "../components/SidebarNav.svelte";

    let localToken = localStorage.getItem("token")

    let userObj = [];
    let user_email;
    let is_administrator = false;
    let is_active = true;

    let errorMessage = "";

    function handleCreateUser(){
        var emailRegex = /\S+@\S+\.\S+/;
        var emailTest =  emailRegex.test(user_email);
        if (emailTest === true){
            createUser();
        } else {
            errorMessage = "Please enter a valid email address.";
        }
    }
    async function createUser() {
        let userObj = {
            "email": user_email, 
            "username": user_email, 
            "is_active": is_active,
            "is_administrator": is_administrator
        };

        await fetch("http://localhost:8000/api/users/", {
            method: "POST",
            headers: {
                Authorization: `JWT ${localToken}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(userObj)
        })
        .then(handleErrors)
        .then(response => response.json())
        .then(response => navigate(`/users/?created=true`, { replace: true }))
    }
</script>

<SidebarNav />

<div class="content-expanded">
    <div class="page-top container-fluid">

        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <div class="page-top mb-lg">

                    <h2 class="mb-xs black"> 
                        Create New User
                    </h2>

                    <div class="card mb-xs"> 
                        {#if errorMessage != ""}
                            <div class="message-negative mb-xs">
                                {errorMessage}
                            </div>
                        {/if}

                        <label>Email</label>
                        <input bind:value="{user_email}" placeholder="User's Email" class="w-100 mb-xs" />

                        <label>User Type</label>
                        <select bind:value="{is_administrator}" class="w-100 mb-xs">
                            <option selected value="false">User</option>
                            <option value="true">Administrator</option>
                        </select>

                        <label>Status</label>
                        <select bind:value="{is_active}" class="w-100 mb-xs">
                            <option selected value="true">Active</option>
                            <option value="false">Deactivated</option>
                        </select>

                        <button on:click={handleCreateUser} class="primary mb-xs w-100">Create New User</button>
                        <a href="/users"><button class="default w-100">Cancel</button></a>
                    </div>
                </div>
            </div>
        </div>

    </div>
</div>