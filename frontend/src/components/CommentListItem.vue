<template>
  <div class="comment">
    <div class="photo">
<!--      <img :src="user.photo" :alt="user.username"> todo: пока нет возможности получить-->
      <EstimationWidget>
        <div>🌟{{ comment.roundedScore() }}</div>
      </EstimationWidget>
    </div>
    <div class="text">{{ comment.text }}</div>
  </div>
</template>

<script lang="ts">

import EstimationWidget from '@/components/BaseEstimation.vue'
import { Comment, User } from '@/api/schemas'
import { defineComponent } from 'vue'

interface State {
  user: User | null
}
export default defineComponent({
  components: { EstimationWidget },
  props: {
    comment: {
      type: Comment,
      required: true
    }
  },
  data (): State {
    return {
      user: null
    }
  }
})

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
