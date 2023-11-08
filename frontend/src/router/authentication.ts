import LoginView from '@/views/LoginView.vue'
import RegistrationView from '@/views/RegistrationView.vue'
import LogoutView from '@/views/LogoutView.vue'

export default [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  }, {
    path: '/registration',
    name: 'registration',
    component: RegistrationView
  }, {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  }
]
