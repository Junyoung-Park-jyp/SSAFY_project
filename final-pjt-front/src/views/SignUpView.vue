<template>
  <div class="signup-container">
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
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to right, #6dd5fa, #ffffff);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.card {
  width: 100%;
  max-width: 600px; /* 기존 크기 유지 */
  padding: 20px;
  margin-bottom: 15%;
  border-radius: 15px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
}

.card-header {
  text-align: center;
  margin-bottom: 20px;
}

.card-title {
  font-size: 28px;
  color: #005c99;
  font-weight: bold;
}

.form-label {
  font-size: 16px;
  color: #333;
  margin-bottom: 5px;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  margin-bottom: 15px;
  transition: border-color 0.3s ease;
}

.form-control:focus {
  border-color: #005c99;
  box-shadow: 0 0 5px rgba(0, 92, 153, 0.5);
}

.btn-primary {
  width: 100%;
  padding: 10px;
  background-color: #005c99;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 18px;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #004080;
}
</style>
