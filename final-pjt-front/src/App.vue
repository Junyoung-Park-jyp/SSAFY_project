<script setup>
import { useArticleStore } from '@/stores/articles'
import { RouterLink, RouterView } from 'vue-router'
import { computed, onMounted, ref } from 'vue'
import MapComponent from './components/MapComponent.vue';
const store = useArticleStore()
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
  <MapComponent/>

  <RouterView />
</template>

<style scoped>
</style>
