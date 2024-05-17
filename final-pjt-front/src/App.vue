<script setup>
import { useProductStore } from '@/stores/products'
import { useUserStore } from '@/stores/users'
import { RouterLink, RouterView } from 'vue-router'
import { computed, onMounted, ref } from 'vue'
const userStore = useUserStore()
const isLogin = computed(() => userStore.isLogin)

</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink> | 
        <RouterLink :to="{name: 'signup'}">Sign Up | </RouterLink>
        <RouterLink :to="{name: 'login'}">Log In | </RouterLink>
        <RouterLink :to="{name: 'community'}">community | </RouterLink>
        <RouterLink :to="{name: 'products'}">products | </RouterLink>
        
        <RouterLink :to="{name: 'accounts'}">accounts | </RouterLink>
        <RouterLink :to="{name: 'profile'}">profile</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
