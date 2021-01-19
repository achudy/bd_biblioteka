<template>
  <div>
    <div class="form">
      <div class="group">
        <label class="typo__label">Nazwa</label>
        <input
          id="title-input"
          type="text"
          class="input"
          required="required"
          v-model="form.name"
        />
      </div>

      <div class="group">
        <label class="typo__label">Adres</label>
        <input
          id="author-input"
          type="text"
          class="input"
          required="required"
          v-model="form.address"
        />
      </div>

      <button class="addButton" @click="addNewBranch()">Dodaj</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import { API_BASE_URL } from "../api/config";
export default {
  name: "AddBranch",
  data() {
    return {
      form: {
        name: "",
        address: "",
      },
    };
  },

  methods: {
    addNewBranch() {
      if (this.validateForm(this.form)) {
        var formdata = new FormData();
        formdata.append("address", this.form.address);
        formdata.append("library_branch_name", this.form.name);
        axios({
          method: "post",
          url: `${API_BASE_URL}/branch`,
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
              alert("Oddział został dodany");
              this.resetInput();
            }
            return true;
          },
        })
          .catch((error) => {
            console.log(error.message);
            this.resetInput();
          })
          .then((response) => {
            if (response.data.error) {
              alert(response.data.error);
            }
            this.resetInput();
          });
      }
    },

    validateForm(form) {
      if (form.name == "") {
        alert("Musisz podać nazwę jednostki");
        return false;
      } else if (form.address == "") {
        alert("Musisz podać adres jednostki");
        return false;
      } else {
        return true;
      }
    },

    resetInput() {
      this.form.name = "";
      this.form.address = "";
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

.addButton {
  width: 10%;
  display: inline;
  min-height: 40px;
  padding: 8px 8px 0 8px;
  border-radius: 5px;
  font-size: 13px;
  text-align: center;
}

.addButton:hover {
  border: 3px solid black;
  background-color: #f2f2f2;
}
</style>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>