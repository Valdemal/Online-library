<template>
  <BookDetailComponent v-if="book && author" :author="author" :book="book"/>
</template>

<script lang="ts">

import { Author, Book } from '@/api/schemas'
import { defineComponent } from 'vue'
import BookDetailComponent from '@/components/BookDetailComponent.vue'
import router from '@/router'

interface State {
  book: Book | null
  author: Author | null
}

export default defineComponent({
  components: { BookDetailComponent },
  data (): State {
    return { book: null, author: null }
  },
  created () {
    const slug = this.$route.params.slug
    console.log(slug)

    if (slug === 'generation-p-viktor-pelevin') {
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
    } else {
      router.push({ name: 'not-found' })
    }
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
