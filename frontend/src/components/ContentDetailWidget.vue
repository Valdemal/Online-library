<template>
  <HeaderWidget>
    <div class="detail-subheader flex-center">
      <div class="title flex-center">
        <slot name="title"></slot>
      </div>
      <div class="side-label flex-center">
        <slot name="side-label"></slot>
      </div>
    </div>
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

<script setup>
import HeaderWidget from '@/components/TheHeader.vue'
</script>

<style scoped>

main {
  margin: 10px 0 0 122px;
  min-height: 800px;
  display: flex;
}

.detail-subheader {
  height: 42px;
  color: #464646;
  font-size: 24px;
}

.detail-subheader >>> div {
  height: 100%;
  background-color: #D9D9D9;
}

.content-detail {
  color: #464646;
  padding-left: 10px;
}

.content-detail >>> .photo {
  width: 30%;
  float: left;
  margin-right: 10px;
  justify-content: center;
  border: 5px solid rgba(63, 159, 248, 0.7);

}

.content-detail >>> .photo img {
  width: 100%;
}

.sidebar {
  min-width: 300px;
  max-width: 300px;
  padding-left: 10px;
}

.sidebar >>> img {
  width: 100%;
}

.title {
  width: 100%;
}

.side-label {
  min-width: 300px;
  margin-left: 10px;
  position: sticky;
}

.side-label >>> a {
  color: #464646;
}

</style>
