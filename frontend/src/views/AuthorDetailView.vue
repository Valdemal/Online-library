<template>
  <ContentDetailWidget>
    <template #title>{{ author.name + ' ' + author.surname }}</template>

    <template #side-label>Книги</template>

    <template #content>
      <DescriptionWidget>
        <div class="photo">
          <img :src="author.image" :alt="author.name + ' ' + author.surname">
          <EstimationWidget>
            <div>🌟{{ author.score }}</div>
            <div>📚{{ author.popularity }}</div>
          </EstimationWidget>
        </div>
        <div class="text">{{ author.description }}</div>
      </DescriptionWidget>
    </template>

    <template #sidebar>
      <BookList :author_slug="author.slug"/>
    </template>
  </ContentDetailWidget>
</template>

<script>

import ContentDetailWidget from '@/components/ContentDetailWidget.vue'
import BookList from '@/components/BookList.vue'
import EstimationWidget from '@/components/BaseEstimation.vue'
import DescriptionWidget from '@/components/BaseDescription.vue'
import { Author } from '@/api/schemas'

export default {
  components: { DescriptionWidget, EstimationWidget, BookList, ContentDetailWidget },
  data () {
    return {
      author: Author
    }
  },
  created () {
    const slug = this.$route.params.slug
    console.log(slug)
    //   Получение данных по слагу
    this.author = {
      score: 3.9000000000000004,
      popularity: 5,
      slug: 'viktor-pelevin',
      name: 'Виктор',
      surname: 'Пелевин',
      image: 'http://127.0.0.1/media/authors/images/322_original.jpeg',
      description: 'Советский и российский писатель, эссеист. Заявил себя как автор романов в 1990-х годах такими работами как «Омон Ра», «Чапаев и Пустота» и «Generation „П“». С 2003 года выпускает в среднем по одной новой книге в год, многие из которых становились литературными событиями. Лауреат многочисленных литературных премий, среди которых «Золотой шар» (1990), «Малый Букер» (1993), «Национальный бестселлер» (2004), «Большая книга» (2010, 3-е место), премия Андрея Белого (2017).'
    }
  }

}
</script>
