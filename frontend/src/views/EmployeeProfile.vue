<template>
  <div>
    <div class="Profile">
      <section>
        <div class="row">
          <div class="column-user-personal-info">
            <div class="img-container">
              <img src="~@/assets/user.png" alt="Profile picture" />
            </div>
            <div class="user-info">
              <span class="first-name"
                >Imię: {{ this.personal_data.name }} </span
              ><br />
              <span class="second-name">
                Nazwisko:
                {{ this.personal_data.surname }}
              </span>
              <span
                >Status użytkownika: {{ this.personal_data.user_type }}
              </span>
            </div>
            <hr />
            <button @click="changeComponent('AddBook')" class="menu-button">
              DODAJ KSIĄŻKĘ
            </button>
            <button @click="changeComponent('DeleteBook')" class="menu-button">
              ZARZĄDZAJ KSIĄŻKAMI
            </button>
            <button @click="changeComponent('AddEmployee')" class="menu-button">
              DODAJ PRACOWNIKA
            </button>
            <button @click="changeComponent('UsersSearch')" class="menu-button">
              UŻYTKOWNICY
            </button>
            <button @click="changeComponent('AddBranch')" class="menu-button">
              DODAJ ODDZIAŁ
            </button>
            <button @click="changeComponent('BorrowBook')" class="menu-button">
              WYPOŻYCZ
            </button>
            <button @click="changeComponent('ReturnBook')" class="menu-button">
              ZWROTY
            </button>
          </div>
          <div class="column-status">
            <component v-bind:is="currentComponent"></component>
          </div>
        </div>
      </section>
    </div>
    <Footer />
  </div>
</template>

<script>
import UsersSearch from "../components/UsersSearch.vue";
import BookSearch from "../components/BookSearch.vue";
import Footer from "../components/Footer.vue";
import AddBook from "../components/AddBook.vue";
import DeleteBook from "../components/DeleteBook.vue";
import AddEmployee from "../components/AddEmployee.vue";
import BorrowBook from "../components/BorrowBook";
import ReturnBook from "../components/ReturnBook";
import AddBranch from "../components/AddBranch";
import axios from "axios";

import { API_BASE_URL } from "../api/config";
import { EventBus } from "../utils/eventBus";
export default {
  name: "EmployeeProfile",
  data() {
    return {
      currentComponent: "",
      personal_data: {
        name: undefined,
        surname: undefined,
        user_type: undefined,
      },
    };
  },
  components: {
    UsersSearch,
    BookSearch,
    AddBook,
    DeleteBook,
    AddEmployee,
    BorrowBook,
    ReturnBook,
    AddBranch,
    Footer,
  },

  created() {
    this.fetchUserPersonalData();
  },

  mounted() {
    if (localStorage.getItem("currentComponent")) {
      this.currentComponent = localStorage.getItem("currentComponent");
    } else {
      this.currentComponent = "AddBook";
    }
    EventBus.$on("componentFromManageBooks", (component) => {
      this.currentComponent = component;
    });
  },

  methods: {
    fetchUserPersonalData() {
      axios
        .get(`${API_BASE_URL}/users/user`, {
          params: {
            login: localStorage.getItem("login"),
          },
          auth: {
            username: localStorage.getItem("login"),
            password: localStorage.getItem("password"),
          },
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
          },
        })
        .then((response) => {
          this.personal_data = response.data[0];
        })
        .catch((error) => {
          console.log(error);
        });
    },

    changeComponent(component) {
      localStorage.setItem("currentComponent", component);
      switch (component) {
        case "UsersSearch":
          this.currentComponent = UsersSearch;
          break;
        case "DeleteBook":
          this.currentComponent = DeleteBook;
          break;
        case "AddBook":
          this.currentComponent = AddBook;
          break;
        case "AddEmployee":
          this.currentComponent = AddEmployee;
          break;
        case "BorrowBook":
          this.currentComponent = BorrowBook;
          break;
        case "ReturnBook":
          this.currentComponent = ReturnBook;
          break;
        case "AddBranch":
          this.currentComponent = AddBranch;
          break;
      }
    },
  },
};
</script>


<style scoped>
* {
  box-sizing: border-box;
}
.Profile {
  height: 100%;
}
.column-user-personal-info {
  float: left;
  width: 20%;
  margin-right: 1%;
  margin-left: 4%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  background-color: rgb(242, 242, 242);
}

.user-info {
  margin-bottom: 30px;
}

.img-container {
  width: 60%;
  margin-left: 20%;
  margin-right: 20%;
  margin-top: 30%;
}

.img-container img {
  display: block;
  width: 100%;
}

.user-info {
  margin-top: 20%;
}

.first-name,
.second-name {
  display: block;
  font-family: Montserrat, "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 30px;
}

.column-status {
  float: left;
  width: 70%;
  margin-right: 4%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  background-color: rgb(242, 242, 242);
}
/* Remove extra left and right margins, due to padding in columns */
.row {
  margin: 1% 0 1% 0;
}

.menu-button {
  width: 100%;
  height: 40px;
  margin-bottom: 10px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

@media screen and (max-width: 600px) {
  .column {
    width: 100%;
    display: block;
    margin-bottom: 20px;
  }
}
</style>