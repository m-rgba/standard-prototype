<script>
    import {auth, getToken } from '../auth/firebase.js';
    import { handleErrors } from "../shared.js";
	import { navigate } from "svelte-routing";
    import SidebarNav from "../components/SidebarNav.svelte";

    let localToken = localStorage.getItem("token");
	let user_email = localStorage.getItem("user_email")

    let message = "";
    let errorCode = "";
    let errorMessage = "";

    let oldPass;
    let passEntry;
    let confirmPassEntry;
    
    function handlePasswordUpdate(){
        /* Validate Password */
        if (passEntry != confirmPassEntry){
            console.log("Error: Password match");
            message = "";
            errorMessage = "Please enter passwords which match to confirm and complete sign-up.";
            return false;
        } else {
            reLogIn();
        }
    };
    function reLogIn(){
        auth.signInWithEmailAndPassword(user_email, oldPass)
        .then(function() {
            changePassword();
        })
        .catch(function(error) {
            // console.log(error);
            errorCode = error.code;
            errorMessage = error.message;
        });
    };
    function changePassword(){
        auth.currentUser.updatePassword(passEntry)
        .then(function() {
            message = "Your password has been udpated."
            console.log("Your password has been udpated.");
        })
        .catch(function(error) {
            console.log(error);
            errorCode = error.code;
            errorMessage = error.message;
        });
    };
</script>

<SidebarNav />

<div class="content-expanded">
    <div class="page-top container-fluid">

        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <div class="page-top mb-lg">

                    <h2 class="mb-xs black"> 
                        Edit Your Profile
                    </h2>

                    <div class="card mb-xs"> 
                        {#if message != ""}
                            <div class="message-positive mb-xs">
                                {message}
                            </div>
                        {/if}

                        {#if errorMessage != ""}
                            <div class="message-negative mb-xs">
                                {errorMessage}
                            </div>
                        {/if}

                        <label>Your Email</label>
                        <input value="{user_email}" class="w-100 mb-xs disabled" disabled />

                        <label>Current Password</label>
                        <input bind:value={oldPass} type="password" placeholder="New Password..." class="w-100 mb-xs" />

                        <hr />

                        <label>Update Your Password</label>
                        <input bind:value={passEntry} type="password" placeholder="New Password..." class="w-100 mb-xs" />
                        <input bind:value={confirmPassEntry} type="password" placeholder="Confirm Password..." class="w-100 mb-xs" />

                        <button on:click={handlePasswordUpdate} class="primary mb-xs w-100">Update Profile</button>
                        <a href="/tickets"><button class="default w-100">Cancel</button></a>
                    </div>
                </div>
            </div>
        </div>

    </div>
</div>