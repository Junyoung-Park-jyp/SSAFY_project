<script setup>
import { useProductStore } from '@/stores/products'
import { RouterLink, RouterView } from 'vue-router'
import { computed, onMounted, ref } from 'vue'
const store = useProductStore()
const isLogin = computed(() => store.isLogin)

</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink> | 
        <RouterLink v-if="!isLogin" :to="{name: 'signup'}">Sign Up | </RouterLink>
        <RouterLink v-if="!isLogin" :to="{name: 'login'}">Log In | </RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
