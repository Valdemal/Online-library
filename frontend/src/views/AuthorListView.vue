<template>
  <TheHeader/>
  <ContentGridWidget>
    <AuthorListViewItem
      v-for="author in authors"
      :key="author.slug"
      :author="author"
    />
  </ContentGridWidget>
</template>

<script lang="ts">

import ContentGridWidget from '@/widgets/ContentGridWidget.vue'
import TheHeader from '@/components/TheHeader.vue'
import AuthorListViewItem from '@/components/AuthorListViewItem.vue'
import { Author } from '@/api/schemas'
import { defineComponent } from 'vue'

export default defineComponent({
  components: { AuthorListViewItem, TheHeader, ContentGridWidget },
  data () {
    return {
      authors: [
        {
          score: 3.9,
          popularity: 5,
          slug: 'viktor-pelevin',
          name: 'Виктор',
          surname: 'Пелевин',
          image: 'http://127.0.0.1/media/authors/images/322_original.jpeg',
          description: 'Советский и российский писатель, эссеист. Заявил себя как автор романов в 1990-х годах такими работами как «Омон Ра», «Чапаев и Пустота» и «Generation „П“». С 2003 года выпускает в среднем по одной новой книге в год, многие из которых становились литературными событиями. Лауреат многочисленных литературных премий, среди которых «Золотой шар» (1990), «Малый Букер» (1993), «Национальный бестселлер» (2004), «Большая книга» (2010, 3-е место), премия Андрея Белого (2017).'
        },
        {
          score: 3.38,
          popularity: 3,
          slug: 'mikhail-elizarov',
          name: 'Михаил',
          surname: 'Елизаров',
          image: 'http://127.0.0.1/media/authors/images/%D0%9F%D0%B8%D1%81%D0%B0%D1%82%D0%B5%D0%BB%D1%8C-%D0%9C%D0%B8%D1%85%D0%B0%D0%B8%D0%BB-%D0%95%D0%BB%D0%B8%D0%B7%D0%B0%D1%80%D0%BE%D0%B2.jpg',
          description: 'Русский писатель и автор-исполнитель. Лауреат литературных премий «Русский Букер» (за роман «Библиотекарь»), «Национальный бестселлер» (за роман «Земля») и Григорьевской поэтической премии.'
        }
      ].map((json) => {
        return new Author(json)
      })
    }
  }
})
</script>
