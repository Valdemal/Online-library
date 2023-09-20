
<template>
  <form action="#">
    <div class="title flex-center">Вход</div>
    <div class="content">
      <label><input type="text" placeholder="Имя пользователя"></label>
      <label><input type="password" placeholder="Пароль"></label>
      <ul class="errors">
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
      <button class="title" type="submit">Войти</button>
    </div>
    <div class="title subtitle flex-center">
      <router-link to="registration">Нет аккаунта?</router-link>|<a href="#">Забыли пароль?</a>
    </div>
  </form>
</template>

<script>

export default {
  data () {
    return {
      errors: [
        'Неверное имя пользователя и пароль!',
        'Еще ошибка'
      ]
    }
  }
}

</script>
