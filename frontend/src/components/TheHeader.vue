<template>
  <header>
    <div class="logo flex-center">
      <img src="../assets/logo.jpg" alt="logo">
    </div>
    <div class="header-container">
      <nav class="flex-right">
        <router-link class="nav-link" to="/books">Книги</router-link>
        <router-link class="nav-link" to="/authors">Авторы</router-link>
        <div class="nav-side">
          <router-link to="/login">Войти</router-link>
          |
          <router-link to="/registration">Зарегистрироваться</router-link>
        </div>
      </nav>
      <slot><Search/></slot>
    </div>
  </header>
</template>

<script setup>
import Search from '@/components/SearchWidget.vue'
</script>

<style scoped>

header {
  display: flex;
}

.header-container {
  width: 100%;
}

.header-container a {
  color: #F5F5F5;
}

header nav {
  background-color: rgba(63, 159, 248, 0.7);
  color: #F5F5F5;
  height: 80px;
  padding: 0 20px 0 20px;
}

.nav-side {
  margin-left: auto;
  font-size: 22px;
}

.nav-link {
  margin-right: 20px;
  font-size: 36px;
}

.logo {
  width: 122px;
  height: 103px;
  border: 10px solid #3F9FF8;
  overflow: hidden;
  justify-content: center;
}

.logo img {
  width: 100%;
  height: 100%;
}

/deep/ .subheader {
  height: 42px;
  padding: 0 20px 0 20px;
  background-color: #D9D9D9;
  color: #464646;
  margin-right: 310px;
}

/deep/ .user-image {
  height: 70px;
  border: 5px solid #3F9FF8;
  margin-left: 10px;
}
</style>
