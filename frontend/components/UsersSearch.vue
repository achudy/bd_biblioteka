<template>
  <div class="users-search-wrapper">
    <div class="filters">
      <input
        class="input-parameter"
        id="search"
        name="search"
        placeholder="Search for users.."
        v-model="searchValue"
        @keyup.enter="search(searchValue)"
      />
      <button class="search-button" @click="search(searchValue)">Search</button>
    </div>
    <div class="results">
      <div v-for="(result, index) in results" v-bind:key="result.id">
        <UserRecord :result="result" v-on:deleteThisRow="deleteThisRow(index)" />
      </div>
    </div>
  </div>
</template>

<script>
import UserRecord from "../components/UserRecord.vue";

import axios from "axios";
import {API_BASE_URL} from "../api/config";

export default {
  name: "UserSearch",
  data() {
    return {
      results: undefined,
      searchValue: undefined,
    };
  },
  created() {
    this.fetchData("users");
  },
  methods: {
    deleteThisRow(index){
      this.$delete(this.results, index)
    },

    fetchData(endpoint) {
      axios
        .get(`${API_BASE_URL}/${endpoint}`, {
          auth: {
            username: localStorage.getItem("login"),
            password: localStorage.getItem("password"),
          },
        })
        .then((response) => {
          this.results = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    search(searchValue) {
      axios
        .get(`${API_BASE_URL}/users/user?login=${searchValue}`, {
          auth: {
            username: localStorage.getItem("login"),
            password: localStorage.getItem("password"),
          },
        })
        .then((response) => {
          this.results = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  
  components: {
    UserRecord,
  },
};
</script>


<style scoped>
* {
  box-sizing: border-box;
}

.users-search-wrapper {
  background-color: grey;
  margin-top: 10%;
  width: 100%;
  height: 30%;
}

/*                SEARCH               */
.filters {
  height: 30px;
  background-color: grey;
  margin-bottom: 20px;
}
.input-parameter {
  height: 100%;
}
.search-button {
  height: 100%;
  width: 5%;
  margin-bottom: 95%;
  display: inline;
}
#search {
  background-image: url("~@/assets/search.png");
  background-position: 8px 1px;
  background-repeat: no-repeat;
  width: 95%;
  font-size: 16px;
  padding: 12px 20px 12px 40px;
  border: 1px solid #ddd;
  margin-bottom: 12px;
}

.results {
  height: 600px;
  overflow: auto;
  margin-bottom: 50px;
}
</style>