<template>
  <div class="container mt-4 profile">
    <div class="card">
      <div class="card-header">
        <h1 class="card-title" style="color:white">{{ user?.username }}님의 프로필 페이지</h1>
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
              <option value="kb국민은행">KB국민은행</option>
              <option value="ibk기업은행">IBK기업은행</option>
              <option value="토스뱅크">토스뱅크</option>
              <option value="농협">농협</option>
              <option value="수협">수협</option>
              <option value="경남은행">경남은행</option>
              <option value="광주은행">광주은행</option>
              <option value="부산은행">부산은행</option>
              <option value="전북은행">전북은행</option>
              <option value="제주은행">제주은행</option>
              <option value="카카오뱅크">카카오뱅크</option>
              <option value="케이뱅크">케이뱅크</option>
              <option value="스탠다드차타드">한국스탠다드차타드은행</option>
              <option value="산업은행">한국산업은행</option>
            </select>
          </p>
          <button @click="updateProfile" class="btn btn-primary">수정하기</button>
        </div>
      </div>
      <div class="card-footer" v-if="user && user_info.saving_options && user_info.deposit_options">
        <h2>가입한 상품들</h2>
        <div class="product-list">
          <div v-for="product in user_info.saving_options" :key="product.id" class="product-card">
            <p><strong>{{ product.product }}</strong> - {{ product.save_trm }}개월</p>
          </div>
          <div v-for="product in user_info.deposit_options" :key="product.id" class="product-card">
            <p><strong>{{ product.product }}</strong> - {{ product.save_trm }}개월</p>
          </div>
        </div>
        <br>
        <div v-if="savingChartData || depositChartData">
          <div v-if="depositChartData">
            <h3>예금 금리 비교</h3>
            <LineChart :chartData="depositChartData" />
          </div>
          <br>
          <div v-if="savingChartData">
            <h3>적금 금리 비교</h3>
            <LineChart :chartData="savingChartData" />
          </div>
        </div>
        <div v-else>
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
import LineChart from '@/components/LineChart.vue';

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
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
      }]
    };
  }

  
  if (user_info.value.deposit_options.length) {
    depositChartData.value = {
      labels: user_info.value.deposit_options.map(option => `${option.product} (${option.save_trm}개월)`),
      datasets: [{
        label: '예금 금리',
        data: user_info.value.deposit_options.map(option => option.intr_rate),
        backgroundColor: 'rgba(153, 102, 255, 0.2)',
        borderColor: 'rgba(153, 102, 255, 1)',
        borderWidth: 1
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
  background-color: #0f4c75;
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

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.product-card {
  background: white;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  flex: 1 1 calc(30% - 40px);
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

h2, h3 {
  color: #0f4c75;
  font-weight: bold;
}

.line-chart {
  background: white;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px 0;
}

.container {
  max-width: 1200px;
  margin: auto;
  padding: 20px;
}

.mt-4 {
  margin-top: 1.5rem !important;
}

/* Navbar */
.navbar {
  background: linear-gradient(to right, #0f4c75, #3282b8);
  padding: 20px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  font-family: 'Montserrat', sans-serif;
  border-bottom: 4px solid #3282b8;
}

.nav-logo {
  width: 60px;
  height: auto;
  margin-right: 15px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 2px solid #fff;
  border-radius: 50%;
}

.nav-logo:hover {
  transform: scale(1.2);
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
}

.navbar-brand {
  display: flex;
  align-items: center;
  font-size: 28px;
  font-weight: bold;
  color: white;
  text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.5);
}

.nav-link {
  color: white !important;
  margin: 0 15px;
  position: relative;
  padding: 5px 0;
  font-weight: 700;
  transition: color 0.3s ease, transform 0.3s ease;
}

.nav-link::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #ffffff;
  transition: width 0.3s ease;
}

.nav-link:hover::after {
  width: 100%;
}

.nav-link:hover {
  color: #ffd700 !important;
  transform: scale(1.1);
}

.nav-link.btn {
  background: none;
  border: 2px solid white;
  color: white;
  cursor: pointer;
  padding: 5px 20px;
  transition: background-color 0.3s ease, color 0.3s ease, box-shadow 0.3s ease;
  border-radius: 30px;
}

.nav-link.btn:hover {
  color: #0f4c75;
  background-color: #ffffff;
  box-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
}

.nav-link.btn:active {
  background-color: rgba(255, 255, 255, 0.2);
}

@media (max-width: 768px) {
  .navbar-brand {
    font-size: 22px;
  }

  .nav-link {
    margin: 10px 0;
  }
}

.nav-item.active .nav-link {
  color: #ffd700 !important;
}

.navbar-nav.ml-auto {
  display: flex;
  align-items: center;
}

.navbar-collapse {
  justify-content: flex-end;
}

@keyframes navLinkGlow {
  0% {
    text-shadow: 0 0 5px rgba(255, 215, 0, 0.5);
  }
  50% {
    text-shadow: 0 0 20px rgba(255, 215, 0, 1);
  }
  100% {    text-shadow: 0 0 5px rgba(255, 215, 0, 0.5);
  }
}

.navbar-brand:hover {
  animation: navLinkGlow 1s infinite;
}

.nav-link.active {
  color: #ffd700 !important;
}

.nav-link.active::after {
  width: 100%;
}

/* Slideshow */
.hero {
  position: relative;
  width: 100%;
  height: 400px;
  overflow: hidden;
  background: linear-gradient(to right, #0f4c75, #3282b8);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  border-radius: 15px;
}

.slideshow-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.slideshow {
  display: flex;
  width: 100%;
  animation: slide 16s infinite;
}

.slide {
  width: 100%;
  flex-shrink: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.slide img {
  width: 100%;
  height: auto;
  object-fit: cover;
  border-radius: 15px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
}

@keyframes slide {
  0%, 12.5%, 100% {
    transform: translateX(0%);
  }
  12.51%, 25% {
    transform: translateX(-100%);
  }
  25.01%, 37.5% {
    transform: translateX(-200%);
  }
  37.51%, 50% {
    transform: translateX(-300%);
  }
  50.01%, 62.5% {
    transform: translateX(-400%);
  }
  62.51%, 75% {
    transform: translateX(-500%);
  }
  75.01%, 87.5% {
    transform: translateX(-600%);
  }
  87.51%, 100% {
    transform: translateX(-700%);
  }
}

/* Features */
.features {
  display: flex;
  justify-content: space-around;
  padding: 60px 20px;
  flex-wrap: wrap;
  background: #e0f7fa;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
  margin-top: -30px;
  position: relative;
  z-index: 1;
}

.feature {
  background: white;
  padding: 30px;
  margin: 10px;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  flex: 1 1 calc(30% - 20px);
  transition: transform 0.3s, box-shadow 0.3s;
}

.feature:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.feature h2 {
  margin-top: 0;
  font-size: 28px;
  color: #0f4c75;
}

.feature p {
  font-size: 18px;
  color: #555;
}

/* Footer */
.footer {
  background: #0f4c75;
  color: white;
  padding: 20px;
  text-align: center;
  position: relative;
  width: 100%;
  bottom: 0;
  box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.2);
  margin-top: 40px;
}

/* Chatbot */
.chatbot {
  position: fixed;
  bottom: 80px;
  right: 20px;
  z-index: 1000;
}

.chatbot-toggle {
  background: linear-gradient(to right, #3282b8, #bbe1fa);
  color: white;
  border: none;
  border-radius: 50%;
  padding: 15px;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.chatbot-toggle img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 50%;
}

.chatbot-toggle:hover {
  transform: scale(1.1);
  background-color: #3282b8;
}

.chatbot-window {
  position: fixed;
  bottom: 120px;
  right: 20px;
  width: 350px;
  max-height: 500px;
  background: white;
  border-radius: 15px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.chatbot-header {
  background: #3282b8;
  color: white;
  padding: 10px;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chatbot-messages {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
  background: #f4f4f9;
}

.user-msg {
  text-align: right;
  margin-bottom: 10px;
}

.bot-msg {
  text-align: left;
  margin-bottom: 10px;
}

.user-msg p, .bot-msg p {
  background: #e0f7fa;
  padding: 10px;
  border-radius: 15px;
  display: inline-block;
  max-width: 80%;
}

form {
  display: flex;
  border-top: 1px solid #ccc;
  background: white;
  padding: 10px;
}

input {
  flex: 1;
  padding: 10px;
  border: none;
  border-radius: 20px;
  margin-right: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

button {
  background: #3282b8;
  color: white;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
  border-radius: 20px;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

button:hover {
  background-color: #0f4c75;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>


