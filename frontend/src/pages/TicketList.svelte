<script>
    import { handleErrors } from "../shared.js";
    import { onMount } from "svelte";
    import moment from 'moment';
    import SidebarNav from "../components/SidebarNav.svelte"

    let localToken = localStorage.getItem("token")
    let tickets = [];
    let deleteSuccess;
    let noTickets;
    let urlParams = new URLSearchParams(window.location.search);
    onMount(() => {
        getTickets();

        if(urlParams.has('del')){
            deleteSuccess = true;
            setTimeout(function(){ 
                deleteSuccess = false;
            }, 10000);
        }
    });

    function createDatatable() {
        if(tickets === undefined || tickets.length == 0){
            noTickets = true;
        } else {
            window.$('#datatable').DataTable({
                columnDefs: [{
                    targets: 1,
                    render: window.$.fn.dataTable.render.ellipsis( 50 )
                }],
                'info': false,
                'paging': false,
                'keys': true
            });
        }
    }

    async function getTickets() {
        await fetch("http://localhost:8000/api/ticket/", {
            method: "GET",
            headers: {
                Authorization: `JWT ${localToken}`
            }})
        .then(handleErrors)
        .then(response => response.json())
        .then(data => {
            tickets = data;
            tickets.forEach(ticket => {
                ticket.created = moment(ticket.created).format('MM/DD/YYYY');
            });
        })
        .then(createDatatable);
    }
</script>

<SidebarNav />

{#if deleteSuccess == true}
    <div class="alert">
        <i class="fas fa-check"></i> Your ticket was successfully deleted.
    </div>
{/if}

<div class="content-expanded">
    <div class="page-top pb-md container-fluid">

        <div class="row">
            <div class="col-md-6 mb-sm">
                <h2 style="padding-top:4px;" class="black">Tickets</h2>
            </div>
            <div class="col-md-6 mb-sm right">
                <a href="/create-ticket"><button class="primary mobile-w100">Create New Ticket</button></a>
            </div>
        </div>

        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <div class="table-responsive">
                        <table id="datatable" class="display dataTable" style="width:100%">
                            <thead>
                                <tr>
                                    <th>Subject</th>
                                    <th>Content</th>
                                    <th>Type</th>
                                    <th>Status</th>
                                    <th>Reported On</th>
                                    <th>Reported By</th>
                                </tr>
                            </thead>
                            <tbody>
                                {#if noTickets == true}
                                    <td colspan="6" style="padding:4px;"class="center">
                                        <p class="w-100 mb-xs">No Tickets Yet</p>
                                        <a href="/create-ticket"><button class="primary">Create a New Ticket</button></a>
                                    </td>
                                {:else}
                                    {#each tickets as ticket}
                                        <tr>
                                            <td><a href="/ticket/{ticket.id}">
                                                {ticket.subject}
                                            </a></td>
                                            <td>
                                                {@html ticket.content}
                                            </td>
                                            <td><span class="badge blue min">
                                                {ticket.type}
                                            </span></td>
                                            <td>
                                                {#if ticket.status == "Completed"} 
                                                    <span class="green"><i class="fas fa-check-circle"></i></span> Completed
                                                {/if}
                                                {#if ticket.status == "Open"} 
                                                    <span class="blue"><i class="far fa-circle"></i> </span> Open
                                                {/if}
                                            </td>
                                            <td>
                                                {ticket.created}
                                            </td>
                                            <td>
                                                {ticket.k_username}
                                            </td>
                                        </tr>
                                    {:else}
                                        <tr>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                        </tr>
                                        <tr>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                        </tr>
                                        <tr>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                        </tr>
                                        <tr>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                        </tr>
                                        <tr>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                            <td><span class="placeholder">**********</span></td>
                                        </tr>
                                    {/each}
                                {/if}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

    </div>
</div>