<template>
  <BookDetailComponent v-if="book && author" :author="author" :book="book"/>
</template>

<script lang="ts">

import { Author, Book } from '@/api/schemas'
import { defineComponent } from 'vue'
import BookDetailComponent from '@/components/BookDetailComponent.vue'
import router from '@/router'
import { AuthorsService, BooksService } from '@/api/services'

interface State {
  book: Book | null
  author: Author | null
}

export default defineComponent({
  components: { BookDetailComponent },
  data (): State {
    return { book: null, author: null }
  },
  created () {
    const slug = this.$route.params.slug.toString()

    BooksService.detail(slug).then((response) => {
      this.book = new Book(response.data)

      AuthorsService.detail(this.book.author).then((response) => {
        this.author = new Author(response.data)
      })
    }).catch(() => {
      router.push({ name: 'not-found' })
    })
  }
})

</script>

<style scoped>
.book-text {
  max-height: 600px;
  overflow: scroll;
  overflow-x: hidden;
}

</style>
