<template>
  <div>
    <h1>정기적금</h1>
    <label for="bank">은행 선택:</label>
    <select id="bank" v-model="selectedBank" @change="filterProducts">
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
    
    <label for="term">예치 기간 선택:</label>
    <select id="term" v-model="selectedTerm" @change="filterProducts">
      <option value="">전체 기간</option>
      <option value="1">1개월</option>
      <option value="3">3개월</option>
      <option value="6">6개월</option>
      <option value="12">12개월</option>
      <option value="24">24개월</option>
      <option value="36">36개월</option>
    </select>
    
    <SavingList :savings="filteredSavings" :terms="terms" @selectSaving="viewSavingDetail" />
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useProductStore } from '@/stores/products';
import SavingList from '@/components/SavingList.vue';

export default {
  components: { SavingList },
  setup() {
    const productStore = useProductStore();
    const router = useRouter();
    const selectedBank = ref('');
    const selectedTerm = ref('');
    
    const filteredSavings = computed(() => {
      return productStore.savings.filter(saving => {
        const matchesBank = !selectedBank.value || saving.kor_co_nm === selectedBank.value;
        const matchesTerm = !selectedTerm.value || (saving.options && saving.options.some(option => option.save_trm === Number(selectedTerm.value)));
        return matchesBank && matchesTerm;
      });
    });

    const terms = computed(() => {
      if (selectedTerm.value) {
        return [Number(selectedTerm.value)];
      } else {
        return [1, 3, 6, 12, 24, 36];
      }
    });

    const filterProducts = () => {
      productStore.getSavings();
    };

    const viewSavingDetail = (id) => {
      router.push({ name: 'savingDetail', params: { id } });
    };

    onMounted(() => {
      productStore.getSavings();
    });

    return { selectedBank, selectedTerm, filteredSavings, terms, filterProducts, viewSavingDetail };
  }
};
</script>
