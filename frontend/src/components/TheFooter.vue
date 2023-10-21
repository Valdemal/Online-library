<template>
  <footer class="flex-right">
    <div class="footer-item flex-center">
      <a class="flex-right" href="#">
        <img src="../assets/online-library.png" alt="Online-library">©️ 2023 Online-library, Inc.
      </a>
    </div>
    <div class="footer-item flex-center">
      <a class="flex-right" href="https://github.com/Valdemal/Online-library">
        <img src="../assets/github.png" alt="GitHub">GitHub
      </a>
    </div>
    <div class="footer-item flex-center">
      <a class="flex-right" href="https://t.me/UsernameWemanresU">
        <img src="../assets/telegram.png" alt="Telegram">Telegram
      </a>
    </div>
  </footer>
</template>

<style scoped>
footer {
  color: #464646;
  margin: 10px 310px 0 142px;
  border-top: 1px solid #3F9FF8;
  font-size: 14px;
  justify-content: space-between;
  padding-right: 20px;
  padding-left: 20px;
}

footer a img:hover {
  opacity: 75%;
}

.footer-item {
  width: 200px;
  height: 50px;
  margin-left: 15px;
  margin-right: 15px;
}

.footer-item img {
  width: 32px;
  height: 32px;
  margin-right: 5px;
}

.footer-item a {
  color: #464646;
}
</style>
