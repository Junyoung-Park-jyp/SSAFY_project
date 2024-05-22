<template>
  <div v-if="depositDetail" class="container deposit-detail">
    <h1 class="title">{{ depositDetail.fin_prdt_nm }}</h1>
    <div class="bank-info">
      <p><strong>은행:</strong> {{ depositDetail.kor_co_nm }}</p>
    </div>
    <table class="table table-hover table-striped">
      <thead class="table-dark">
        <tr>
          <th>가입 기간</th>
          <th>금리</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="option in depositDetail.options" :key="option.save_trm">
          <td>{{ option.save_trm }}개월 <button @click="addDeposit(option.id)" class="btn" style="color: white; background-color: #004080;">가입하기</button></td>
          <td>{{ option.intr_rate }}%</td>
        </tr>
      </tbody>
    </table>
    <div class="note">
      <p><strong>특이사항:</strong> {{ depositDetail.etc_note }}</p>
    </div>
    <br>
    
  </div> 
  <div v-else class="loading">
    <p>Loading...</p>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useProductStore } from '@/stores/products';
import { useUserStore } from '@/stores/users';
import axios from 'axios';
export default {
  setup() {
    const route = useRoute();
    const productStore = useProductStore();
    const userStore = useUserStore();
    const token = userStore.token
    const depositDetail = ref(null);
    onMounted(() => {
      const id = route.params.id;
      depositDetail.value = productStore.deposits.find(deposit => deposit.id === Number(id));
    });
    const addDeposit = function(pk) {
      axios({
        method: 'put',
        url: 'http://127.0.0.1:8000/api/v1/accounts/add-deposit/',
        data:{
          pk : pk
        },
        headers: {
          Authorization: `token ${token}`
        }
      })
      .then((res) => {
        alert(`${depositDetail.value.fin_prdt_nm}상품 가입이 완료되었습니다!`)
      })
      .catch(err => console.log(err))
    }
    return { depositDetail, addDeposit };
  }
};
</script>

<style scoped>
.container {
  background: white;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  margin-top: 40px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  transition: all 0.3s ease;
}

.title {
  color: #004080;
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 30px;
  text-align: center;
}

.bank-info {
  margin-bottom: 20px;
  font-size: 18px;
}

.table {
  width: 100%;
  margin-top: 20px;
  border-collapse: collapse;
}

.table th,
.table td {
  padding: 15px;
  text-align: left;
}

.table-hover tbody tr:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

.table-striped tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.03);
}

.table-dark thead th {
  background-color: #004080;
  color: white;
}

.note {
  margin-top: 30px;
  font-size: 16px;
  background: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  border-left: 5px solid #004080;
}

.loading {
  text-align: center;
  font-size: 20px;
  color: #666;
  margin-top: 40px;
}
</style>
