<template>
  <AuthorDetailComponent v-if="author" :author="author"/>
</template>

<script lang="ts">

import { defineComponent } from 'vue'
import { Author } from '@/api/schemas'
import AuthorDetailComponent from '@/components/AuthorDetailComponent.vue'
import { AuthorsService } from '@/api/services'
import router from '@/router'

interface State {
  author: Author | null
}

export default defineComponent({
  components: { AuthorDetailComponent },
  data (): State {
    return {
      author: null
    }
  },
  created () {
    const slug = this.$route.params.slug.toString()

    AuthorsService.detail(slug).then((response) => {
      this.author = new Author(response.data)
    }).catch(() => {
      router.push({ name: 'not-found' })
    })
  }

})
</script>
