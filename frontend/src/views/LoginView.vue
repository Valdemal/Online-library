
<template>
  <form action="#">
    <div class="title flex-center">Вход</div>
    <div class="content">
      <label><input v-model="username" type="text" placeholder="Имя пользователя"></label>
      <label><input v-model="password" type="password" placeholder="Пароль"></label>
      <ul class="errors">
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
      <button @click.prevent="onLogin" class="title" type="submit">Войти</button>
    </div>
    <div class="title subtitle flex-center">
      <router-link to="registration">Нет аккаунта?</router-link>|<a href="#">Забыли пароль?</a>
    </div>
  </form>
</template>

<script lang="ts">

import { defineComponent } from 'vue'
import router from '@/router'
import { mapActions } from 'vuex'

interface State {
  username: string
  password: string
  errors: string[]
}

export default defineComponent({
  data (): State {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  methods: {
    ...mapActions(['login']),
    async onLogin () {
      try {
        await this.login({ username: this.username, password: this.password })
        await router.push({ name: 'index' })
      } catch (error: any) {
        console.log(error)
        this.errors = error.response.data.non_field_errors
      }
    }
  }
})

</script>
