<template>
  <div class="book-search-wrapper">
    <div class="filters-wrapper">
      <Filters @search="search" />
    </div>
    <div class="books">
      <div v-for="result in results" v-bind:key="result.id">
        <BookRecordWithOptions :result="result" />
      </div>
    </div>
  </div>
</template>

<script>
import Filters from "../components/Filters.vue";
import BookRecordWithOptions from "../components/BookRecordWithOptions.vue";
import axios from "axios";

import {API_BASE_URL} from "../api/config";

export default {
  name: "BookSearch",

  data() {
    return {
      results: undefined,
      selected: undefined,
      searchValue: undefined,
    };
  },
  created() {
    this.fetchData("books");
  },
  methods: {
    fetchData(endpoint) {
      axios
        .get(`${API_BASE_URL}/${endpoint}`)
        .then((response) => {
          this.results = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    search(selected, searchValue) {
      let endpoint = undefined;
      if (searchValue) {
        switch (selected) {
          case "Tytuł":
            endpoint = "title";
            break;
          case "Kategoria":
            endpoint = "category";
            break;
          case "Autor":
            endpoint = "author";
            break;
        }
      }
      if (endpoint != undefined) {
        axios
          .get(`${API_BASE_URL}/books/filter?${endpoint}=${searchValue}`)
          .then((response) => {
            this.results = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
  components: {
    Filters,
    BookRecordWithOptions,
  },
};
</script>

<style scoped>
.book-search-wrapper {
  background-color: grey;
  margin-top: 10%;
  width: 100%;
  height: 30%;
}

.filters-wrapper {
  background-color: grey;
}

.books {
  height: 300px; /*do naprawy */
  overflow: auto;
}
</style>