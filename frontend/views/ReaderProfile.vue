<template>
  <div>
    <div class="profile">
      <section>
        <div class="row">
          <div class="column-user-personal-info">
            <div class="img-container">
              <img src="~@/assets/user.png" alt="Profile picture" />
            </div>
            <div class="user-info">
              <span class="first-name"> {{ this.personal_data.name }} </span
              ><br />
              <span class="second-name">
                {{ this.personal_data.surname }}
              </span>
              <span> {{ this.personal_data.user_type }} </span><br />
              <span> Kara za nieoddane książki: {{ this.penalty }} </span>
            </div>
          </div>

          <div class="column-status">
            <div class="borrowed-books">
              <hr />
              <p>Wypożyczone książki</p>
              <hr />

              <div v-for="result in results" v-bind:key="result.id">
                <BorrowedBook :result="result" />
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
    <Footer />
  </div>
</template>

<script>
import Footer from "../components/Footer.vue";
import BorrowedBook from "../components/BorrowedBook.vue";
import axios from "axios";
import { API_BASE_URL } from "../api/config";

export default {
  name: "Profile",
  components: {
    Footer,
    BorrowedBook,
  },

  data() {
    return {
      results: undefined,
      personal_data: {
        name: undefined,
        surname: undefined,
        user_type: undefined,
      },
      penalty: undefined,
    };
  },

  created() {
    this.fetchBorrowedBooks();
    this.fetchUserPersonalData();
    this.fetchPenalty();
  },

  methods: {
    fetchBorrowedBooks() {
      axios
        .get(`${API_BASE_URL}/borrowed/user`, {
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
          this.results = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

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

    fetchPenalty() {
      axios
        .get(`${API_BASE_URL}/penalty`, {
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
          this.penalty = response.data["penalty in PLN"];
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>


<style scoped>
* {
  box-sizing: border-box;
}

.profile {
  height: 100vh;
}
.column-user-personal-info {
  float: left;
  width: 20%;
  margin-right: 1%;
  margin-left: 4%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  background-color: rgb(242, 242, 242);
  height: auto;
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
  height: 100%;
}
/* Remove extra left and right margins, due to padding in columns */
.row {
  margin: 1% 0 1% 0;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

.borrowed-books {
  margin-top: 10%;
}

@media screen and (max-width: 1000px) {
  .column-status {
    width: 100%;
    display: block;
    margin-bottom: 20px;
  }
  .column-user-personal-info {
    width: 100%;
    display: block;
    margin-bottom: 20px;
  }
}
</style>