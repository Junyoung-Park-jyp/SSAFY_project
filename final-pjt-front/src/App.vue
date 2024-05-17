<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink> | 
        <RouterLink :to="{name: 'signup'}">Sign Up</RouterLink> |
        <RouterLink :to="{name: 'login'}">Log In</RouterLink> |
        <RouterLink :to="{name: 'community'}">Community</RouterLink> |
        <RouterLink :to="{name: 'products'}">Products</RouterLink> |
        <RouterLink :to="{name: 'profile'}">Profile</RouterLink> |
        <RouterLink :to="{name: 'exchangeRateCalculator'}">환율 계산기</RouterLink> <!-- 추가된 부분 -->
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<script setup>
import { useUserStore } from '@/stores/users'
import { computed } from 'vue'
const userStore = useUserStore()
const isLogin = computed(() => userStore.isLogin)
</script>

<style scoped>
/* 스타일 추가 */
</style>
