<script lang="ts">
import { defineComponent } from 'vue'
import TheHeader from '@/components/TheHeader.vue'
import TheFooter from '@/components/TheFooter.vue'

export default defineComponent({
  name: 'NotFoundView',
  components: { TheFooter, TheHeader }
})
</script>

<template>
  <TheHeader>
    <div class="subheader flex-center">Страница не найдена!</div>
  </TheHeader>
  <main>
    <h1>404 Not Found!</h1>
  </main>
  <TheFooter/>
</template>

<style scoped>
main {
  margin: 10px 310px 0 122px;
  min-height: 400px;
  color: #464646;
}
</style>
