
<template>
  <router-link class="book-link" :to="{name:'book-detail', params: {slug: this.book.slug}}">
    <div class="book flex-center">
      <div class="name">{{ book.title }}</div>
      <div class="score" v-if="book.score">
        🌟{{ book.roundedScore() }}
      </div>
      <div class="popularity" v-if="book.popularity">
        📚{{ book.popularity }}
      </div>
    </div>
  </router-link>
</template>

<script>
import { Book } from '@/api/schemas'

export default {
  components: { },
  props: {
    book: {
      type: Book,
      required: true
    }
  }
}
</script>

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
