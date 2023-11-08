<template>
  <div class="subheader flex-center">
    <div class="search flex-right">
      <input placeholder="Поиск">
      <span>▼</span>
      <span>🔍</span>
    </div>
  </div>
</template>

<style scoped>

.search {
  width: 100%;
  height: 42px;
  padding: 0 20px 0 20px;
  background-color: #D9D9D9;
  color: #464646;
  margin-right: 310px;
}

.search input {
  width: 100%;
  font-size: 15px;
  background-color: #D9D9D9;
  border: none;
  border-bottom: 1px solid #464646;
  outline: none;
}

.search span {
  margin-left: 5px;
  font-size: 20px;
  cursor: pointer;
}

</style>
