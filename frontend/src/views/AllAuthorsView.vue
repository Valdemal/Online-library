<template>
  <HeaderWidget/>
  <ContentGridWidget>
    <AuthorItem/>
  </ContentGridWidget>
</template>

<script setup>
import AuthorItem from '@/components/AuthorGridItem.vue'
import HeaderWidget from '@/components/HeaderWidget.vue'
import ContentGridWidget from '@/layouts/ContentGridWidget.vue'
</script>
