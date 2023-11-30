<script lang="ts">
import { defineComponent } from 'vue'
import router from '@/router'
import { mapActions } from 'vuex'

export default defineComponent({
  name: 'LogoutView',
  async created () {
    try {
      await this.logout()
    } finally {
      await router.push({ name: 'index' })
    }
  },
  methods: mapActions(['logout'])
})
</script>
