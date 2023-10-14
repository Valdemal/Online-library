<template>
  <ContentDetailWidget>
    <template #title>
      {{ book.title }}
    </template>

    <template #side-label>
      <router-link :to="{name:'author-detail', params: {slug: author.slug}}">
        {{ author.fullName}}
      </router-link>
    </template>

    <template #content>
      <DescriptionWidget>
        <div class="photo">
          <img :src="book.cover" :alt="book.title">
          <EstimationWidget>
            <div>🌟{{ book.roundedScore() }}</div>
            <div>📚{{ book.popularity }}</div>
          </EstimationWidget>
        </div>
        <div class="text book-text">{{ book.description }}</div>
      </DescriptionWidget>
      <CommentsList :book_slug="book.slug"/>
    </template>

    <template #sidebar>
      <img :src="author.image" :alt="author.fullName">
    </template>
  </ContentDetailWidget>
</template>

<script lang="ts">

import CommentsList from '@/components/CommentList.vue'
import ContentDetailWidget from '@/components/ContentDetailWidget.vue'
import EstimationWidget from '@/components/BaseEstimation.vue'
import DescriptionWidget from '@/components/BaseDescription.vue'
import { Author, Book } from '@/api/schemas'
import { defineComponent } from 'vue'

interface State {
  book: Book | null
  author: Author | null
}

export default defineComponent({
  components: { DescriptionWidget, EstimationWidget, ContentDetailWidget, CommentsList },
  data () : State {
    return { book: null, author: null }
  },
  created () {
    const slug = this.$route.params.slug
    console.log(slug)
    //   Получение данных по слагу
    this.book = new Book({
      author: 'viktor-pelevin',
      genres: [
        'roman',
        'postmodernizm'
      ],
      score: 3.9000000000000004,
      popularity: 3,
      slug: 'generation-p-viktor-pelevin',
      title: 'Generation "П"',
      description: 'Постмодернистский роман российского писателя Виктора Пелевина о поколении россиян, которое взрослело и формировалось во времена политических и экономических реформ 1990-х годов. Действие романа разворачивается в Москве 1990-х годов. Главный герой романа - Вавилен Татарский, интеллигентный юноша, выпускник Литературного института, своё необычное имя он получил от отца - поклонника Василия Аксёнова и Владимира Ленина. Татарский - собирательный образ «поколения „П“» - поколения семидесятых',
      file: 'http://127.0.0.1/media/books/files/genration_p.pdf',
      year_of_writing: 1999,
      cover: 'http://127.0.0.1/media/books/covers/generation_p.jpg'
    })
    this.author = new Author({
      score: 3.9000000000000004,
      popularity: 5,
      slug: 'viktor-pelevin',
      name: 'Виктор',
      surname: 'Пелевин',
      image: 'http://127.0.0.1/media/authors/images/322_original.jpeg',
      description: 'Советский и российский писатель, эссеист. Заявил себя как автор романов в 1990-х годах такими работами как «Омон Ра», «Чапаев и Пустота» и «Generation „П“». С 2003 года выпускает в среднем по одной новой книге в год, многие из которых становились литературными событиями. Лауреат многочисленных литературных премий, среди которых «Золотой шар» (1990), «Малый Букер» (1993), «Национальный бестселлер» (2004), «Большая книга» (2010, 3-е место), премия Андрея Белого (2017).'
    })
  }
})

</script>

<style scoped>
.book-text {
  max-height: 600px;
  overflow: scroll;
  overflow-x: hidden;
}

</style>
