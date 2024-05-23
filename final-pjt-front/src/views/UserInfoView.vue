<template>
  <div class="container mt-4 userinfo">
    <div class="card">
      <div class="card-header">
        <h1 class="card-title" style="color:white;">{{ username }}님 가입을 환영합니다!</h1>
      </div>
      <div class="card-body">
        <form @submit.prevent="UserInfo">
          <div class="mb-3">
            <label for="current_balance" class="form-label">현재 가진 금액:</label>
            <input type="number" id="current_balance" class="form-control" v-model.trim="current_balance">
          </div>
          <div class="mb-3">
            <label for="annual_salary" class="form-label">연봉:</label>
            <input type="number" id="annual_salary" class="form-control" v-model.trim="annual_salary">
          </div>
          <div class="mb-3">
            <label for="age" class="form-label">나이:</label>
            <input type="number" id="age" class="form-control" v-model.trim="age">
          </div>
          <div class="mb-3">
            <label for="bank" class="form-label">이용하시는 은행을 고르세요:</label>
            <select id="bank" class="form-select" v-model="bank">
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
          </div>
          <button type="submit" class="btn btn-primary">회원가입 완료</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { ref } from 'vue'
import { useUserStore } from '@/stores/users'
import { storeToRefs } from 'pinia'

const age = ref(null)
const bank = ref(null)
const current_balance = ref(null)
const annual_salary = ref(null)
const store = useUserStore()
const route = useRoute()
const username = route.params.username

const UserInfo = function(){
  const payload = {
      username: username,
      age: age.value,
      bank: bank.value,
      current_balance: current_balance.value,
      annual_salary: annual_salary.value,
    }
  console.log(payload)
  store.UserInfo(payload)
}

</script>
<script>
export default {
  name: 'UserInfo',
  beforeRouteLeave(to, from, next) {
    const confirmMessage = "상세 정보를 입력하지 않으면 추천이 제대로 이루어지지 않을 수 있습니다.";
    if (this.isSubmitting) {
      next(); // Form is being submitted, allow navigation
    } else if (window.confirm(confirmMessage)) {
      next(); // '예'를 누르면 페이지를 떠납니다.
    } else {
      next(false); // '아니오'를 누르면 페이지를 떠나지 않습니다.
    }
  },
};
</script>

<style scoped>
.userinfo {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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

.form-label {
  font-size: 16px;
  color: #555;
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
  padding: 10px 20px;
  background-color: #002b5c;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #005c99;
}
</style>
