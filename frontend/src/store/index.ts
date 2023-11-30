import { InjectionKey } from 'vue'
import { createStore, Store } from 'vuex'
import { RootState } from '@/store/types'
import { currentUserModule } from '@/store/current_user'

// eslint-disable-next-line symbol-description
export const key: InjectionKey<Store<RootState>> = Symbol()

export const store = createStore<RootState>({
  state: {},
  modules: { currentUser: currentUserModule }
})
