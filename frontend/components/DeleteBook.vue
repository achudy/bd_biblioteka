<template>
  <div class="book-search-wrapper">
    <div class="filters-wrapper">
      <Filters @search="search" />
    </div>
    <div class="books">
      <div v-for="(result, index) in results" v-bind:key="result.id">
        <BookRecordWithOptions
          :result="result"
          v-on:deleteThisRow="deleteThisRow(index)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Filters from "../components/Filters.vue";
import BookRecordWithOptions from "../components/BookRecordWithOptions.vue";
import axios from "axios";

import { API_BASE_URL } from "../api/config";

export default {
  name: "DeleteBook",

  data() {
    return {
      results: undefined,
      selected: undefined,
      searchValue: undefined,
      title: "",
      author: "",
      category: "",
    };
  },
  created() {
    this.fetchData("books");
  },
  methods: {
    deleteThisRow(index) {
      this.$delete(this.results, index);
    },

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
    search(selected, searchValue, selectedCategory) {
      let params = {};
      switch (selected) {
        case "title":
          params.title = searchValue;
          break;
        case "author":
          params.author = searchValue;
          break;
      }
      if (selectedCategory != "") {
        params.category = selectedCategory;
      }

      axios
        .get(`${API_BASE_URL}/books/filter`, {
          params,
          headers: {
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
  height: 500px; /*do naprawy */
  overflow: auto;
  margin-bottom: 50px;
}
</style>