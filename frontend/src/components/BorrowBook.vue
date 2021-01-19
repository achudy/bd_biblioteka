<template>
  <div>
    <div class="form">
      <div class="group">
        <label class="typo__label">Wybierz książkę</label>
        <multiselect
          v-model="selectedBook"
          :options="books"
          placeholder="Wybierz jedną"
          deselect-label="Naciśnij ponownie, aby odznaczyć"
          select-label="Naciśnij aby wybrać"
          selected-label="Wybrane"
          track-by="title"
          label="title"
        ></multiselect>
      </div>

      <div class="group">
        <button class="checkButton" @click="fetchInstances()">Sprawdź dostępne egzemplarze</button
        ><br />
        <label class="typo__label">Wybierz egzemplarz</label>
        <multiselect
          v-model="selectedInstance"
          :options="booksInstances"
          placeholder="Wybierz jedną"
          deselect-label="Naciśnij ponownie, aby odznaczyć"
          select-label="Naciśnij aby wybrać"
          selected-label="Wybrane"
          track-by="address"
          label="address"
        ></multiselect>
      </div>

      <div class="group">
        <label class="typo__label">Wybierz użytkownika</label>
        <multiselect
          v-model="selectedUser"
          :options="users"
          placeholder="Wybierz jedną"
          deselect-label="Naciśnij ponownie, aby odznaczyć"
          select-label="Naciśnij aby wybrać"
          selected-label="Wybrane"
          track-by="login"
          label="login"
        ></multiselect>
      </div>

      <div class="group">
        <button class="borrowButton" @click="borrowBook">Wypożycz</button>
      </div>
    </div>
  </div>
</template>

<script>
import Multiselect from "vue-multiselect";
import axios from "axios";

import { API_BASE_URL } from "../api/config";

export default {
  components: {
    Multiselect,
  },
  data() {
    return {
      books: [],
      selectedBook: undefined,

      booksInstances: [],
      selectedInstance: undefined,

      users: [],
      selectedUser: undefined,

      form: {
        user_id: null,
        book_instance_id: null,
      },
    };
  },

  created() {
    this.fetchBooks();
    this.fetchUsers();
  },
  methods: {
    fetchBooks() {
      axios
        .get(`${API_BASE_URL}/books`, {
          headers: {
            "Access-Control-Allow-Credentials": "true",
          },
        })
        .then((response) => {
          this.books = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    fetchInstances() {
      axios
        .get(`${API_BASE_URL}/availability`, {
          params: {
            title: this.selectedBook.title,
            author: this.selectedBook.author,
          },
          auth: {
            username: localStorage.getItem("login"),
            password: localStorage.getItem("password"),
          },
          headers: {
            "Access-Control-Allow-Credentials": "true",
          },
        })
        .then((response) => {
          this.booksInstances = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
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
          console.log(error.message);
        });
    },

    borrowBook() {
      if (this.selectedInstance == undefined) {
        alert("Proszę wybrać książkę");
        return;
      }

      if (this.selectedUser == undefined) {
        alert("Proszę wybrać użytkownika");
        return;
      }
      this.form.book_instance_id = this.selectedInstance[
        "book instance ids"
      ].split(",")[0];
      this.form.user_id = this.selectedUser.id;
      if (this.validateForm(this.form)) {
        var formdata = new FormData();
        formdata.append("book_instance_id", this.form.book_instance_id);
        formdata.append("user_id", this.form.user_id);

        axios({
          method: "post",
          url: `${API_BASE_URL}/borrowed`,
          data: formdata,
          auth: {
            username: localStorage.getItem("login"),
            password: localStorage.getItem("password"),
          },
          headers: {
            "Access-Control-Allow-Credentials": "true",
          },
          validateStatus: (status) => {
            if (status == "200") {
              alert("Książka została wypożyczona");
              this.clearForm();
            }

            return true;
          },
        })
          .catch((error) => {
            console.log(error);
            this.clearForm();
          })
          .then((response) => {
            if (response.data.ids != undefined) {
              alert("Użytkownik ma zaległe książki które musi zwrócić");
            }

            this.clearForm();
          });
      }
    },
    validateForm(form) {
      if (form.book_instance_id == "") {
        alert("Proszę wybrać książkę");
        return false;
      } else if (form.user_id == "") {
        alert("Proszę wybrać użytkownika");
        return false;
      } else {
        return true;
      }
    },

    clearForm() {
      this.selectedUser = undefined;
      this.selectedInstance = undefined;
      this.selectedBook = [];
    },
  },
};
</script>

<style scoped>
.form {
  margin-top: 300px;
  padding: 15px;
}

.checkButton {
  margin: 10px;
  border-radius: 5px;
  font-size: 13px;
  text-align: center;
}

.checkButton:hover {
  border: 3px solid black;
  background-color: #f2f2f2;
}

.borrowButton {
  margin-top: 10px;
  width: 10%;
  display: inline;
  min-height: 40px;
  padding: 8px 8px 0 8px;
  border-radius: 5px;
  font-size: 13px;
  text-align: center;
}

.borrowButton:hover {
  border: 3px solid black;
  background-color: #f2f2f2;
}
</style>