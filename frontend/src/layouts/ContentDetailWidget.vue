<script setup >

import HeaderWidget from '@/components/HeaderWidget.vue'
</script>

<template>
  <HeaderWidget>
    <slot name="title"></slot>
  </HeaderWidget>
  <main>
    <div class="content-detail">
      <slot name="content"></slot>
    </div>
    <div class="sidebar">
      <slot name="sidebar"></slot>
    </div>
  </main>
</template>

<style scoped>
main {
  margin: 10px 0 0 122px;
  min-height: 800px;
  display: flex;
}

/deep/ .detail-subheader {
  height: 42px;
  color: #464646;
  font-size: 24px;
}

/deep/ .detail-subheader div {
  height: 100%;
  background-color: #D9D9D9;
}

/deep/ .title {
  width: 100%;
}

/deep/ .side-label {
  min-width: 300px;
  margin-left: 10px;
  position: sticky;
}

/deep/ .sidebar {
  min-width: 300px;
  max-width: 300px;
  padding-left: 10px;
}

/deep/ .sidebar img {
  width: 100%;
}

/deep/ .content-detail {
  color: #464646;
  padding-left: 10px;
}

/deep/ .content-detail .photo {
  width: 30%;
  float: left;
  margin-right: 10px;
  justify-content: center;
  border: 5px solid rgba(63, 159, 248, 0.7);

}

/deep/ .content-detail .photo img {
  width: 100%;
}

/deep/ .description {
  display: flow-root;
}

/deep/ .estimation {
  display: flex;
  justify-content: center;
  padding-bottom: 4px;
  width: 100%;
  height: 100%;
}

/deep/ .estimation div {
  padding-left: 25px;
  padding-right: 25px;
}

/deep/ .side-label a {
  color: #464646;
}

</style>
