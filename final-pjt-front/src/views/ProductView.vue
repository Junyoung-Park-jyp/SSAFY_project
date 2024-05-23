<template>
  <div class="container mt-5 product-view">
    <nav class="nav nav-pills justify-content-center mb-4">
      <RouterLink class="nav-link" style="margin-right: 500px;" :to="{ name: 'deposit' }">정기예금</RouterLink>
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
  background: linear-gradient(to right, #ffffff, #e0e0e0);
  padding: 60px;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  margin-top: 40px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  transition: all 0.3s ease;
}

.product-view:hover {
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25);
}

.nav-pills {
  border-bottom: 2px solid #ccc;
  padding-bottom: 10px;
}

.nav-pills .nav-link {
  margin: 0 15px;
  padding: 12px 30px;
  background: linear-gradient(135deg, #0f4c75, #3282b8, #bbe1fa);
  color: white;
  border-radius: 30px;
  font-size: 18px;
  font-weight: 600;
  transition: background-color 0.3s, transform 0.3s, box-shadow 0.3s;
}

.nav-pills .nav-link:hover {
  background-color: #0066cc;
  transform: translateY(-2px);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}

.nav-pills .nav-link.active {
  background-color: #003f7f;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.popular-option-card {
  background: #ffffff;
  border-radius: 15px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.popular-option-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.25);
}

.popular-option-card .card-body {
  padding: 25px;
}

.popular-option-card .card-title {
  font-size: 26px;
  font-weight: 700;
  margin-bottom: 20px;
  color: #00509e;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}

.popular-option-card .card-text {
  font-size: 20px;
  color: #444;
  margin-bottom: 15px;
  line-height: 1.5;
}

.popular-option-card .card-text::before {
  content: "• ";
  color: #00509e;
}

.container {
  max-width: 1200px;
  margin: auto;
}

body {
  background: #f2f2f2;
  color: #333;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h3 {
  color: #00509e;
}

.row {
  display: flex;
  flex-wrap: wrap;
}

.col-md-6 {
  flex: 0 0 50%;
  max-width: 50%;
  padding: 15px;
  box-sizing: border-box;
}

.card {
  border: none;
}

.card-body {
  background: linear-gradient(to bottom, #ffffff, #f0f0f0);
  border-radius: 15px;
  padding: 20px;
}

@media (max-width: 768px) {
  .col-md-6 {
    flex: 0 0 100%;
    max-width: 100%;
  }

  .nav-pills .nav-link {
    margin: 5px 0;
    padding: 10px 20px;
  }
}
</style>

