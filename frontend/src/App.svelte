<script>
	import { Router, Route, navigate } from "svelte-routing";

	/* Auth */
	import LoginFlow from "./auth/Auth.svelte";

	/* Helpers */
	import Redirect from "./components/Redirect.svelte";

	/* Ticket Pages */
	import TicketList from "./pages/TicketList.svelte";
	import TicketExpanded from "./pages/TicketExpanded.svelte";
	import TicketCreate from "./pages/TicketCreate.svelte";
	import TicketEdit from "./pages/TicketEdit.svelte";

	/* User Management */
	import Users from "./pages/Users.svelte";
	import Profile from "./pages/Profile.svelte";
	import UserCreate from "./pages/UserCreate.svelte";
	import UserEdit from "./pages/UserEdit.svelte";

	let localToken = localStorage.getItem("token")
	if (localToken === null){
		navigate("/login", { replace: true });
	}
</script>

<Router>
	<Route path="login"><LoginFlow /></Route>
	
	<Route path="/"><Redirect to="tickets" /></Route>
	<Route path="tickets"><TicketList /></Route>
	<Route path="create-ticket"><TicketCreate /></Route>
	<Route path="ticket/:id/edit" let:params> <TicketEdit id="{params.id}" /> </Route>
	<Route path="ticket/:id" let:params> <TicketExpanded id="{params.id}" /> </Route>

	<Route path="users"><Users /></Route>
	<Route path="create-user"><UserCreate /></Route>
	<Route path="user/:id" let:params><UserEdit id="{params.id}" /></Route>
	<Route path="profile"><Profile /></Route>
</Router>