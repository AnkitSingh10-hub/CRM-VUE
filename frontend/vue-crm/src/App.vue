<template>
  <!-- navbar -->
  <NavbarView :receivedMessage="message" />
  <div class="container-fluid">
    <RouterView></RouterView>


  </div>
  <FooterView />
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import NavbarView from './components/NavbarView.vue'
import FooterView from './components/FooterView.vue'


export default defineComponent({
  components: {
    NavbarView,
    FooterView
  },
  setup() {

    const message = ref<string>('You are not logged in')
    onMounted(async () => {
      const response = await fetch('http://localhost:8000/user', {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
      })
      const content = await response.json()
      message.value = `Hi ${content.username}`
    }
    )



    return { message }


  }
})
</script>

<style scoped></style>