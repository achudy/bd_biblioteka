<template>
  <div class="card-result" style="height: 200px">
    <div class="img-container">
      <img class="book-icon" src="~@/assets/book_icon.png" alt="Book" />
    </div>

    <p class = "title-p">{{ result.title }}</p>
    <br />
    <p>{{ result.author }}</p>
    <br />

    <!--
    <div class="category">
      <p>{{ result.category }}</p>
    </div>


    <div class="branch">
      <p>{{ result.branch }}</p>
    </div>
    -->

    <button @click="expand(result.title, result.author)" class="collapsible">
      Sprawdź dostępność
    </button>
    <div class="availability">
      <table>
        <thead>
          <tr>
            <th>Adres</th>
            <th>Nazwa jednostki</th>
            <th>Ilość dostępnych kopii</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="record in availability" v-bind:key="record.id">
            <th>
              {{ record.address }}
            </th>
            <th>
              {{ record.library_branch_name }}
            </th>
            <th>
              {{ record["number of copies"] }}
            </th>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import { API_BASE_URL } from "../api/config";

export default {
  name: "BookRecord",
  data() {
    return {
      availability: undefined,
    };
  },
  props: {
    result: {
      type: Object,
    },
  },
  methods: {
    expand(title, author) {
      let card = document.getElementsByClassName("card-result");
      for (var i = 0; i < card.length; i++) {
        if (card[i].getElementsByClassName("title-p")[0].innerHTML == title) {
          if (card[i].style.height == "200px") {
            card[i].getElementsByClassName(
              "collapsible"
            )[0].style.marginBottom = "170px";
            card[i].style.overflow = "auto";
            card[i].style.height = "400px";
            card[i].getElementsByClassName("collapsible")[0].innerHTML = "Ukryj dostępność";
          } else {
            card[i].getElementsByClassName(
              "collapsible"
            )[0].style.marginBottom = "0px";
            card[i].style.overflow = "hidden";
            card[i].style.height = "200px";
            card[i].getElementsByClassName("collapsible")[0].innerHTML = "Sprawdź dostępność";
          }
        }
      }
      this.getAviability(title, author);
    },
    getAviability(title, author) {
      axios
        .get(`${API_BASE_URL}/availability?title=${title}&author=${author}`)
        .then((response) => {
          this.availability = response.data;
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
  margin: 2%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  text-align: center;
  background-color: #f1f1f1;
  overflow: hidden;
}

.book-icon {
  position: absolute;
  height: 150px;
  display: inline;
}

.img-container {
  margin-bottom: 10px;
  margin-right: 80%;
  width: 10%;
  height: 150px;
  display: inline;
}

.title,
.author,
.category,
.branch {
  display: inline;
  overflow: auto;
  width: 30%;
  margin-left: 25%;
}

.collapsible {
  position: absolute;
  bottom: 0px;
  outline: none;
  width: 100%;
  margin-left: 0px;
  margin-right: 0px;
  display: block;
}

.collapsible:hover {
  background-color: #ccc;
}

.content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  background-color: #f1f1f1;
}

.availability {
  margin-top: 160px;
}

table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
}

table {
  width: 100%;
}
</style>