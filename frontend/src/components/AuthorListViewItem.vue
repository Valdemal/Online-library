<template>
  <router-link :to="{name:'author-detail', params: {slug: schema.slug}}">
  <ContentItem>
    <img :src="schema.image" :alt="fullname()">
    <div class="text">
      <div class="name flex-center">{{ fullname() }}</div>
      <div class="description"><p>{{ schema.description }}</p></div>
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
    schema: Author
  },
  methods: {
    fullname () {
      return this.schema.name + ' ' + this.schema.surname
    }
  }
}
</script>
