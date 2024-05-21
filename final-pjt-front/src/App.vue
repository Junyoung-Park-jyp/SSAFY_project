<template>
  <header>
    <div class="wrapper">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <div class="container-fluid">
        <RouterLink class="navbar-brand" to="/">Home</RouterLink>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item" v-if="!isLogin">
              <RouterLink class="nav-link" :to="{name: 'signup'}">Sign Up</RouterLink>
            </li>
            <li class="nav-item" v-if="!isLogin">
              <RouterLink class="nav-link" :to="{name: 'login'}">Log In</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{name: 'community'}">Community</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{name: 'products'}">Products</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{name: 'profile'}">Profile</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{name: 'search'}">가까운 은행 찾기</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{name: 'exchangeRateCalculator'}">환율 계산기</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
  </header>
  <MapComponent/>

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
