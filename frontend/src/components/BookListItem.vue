
<template>
  <router-link class="book-link" :to="{name:'book-detail', params: {slug: schema.slug}}">
    <div class="book flex-center">
      <div class="name">{{ schema.title }}</div>
      <div class="score" v-if="schema.score">
        🌟{{ schema.score.toFixed(2) }}
      </div>
      <div class="popularity" v-if="schema.popularity">
        📚{{ schema.popularity }}
      </div>
    </div>
  </router-link>
</template>

<script>
import { Book } from '@/api/schemas'

export default {
  components: { },
  props: {
    schema: Book
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
