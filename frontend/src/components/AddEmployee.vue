<template>
  <div class="background">
    <div class="wraper">
      
      <div class="login-wrap">
        
        <div class="login-html">
          <input
            id="tab-1"
            type="radio"
            name="tab"
            class="sign-in"
            checked
          /><label for="tab-1" class="tab">Instrukcja</label>
          <input id="tab-2" type="radio" name="tab" class="sign-up" /><label
            for="tab-2"
            class="tab"
            >Sign Up</label
          >
          <div class="login-form">
            <div class="sign-in-htm">
              <div class="instruction">
                <p>
                  W przypadku przyjęcia nowego pracownika należy założyć mu
                  oddzielne konto pracownicze w systemie. W tym celu należy
                  nacisnąć powyższy przycisk SIGN UP i uzupełnić wszystkie
                  informacje zgodnie z prawdą.
                </p>
              </div>

              <div class="hr"></div>
            </div>
           <!--  ============================= SIGN UP ============================= -->
            <div class="sign-up-htm">
              <div class="group">
                <label for="user" class="label">Imię</label>
                <input
                  id="user"
                  type="text"
                  class="input"
                  required="required"
                  v-model="form.name"
                />
              </div>
              <div class="group">
                <label for="user" class="label">Nazwisko</label>
                <input
                  id="user"
                  type="text"
                  class="input"
                  v-model="form.surname"
                />
              </div>
              <div class="group">
                <label for="user" class="label">Login</label>
                <input
                  id="user"
                  type="text"
                  class="input"
                  v-model="form.login"
                />
              </div>
              <div class="group">
                <label for="pass" class="label">Hasło</label>
                <input
                  id="pass"
                  type="password"
                  class="input"
                  data-type="password"
                  v-model="form.password"
                />
              </div>
              <div class="group">
                <label for="pass" class="label">Powtórz hasło</label>
                <input
                  id="pass"
                  type="password"
                  class="input"
                  data-type="password"
                  v-model="form.password_repeat"
                />
              </div>
              <div class="group">
                <label for="pass" class="label">Data urodzenia</label>
                <input
                  id="pass"
                  type="date"
                  class="input"
                  min="1900-01-01"
                  max="2020-12-31"
                  v-model="form.birth_date"
                />
              </div>
              <div class="group">
                <input
                  type="submit"
                  class="button"
                  value="Sign Up"
                  @click="submitForm"
                />
              </div>
              <div class="hr"></div>
            </div>
            
            <!-- ============================= SIGN UP - END ============================= -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import axios from "axios";
import {API_BASE_URL} from "../api/config";

