<template>
  <div class="card-result">
    <div class="img-container">
      <img class="book-icon" src="~@/assets/book_icon.png" alt="Book" />
    </div>
    <div class="title">
      <p>Tytuł: {{ result.title }}</p>
    </div>

    <div class="end-time">
      <p>Termin oddania: {{ result.end_time }}</p>
    </div>

    <div class="address">
      <p>Adres biblioteki: {{ result.address }}</p>
    </div>
    <div class="branch_name">
      <p>Nazwa biblioteki: {{ result.library_branch_name }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "BorrowedBook",
  props: {
    result: {
      type: Object,
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}
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
  height: 80%;
  display: inline;
}

.img-container {
  margin-bottom: 10px;
  margin-right: 90%;
  width: 10%;
  height: 80%;
  display: inline;
}

.title,
.end-time,
.address,
.branch_name {
  display: inline;
  overflow: auto;
  width: 30%;
  margin-left: 25%;
}
p {
  text-align: left;
  overflow: auto;
  margin-left: 25%;
}
</style>