<template>
  <a href="/authors/slug">
    <div class="content-item">
      <slot></slot>
    </div>
  </a>
</template>

<script>

</script>

<style>

.content-item {
  height: 320px;
  margin-bottom: 10px;
  margin-left: 10px;
  cursor: pointer;
  position: relative;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.25);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  flex-wrap: nowrap;
}

.content-item img {
  width: 100%;
  height: 100%;
  position: absolute;
}

.content-item .text {
  position: absolute;
  width: 100%;
}

.content-item .name {
  background-color: #3F9FF8;
  color: #F5F5F5;
  font-size: 16px;
  min-height: 40px;
  text-align: center;
}

.content-item .description {
  max-height: 0;
  transition: 0.5s;
  color: #464646;
  background-color: rgba(217, 217, 217, 0.79);
  font-size: 14px;
  overflow: scroll;
}

.content-item:hover .description {
  max-height: 280px;
  height: 280px;
}

.content-item .description p {
  margin: 8px 4px;
  text-align: justify;
}

.content-item .description::-webkit-scrollbar {
  display: none;
}

</style>
