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
          <td>{{ option.save_trm }}개월</td>
          <td>{{ option.intr_rate }}%</td>
        </tr>
      </tbody>
    </table>
    <div class="note">
      <p><strong>특이사항:</strong> {{ savingDetail.etc_note }}</p>
    </div>
    <button class="btn btn-primary">가입하기</button>
  </div>
  <div v-else class="loading">
    <p>Loading...</p>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useProductStore } from '@/stores/products';

export default {
  setup() {
    const route = useRoute();
    const productStore = useProductStore();
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

    return { savingDetail, uniqueOptions };
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
