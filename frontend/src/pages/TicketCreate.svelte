<script>
    import { handleErrors } from "../shared.js";
    import SidebarNav from "../components/SidebarNav.svelte";
	import { navigate } from "svelte-routing";

    let localToken = localStorage.getItem("token")
    let subject;
    let type;
    let content;
    let res = []

    let errorMessage = "";

    function handleTicket() {
        if (subject && type && content){
            addTicket();
        } else {
            errorMessage = "Subject, Type, and a Message is required to create a ticket.";
        }
    }
    async function addTicket() {
        let postObj = {
            "subject": subject, 
            "type": type, 
            "content": content
        };
        await fetch("http://localhost:8000/api/ticket/", {
            method: "POST",
            headers: {
                Authorization: `JWT ${localToken}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(postObj)
        })
        .then(handleErrors)
        .then(response => response.json())
        // .then(response => console.log(response))
        .then(response => navigate(`/ticket/${response.id}`, { replace: true }))
    }
</script>

<SidebarNav />

<div class="content-expanded">
    <div class="page-top container-fluid">
    
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <div class="page-top mb-lg">
                    <h2 class="mb-xs black">Create New Ticket</h2>
                    <div class="card mb-xs"> 
                        {#if errorMessage != ""}
                            <div class="message-negative mb-xs">
                                {errorMessage}
                            </div>
                        {/if}

                        <label>Subject</label>
                        <input bind:value={subject} placeholder="Subject..." class="w-100 mb-xs" />
            
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
                            placeholder="Please leave a detailed description of your issue..." 
                            contenteditable="true">
                        </div>
        
                        <button on:click={handleTicket} class="primary mb-xs w-100">Create New Ticket</button>
                        <a href="/tickets"><button class="default w-100">Cancel</button></a>
                    </div>
                </div>
            </div>
        </div>

    </div>
</div>