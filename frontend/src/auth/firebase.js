import firebase from 'firebase/app';
import 'firebase/auth';
import { navigate } from "svelte-routing";
import { handleErrors } from "../shared.js";

/* ADD FIREBASE CONFIG INFO HERE */
var firebaseConfig = {
};

firebase.initializeApp(firebaseConfig)

function getToken(){
    return new Promise(function(resolve, reject) {
        auth.onAuthStateChanged(function(user) {
            if (user) {
                auth.currentUser.getIdToken(true)
                .then(function(token) {
                    localStorage.setItem("token", token);
                })
                .then(function() {
                    var token = localStorage.getItem("token");            
                    fetch("http://localhost:8000/api/profile/", {
                        method: "GET",
                        headers: {
                        Authorization: `JWT ${token}`
                    }})
                    .then(handleErrors)
                    .then(response => response.json())
                    .then(data => {
                        var user_email = data[0].email;
                        var is_administrator = data[0].is_administrator;
                
                        localStorage.setItem("user_email", user_email);
                        localStorage.setItem("is_administrator", is_administrator);

                        console.log("Token Refreshed >>")
                        console.log(token);
                        console.log(user_email);
                        console.log(is_administrator);
                        resolve();
                    })
                })
                .catch(function(error) {
                    console.log(error);
                    navigate("/login", { replace: true });
                    reject();
                });
            }
        });
    });
};

export const auth = firebase.auth();
export const emailProvider = new firebase.auth.EmailAuthProvider();
export const googleProvider = new firebase.auth.GoogleAuthProvider();

export { getToken };