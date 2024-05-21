// SignUpView.vue

<template>
  <div class="container mt-4 signup">
    <div class="card">
      <div class="card-header">
        <h1 class="card-title" style="color:white;">회원가입 페이지</h1>
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
.signup {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  color: #002b5c;
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 20px;
}

.card {
  border: none;
  border-radius: 10px;
  overflow: hidden;
}

.card-header {
  background: #002b5c;
  color: white;
  padding: 20px;
}

.card-title {
  margin: 0;
  font-size: 24px;
}

.card-body {
  padding: 20px;
}

.signup-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.btn-primary {
  padding: 10px 20px;
  background-color: #002b5c;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #005c99;
}
</style>
