<script>
    import { handleErrors } from "../shared.js";
    import { onMount } from "svelte";
	import { navigate } from "svelte-routing";
    import moment from 'moment';
    import SidebarNav from "../components/SidebarNav.svelte"

    export let id;
    let localToken = localStorage.getItem("token")
    let ticket = [];

    let newMessage;
    let messageObj;
    let messages = [];

    onMount(() => {
        getTicket();
        getMessages();
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
            ticket = data;
            ticket.created = moment(ticket.created).format('MM/DD/YYYY');
        });
    }

    async function deleteTicket() {
        await fetch(`http://localhost:8000/api/ticket/${id}/`, {
            method: "DELETE",
            headers: {
                Authorization: `JWT ${localToken}`
            }})
        .then(handleErrors)
        await navigate("/tickets?del=true", { replace: true });
    }

    async function completeTicket() {
        let statusObj = {
            "status": "Completed"
        };
        await fetch(`http://localhost:8000/api/ticket/${id}/`, {
            method: "PATCH",
            headers: {
                Authorization: `JWT ${localToken}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(statusObj)
        })
        .then(handleErrors)
        await getTicket();
    }

    async function openTicket() {
        let statusObj = {
            "status": "Open"
        };
        await fetch(`http://localhost:8000/api/ticket/${id}/`, {
            method: "PATCH",
            headers: {
                Authorization: `JWT ${localToken}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(statusObj)
        })
        .then(handleErrors)
        await getTicket();
    }

    async function getMessages() {
        await fetch(`http://localhost:8000/api/ticket_message/?k_ticket=${id}`, {
            method: "GET",
            headers: {
                Authorization: `JWT ${localToken}`
            }})
        .then(handleErrors)
        .then(response => response.json())
        .then(data => {
            messages = data;
            messages.forEach(message => {
                message.created = moment(message.created).format('MM/DD/YYYY');
            });
        });
    }

    async function addMessage() {
        let messageObj = {
            "k_ticket": id, 
            "message": newMessage
        };
        await fetch("http://localhost:8000/api/ticket_message/", {
            method: "POST",
            headers: {
                Authorization: `JWT ${localToken}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(messageObj)
        })
        .then(handleErrors)
        .then(document.getElementById('message-field').innerHTML = '')
        await getMessages();
    }
</script>

<SidebarNav />
        
<div class="content-expanded">
    <div class="page-top container-fluid">

        <div class="row">
            <div class="col-md-9">
                <div class="mb-sm">
                    <h2 class="mb-xs black">
                        {#if ticket.subject}
                            {ticket.subject}
                        {:else}
                            <span class="placeholder">***************</span> 
                        {/if}
                    </h2>
                    <p class="description mb-sm">
                        {#if ticket.content}
                            {@html ticket.content}
                        {:else}
                            <span class="placeholder">***************</span> 
                        {/if}
                    </p>

                    <hr class="mb-sm" />

                    <h3 class="mb-xs">Responses</h3>
                    <div class="compose-message sticky-top mb-sm card">
                        <div id="message-field" bind:innerHTML={newMessage} class="transparent" contenteditable="true" placeholder="Enter your response here..."></div>
                        <div class="right"> 
                            <button on:click={addMessage} class="primary sm">Submit</button>
                        </div>
                    </div>            
                    {#each messages as message}
                        <div class="response-box mb-xs"> 
                            <div class="row">
                                <div class="col-md-12 mb-xs">
                                    <p class="response">{@html message.message}</p>
                                </div>
                                <div class="col-md-6 min muted">
                                    <strong>{message.k_username}</strong>
                                </div>
                                <div class="col-md-6 min right muted">
                                    <strong>{message.created}</strong>
                                </div>
                            </div>
                        </div>
                    {/each}
                </div>
            </div>

            <div class="col-md-3 sticky-top">
                <div class="card mb-sm">
                    <p class="min mb-xs"><strong>Actions</strong></p>
                    <div class="row">
                        <div class="col-md-6 action-panel-left">
                            <a href="/ticket/{ticket.id}/edit"><button class="default w-100 sm"><i class="far fa-edit"></i> Edit</button></a>
                        </div>
                        <div class="col-md-6 action-panel-right" style="padding:0; padding-right: 15px;  padding-left:3px;">
                            <button on:click={deleteTicket} class="default w-100 sm red"><i class="far fa-trash-alt"></i> Delete</button>
                        </div>    
                    </div>
                </div>

                <div class="card">
                    <p class="min mb-xs"><strong>Category</strong></p>
                    <span class="badge blue min">
                        {#if ticket.type}
                            {ticket.type}
                        {/if}
                    </span>

                    <hr />

                    <p class="min"><strong>Reported By</strong></p>
                    <p class="">
                        {#if ticket.k_username}
                            {ticket.k_username}
                        {:else}
                            <span class="placeholder">***************</span> 
                        {/if}
                    </p>

                    <hr />

                    <p class="min"><strong>Reported On</strong></p>
                    <p>
                        {#if ticket.created}
                            {ticket.created}
                        {:else}
                            <span class="placeholder">***************</span> 
                        {/if}
                    </p>

                    <hr />

                    <p class="min"><strong>Status</strong></p>
                    <p class="mb-xs">
                        {#if ticket.status} 
                            {#if ticket.status == "Completed"} 
                                <span class="green"><i class="fas fa-check-circle"></i></span> Completed
                            {/if}
                            {#if ticket.status == "Open"} 
                                <span class="blue"><i class="far fa-circle"></i> </span> Open
                            {/if}
                        {:else}
                            <span class="placeholder">***************</span> 
                        {/if}
                    </p>

                    {#if ticket.status == "Completed"} 
                        <button on:click={openTicket} class="default blue sm w-100">Mark as Open</button>
                    {/if}
                    {#if ticket.status == "Open"} 
                        <button on:click={completeTicket} class="default blue sm w-100">Mark as Completed</button>
                    {/if}

                </div>
            </div>
        </div>
    </div>
</div>