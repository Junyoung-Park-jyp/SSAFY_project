<template>
  <div class="login-container">
    <div class="card">
      <div class="card-header">
        <h1 class="card-title">로그인</h1>
      </div>
      <div class="card-body">
        <form @submit.prevent="logIn">
          <div class="form-group">
            <label for="username">아이디:</label>
            <input type="text" v-model="username" id="username" required />
          </div>
          <div class="form-group">
            <label for="password">비밀번호:</label>
            <input type="password" v-model="password" id="password" required />
          </div>
          <button type="submit" class="btn btn-primary">로그인</button>
          <p v-if="userStore.errorMessage" class="error-message">{{ userStore.errorMessage }}</p>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useUserStore } from '@/stores/users'

export default {
  setup() {
    const username = ref('')
    const password = ref('')
    const userStore = useUserStore()

    const logIn = async () => {
      if (!username.value || !password.value) {
        userStore.errorMessage = '아이디와 비밀번호를 입력해주세요.'
      } else {
        await userStore.LogIn({ username: username.value, password: password.value });
      }
    }

    return {
      username,
      password,
      userStore,
      logIn
    }
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to right, #6dd5fa, #ffffff);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.card {
  width: 100%;
  max-width: 400px;
  padding: 20px;
  margin-bottom: 20%;
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

.card-body {
  padding: 20px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  color: #005c99;
}

.form-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.btn-primary {
  display: inline-block;
  width: 100%;
  padding: 12px 24px;
  background: linear-gradient(135deg, #0f4c75, #3282b8, #bbe1fa);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
}

.btn-primary:hover {
  background-color: #004080;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.error-message {
  color: red;
  margin-top: 10px;
  text-align: center;
}
</style>
