<template>
  <div class="card-result">
    <div class="img-container">
      <img class="user-icon" src="~@/assets/user.png" alt="User" />
    </div>

    <div class="login">
      <p>Login: {{ result.login }}</p>
    </div>

    <div class="name">
      <p>Imię: {{ result.name }}</p>
    </div>

    <div class="surname">
      <p>Nazwisko: {{ result.surname }}</p>
    </div>

    <div class="birth-date">
      <p>Data urodzenia: {{ result.birth_date }}</p>
    </div>

    <button @click="deleteUser(result.id)">Usuń konto</button>
  </div>
</template>


<script>
import axios from "axios";
import {API_BASE_URL} from "../api/config";
export default {
  name: "UserRecord",
  props: {
    result: {
      type: Object,
    },
  },
  methods: {
    deleteUser(id) {
      axios
        .delete(`${API_BASE_URL}/users`, {
          params: {
            id: id,
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
          if(response.data.status == "OK"){
            alert("Konto zostało usunięte");
            this.$emit("deleteThisRow");

          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>


<style scoped>
.card-result {
  position: relative;
  margin: 1%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  padding: 16px;
  text-align: center;
  background-color: #f1f1f1;
}

.user-icon {
  height: 80%;
  display: block;
}

.img-container {
  position: absolute;
  margin-bottom: 10px;
  width: 10%;
  height: 90%;
}

.login,
.name,
.surname,
.birth-date {
  overflow: auto;
  position: relative;
  width: 50%;
  margin-left: 20%;
}

button{
  width: 20%;
  margin-right: 10%;
}

p{
  text-align: left;
}
</style>