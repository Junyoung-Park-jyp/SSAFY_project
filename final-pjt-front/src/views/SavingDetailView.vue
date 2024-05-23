<template>
  <div v-if="savingDetail" class="container saving-detail">
    <h1 class="title">{{ savingDetail.fin_prdt_nm }}</h1>
    <div class="bank-info">
      <p><strong>은행:</strong> {{ savingDetail.kor_co_nm }}</p>
    </div>
    <table class="table table-hover table-striped">
      <thead class="table-dark">
        <tr>
          <th>가입 기간</th>
          <th>금리</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="option in uniqueOptions" :key="option.save_trm">
          <td>{{ option.save_trm }}개월 <button v-if="isLogin" @click="addSaving(option)" class="btn" style="color: white; background-color: #004080; ">가입하기</button></td>
          <td>{{ option.intr_rate }}%</td>
        </tr>
      </tbody>
    </table>
    <div class="note">
      <p><strong>특이사항:</strong> {{ savingDetail.etc_note }}</p>
    </div>
    <br>
    
  </div>
  <div v-else class="loading">
    <p>Loading...</p>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useProductStore } from '@/stores/products';
import { useUserStore } from '@/stores/users';
import axios from 'axios';

export default {
  setup() {
    const route = useRoute();
    const productStore = useProductStore();
    const userStore = useUserStore();
    const isLogin = ref(userStore.isLogin);
    const updateIsLogin = computed(() => userStore.isLogin);
    updateIsLogin.value = userStore.isLogin;
    const token = userStore.token
    const savingDetail = ref(null);
    onMounted(() => {
      const id = route.params.id;
      savingDetail.value = productStore.savings.find(saving => saving.id === Number(id));
    });

    const uniqueOptions = computed(() => {
      if (!savingDetail.value) return [];
      const options = savingDetail.value.options.reduce((acc, option) => {
        if (!acc.some(o => o.save_trm === option.save_trm)) {
          acc.push(option);
        }
        return acc;
      }, []);
      return options.sort((a, b) => a.save_trm - b.save_trm);
    });

    const addSaving = function(option){
      axios({
        method: 'put',
        url: 'http://127.0.0.1:8000/api/v1/accounts/add-saving/',
        data:{
          pk : option.id
        },
        headers: {
          Authorization: `token ${token}`
        }
      })
      .then((res) => {
        alert(`${savingDetail.value.fin_prdt_nm}상품 가입이 완료되었습니다!`)
      })
      .catch(err => console.log(err))
    }

    return { savingDetail, uniqueOptions, addSaving, isLogin };
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
