<template>
  <div>
    <div class="form">
      <div class="group">
        <label class="typo__label">Tytuł</label>
        <input
          id="title-input"
          type="text"
          class="input"
          required="required"
          v-model="form.title"
        />
      </div>

      <div class="group">
        <label class="typo__label">Autor</label>
        <input
          id="author-input"
          type="text"
          class="input"
          required="required"
          v-model="form.author"
        />
      </div>

      <div class="group">
        <label class="typo__label">Wybierz oddział</label>
        <multiselect
          v-model="form.selectedBranch"
          deselect-label="Nie można usunąć"
          select-label="Naciśnij aby wybrać"
          track-by="address"
          label="address"
          placeholder="Wybierz jeden"
          :options="branches"
          :searchable="false"
          :allow-empty="false"
        >
          <template slot="singleLabel" slot-scope="{ option }"
            ><strong>{{ option.address }}</strong>
          </template>
        </multiselect>
      </div>
      <div class="group">
        <div>
          <label class="typo__label">Wybierz kategorię</label>
          <multiselect
            v-model="form.selectedCategory"
            deselect-label="Naciśnij ponownie, aby odznaczyć"
            select-label="Naciśnij aby wybrać"
            selected-label="Wybrane"
            placeholder="Wybierz"
            :options="categories"
            :multiple="true"
            :close-on-select="false"
            :clear-on-select="false"
            :preserve-search="true"
          >
          </multiselect>
        </div>
      </div>

      <div class="group">
        <label class="typo__label">Dodaj nową kategorię</label>
        <input
          id="addCategoryInput"
          type="text"
          class="input"
          v-model="new_category"
          placeholder="Wprowadż kategorię którą chcesz dodać"
        />
        <button class="addCategoryButton" @click="addNewCategory">Dodaj</button>
      </div>

      <div class="group">
        <label class="typo__label">Ilość instancji: </label>
        <input type="number" v-model="form.amount" min="1" max="100" />
      </div>

      <div class="group">
        <label class="typo__label">Dla dorosłych</label>
        <input type="checkbox" id="checkbox" v-model="form.isForAdult" />
      </div>
      <button class="addCategoryButton" @click="postBook()">Dodaj</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Multiselect from "vue-multiselect";

import { API_BASE_URL } from "../api/config";

export default {
  name: "AddBook",
  components: {
    Multiselect,
  },
  data() {
    return {
      branches: [],
      categories: [],
      new_category: undefined,
      form: {
        title: "",
        author: "",
        selectedCategory: [],
        selectedBranch: null,
        isForAdult: false,
        amount: 1,
      },
    };
  },

  created() {
    this.fetchBranches();
    this.fetchCategories();
  },

  mounted() {
    this.fetchBranches();
    this.fetchCategories();
    this.update();
  },

  beforeDestroy() {
    localStorage.setItem("title", "");
    localStorage.setItem("author", "");
    localStorage.setItem("selectedCategory", []);
    localStorage.setItem("isForAdult", "");
  },

  methods: {
    update() {
      this.form.title = localStorage.getItem("title");
      this.form.author = localStorage.getItem("author");
      this.form.selectedCategory = localStorage.getItem("selectedCategory");
      if (localStorage.getItem("isForAdult") == "true") {
        this.form.isForAdult = true;
      } else {
        this.form.isForAdult = false;
      }
    },

    fetchBranches() {
      axios
        .get(`${API_BASE_URL}/branches`, {
          headers: {
            "Access-Control-Allow-Credentials": "true",
          },
        })
        .then((response) => {
          this.branches = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    fetchCategories() {
      axios
        .get(`${API_BASE_URL}/categories`, {
          headers: {
            "Access-Control-Allow-Credentials": "true",
          },
        })
        .then((response) => {
          for (let i = 0; i < response.data.length; i++) {
            this.categories.push(response.data[i].category_name);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    addNewCategory() {
      var formdata = new FormData();
      formdata.append("category_name", this.new_category);
      axios({
        method: "post",
        url: `${API_BASE_URL}/category`,
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
            alert("Kategoria została dodana");
            this.categories.push(this.new_category);
            this.new_category = "";
          }
          return true;
        },
      })
        .catch((error) => {
          console.log(error);
          this.resetInput();
        })
        .then(() => {
          this.resetInput();
        });
    },

    postBook() {
      if (this.validateForm(this.form)) {
        var formdata = new FormData();
        formdata.append("title", this.form.title);
        formdata.append("author", this.form.author);
        formdata.append("library_branch", this.form.selectedBranch.id);
        formdata.append("category_names", this.form.selectedCategory);
        formdata.append("for_adults", this.form.isForAdult);
        formdata.append("number_of_book_instances", this.form.amount);

        axios({
          method: "post",
          url: `${API_BASE_URL}/book`,
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
              alert("Książka została dodana");
            }
            return true;
          },
        })
          .catch((error) => {
            console.log(error);
            this.resetInput();
          })
          .then(() => {
            this.resetInput();
          });
      }
    },

    validateForm(form) {
      if (form.title == "") {
        alert("Musisz podać tytuł");
        return false;
      } else if (form.author == "") {
        alert("Musisz podać autora");
        return false;
      } else if (form.selectedBranch == undefined) {
        alert("Musisz podać oddział");
        return false;
      } else if (form.selectedCategory == undefined) {
        alert("Musisz podać kategorię");
        return false;
      } else {
        if (form.isForAdult) {
          form.isForAdult = 1;
        } else {
          form.isForAdult = 0;
        }
        return true;
      }
    },

    resetInput() {
      this.form.title = "";
      this.form.author = "";
      this.form.selectedBranch = [];
      this.form.selectedCategory = [];
      this.form.isForAdult = false;
      this.form.amount = 1;
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}
.form {
  padding: 10px;
  margin-top: 300px;
  box-shadow: 0 12px 15px 0 rgba(0, 0, 0, 0.24),
    0 17px 50px 0 rgba(0, 0, 0, 0.19);
}

.group {
  margin: 10px;
}

.group label {
  width: 100%;
  display: block;
}

.input {
  width: 100%;
  min-height: 40px;
  display: block;
  padding: 8px 40px 0 8px;
  border-radius: 5px;
  border: 1px solid #e8e8e8;
  background: #fff;
  font-size: 14px;
}

#addCategoryInput {
  width: 90%;
  display: inline;
}

.addCategoryButton {
  width: 10%;
  display: inline;
  min-height: 40px;
  padding: 8px 8px 0 8px;
  border-radius: 5px;
  font-size: 13px;
  text-align: center;
}

.addCategoryButton:hover {
  border: 3px solid black;
  background-color: #f2f2f2;
}
</style>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
