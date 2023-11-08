<script lang="ts">
import { defineComponent } from 'vue'
import { AuthService } from '@/api/services'
import router from '@/router'

export default defineComponent({
  name: 'LogoutView',
  async created () {
    try {
      const authService = new AuthService()
      await authService.logout()
      localStorage.removeItem('authToken')
    } finally {
      await router.push({ name: 'index' })
    }
  }
})
</script>
