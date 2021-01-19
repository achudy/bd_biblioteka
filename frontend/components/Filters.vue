<template>
  <div class="card-filters">
    <select class="select-parameter" v-model="selected">
      <option value="title" selected="selected">Tytuł</option>
      <option value="author">Autor</option>
    </select>

    <input
      class="input-parameter"
      id="search"
      name="search"
      v-model="searchValue"
      placeholder="Szukaj..."
      @keyup.enter="sendToParent(selected, searchValue)"
    />

    <div class="group">
      <label class="typo__label">Wybierz kategorię</label>
      <multiselect
        v-model="selectedCategory"
        deselect-label="Nacij ponownie aby usunąć"
        select-label="Naciśnij aby wybrać"
        track-by="category_name"
        label="category_name"
        selected-label="Wybrane"
        placeholder="Wybierz"
        :options="categories"
        :searchable="false"
      >
        <template slot="singleLabel" slot-scope="{ option }"
          ><strong>{{ option.category_name }}</strong>
        </template>
      </multiselect>
    </div>
    <button
      class="search-button"
      @click="
        sendToParent(selected, searchValue, selectedCategory.category_name)
      "
    >
      Szukaj
    </button>
  </div>
</template>


<script>
import Multiselect from "vue-multiselect";
import axios from "axios";

import { API_BASE_URL } from "../api/config";
export default {
  name: "Filters",

  components: {
    Multiselect,
  },
  data() {
    return {
      searchValue: "",
      selected: "title",
      selectedCategory: "",
      categories: [],
    };
  },

  created() {
    this.fetchCategories();
  },

  methods: {
    sendToParent(selected, searchValue, selectedCategory) {
      this.$emit("search", selected, searchValue, selectedCategory);
    },

    fetchCategories() {
      axios
        .get(`${API_BASE_URL}/categories`, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
          },
        })
        .then((response) => {
          this.categories = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.group {
  margin: 10px;
  width: 70%;
  margin-left: 15%;
}

.group label {
  width: 100%;
  display: block;
}

.card-filters {
  height: 10%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  padding: 16px;
  text-align: center;
  background-color: #f1f1f1;
}

.select-parameter {
  display: inline;
  font-size: 16px;
  font-family: sans-serif;
  font-weight: 700;
  color: #444;
  line-height: 1.3;
  padding: 0.6em 1.4em 0.5em 0.8em;
  width: 30%;
  max-width: 100%;
  box-sizing: border-box;
  margin: 0;
  border: 1px solid #aaa;
  box-shadow: 0 1px 0 1px rgba(0, 0, 0, 0.04);
  border-radius: 0.5em;
  -moz-appearance: none;
  -webkit-appearance: none;
  appearance: none;
  background-color: #fff;
  background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23007CB2%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E"),
    linear-gradient(to bottom, #ffffff 0%, #e5e5e5 100%);
  background-repeat: no-repeat, repeat;
  background-position: right 0.7em top 50%, 0 0;
  background-size: 0.65em auto, 100%;
}

.input-parameter {
  font-size: 16px;
  font-family: sans-serif;
  font-weight: 700;
  color: #444;
  line-height: 1.3;
  padding: 0.6em 1.4em 0.5em 0.8em;
  display: inline;
  width: 40%;
  height: 20%;
  position: relative;
  margin-top: 5%;
}

.search-button {
  font-size: 16px;
  font-family: sans-serif;
  font-weight: 700;
  color: #444;
  line-height: 1.3;
  padding: 0.6em 1.4em 0.5em 0.8em;
  display: inline;
  height: 20%;
}

</style>