<template>
  <router-link :to="{name:'book-detail', params: {slug: this.book.slug}}">
    <ContentItem>
      <img src="{{ book.cover }}" alt="{{ book.title }}">
      <div class="text">
        <div class="name flex-center">{{ book.title }}</div>
        <div class="description"><p>{{ book.description }}</p></div>
      </div>
    </ContentItem>
  </router-link>
</template>

<script>
import ContentItem from '@/components/ContentGridWidgetItem.vue'
import { Book } from '@/api/schemas'

export default {
  components: { ContentItem },
  props: {
    book: {
      type: Book,
      required: true
    }
  }
}
</script>
