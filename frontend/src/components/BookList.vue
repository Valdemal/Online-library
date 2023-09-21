<template>
  <div class="book-list">
    <a class="book-link" href="/books/slug">
      <div class="book flex-center">
        <div class="name">
          Преступление и наказание
        </div>
        <div class="score">🌟5</div>
        <div class="popularity">📚900</div>
      </div>
    </a>
  </div>
</template>

<style scoped>
.book {
  background-color: #D9D9D9;
  min-height: 40px;
  margin-bottom: 10px;
  color: #464646;
}

.book div {
  text-align: center;
}

.book .name {
  width: 80%;
}

.book-link:hover {
  text-decoration: none;
  opacity: 0.8;
}
</style>