export default {
  data() {
    return {
      form: {
        name: "",
        surname: "",
        login: "",
        password: "",
        password_repeat: "",
        birth_date: "",
        user_type: "admin",
      },
      login_data: {
        login: "",
        password: "",
      },
    };
  },

  methods: {
    submitForm() {
      if (this.validateForm(this.form)) {
        var formdata = new FormData();
        formdata.append("name", this.form.name);
        formdata.append("surname", this.form.surname);
        formdata.append("login", this.form.login);
        formdata.append("password", this.form.password);
        formdata.append("birth_date", this.form.birth_date);
        formdata.append("user_type", this.form.user_type);

        axios({
          method: "post",
          url: `${API_BASE_URL}/register`,
          data: formdata,
          headers: {
            "Access-Control-Allow-Credentials": "true",
          },
          validateStatus: (status) => {
            if (status == "200") {
              alert("Konto zostało utworzone");
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
      if (form.name == "") {
        alert("Musisz podać imię");
        return false;
      } else if (form.surname == "") {
        alert("Musisz podać nazwisko");
        return false;
      } else if (form.login == "") {
        alert("Musisz podać login");
        return false;
      } else if (form.birth_date == "") {
        alert("Musisz podać swoją datę urodzenia");
        return false;
      } else if (form.password != form.password_repeat) {
        alert("Musisz wpisać dwa razy takie same hasło");
        return false;
      } else {
        return true;
      }
    },

    login() {
      var username = this.login_data.login;
      var password = this.login_data.password;

      axios
        .get(`${API_BASE_URL}/authtest`, {
          auth: {
            username: username,
            password: password,
          },
          headers: {
            "Access-Control-Allow-Credentials": "true",
          },
        })
        .then((response) => {
          if (response.status == "200") {
            localStorage.setItem("login", username);
            localStorage.setItem("password", password);
            if (response.data.user_type == "admin") {
              localStorage.setItem("is_admin", true);
              this.$emit("authenticated", true);
              this.$router.replace({ name: "EmployeeProfile" });
            } else {
              localStorage.setItem("is_admin", false);
              this.$emit("authenticated", true);
              this.$router.replace({ name: "ReaderProfile" });
            }
          }
        })
        .catch((error) => {
          console.log(error);
          localStorage.removeItem("login");
          localStorage.removeItem("password");
          localStorage.removeItem("is_admin");
        });
    },

    resetInput() {
      this.form.name = "";
      this.form.surname = "";
      this.form.login = "";
      this.form.password = "";
      this.form.password_repeat = "";
      this.form.birth_date = "";
    },
  },
};
</script>


<style scoped>
.background {
  margin-top: 0px;
}

*,
:after,
:before {
  box-sizing: border-box;
}

.instruction p {
  color: rgb(0, 0, 0);
  font-size: 20px;
}
.clearfix:after,
.clearfix:before {
  content: "";
  display: table;
}
.clearfix:after {
  clear: both;
  display: block;
}
a {
  color: inherit;
  text-decoration: none;
}

.login-wrap {
  width: 100%;
  margin: auto;
  margin-top: 8%;
  /* max-width: 525px; */
  min-height: 800px;
  position: relative;
  box-shadow: 0 12px 15px 0 rgba(0, 0, 0, 0.24),
    0 17px 50px 0 rgba(0, 0, 0, 0.19);
}
.login-html {
  width: 100%;
  height: 100%;
  position: absolute;
  padding: 90px 70px 50px 70px;
  background: rgba(74, 77, 87, 0.0);
}
.login-html .sign-in-htm,
.login-html .sign-up-htm {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  position: absolute;
  transform: rotateY(180deg);
  backface-visibility: hidden;
  transition: all 0.4s linear;
}
.login-html .sign-in,
.login-html .sign-up,
.login-form .group .check {
  display: none;
}
.login-html .tab,
.login-form .group .label,
.login-form .group .button {
  text-transform: uppercase;
}
.login-html .tab {
  font-size: 22px;
  margin-right: 15px;
  padding-bottom: 5px;
  margin: 0 15px 10px 0;
  display: inline-block;
  border-bottom: 2px solid transparent;
}
.login-html .sign-in:checked + .tab,
.login-html .sign-up:checked + .tab {
  color: rgb(0, 0, 0);
  border-color: #1161ee;
}
.login-form {
  min-height: 345px;
  position: relative;
  perspective: 1000px;
  transform-style: preserve-3d;
}
.login-form .group {
  margin-bottom: 15px;
}
.login-form .group .label,
.login-form .group .input,
.login-form .group .button {
  width: 100%;
  color: rgb(0, 0, 0);
  display: block;
}
.login-form .group .input,
.login-form .group .button {
  border: none;
  padding: 15px 20px;
  border-radius: 25px;
}
.login-form .group input[data-type="password"] {
  -text-security: circle;
  -webkit-text-security: circle;
}
.login-form .group .label {
  color: rgb(0, 0, 0);
  font-size: 12px;
}
.login-form .group .button {
  background: #8c929c;
}
.login-form .group label .icon {
  width: 15px;
  height: 15px;
  border-radius: 2px;
  position: relative;
  display: inline-block;
  background: rgba(223, 43, 43, 0.1);
}
.login-form .group label .icon:before,
.login-form .group label .icon:after {
  content: "";
  width: 10px;
  height: 2px;
  background: rgb(0, 0, 0);
  position: absolute;
  transition: all 0.2s ease-in-out 0s;
}
.login-form .group label .icon:before {
  left: 3px;
  width: 5px;
  bottom: 6px;
  transform: scale(0) rotate(0);
}
.login-form .group label .icon:after {
  top: 6px;
  right: 0;
  transform: scale(0) rotate(0);
}
.login-form .group .check:checked + label {
  color: rgb(0, 0, 0);
}
.login-form .group .check:checked + label .icon {
  background: #1161ee;
}
.login-form .group .check:checked + label .icon:before {
  transform: scale(1) rotate(45deg);
}
.login-form .group .check:checked + label .icon:after {
  transform: scale(1) rotate(-45deg);
}
.login-html
  .sign-in:checked
  + .tab
  + .sign-up
  + .tab
  + .login-form
  .sign-in-htm {
  transform: rotate(0);
}
.login-html .sign-up:checked + .tab + .login-form .sign-up-htm {
  transform: rotate(0);
}

.hr {
  height: 2px;
  margin: 60px 0 50px 0;
  background: rgba(255, 255, 255, 0.2);
}
.foot-lnk {
  text-align: center;
}

span {
  color: rgba(0, 0, 0, 0.19);
}
</style>