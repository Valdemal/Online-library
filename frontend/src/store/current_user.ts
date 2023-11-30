import { Module } from 'vuex'
import { RootState } from '@/store/types'
import { User } from '@/api/schemas'
import { AuthService, MeService } from '@/api/services'
import { LoginCredentials } from '@/api/schemas/types'

interface State {
  currentUser: User | null;
}

const ME_SERVICE = new MeService()
const AUTH_SERVICE = new AuthService()

export const currentUserModule: Module<State, RootState> = {
  state: {
    currentUser: null
  },
  actions: {
    async fetchCurrentUser (context) {
      if (ME_SERVICE.isAuthenticated()) {
        const data = await ME_SERVICE.get()
        context.commit('updateCurrentUser', data)
      }
    },
    async login (context, credentials: LoginCredentials) {
      const token = await AUTH_SERVICE.login(credentials)
      localStorage.authToken = token
    },
    async logout (context) {
      await AUTH_SERVICE.logout()
      localStorage.removeItem('authToken')
      context.commit('updateCurrentUser', null)
    }
  },
  mutations: {
    updateCurrentUser (state, newUser: User | null) {
      state.currentUser = newUser
    }
  },
  getters: {
    currentUser (state) {
      return state.currentUser
    }
  }
}
