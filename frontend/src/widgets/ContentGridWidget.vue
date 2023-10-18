<template>
  <main>
    <div class="content-grid">
      <slot></slot>
    </div>
  </main>
</template>

<style scoped>

main {
  margin: 10px 310px 0 122px;
  min-height: 800px;
}

.content-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
}

@media screen and (max-width: 1200px){
  .content-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }
}

@media screen and (max-width: 900px){
  .content-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
  }
}

</style>
