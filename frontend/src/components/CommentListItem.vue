<template>
  <div class="comment">
    <div class="photo">
      <img src="../assets/Булгаков.jpg" alt="Булгаков">
      <EstimationWidget>
        <div>🌟{{ schema.score }}</div>
      </EstimationWidget>
    </div>
    <div class="text">{{ schema.text }}</div>
  </div>
</template>

<script>

import EstimationWidget from '@/components/BaseEstimation.vue'
import { Comment } from '@/api/schemas'

export default {
  components: { EstimationWidget },
  props: {
    schema: Comment
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
