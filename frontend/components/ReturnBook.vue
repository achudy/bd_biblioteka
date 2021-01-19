<template>
  <div>
    <div class="form">
      <div class="group">
        <label class="typo__label">Wybierz użytkownika</label>
        <multiselect
          v-model="selectedUser"
          :options="users"
          placeholder="Wybierz jednego"
          deselect-label="Naciśnij ponownie, aby odznaczyć"
          select-label="Naciśnij aby wybrać"
          selected-label="Wybrane"
          track-by="login"
          label="login"
        ></multiselect>
        <button class="returnButton" @click="fetchBorrowedBooks">Sprawdź zaległości</button>
      </div>
    </div>
    <div v-for="(result, index) in borrowedBooks" v-bind:key="result.id">
      <BorrowedBookWithOptions
        :result="result"
        v-on:deleteThisRow="deleteThisRow(index)"
      />
    </div>
  </div>
</template>

<script>
import Multiselect from "vue-multiselect";
import axios from "axios";
import BorrowedBookWithOptions from "./BorrowedBookWithOptions.vue";

import { API_BASE_URL } from "../api/config";
export default {
  components: {
    Multiselect,
    BorrowedBookWithOptions,
  },
  data() {
    return {
      users: [],
      selectedUser: undefined,
      borrowedBooks: undefined,
      // borrowedBook: undefined,
    };
  },

  created() {
    this.fetchUsers();
  },
  methods: {
    deleteThisRow(index) {
      this.$delete(this.borrowedBooks, index);
    },
    fetchUsers() {
      axios
        .get(`${API_BASE_URL}/users`, {
          auth: {
            username: localStorage.getItem("login"),
            password: localStorage.getItem("password"),
          },
        })
        .then((response) => {
          this.users = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    fetchBorrowedBooks() {
      axios
        .get(`${API_BASE_URL}/borrowed/user`, {
          params: {
            login: this.selectedUser.login,
          },
          auth: {
            username: localStorage.getItem("login"),
            password: localStorage.getItem("password"),
          },
        })
        .then((response) => {
          this.borrowedBooks = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.form {
  margin-top: 300px;
}

.returnButton {
  margin-top: 10px;
  width: 15%;
  display: inline;
  min-height: 40px;
  padding: 8px 8px 0 8px;
  border-radius: 5px;
  font-size: 13px;
  text-align: center;
}

.returnButton:hover {
  border: 3px solid black;
  background-color: #f2f2f2;
}
</style>