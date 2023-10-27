<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <img src="">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav"
      aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <router-link :to="{ name: 'dashboard' }" class="nav-link">Dashboard</router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'customer' }" class="nav-link">Customers</router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'product' }" class="nav-link">Products</router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'login' }" class="nav-link">Login</router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'register' }" class="nav-link">SignUp</router-link>
        </li>
        <li class="nav-item">
          <p>{{ receivedMessage }}</p>
        </li>



      </ul>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    receivedMessage: String, // Define the prop in the child component
  },
  setup() {
  }
})
</script>

<style scoped></style>