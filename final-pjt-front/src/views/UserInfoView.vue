<template>
<div class="container mt-4">
    <div class="card">
      <div class="card-header">
        <h1 class="card-title">{{ username }}님 가입을 환영합니다!</h1>
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
          </div>
          <button type="submit" class="btn btn-primary">회원가입 완료</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
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

<style scoped>

</style>
