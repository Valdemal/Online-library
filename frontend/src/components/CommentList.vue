<template>
  <div class="comments-layout" v-if="comments.length !== 0">
    <div class="comments-label flex-center">Комментарии</div>
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script lang="ts">
import CommentListItem from '@/components/CommentListItem.vue'
import { Comment } from '@/api/schemas'
import { defineComponent } from 'vue'
import { CommentsService } from '@/api/services'

interface State {
  comments: Comment[]
}

export default defineComponent({
  components: { CommentListItem },
  props: {
    book_slug: {
      type: String,
      required: false
    },
    username: {
      type: String,
      required: false
    }
  },
  data (): State {
    return {
      comments: []
    }
  },
  created () {
    CommentsService.list({ book: this.book_slug, user: this.username }).then((response) => {
      this.comments = response.data.results.map((json: any) => {
        return new Comment(json)
      })
    })
  }
})

</script>

<style scoped>

.comments-label {
  background-color: #D9D9D9;
  font-size: 20px;
}

.comments-layout {
  margin-top: 10px;
}

</style>
