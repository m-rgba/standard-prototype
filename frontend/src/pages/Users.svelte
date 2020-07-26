<script>
    import { handleErrors } from "../shared.js";
    import { onMount } from "svelte";
    import moment from 'moment';
    import SidebarNav from "../components/SidebarNav.svelte"

    let localToken = localStorage.getItem("token")

    let users = [];
    let noUsers;

    let userUpdated;
    let userCreated;

    let urlParams = new URLSearchParams(window.location.search);

    onMount(() => {
        getUsers();
        if(urlParams.has('updated')){
            userUpdated = true;
            setTimeout(function(){ 
                userUpdated = false;
            }, 10000);
        }
        if(urlParams.has('created')){
            userCreated = true;
            setTimeout(function(){ 
                userCreated = false;
            }, 10000);
        }
    });

    function createDatatable() {
        if(users === undefined || users.length == 0){
            noUsers = true;
        } else {
            window.$('#datatable').DataTable({
                'info': false,
                'paging': false,
                'keys': true
            });
        }
    }

    async function getUsers() {
        await fetch("http://localhost:8000/api/users/", {
            method: "GET",
            headers: {
                Authorization: `JWT ${localToken}`
            }})
        .then(handleErrors)
        .then(response => response.json())
        .then(data => {
            users = data;
            users.forEach(user => {
                user.date_joined = moment(user.date_joined).format('MM/DD/YYYY');
            });
        })
        .then(createDatatable);
    }
</script>

<SidebarNav />

{#if userUpdated == true}
    <div class="alert">
        <i class="fas fa-check"></i> The user has been updated.
    </div>
{/if}
{#if userCreated == true}
    <div class="alert">
        <i class="fas fa-check"></i> The user has been created.
    </div>
{/if}

<div class="content-expanded">
    <div class="page-top pb-md container-fluid">

        <div class="row">
            <div class="col-md-6 mb-sm">
                <h2 style="padding-top:4px;" class="black">Users</h2>
            </div>
            <div class="col-md-6 mb-sm right">
                <a href="/create-user"><button class="primary mobile-w100">Create New User</button></a>
            </div>
        </div>

        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <div class="table-responsive">
                        <table id="datatable" class="display dataTable" style="width:100%">
                            <thead>
                                <tr>
                                    <th>Email</th>
                                    <th>User Type</th>
                                    <th>Active</th>
                                    <th>Added On</th>
                                </tr>
                            </thead>
                            <tbody>
                                {#if noUsers == true}
                                    <td colspan="6" style="padding:4px;"class="center">
                                        <p class="w-100 mb-xs">No Tickets Yet</p>
                                        <a href="/create-ticket"><button class="primary">Create a New Ticket</button></a>
                                    </td>
                                {:else}
                                    {#each users as user}
                                        <tr>
                                            <td><a href="/user/{user.id}">
                                                {user.email}
                                            </a></td>
                                            <td>
                                                {#if user.is_administrator == true} 
                                                    <strong>Administrator</strong>
                                                {/if}
                                                {#if user.is_administrator == false} 
                                                    User
                                                {/if}
                                            </td>
                                            <td>
                                                {#if user.is_active == true} 
                                                    <i class="far fa-check-circle green"></i> Active
                                                {/if}
                                                {#if user.is_active == false} 
                                                    <i class="far fa-times-circle red"></i> Inactive
                                                {/if}
                                            </td>
                                            <td>
                                                {user.date_joined}
                                            </td>
                                        </tr>
                                    {:else}
                                        <tr>
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
                                        </tr>
                                        <tr>
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
                                        </tr>
                                        <tr>
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