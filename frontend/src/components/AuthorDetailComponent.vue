<template>
  <ContentDetailWidget>
    <template #title>{{ author.fullName }}</template>

    <template #side-label>Книги</template>

    <template #content>
      <DescriptionWidget>
        <div class="photo">
          <img :src="author.image" :alt="author.fullName">
          <EstimationWidget>
            <div v-if="author.roundedScore()">🌟{{ author.roundedScore() }}</div>
            <div v-if="author.popularity">📚{{ author.popularity }}</div>
          </EstimationWidget>
        </div>
        <div class="text">{{ author.description }}</div>
      </DescriptionWidget>
    </template>

    <template #sidebar>
      <BookList :author_slug="author.slug"/>
    </template>
  </ContentDetailWidget>
</template>

<script lang="ts">

import ContentDetailWidget from '@/widgets/ContentDetailWidget.vue'
import BookList from '@/components/BookList.vue'
import EstimationWidget from '@/components/BaseEstimation.vue'
import DescriptionWidget from '@/components/BaseDescription.vue'
import { defineComponent, PropType } from 'vue'
import { Author } from '@/api/schemas'

export default defineComponent({
  components: { DescriptionWidget, EstimationWidget, BookList, ContentDetailWidget },
  props: {
    author: {
      type: Object as PropType<Author>,
      required: true
    }
  }
})
</script>
