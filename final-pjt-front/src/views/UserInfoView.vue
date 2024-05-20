<template>
  <div>
    <h1>{{ username }}님 가입을 환영합니다! </h1>
    <form @submit.prevent="UserInfo">
      <p>
        <label for="current_balance">현재 가진 금액:</label>
        <input type="number" id="current_balance" v-model.trim="current_balance">
      </p>
      <p>
        <label for="annual_salary">연봉:</label>
        <input type="number" id="annual_salary" v-model.trim="annual_salary">
      </p>
      <p>
        <label for="age">나이:</label>
        <input type="number" id="age" v-model.trim="age">
      </p>
      <p>
        <label for="bank">이용하시는 은행을 고르세요:</label>
        <select id="bank" v-model="bank">
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
      <input type="submit">
    </form>
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
      email: email.value
    }
  console.log(payload)
  store.UserInfo(payload)
}

</script>

<style scoped>

</style>