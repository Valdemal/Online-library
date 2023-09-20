<template>
  <div class="comments-layout">
    <div class="comments-label flex-center">Комментарии</div>
    <CommentItem/>
    <CommentItem/>
    <CommentItem/>
  </div>
</template>

<script setup>

import CommentItem from '@/components/CommentItem.vue'
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
