<template>
  <div class="comments-layout">
    <div class="comments-label flex-center">Комментарии</div>
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :schema="comment"
    />
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import { Slug } from '@/api/schemas'

export default {
  components: { CommentListItem },
  props: {
    book_slug: {
      type: Slug,
      required: false
    },
    username: {
      type: String,
      required: false
    }
  },
  data () {
    return {
      comments: [
        {
          id: 9,
          book: 'generation-p-viktor-pelevin',
          user: 'staff_user',
          score: 3,
          text: 'Бредово, но пойдет',
          creation_time: '2022-12-18T04:18:55.497852+03:00'
        },
        {
          id: 8,
          book: 'marsianskie-khroniki-rej-bredberi',
          user: 'staff_user',
          score: 5,
          text: 'Здорово!!!',
          creation_time: '2022-12-18T04:18:33.102122+03:00'
        }
      ]
    }
  }
}
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
