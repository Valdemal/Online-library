<template>
  <header>
    <div class="logo flex-center">
      <router-link :to="{name: 'index'}">
        <img src="../assets/logo.jpg" alt="logo">
      </router-link>
    </div>
    <div class="header-container">
      <nav class="flex-right">
        <router-link class="nav-link" :to="{name:'books'}">Книги</router-link>
        <router-link class="nav-link" :to="{name:'authors'}">Авторы</router-link>
        <a v-if="me" class="nav-link">Полка</a>
        <user-nav v-if="me" :user="me" class="nav-side flex-center"/>
        <div v-else class="nav-side">
          <router-link :to="{name:'login'}">Войти</router-link>
          |
          <router-link :to="{name:'registration'}">Зарегистрироваться</router-link>
        </div>
      </nav>
      <slot><TheSearch/></slot>
    </div>
  </header>
</template>

<script lang="ts">
import TheSearch from '@/components/TheSearch.vue'
import { defineComponent } from 'vue'
import { MeService } from '@/api/services'
import { User } from '@/api/schemas'
import UserNav from '@/components/UserNav.vue'

interface State {
  me: User|null
}

export default defineComponent({
  components: { UserNav, TheSearch },
  data (): State {
    return {
      me: null
    }
  },
  async created () {
    const service = new MeService()

    if (service.isAuthenticated()) {
      try {
        this.me = await service.get()
      } catch (e) {
        console.log(e)
      }
    }
  }
})
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

</style>
