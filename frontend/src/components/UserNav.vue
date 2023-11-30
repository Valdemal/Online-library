<script lang="ts">
import { defineComponent } from 'vue'
import { mapActions, mapGetters } from 'vuex'

export default defineComponent({
  name: 'UserNav',
  computed: mapGetters(['currentUser']),
  methods: mapActions(['fetchCurrentUser']),
  async created () {
    try {
      await this.fetchCurrentUser()
    } catch (e) {
      console.log(e)
    }
  }
})
</script>

<template>
  <div v-if="this.currentUser">
    <a href="#">{{ this.currentUser.username }}</a>
    |
    <router-link :to="{name: 'logout'}">выйти</router-link>
    <img class="user-image" :src="this.currentUser.photo" alt="Фото профиля">
  </div>
  <div v-else>
    <router-link :to="{name:'login'}">Войти</router-link>
    |
    <router-link :to="{name:'registration'}">Зарегистрироваться</router-link>
  </div>
</template>

<style scoped>
.user-image {
  height: 70px;
  border: 5px solid #3F9FF8;
  margin-left: 10px;
}
</style>
