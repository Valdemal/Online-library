import AuthorsList from '@/views/AuthorListView.vue'
import AuthorDetail from '@/views/AuthorDetailView.vue'
import BooksList from '@/views/BookListView.vue'
import BookDetail from '@/views/BookDetailView.vue'

export default [
  {
    path: '',
    name: 'index',
    redirect: { name: 'books' }
  }, {
    path: '/authors',
    name: 'authors',
    component: AuthorsList
  }, {
    path: '/authors/:slug',
    name: 'author-detail',
    component: AuthorDetail
  }, {
    path: '/books',
    name: 'books',
    component: BooksList
  }, {
    path: '/books/:slug',
    name: 'book-detail',
    component: BookDetail
  }
]
