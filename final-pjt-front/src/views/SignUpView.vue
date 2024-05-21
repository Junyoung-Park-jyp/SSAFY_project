// SignUpView.vue

<template>
  <div class="container mt-4">
    <div class="card">
      <div class="card-header">
        <h1 class="card-title">회원가입 페이지</h1>
      </div>
      <div class="card-body">
        <form @submit.prevent="SignUp">
          <div class="mb-3">
            <label for="username" class="form-label">아이디:</label>
            <input type="text" id="username" class="form-control" v-model.trim="username">
          </div>
          <div class="mb-3">
            <label for="password1" class="form-label">비밀번호:</label>
            <input type="password" id="password1" class="form-control" v-model.trim="password1">
          </div>
          <div class="mb-3">
            <label for="password2" class="form-label">비밀번호 확인:</label>
            <input type="password" id="password2" class="form-control" v-model.trim="password2">
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">이메일:</label>
            <input type="email" id="email" class="form-control" v-model.trim="email">
          </div>
          <button type="submit" class="btn btn-primary">회원가입</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/users'
import { storeToRefs } from 'pinia'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const email = ref(null)
const store = useUserStore()
const SignUp = function(){
  const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      email: email.value,
    }
  console.log(payload)
  store.SignUp(payload)
}
</script>

<style scoped>
</style>
