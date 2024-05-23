<template>
  <div class="container mt-4 profile">
    <div class="card">
      <div class="card-header">
        <h1 class="card-title">{{ user?.username }}님의 프로필 페이지</h1>
      </div>
      <div class="card-body">
        <div v-if="user">
          <p>회원번호: {{ user.id }}</p>
          <p>ID: {{ user.username }}</p>
          <p>Email: <input v-model="user.email" class="form-control" /></p>
          <p>나이: <input v-model="user_info.age" class="form-control" /></p>
          <p>현재 가진 금액: <input v-model="user_info.current_balance" class="form-control" /></p>
          <p>연봉: <input v-model="user_info.annual_salary" class="form-control" /></p>
          <p>
            <label for="bank">주 이용은행:</label>
            <select id="bank" v-model="user_info.bank" class="form-select">
              <option value="우리은행">우리은행</option>
              <option value="신한은행">신한은행</option>
              <option value="하나은행">하나은행</option>
              <option value="국민은행">KB국민은행</option>
              <option value="중소기업은행">IBK기업은행</option>
              <option value="토스뱅크 주식회사">토스뱅크</option>
              <option value="농협은행주식회사">농협</option>
              <option value="수협은행">수협</option>
              <option value="경남은행">경남은행</option>
              <option value="광주은행">광주은행</option>
              <option value="부산은행">부산은행</option>
              <option value="전북은행">전북은행</option>
              <option value="제주은행">제주은행</option>
              <option value="주식회사 카카오뱅크">카카오뱅크</option>
              <option value="주식회사 케이뱅크">케이뱅크</option>
              <option value="한국스탠다드차타드은행">한국스탠다드차타드은행</option>
              <option value="한국산업은행">한국산업은행</option>
            </select>
          </p>
          <button @click="updateProfile" class="btn btn-primary">수정하기</button>
        </div>
      </div>
      <div class="card-footer" v-if="user && user_info.saving_options && user_info.deposit_options">
        <h2>가입한 상품들</h2>
        <br>
        <div class="product-chart-row">
          <div class="product-section">
            <h3>가입한 예금</h3>
            <br>
            <div class="product-list">
              <div v-for="product in user_info.deposit_options" :key="product.id" class="product-card">
                <p><strong>{{ product.product }}</strong> - {{ product.save_trm }}개월</p>
              </div>
            </div>
          </div>
          <div class="bar-chart">
            <h3>예금 금리 비교</h3>
            <BarChart :chartData="depositChartData" />
          </div>
        </div>
        <br>
        <div class="product-chart-row">
          <div class="product-section">
            <h3>가입한 적금</h3>
            <br>
            <div class="product-list">
              <div v-for="product in user_info.saving_options" :key="product.id" class="product-card">
                <p><strong>{{ product.product }}</strong> - {{ product.save_trm }}개월</p>
              </div>
            </div>
          </div>
          <div class="bar-chart">
            <h3>적금 금리 비교</h3>
            <BarChart :chartData="savingChartData" />
          </div>
        </div>
        <div v-if="user_info.saving_options.length === 0 && user_info.deposit_options.length === 0">
          <p>가입한 상품이 없습니다.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/users';
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import BarChart from '@/components/BarChart.vue';

const user = ref(null);
const user_info = ref(null);
const store = useUserStore();
const router = useRouter();
const savingChartData = ref(null);
const depositChartData = ref(null);

const loadUserProfile = async () => {
  const profile = await store.getProfile();
  user.value = profile;
  user_info.value = profile.user_info;
  console.log(user_info.value)
  if (user_info.value.saving_options.length) {
    savingChartData.value = {
      labels: user_info.value.saving_options.map(option => `${option.product} (${option.save_trm}개월)`),
      datasets: [{
        label: '적금 금리',
        data: user_info.value.saving_options.map(option => option.intr_rate),
        backgroundColor: 'rgba(75, 192, 192, 1)', // Make bars fully opaque
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
        barPercentage: 0.5
      }]
    };
  }

  
  if (user_info.value.deposit_options.length) {
    depositChartData.value = {
      labels: user_info.value.deposit_options.map(option => `${option.product} (${option.save_trm}개월)`),
      datasets: [{
        label: '예금 금리',
        data: user_info.value.deposit_options.map(option => option.intr_rate),
        backgroundColor: 'rgba(54, 162, 235, 1)', // Make bars fully opaque
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1,
        barPercentage: 0.5
      }]
    };
  }
};

const updateProfile = async () => {
  try {
    const authToken = store.token;
    const userResponse = await axios.put('http://127.0.0.1:8000/api/v1/accounts/profile/update-profile/', {
      email: user.value.email,
    }, {
      headers: {
        'Authorization': `token ${authToken}`
      }
    });

    const userInfoResponse = await axios.put('http://127.0.0.1:8000/api/v1/accounts/profile/update-info/', user_info.value, {
      headers: {
        'Authorization': `token ${authToken}`
      }
    });

    user.value = userResponse.data;
    user_info.value = userInfoResponse.data;
    alert('프로필이 성공적으로 업데이트되었습니다.');
    router.push({ name: 'home' });
  } catch (error) {
    console.error('프로필 업데이트 중 오류가 발생했습니다:', error);
    alert('프로필 업데이트 중 오류가 발생했습니다.');
  }
};

onMounted(() => {
  loadUserProfile();
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

body {
  font-family: 'Montserrat', sans-serif;
  background: #f4f4f9;
  color: #333;
  margin: 0;
  padding: 0;
}

.profile {
  background: linear-gradient(to bottom right, #e0f7fa, #ffffff);
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  margin: 20px;
  position: relative;
  z-index: 1;
}

h1 {
  color: white;
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 20px;
}

.card {
  border: none;
  border-radius: 15px;
  overflow: hidden;
}

.card-header {
  background: linear-gradient(to right, #0f4c75, #3282b8);
  color: white;
  padding: 20px;
  text-align: center;
}

.card-title {
  margin: 0;
  font-size: 24px;
}

.card-body {
  padding: 20px;
  background: white;
  border-top: 1px solid #3282b8;
}

.card-footer {
  background: white;
  padding: 20px;
}

.form-control, .form-select {
  padding: 10px;
  margin-top: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.form-control:focus, .form-select:focus {
  border-color: #0f4c75;
  box-shadow: 0 0 8px rgba(15, 76, 117, 0.1);
}

.btn-primary {
  background: linear-gradient(135deg, #0f4c75, #3282b8, #bbe1fa);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 30px;
  cursor: pointer;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.btn-primary:hover {
  background-color: #3282b8;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.product-chart-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-top: 20px;
  flex-wrap: wrap;
}

.product-section {
  flex: 1;
  max-width: 50%;
}

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.product-card {
  background: white;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  flex: 1 1 calc(50% - 20px);
  box-sizing: border-box;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.product-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.product-card p {
  margin: 0;
  color: #333;
}

.bar-chart {
  flex: 1;
  background: white;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-left: 20px;
  max-width: 800px;
}

h2, h3 {
  color: #0f4c75;
  font-weight: bold;
}

.container {
  max-width: 1200px;
  margin: auto;
  padding: 20px;
}

.mt-4 {
  margin-top: 1.5rem !important;
}
</style>
