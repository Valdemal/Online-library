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
  created () {
    BooksService.list().then((response) => {
      this.books = response.data.results.map((json: any) => {
        return new Book(json)
      })
    }).catch((error) => {
      console.log(error)
    })
  }
})
</script>
