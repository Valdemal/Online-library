<template>
  <router-link :to="{name:'author-detail', params: {slug: this.author.slug}}">
  <ContentItem>
    <img :src="author.image" :alt="author.fullName">
    <div class="text">
      <div class="name flex-center">{{ author.fullName }}</div>
      <div class="description"><p>{{ author.description }}</p></div>
    </div>
  </ContentItem>
  </router-link>
</template>

<script>
import ContentItem from '@/components/ContentGridWidgetItem.vue'
import { Author } from '@/api/schemas'

export default {
  components: { ContentItem },
  props: {
    author: {
      type: Author,
      required: true
    }
  }
}
</script>
