<template>
  <div>
    <div class="books">
      <div class="title">
        <h1>Nasze zbiory</h1>
        <h3>
          "Books give soul to the universe, wings to the mind, flight to the
          imagination, and life to everything”
        </h3>
      </div>

      <section>
        <div class="row">
          <div class="column-results">
            <div>
              <Filters @search="search" />
            </div>
            <div class="results">
              <div v-for="result in results" v-bind:key="result.id">
                <BookRecord :result="result" />
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
import Filters from "../components/Filters.vue";
import BookRecord from "../components/BookRecord.vue";
import { API_BASE_URL } from "../api/config";
import axios from "axios";



export default {
  name: "Books",
  data() {
    return {
      results: undefined,
      selected: undefined,
      searchValue: undefined,
      selectedCategory: "",
      availability: undefined,
    };
  },

  created() {
    this.fetchData("books");
  },

  methods: {
    fetchData(endpoint) {
      axios
        .get(`${API_BASE_URL}/${endpoint}`, {
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
    Footer,
    Filters,
    BookRecord,
  },
};
</script>




<style scoped>
* {
  box-sizing: border-box;
}
.title {
  padding-top: 100px;
}

.books {
  height: 100%;
}
.results {
  height: 600px;
  overflow: auto;
  margin-bottom: 50px;
}

h1 {
  padding: 0;
  margin: 0em 0;
  font-weight: 400;
  font-style: normal;
  font-family: "Abril Fatface", display;
  color: #3e3e3e;
  font-size: 80px;
  line-height: 1;
  letter-spacing: 0px;
  transition: 0.3s;
}

h3 {
  margin: 0;
  padding: 0;
  font-weight: 400;
  font-style: normal;
  font-family: "Eczar", serif;
  color: #1d2023;
  font-size: 30px;
  line-height: 1.2;
  letter-spacing: 0px;
  transition: 0.3s;
}

.column-results {
  float: left;
  position: relative;
  width: 80%;
  padding: 2%;
  margin-left: 10%;
  margin-right: 10%;
}
/* Remove extra left and right margins, due to padding in columns */
.row {
  margin: 1% 0 1% 0;
  height: 100vh;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Responsive columns - one column layout (vertical) on small screens */
@media screen and (max-width: 600px) {
  .column-results {
    width: 100%;
    display: block;
    margin-bottom: 20px;
  }
}
</style>