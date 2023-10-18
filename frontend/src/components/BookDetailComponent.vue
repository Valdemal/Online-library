<template>
  <ContentDetailWidget>
    <template #title>
      {{ book.title }}
    </template>

    <template #side-label>
      <router-link :to="{name:'author-detail', params: {slug: author.slug}}">
        {{ author.fullName }}
      </router-link>
    </template>

    <template #content>
      <DescriptionWidget>
        <div class="photo">
          <img :src="book.cover" :alt="book.title">
          <EstimationWidget>
            <div>🌟{{ book.roundedScore() }}</div>
            <div>📚{{ book.popularity }}</div>
          </EstimationWidget>
        </div>
        <div class="text book-text">{{ book.description }}</div>
      </DescriptionWidget>
      <CommentsList :book_slug="book.slug"/>
    </template>

    <template #sidebar>
      <img :src="author.image" :alt="author.fullName">
    </template>
  </ContentDetailWidget>
</template>

<script lang="ts">

import CommentsList from '@/components/CommentList.vue'
import EstimationWidget from '@/components/BaseEstimation.vue'
import DescriptionWidget from '@/components/BaseDescription.vue'
import { Author, Book } from '@/api/schemas'
import { defineComponent, PropType } from 'vue'
import ContentDetailWidget from '@/widgets/ContentDetailWidget.vue'

export default defineComponent({
  components: { DescriptionWidget, EstimationWidget, ContentDetailWidget, CommentsList },
  props: {
    book: {
      type: Object as PropType<Book>,
      required: true
    },
    author: {
      type: Object as PropType<Author>,
      required: true
    }
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
