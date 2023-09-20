import { createRouter, createWebHistory } from 'vue-router'
import AuthenticationLayout from '@/layouts/AuthenticationLayout.vue'
import LoginView from '@/views/LoginView.vue'
import ContentLayout from '@/layouts/ContentLayout.vue'
import AuthorsList from '@/views/AllAuthorsView.vue'
import RegistrationView from '@/views/RegistrationView.vue'
import BooksList from '@/views/AllBooksView.vue'
import AuthorDetail from '@/views/AuthorDetailView.vue'
import BookDetail from '@/views/BookDetailView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: ContentLayout,
    children: [
      {
        path: '',
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
  }, {
    path: '/auth',
    name: 'authentication',
    component: AuthenticationLayout,
    children: [
      {
        path: '/login',
        name: 'login',
        component: LoginView
      }, {
        path: '/registration',
        name: 'registration',
        component: RegistrationView
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
