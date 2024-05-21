<template>
  <div class="container mt-4">
    <div class="card">
      <div class="card-header">
        <h1 class="card-title">로그인 페이지</h1>
      </div>
      <div class="card-body">
        <form @submit.prevent="LogIn">
          <div class="mb-3">
            <label for="username" class="form-label">아이디:</label>
            <input type="text" id="username" class="form-control" v-model.trim="username" required>
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">비밀번호:</label>
            <input type="password" id="password" class="form-control" v-model.trim="password" required>
          </div>
          <button type="submit" class="btn btn-primary">로그인</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/users'
import { useRouter } from 'vue-router'
const username = ref('')
const router = useRouter()
const password = ref('')
const store = useUserStore()

const LogIn = function(){
  if (!username.value || !password.value) {
    alert('아이디와 비밀번호를 모두 입력해주세요.')
    return
  }

  const payload = {
    username: username.value,
    password: password.value
  }
  store.LogIn(payload)
    .then(() => {
      router.push({ name: 'home' })
    })
    .catch(err => {
      alert('로그인에 실패했습니다.')
      console.error(err)
    })
}
</script>


<style scoped>
</style>
