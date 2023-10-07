<template>
  <div class="book-list">
    <BookListItem
      v-for="book in books" :key="book.slug"
      :schema="book"
    />
  </div>
</template>

<script>
import BookListItem from '@/components/BookListItem.vue'
import { Slug } from '@/api/schemas'

export default {
  components: { BookListItem },
  props: {
    author_slug: {
      type: Slug,
      required: false
    }
  },
  data () {
    return {
      books: [
        {
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
        },
        {
          author: 'viktor-pelevin',
          genres: [
            'roman',
            'postmodernizm',
            'antiutopiya',
            'nauchnaya-fantastika'
          ],
          score: null,
          popularity: 2,
          slug: 'snuff-viktor-pelevin',
          title: 'S.N.U.F.F',
          description: 'Десятый роман Виктора Пелевина, впервые опубликованный в декабре 2011 года тиражом 150 000 экземпляров с аннотацией: «Роман-утøпія о глубочайших тайнах женского сердца и высших секретах лётного мастерства!»',
          file: 'http://127.0.0.1/media/books/files/pelevin-viktor-snuff.130.pdf',
          year_of_writing: 2011,
          cover: 'http://127.0.0.1/media/books/covers/snuff.jpg'
        }
      ]
    }
  }
}
</script>
