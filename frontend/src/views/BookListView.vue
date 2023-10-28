<template>
  <TheHeader/>
  <ContentGridWidget>
    <BookListViewItem
      v-for="book in books" :key="book.slug"
      :book="book"
    />
  </ContentGridWidget>
</template>

<script lang="ts">

import ContentGridWidget from '@/widgets/ContentGridWidget.vue'
import TheHeader from '@/components/TheHeader.vue'
import BookListViewItem from '@/components/BookListViewItem.vue'
import { Book } from '@/api/schemas'
import { defineComponent } from 'vue'
import { BooksService } from '@/api/services'

interface State {
  books: Book[]
}

export default defineComponent({
  components: { BookListViewItem, TheHeader, ContentGridWidget },
  data (): State {
    return {
      books: []
    }
  },
  async created () {
    try {
      this.books = await new BooksService().list()
    } catch (error) {
      console.log(error)
    }
  }
})
</script>
