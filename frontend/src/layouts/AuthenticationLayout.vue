<script>
import { defineComponent } from 'vue'
import FooterWidget from '@/components/FooterWidget.vue'

export default defineComponent({
  name: 'AuthenticationLayout',
  components: { FooterWidget }
})
</script>

<template>
  <header class="flex-center">
    <div class="logo flex-center">
      <img src="../assets/logo.jpg" alt="logo">
    </div>
  </header>
  <main class="flex-center">
    <router-view/>
  </main>
  <footer-widget class="authorization-footer"/>
</template>

<style scoped>

header {
  height: 80px;
  background-color: rgba(63, 159, 248, 0.7);
}

main {
  margin: 0 0 0 0;
  min-height: 0;
}

main >>> form {
  background-color: #D9D9D9;
  margin-top: 60px;
  margin-bottom: 60px;
  width: 590px;
}

main >>> .content {
  padding: 20px 10px 20px 10px;
  text-align: center;
  color: #464646;
}

main >>> .content label {
  width: 100%;
}

main >>> .content ul {
  padding-left: 20px;
  margin: 0;
}

main >>> .content li {
  text-align: left;
  margin-bottom: 2px;
}

main >>> .content input {
  width: 98%;
  height: 27px;
  margin-bottom: 10px;
  padding-left: 5px;
  font-size: 16px;
  color: #464646;
  border: none;
  outline: none;
}

main >>> .content button {
  border: none;
  font-size: 16px;
  height: 30px;
  width: 230px;
  cursor: pointer;
  margin-top: 10px;
}

main >>> .content button:hover {
  opacity: 0.8;
}

main >>> .title {
  height: 25px;
  background-color: rgba(63, 159, 248, 0.7);
  color: #F5F5F5;
  font-size: 20px;
}

main >>> .subtitle {
  font-size: 18px;
}

main >>> .subtitle a {
  padding-left: 5px;
  padding-right: 5px;
}

.logo {
  width: 90px;
  height: 80px;
  overflow: hidden;
  justify-content: center;
}

.logo img {
  width: 100%;
  height: 100%;
}

.authorization-footer {
  margin: 10px 260px 0 260px;
}

</style>
