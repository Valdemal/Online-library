<template>
  <TheHeader/>
  <ContentGridWidget>
    <AuthorListViewItem
      v-for="author in authors"
      :key="author.slug"
      :author="author"
    />
  </ContentGridWidget>
</template>

<script lang="ts">

import ContentGridWidget from '@/widgets/ContentGridWidget.vue'
import TheHeader from '@/components/TheHeader.vue'
import AuthorListViewItem from '@/components/AuthorListViewItem.vue'
import { defineComponent } from 'vue'
import AuthorsService from '@/api/services/authors'
import { Author } from '@/api/schemas'

interface State {
  authors: Author[]
}

export default defineComponent({
  components: { AuthorListViewItem, TheHeader, ContentGridWidget },
  data (): State {
    return {
      authors: []
    }
  },
  created () {
    AuthorsService.list().then((response) => {
      this.authors = response.data.results.map((json: any) => {
        return new Author(json)
      })
    }).catch(() => {
      console.error('Авторы не получены!')
    })
  }
})
</script>
