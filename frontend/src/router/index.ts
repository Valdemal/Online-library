import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import ContentLayout from '@/layouts/ContentLayout.vue'
import AuthenticationLayout from '@/layouts/AuthenticationLayout.vue'

import content from '@/router/content'
import authentication from '@/router/authentication'
import NotFound from '@/views/NotFoundView.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: ContentLayout,
    children: content
  }, {
    path: '/auth',
    name: 'authentication',
    component: AuthenticationLayout,
    children: authentication
  }, {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
