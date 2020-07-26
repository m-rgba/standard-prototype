<script>
    import { onMount } from "svelte";
    import { auth, getToken, googleProvider, emailProvider } from './firebase.js'
    import { handleErrors } from "../shared.js";

    let localToken;    
    let loginType = "login";
    let usernameEntry;
    let passEntry;
    let confirmPassEntry;

    let message = "";
    let errorCode = "";
    let errorMessage = "";

    onMount(() => {
        refreshLocalToken();
        if(localToken != undefined){
            getToken()
            .then(function() {
                refreshLocalToken();
            })
        }
    });

    function refreshLocalToken(){
        localToken = localStorage.getItem("token");
        console.log("Local Token >>")
        console.log(localToken)
    };

    function handleLogin(){
        auth.signInWithEmailAndPassword(usernameEntry, passEntry)
        .then(function() {
            getToken()
            .then(function() {
                refreshLocalToken();
            })
        })
        .catch(function(error) {
            errorCode = error.code;
            errorMessage = error.message;
        })
        .then(function() {
            refreshLocalToken();
        })
    };

    function handleSignup(){
        /* Validate Password */
        if (passEntry != confirmPassEntry){
            message = "";
            errorMessage = "Please enter passwords which match to confirm and complete sign-up.";
            return false;
        } else {
            finalizeSignup();
        }
    };
    function finalizeSignup(){
        auth.createUserWithEmailAndPassword(usernameEntry, passEntry)
        .then(function() {
            getToken()
            .then(function() {
                refreshLocalToken();
            })
        })
        .catch(function(error) {
            errorCode = error.code;
            errorMessage = error.message;
        })
    };

    function handleForgotPassword(){
        auth.sendPasswordResetEmail(usernameEntry)
        .then(function() {
            message = "An account recovery link has been sent to your email - if you have trouble finding it, make sure to check your junk mail folder."
            errorMessage = "";
        }).catch(function(error) {
            errorCode = error.code;
            errorMessage = error.message;
        });
    };
    function googleLogin(){
        auth.signInWithPopup(googleProvider);
        getToken()
        .then(function() {
            refreshLocalToken();
        })
    };
    function authSignOut(){
        auth.signOut();
        localStorage.clear();
        refreshLocalToken();
    };
</script>

<div class="signup-center card">
  <div class="w-100 center mb-sm"> 
      <img style="width:42px;" alt="Logo" src="/logo.svg" />
  </div>

    {#if localToken}
        <div class="message-positive mb-xs">
            <p><strong>Account Confirmed:</strong></p>
            <p>You're currently signed-in.</p>
        </div>
        <a href="/"><button class="primary mb-xs w-100">Proceed to Application</button></a>
        <button class="default w-100 mb-xs" on:click={authSignOut}>Log Out</button>
    {/if}

    {#if !localToken}
        <button class="default w-100 mb-xs" on:click={googleLogin}><i class="fab fa-google red" style="margin-right:8px;"></i> Log in with Google</button>
        <hr />

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

        {#if loginType == "login"}
            <label>Email</label>
            <input class="mb-xs lg w-100" placeholder="Email..." bind:value={usernameEntry} />

            <label>Password</label>
            <input class="mb-xs lg w-100" type="password" placeholder="Password..." bind:value={passEntry} />

            <button class="primary w-100 mb-xs" on:click={handleLogin}>Login</button>
            <button class="default w-100 mb-xs" on:click={()=>loginType="signup"}>I need an account, sign me up</button>
            <button class="blank w-100" on:click={()=>loginType="forgotpass"}>Reset My Password</button>
        {/if}

        {#if loginType == "signup"}
            <label>Email</label>
            <input class="mb-xs lg w-100" placeholder="Email..." bind:value={usernameEntry} />

            <label>Password</label>
            <input class="mb-xs lg w-100" type="password" placeholder="Password..." bind:value={passEntry} />
            <input class="mb-xs lg w-100" type="password" placeholder="Confirm Password..." bind:value={confirmPassEntry} />

            <button class="primary w-100 mb-xs" on:click={handleSignup}>Sign Up</button>
            <button class="default w-100 mb-xs" on:click={()=>loginType="login"}>I already have an account, log me in</button>
            <button class="blank w-100" on:click={()=>loginType="forgotpass"}>Reset My Password</button>
        {/if}

        {#if loginType == "forgotpass"}
            <label>Email</label>
            <input class="mb-xs lg w-100" placeholder="Email..." bind:value={usernameEntry} />
            <button class="primary w-100 mb-xs" on:click={handleForgotPassword}>Send Password Reset</button>

            <button class="default w-100 mb-xs" on:click={()=>loginType="signup"}>I need an account, sign me up</button>
            <button class="default w-100" on:click={()=>loginType="login"}>I already have an account, log me in</button>
        {/if}
    {/if}

</div>