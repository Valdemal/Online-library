<template>
  <ContentDetailWidget>
    <template #title>{{ author_name }}</template>

    <template #side-label>Книги</template>

    <template #content>
      <DescriptionWidget>
        <div class="photo">
          <img :src="model.image" :alt="author_name">
          <EstimationWidget>
            <div>🌟{{ model.score }}</div>
            <div>📚{{ model.popularity }}</div>
          </EstimationWidget>
        </div>
        <div class="text">{{ model.description }}</div>
      </DescriptionWidget>
    </template>

    <template #sidebar>
      <BookList/>
    </template>
  </ContentDetailWidget>
</template>

<script>

import ContentDetailWidget from '@/components/ContentDetailWidget.vue'
import BookList from '@/components/BookList.vue'
import EstimationWidget from '@/components/BaseEstimation.vue'
import DescriptionWidget from '@/components/BaseDescription.vue'

export default {
  components: { DescriptionWidget, EstimationWidget, BookList, ContentDetailWidget },
  data () {
    return {
      model: {
        name: 'Федор',
        surname: 'Достоевский',
        image: '/img/Достоевский.d8b22864.jpg',
        score: 4.9,
        popularity: 1500,
        description: ' Фёдор Миха́йлович Достое́вский (30 октября [11 ноября] 1821, Москва — 28 января [9 февраля] 1881,\n' +
          '          Санкт-Петербург[2]) — русский писатель, мыслитель, философ и публицист[3]. Член-корреспондент\n' +
          '          Петербургской академии наук с 1877 года[4]. Классик мировой литературы, по данным ЮНЕСКО, один из самых\n' +
          '          читаемых писателей в мире. Собрание сочинений Достоевского состоит из 12 романов, четырёх новелл, 16\n' +
          '          рассказов и множества других произведений.'
      }
    }
  },
  computed: {
    author_name () {
      return this.model.name + ' ' + this.model.surname
    }
  }
}
</script>
