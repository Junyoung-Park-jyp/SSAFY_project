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
        <RouterLink v-if="!isLogin" :to="{name: 'signup'}">Sign Up | </RouterLink>
        <RouterLink v-if="!isLogin" :to="{name: 'login'}">Log In | </RouterLink>
        <RouterLink :to="{name: 'community'}">Community</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
