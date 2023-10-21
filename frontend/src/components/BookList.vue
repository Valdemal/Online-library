<template>
  <div class="book-list">
    <BookListItem
      v-for="book in books" :key="book.slug"
      :book="book"
    />
  </div>
</template>

<script lang="ts">
import BookListItem from '@/components/BookListItem.vue'
import { Book } from '@/api/schemas'
import { defineComponent } from 'vue'
import { BooksService } from '@/api/services'

interface State {
  books: Book[]
}

export default defineComponent({
  components: { BookListItem },
  props: {
    author_slug: {
      type: String,
      required: false
    }
  },
  data (): State {
    return {
      books: []
    }
  },
  created () {
    BooksService.list({ author: this.author_slug }).then((response) => {
      this.books = response.data.results.map((json: any) => {
        return new Book(json)
      })
    })
  }
})
</script>
