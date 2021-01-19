<template>
  <div class="home">
    <!-- Header -->
    <header>
      <div class="container">
        <div class="intro-text">
          <div class="intro-heading">The Wonderful World of Reading</div>
        </div>
      </div>
    </header>

    <!-- quotes and news section -->

    <section>
      <div class="row">
        <div class="column">
          <div class="card">
       
            <p>
              – To wódka? – słabym głosem zapytała Małgorzata.(...) – Na litość
              boską, królowo – zachrypiał – czy ośmieliłbym się nalać damie
              wódki? To czysty spirytus.
            </p>
            <hr />
            <i> Michaił Bułhakow, Mistrz i Małgorzata</i>
          </div>
        </div>
        <div class="column">
          <div class="card">
        
            <p>Zabijanie dla pokoju jest jak pieprzenie się dla cnoty.</p>
            <hr />
            <i> Stephen King, Serca Atlantydów</i>
          </div>
        </div>
        <div class="column">
          <div class="card">

            <p>
              Zwierzęta w ogrodzie patrzyły to na świnię, to na człowieka, potem
              znów na świnię i na człowieka, ale nikt już nie mógł się połapać,
              kto jest kim.
            </p>
            <hr />
            <i> George Orwell, Folwark zwierzęcy</i>
          </div>
        </div>
        <div class="column">
          <div class="card">

            <p>
              Żaden dzień się nie powtórzy, nie ma dwóch podobnych nocy, dwóch
              tych samych pocałunków, dwóch jednakich spojrzeń w oczy.
            </p>
            <hr />
            <i>
              Wisława Szymborska, Nic dwa razy: Wybór wierszy - Nothing Twice:
              Selected Poems</i
            >
          </div>
        </div>
      </div>
    </section>

    <!-- Recommended books section - change into component -->
    <section class="recommended-section">
      <div><p class="section-title">Rekomendowane książki</p></div>

      <div class="row">
        <div class="column">
          <div class="card">
            <img class="cover" src="~@/assets/cover1.png" alt="Book" />
          </div>
        </div>
        <div class="column">
          <div class="card">
            <img class="cover" src="~@/assets/cover2.png" alt="Book" />
          </div>
        </div>
        <div class="column">
          <div class="card">
            <img class="cover" src="~@/assets/cover3.jpg" alt="Book" />
          </div>
        </div>
        <div class="column">
          <div class="card">
            <img class="cover" src="~@/assets/cover4.jpg" alt="Book" />
          </div>
        </div>
      </div>
    </section>

    <!-- Comming events  -->
    <section>
      <div><p class="section-title">Nadchodzące wydarzenia</p></div>
      <div class="row">
        <div class="column">
          <div class="card">
            <h2>21 stycznia - Dzień Babci</h2>
          </div>
        </div>
        <div class="column">
          <div class="card">
            <h2>22 stycznia - Dzień Dziadka</h2>
          </div>
        </div>
        <div class="column">
          <div class="card">
            <h2>11 Luty - Tłusty Czwartek</h2>
          </div>
        </div>
        <div class="column">
          <div class="card">
            <h2>8 Marca - Dzień Kobiet</h2>
          </div>
        </div>
      </div>
    </section>

    <!--          FOOTER           -->
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Footer from "../components/Footer.vue";

export default {
  name: "Home",
  components: {
    Footer,
  },
};
</script>



<style scoped>
.container {
  height: 100vh;
}

.img-centered {
  margin: 0 auto;
}

header {
  text-align: center;
  color: #fff;
  background-attachment: scroll;
  background-image: url("~@/assets/library_main_page.jpg");
  background-position: center center;
  background-repeat: none;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  background-size: cover;
  -o-background-size: cover;
}

header .intro-text .intro-heading {
  margin-bottom: 25px;
  font-style: normal;
  font-family: Montserrat, "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 95px;
  font-weight: 400;
  line-height: 1;
  letter-spacing: 0px;
}

@media (min-width: 768px) {
  header .intro-text {
    padding-top: 300px;
    padding-bottom: 200px;
  }

  header .intro-text .intro-lead-in {
    margin-bottom: 25px;
    font-family: "Droid Serif", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 40px;
    font-style: italic;
    line-height: 40px;
  }

  header .intro-text .intro-heading {
    margin-bottom: 50px;
    text-transform: uppercase;
    font-family: Montserrat, "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 75px;
    font-weight: 700;
    line-height: 75px;
  }
}

/* ========================== MAIN SECTION ========================== */
/*=========================== QUOTES ==============================*/
/* Float four columns side by side */
.column {
  float: left;
  width: 25%;
  padding: 2%;
}

/* Remove extra left and right margins, due to padding in columns */
.row {
  margin: 1% 0 1% 0;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Style the counter cards */
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* this adds the "card" effect */
  padding: 16px;
  text-align: center;
  background-color: #f1f1f1;
}

/* Responsive columns - one column layout (vertical) on small screens */
@media screen and (max-width: 600px) {
  .column {
    width: 100%;
    display: block;
    margin-bottom: 20px;
  }
}

/*========================== RECOMENDED ============================*/

.recommended-section {
  background-color: rgb(242, 242, 242);
}

.section-title {
  padding: 1%;
  font-size: 40px;
  text-align: center;
  line-height: 1.3;
  letter-spacing: 0px;
}

.cover {
  width: 100%;
  height: 100%;
}




</style>
