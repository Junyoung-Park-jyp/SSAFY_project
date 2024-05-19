<template>
  <div>
    <h1>로그인 페이지</h1>
    <form @submit.prevent="LogIn">
      <p>
        <label for="username">아이디:</label>
        <input type="text" id="username" v-model.trim="username">
      </p>
      <p>
        <label for="password">비밀번호:</label>
        <input type="password" id="password" v-model.trim="password">
      </p>
      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/users'

const username = ref(null)
const password = ref(null)
const store = useUserStore()

const LogIn = function(){
  const payload = {
    username: username.value,
    password: password.value
  }
  store.LogIn(payload)
}
</script>

<style scoped>
</style>
