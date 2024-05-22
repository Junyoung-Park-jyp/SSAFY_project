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
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/users';
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'

const user = ref(null);
const user_info = ref(null);
const store = useUserStore();
const router = useRouter()
const loadUserProfile = async () => {
  const profile = await store.getProfile();
  user.value = profile;
  user_info.value = profile.user_info;
};

const updateProfile = async () => {
  try {
    // 인증 토큰
    const authToken = store.token

    // 프로필 업데이트 요청
    const userResponse = await axios.put('http://127.0.0.1:8000/api/v1/accounts/profile/update-profile/', {
      email: user.value.email,
    }, {
      headers: {
        'Authorization': `token ${authToken}` // 인증 토큰을 헤더에 추가합니다.
      }
    });

    // 유저 정보 업데이트 요청
    const userInfoResponse = await axios.put('http://127.0.0.1:8000/api/v1/accounts/profile/update-info/', user_info.value, {
      headers: {
        'Authorization': `token ${authToken}` // 인증 토큰을 헤더에 추가합니다.
      }
    });

    // 응답 처리
    user.value = userResponse.data;
    user_info.value = userInfoResponse.data;
    alert('프로필이 성공적으로 업데이트되었습니다.');
    router.push({name: 'home'})

  } catch (error) {
    console.error('프로필 업데이트 중 오류가 발생했습니다:', error);
    alert('프로필 업데이트 중 오류가 발생했습니다.');
  }
};


onMounted(() => {
  loadUserProfile()
})

</script>

<style scoped>
.profile {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  color: #002b5c;
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 20px;
}

.card {
  border: none;
  border-radius: 10px;
  overflow: hidden;
}

.card-header {
  background: #002b5c;
  color: white;
  padding: 20px;
}

.card-title {
  margin: 0;
  font-size: 24px;
}

.card-body {
  padding: 20px;
}

.card-footer {
  background: #f0f0f0;
  padding: 20px;
}

.form-control, .form-select {
  padding: 10px;
  margin-top: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.btn-primary {
  background-color: #002b5c;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #005c99;
}

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.product-card {
  background: white;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  flex: 1 1 calc(100% - 20px);
  box-sizing: border-box;
  margin: 10px 0;
}

.product-card p {
  margin: 0;
}
</style>
