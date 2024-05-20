<template>
  <div class="container mt-4">
    <div class="card">
      <div class="card-header">
        <h1 class="card-title">{{ user?.username }}님의 프로필 페이지</h1>
      </div>
      <div class="card-body">
        <div v-if="user">
          <p>회원번호: {{ user.id }}</p>
          <p>ID: {{ user.username }}</p>
          <p>Email: <input v-model="user.email" class="form-control" /></p>
          <p>나이: <input v-model="user.user_info.age" class="form-control" /></p>
          <p>현재 가진 금액: <input v-model="user.user_info.current_balance" class="form-control" /></p>
          <p>연봉: <input v-model="user.user_info.annual_salary" class="form-control" /></p>
          <p>
            <label for="bank">주 이용은행:</label>
            <select id="bank" v-model="user.user_info.bank" class="form-select">
              <!-- 옵션들은 이전과 동일하게 유지됩니다. -->
            </select>
          </p>
          <button @click="updateProfile" class="btn btn-primary">수정하기</button>
        </div>
      </div>
      <div class="card-footer" v-if="user && user.saving_products && user.deposit_products">
        <h2>가입한 상품들</h2>
        <ul>
          <li v-for="product in user.saving_products" :key="product.id">{{ product.name }}</li>
          <li v-for="product in user.deposit_products" :key="product.id">{{ product.name }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script setup>
import { useUserStore } from '@/stores/users';
import { ref, onMounted } from 'vue'
const user = ref(null)
const store = useUserStore()
const loadUserProfile = async () => {
  user.value = await store.getProfile()
}

onMounted(() => {
  loadUserProfile()
})
</script>
<!-- <script>
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
</script> -->