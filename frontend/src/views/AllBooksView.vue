<template>
  <HeaderWidget/>
  <ContentGridWidget>
    <BookItem/>
  </ContentGridWidget>
</template>

<script setup>
import ContentGridWidget from '@/layouts/ContentGridWidget.vue'
import HeaderWidget from '@/components/HeaderWidget.vue'
import BookItem from '@/components/BookGridItem.vue'
</script>
