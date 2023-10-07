<template>
  <router-link :to="{name:'book-detail', params: {slug: schema.slug}}">
    <ContentItem>
      <img src="{{ schema.cover }}" alt="{{ schema.title }}">
      <div class="text">
        <div class="name flex-center">{{ schema.title }}</div>
        <div class="description"><p>{{ schema.description }}</p></div>
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
    schema: Book
  }
}
</script>
