<template>
  <AuthorDetailComponent v-if="author" :author="author"/>
</template>

<script lang="ts">

import { defineComponent } from 'vue'
import { Author } from '@/api/schemas'
import AuthorDetailComponent from '@/components/AuthorDetailComponent.vue'
import router from '@/router'

interface State {
  author: Author | null
}

export default defineComponent({
  components: { AuthorDetailComponent },
  data (): State {
    return {
      author: null
    }
  },
  created () {
    const slug = this.$route.params.slug
    console.log(slug)

    if (slug === 'viktor-pelevin') {
      //   Получение данных по слагу
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
