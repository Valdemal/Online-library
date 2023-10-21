<template>
  <div class="estimation">
    <slot></slot>
  </div>
</template>

<style scoped>
.estimation {
  display: flex;
  justify-content: center;
  padding-bottom: 4px;
  width: 100%;
  height: 100%;
}

.estimation >>> div {
  padding-left: 25px;
  padding-right: 25px;
}
</style>
