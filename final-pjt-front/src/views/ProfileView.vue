<template>
  <div>
    <h1>{{ user.username }}님의 프로필 페이지</h1>
    <div>
      <p>회원번호: {{ user.id }}</p>
      <p>ID: {{ user.username }}</p>
      <p>Email: <input v-model="user.email" /></p>
      <p>나이: <input v-model="user.age" /></p>
      <p>현재 가진 금액: <input v-model="user.current_balance" /></p>
      <p>연봉: <input v-model="user.annual_salary" /></p>
      <p>이용하시는 은행: <input v-model="user.bank" /></p>
      <button @click="updateProfile">수정하기</button>
    </div>
    <div>
      <h2>가입한 상품들</h2>
      <ul>
        <li v-for="product in user.saving_products" :key="product.id">{{ product.name }}</li>
        <li v-for="product in user.deposit_products" :key="product.id">{{ product.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { useUserStore } from '@/stores/users'

export default {
  data() {
    return {
      user: {},
    }
  },
  async created() {
    const userStore = useUserStore()
    const profile = await userStore.getProfile()
    if (profile) {
      this.user = profile
    }
  },
  methods: {
    async updateProfile() {
      const userStore = useUserStore()
      try {
        const response = await axios.put('http://127.0.0.1:8000/api/v1/accounts/profile/update/', this.user, {
          headers: { Authorization: `Token ${userStore.token}` }
        })
        alert('프로필이 수정되었습니다.')
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
