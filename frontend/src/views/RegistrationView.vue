<template>
  <form action="#">
    <div class="title flex-center">Регистрация</div>
    <div class="content">
      <label><input type="email" placeholder="Email"></label>
      <label><input type="text" placeholder="Имя пользователя"></label>
      <label><input type="password" placeholder="Пароль"></label>
      <label><input type="password" placeholder="Повторите пароль"></label>
      <ul class="errors">
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
      <button class="title" type="submit">Зарегистрироваться</button>
    </div>
    <div class="title subtitle flex-center"><router-link to="login">Есть аккаунт?</router-link></div>
  </form>
</template>

<script>

export default {
  data () {
    return {
      errors: [
        'Имя пользователя занято!',
        'Email занят!'
      ]
    }
  }
}

</script>

<style scoped>

</style>
