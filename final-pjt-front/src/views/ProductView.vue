<template>
  <div class="container mt-5 product-view">
    <nav class="nav nav-pills justify-content-center mb-4">
      <RouterLink class="nav-link" :to="{ name: 'deposit' }">정기예금</RouterLink>
      <RouterLink class="nav-link" :to="{ name: 'saving' }">정기적금</RouterLink>
    </nav>
    <RouterView />
    <div class="row">
      <div class="col-md-6" v-if="popularOptions.mostPopularDepositOption">
        <div class="card popular-option-card">
          <div class="card-body">
            <h3 class="card-title">가장 인기 있는 예금 상품</h3>
            <p class="card-text">은행: {{ popularOptions.mostPopularDepositOption.bank }}</p>
            <p class="card-text">상품명: {{ popularOptions.mostPopularDepositOption.name }}</p>
            <p class="card-text">가입자: {{ popularOptions.mostPopularDepositOption.num_users }}명</p>
          </div>
        </div>
      </div>
      <div class="col-md-6" v-if="popularOptions.mostPopularSavingOption">
        <div class="card popular-option-card">
          <div class="card-body">
            <h3 class="card-title">가장 인기 있는 적금 상품</h3>
            <p class="card-text">은행: {{ popularOptions.mostPopularSavingOption.bank }}</p>
            <p class="card-text">상품명: {{ popularOptions.mostPopularSavingOption.name }}</p>
            <p class="card-text">가입자: {{ popularOptions.mostPopularSavingOption.num_users }}명</p>
          </div>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import { useProductStore } from '../stores/products';
import { useUserStore } from '@/stores/users';

const productStore = useProductStore();
const userStore = useUserStore()
const popularOptions = productStore.popularOptions;
const isLogin = computed(() => userStore.isLogin);
onMounted(async () => {
  await productStore.getPopularOptions();
});
</script>

<style scoped>
.product-view {
  background: linear-gradient(to right, #ffffff, #f7f7f7);
  padding: 60px;
  border-radius: 20px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  margin-top: 40px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  transition: all 0.3s ease;
}

.product-view:hover {
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.nav-pills {
  border-bottom: 2px solid #ddd;
  padding-bottom: 10px;
}

.nav-pills .nav-link {
  margin: 0 15px;
  padding: 12px 25px;
  background-color: #004080;
  color: white;
  border-radius: 30px;
  font-size: 18px;
  font-weight: 500;
  transition: background-color 0.3s, transform 0.3s;
}

.nav-pills .nav-link:hover {
  background-color: #0059b3;
  transform: translateY(-2px);
}

.nav-pills .nav-link.active {
  background-color: #003366;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.popular-option-card {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.popular-option-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.popular-option-card .card-body {
  padding: 20px;
}

.popular-option-card .card-title {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 15px;
  color: #004080;
}

.popular-option-card .card-text {
  font-size: 18px;
  color: #333;
  margin-bottom: 10px;
}
</style>
