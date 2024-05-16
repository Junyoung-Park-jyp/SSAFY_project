<template>
  <div>
    <h1>로그인 페이지</h1>
    <form @submit.prevent="LogIn">
      <label for="username">아이디:</label>
      <input type="text" id="username" v-model.trim="username">
      <label for="password">비밀번호:</label>
      <input type="password" id="password" v-model.trim="password">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles';
import { storeToRefs } from 'pinia';

const username = ref(null)
const password = ref(null)
const store = useArticleStore()
const LogIn = function(){
  const payload = {
      username : username.value,
      password : password.value
    }
  store.LogIn(payload)
}

</script>

<style scoped>

</style>