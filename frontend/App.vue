<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">HOME</router-link> |
      <router-link to="/books">BOOKS</router-link> |
      <router-link to="/Registration">PROFILE</router-link>
      <!-- dodanie tylko sprawia że mamy nowy link ale nie wie co wyświetlić w router-view (bo tam jest wszystko wyswietlane) -->
      <router-link
        v-if="authenticated"
        to = 'Registration'
        v-on:click.native="logoutUser()"
        replace
        >Logout</router-link
      >
    </div>
    <router-view @authenticated="setAuthenticated" />
  </div>
</template>



<script>
import {isLoggedIn, logout} from "./utils/auth.js";

export default {
  name: "App",
  data() {
    return {
      authenticated: false,
    };
  },
  created(){
      this.authenticated = isLoggedIn();
  },

  methods: {
    setAuthenticated(status) {
      this.authenticated = status;
    },
    logoutUser(){
      logout();
      this.authenticated = false;
      this.$router.replace({ name: "Registration" });
    }

  },
};
</script>


<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, Helvetica, sans-serif;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: black;
}

#nav {
  top: 0px;
  z-index: 100;
  position: fixed;
  width: 100%;
  padding: 30px;
  background-color: rgba(81, 81, 81, 0.8);
}

#nav a {
  color: rgb(224, 224, 224);
  text-decoration: none;
  padding: 1%;
}

#nav a.router-link-exact-active {
  color: whitesmoke;
}

#nav a.router-link-exact-active {
  background-color: rgba(89, 89, 89, 0.4);;
}
</style>
