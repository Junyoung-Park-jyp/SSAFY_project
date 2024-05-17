<template>
  <div>
    <h1>{{ user.username }}님의 프로필 페이지</h1>
    <div>
      <p>회원번호: {{ user.id }}</p>
      <p>ID: {{ user.username }}</p>
      <p>Email: <input v-model="user.email" /></p>
      <p>Nickname: <input v-model="user.nickname" /></p>
      <p>나이: <input v-model="user.age" /></p>
      <p>현재 가진 금액: <input v-model="user.current_balance" /></p>
      <p>연봉: <input v-model="user.annual_salary" /></p>
      <button @click="updateProfile">수정하기</button>
    </div>
    <div>
      <h2>가입한 상품들</h2>
      <ul>
        <li v-for="product in user.saving_products" :key="product.id">{{ product.name }}</li>
        <li v-for="product in user.deposit_products" :key="product.id">{{ product.name }}</li>
      </ul>
    </div>
    <div>
      <h2>가입한 상품 금리</h2>
      <ProductChart :savingProducts="user.saving_products" :depositProducts="user.deposit_products" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useUserStore } from '@/stores/users'
import ProductChart from '@/components/ProductChart.vue'

export default {
  components: {
    ProductChart
  },
  data() {
    return {
      user: {},
    };
  },
  methods: {
    fetchProfile() {
      const userStore = useUserStore()
      axios.get('/api/v1/profile/', {
        headers: { Authorization: `Token ${userStore.token}` }
      })
        .then(response => {
          this.user = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    updateProfile() {
      const userStore = useUserStore()
      axios.put('/api/v1/profile/update/', this.user, {
        headers: { Authorization: `Token ${userStore.token}` }
      })
        .then(response => {
          alert('프로필이 수정되었습니다.');
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  mounted() {
    this.fetchProfile();
  }
};
</script>
