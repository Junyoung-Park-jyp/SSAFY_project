<template>
  <div class="container mt-4 deposit">
    <h1>정기예금</h1>
    <div class="filters">
      <div class="mb-3">
        <label for="bank" class="form-label">은행 선택:</label>
        <select id="bank" v-model="selectedBank" @change="filterProducts" class="form-select">
          <option value="">전체 은행</option>
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
    
      <div class="mb-3">
        <label for="term" class="form-label">예치 기간 선택:</label>
        <select id="term" v-model="selectedTerm" @change="filterProducts" class="form-select">
          <option value="">전체 기간</option>
          <option value="6">6개월</option>
          <option value="12">12개월</option>
          <option value="24">24개월</option>
          <option value="36">36개월</option>
        </select>
      </div>
    </div>
    <DepositList :deposits="filteredDeposits" :terms="terms" @selectDeposit="viewDepositDetail" />
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useProductStore } from '@/stores/products';
import DepositList from '@/components/DepositList.vue';

export default {
  components: { DepositList },
  setup() {
    const productStore = useProductStore();
    const router = useRouter();
    const selectedBank = ref('');
    const selectedTerm = ref('');
    
    const filteredDeposits = computed(() => {
      return productStore.deposits.filter(deposit => {
        const matchesBank = !selectedBank.value || deposit.kor_co_nm === selectedBank.value;
        const matchesTerm = !selectedTerm.value || (deposit.options && deposit.options.some(option => option.save_trm === Number(selectedTerm.value)));
        return matchesBank && matchesTerm;
      });
    });

    const terms = computed(() => {
      if (selectedTerm.value) {
        return [Number(selectedTerm.value)];
      } else {
        return [6, 12, 24, 36];  // 표시할 기간 목록
      }
    });

    const filterProducts = () => {
      productStore.getDeposits();
    };

    const viewDepositDetail = (id) => {
      router.push({ name: 'depositDetail', params: { id } });
    };

    onMounted(() => {
      productStore.getDeposits();
    });

    return { selectedBank, selectedTerm, filteredDeposits, terms, filterProducts, viewDepositDetail };
  }
};
</script>

<style scoped>
.deposit {
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

.filters {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
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
</style>
