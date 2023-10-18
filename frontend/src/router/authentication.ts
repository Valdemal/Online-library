import LoginView from '@/views/LoginView.vue'
import RegistrationView from '@/views/RegistrationView.vue'

export default [
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
