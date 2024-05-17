<template>
  <div>
    <h1>회원가입 페이지</h1>
    <form @submit.prevent="SignUp">
      <p>
        <label for="username">아이디:</label>
        <input type="text" id="username" v-model.trim="username">
      </p>
      <p>
        <label for="password1">비밀번호:</label>
        <input type="password" id="password1" v-model.trim="password1">
      </p>
      <p>
        <label for="password2">비밀번호 확인:</label>
        <input type="password" id="password2" v-model.trim="password2">
      </p>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/users';
import { storeToRefs } from 'pinia';

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const store = useUserStore()
const SignUp = function(){
  const payload = {
      username : username.value,
      password1 : password1.value,
      password2 : password2.value
    }
  store.SignUp(payload)
}



</script>

<style scoped>

</style>