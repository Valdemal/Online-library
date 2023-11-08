<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { User } from '@/api/schemas'

const USER_PHOTO_PLACEHOLDER_SRC = new URL('@/assets/user_photo_placeholder.png', import.meta.url).href

export default defineComponent({
  name: 'UserNav',
  props: {
    user: {
      type: Object as PropType<User>,
      required: true
    }
  },
  computed: {
    userPhoto () {
      return this.user.photo ? this.user.photo : USER_PHOTO_PLACEHOLDER_SRC
    }
  }
})
</script>

<template>
  <div>
    <a href="#">{{ user.username }}</a>
    |
    <router-link :to="{name: 'logout'}">выйти</router-link>
    <img class="user-image" :src="userPhoto" alt="Фото профиля">
  </div>
</template>

<style scoped>
.user-image {
  height: 70px;
  border: 5px solid #3F9FF8;
  margin-left: 10px;
}
</style>
