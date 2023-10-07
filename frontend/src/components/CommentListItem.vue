<template>
  <div class="comment">
    <div class="photo">
      <img :src="user.photo" :alt="user.username">
      <EstimationWidget>
        <div>🌟{{ comment.roundedScore() }}</div>
      </EstimationWidget>
    </div>
    <div class="text">{{ comment.text }}</div>
  </div>
</template>

<script>

import EstimationWidget from '@/components/BaseEstimation.vue'
import { Comment, User } from '@/api/schemas'

export default {
  components: { EstimationWidget },
  props: {
    comment: {
      type: Comment,
      required: true
    }
  },
  data () {
    return {
      user: {
        type: User
      }
    }
  },
  created () {
    // Получение данных пользователя по полю comment.user
    this.user = new User({
      username: 'vovan',
      email: 'vovanex12@gmail.com',
      photo: 'http://127.0.0.1/media/users/photos/%D0%9D%D0%B0_%D0%BF%D0%B0%D1%81%D0%BF%D0%BE%D1%80%D1%82.jpg',
      is_staff: true
    })
  }
}

</script>

<style scoped>

.comment .photo {
  border-top: none;
  width: 110px;
  min-width: 110px;
}

.comment {
  display: flex;
  margin-top: 10px;
  border-top: 5px solid rgba(63, 159, 248, 0.7);
  max-height: 200px;
}

.comment .text {
  overflow: scroll;
  overflow-x: hidden;
}

</style>
