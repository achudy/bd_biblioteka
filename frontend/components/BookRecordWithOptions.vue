<template>
  <div class="card-result" style="height: 200px">
    <div class="img-container">
      <img class="book-icon" src="~@/assets/book_icon.png" alt="Book" />
    </div>

    <p class="title-p">{{ result.title }}</p>
    <br />
    <p>{{ result.author }}</p>
    <br />

    <button @click="deleteBook(result.id)">Usuń książkę</button>

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
            <th>Usuń</th>
            <th>Dodaj</th>
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
            <th>
              <button
                @click="
                  deleteInstance(
                    record['book instance ids'],
                    result.title,
                    result.author
                  )
                "
              >
                USUŃ
              </button>
            </th>
            <th>
              <button
                class="addInstance"
                @click="
                  addInstance(
                    result.title,
                    result.author,
                    result.for_adults,
                    record.id
                  )
                "
              >
                DODAJ
              </button>
            </th>
          </tr>
        </tbody>
      </table>

      <button
        @click="
          addNewInstanceOfExistingBook(
            result.title,
            result.author,
            result['for_adults']
          )
        "
      >
        Dodaj instancje
      </button>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import { API_BASE_URL } from "../api/config";
import { EventBus } from "../utils/eventBus";
export default {
  name: "BookRecordWithOptions",
  data() {
    return {
      availability: undefined,
      bookToAdd: {
        title: "",
        author: "",
        selectedCategory: [],
        isForAdult: "",
      },
      form: {
        title: "",
        author: "",
        selectedCategory: [],
        selectedBranch: null,
        isForAdult: "",
        amount: 1,
      },
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

    deleteInstance(id, title, author) {
      id = id.split(",")[0];
      axios
        .delete(`${API_BASE_URL}/bookinstance`, {
          params: {
            id: id,
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
          this.availability = response.data;
          this.getAviability(title, author);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    deleteBook(bookId) {
      axios
        .delete(`${API_BASE_URL}/book`, {
          params: {
            id: bookId,
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
          if (response.status == "200") {
            this.$emit("deleteThisRow");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    addNewInstanceOfExistingBook(title, author, for_adults) {
      axios
        .get(`${API_BASE_URL}/categories/book`, {
          params: {
            title: title,
            author: author,
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
          if (response.status) {
            for (let i = 0; i < response.data.length; i++) {
              this.bookToAdd.selectedCategory.push(
                response.data[i].category_name
              );
            }
            this.bookToAdd.title = title;
            this.bookToAdd.author = author;
          
            if (for_adults == "1") {
              this.bookToAdd.isForAdult = true;
            } else {
              this.bookToAdd.isForAdult = false;
            }
            
            localStorage.setItem("title", this.bookToAdd.title);
            localStorage.setItem("author", this.bookToAdd.author);
            localStorage.setItem("isForAdult", this.bookToAdd.isForAdult);
            localStorage.setItem(
              "selectedCategory",
              this.bookToAdd.selectedCategory
            );
            EventBus.$emit("componentFromManageBooks", "AddBook");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    addInstance(title, author, for_adults, library_branch) {
      axios
        .get(`${API_BASE_URL}/categories/book`, {
          params: {
            title: title,
            author: author,
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
          if (response.status) {
            for (let i = 0; i < response.data.length; i++) {
              this.form.selectedCategory.push(response.data[i].category_name);
            }
            this.form.title = title;
            this.form.author = author;
            this.form.for_adults = for_adults;
            this.form.selectedBranch = library_branch;
            this.postBook(this.form);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    postBook() {
      if (this.validateForm(this.form)) {
        var formdata = new FormData();
        formdata.append("title", this.form.title);
        formdata.append("author", this.form.author);
        formdata.append("library_branch", this.form.selectedBranch);
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
              this.getAviability(this.form.title, this.form.author);
            }
            return true;
          },
        })
          .catch((error) => {
            console.log(error);
          })
          .then(() => {});
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
  },
};
</script>


<style scoped>
.card-result {
  position: relative;
  height: 200px;
  margin: 1%;
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

.content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  background-color: #f1f1f1;
}

.availability {
  margin-top: 150px;
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
