import { navigate } from "svelte-routing";

function handleErrors(response) {
	if (response.status === 401 ) {
		navigate("/login/?auth_error=true", { replace: true });
	}
	if (!response.ok) {
		console.log(response)
		throw Error(response.statusText);
		statusText = response.statusText;
	}
	return response;
}

export { handleErrors }