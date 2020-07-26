<script>
    import { handleErrors } from "../shared.js";
    import { onMount } from "svelte";
    import SidebarNav from "../components/SidebarNav.svelte";
	import { navigate } from "svelte-routing";

    let localToken = localStorage.getItem("token")
    export let id;

    let subject;
    let type;
    let content;
    let res = []

    onMount(() => {
        getTicket();
    });

    async function getTicket() {
        await fetch(`http://localhost:8000/api/ticket/${id}/`, {
            method: "GET",
            headers: {
                Authorization: `JWT ${localToken}`
            }})
        .then(handleErrors)
        .then(response => response.json())
        .then(data => {
            subject = data.subject;
            type = data.type;
            content = data.content;
        });
    }

    async function editTicket() {
        let postObj = {
            "subject": subject, 
            "type": type, 
            "content": content
        };
        await fetch(`http://localhost:8000/api/ticket/${id}/`, {
            method: "PUT",
            headers: {
                Authorization: `JWT ${localToken}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(postObj)
        })
        .then(handleErrors)
        .then(response => response.json())
        .then(response => navigate(`/ticket/${response.id}`, { replace: true }))
    }
</script>

<SidebarNav />

<div class="content-expanded">
    <div class="page-top container-fluid">

        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <div class="page-top mb-lg">

                    <h2 class="mb-xs black"> 
                        {#if subject}
                            Edit {subject}
                        {:else}
                            <span class="placeholder">***************</span> 
                        {/if}
                    </h2>

                    <div class="card mb-xs"> 
                        <label>Subject</label>
                        <input bind:value={subject} placeholder="" class="w-100 mb-xs" />
            
                        <label>Subject</label>
                        <select bind:value={type} class="w-100 mb-xs">
                            <option value="">---</option>
                            <option value="Bug">Bug</option>
                            <option value="Feature">Feature</option>
                            <option value="Enhancement">Enhancement</option>
                        </select>
            
                        <label>Message</label>
                        <div bind:innerHTML={content}
                            class="w-100 mb-xs" 
                            style="min-height:80px;" 
                            placeholder="" 
                            contenteditable="true">
                        </div>
        
                        <button on:click={editTicket} class="primary mb-xs w-100">Edit Ticket Content</button>
                        <a href="/ticket/{id}"><button class="default w-100">Cancel</button></a>
                    </div>
                </div>
            </div>
        </div>

    </div>
</div>