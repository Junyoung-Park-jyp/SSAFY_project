<template>
  <div v-if="depositDetail">
    <h1>{{ depositDetail.fin_prdt_nm }}</h1>
    <p>은행: {{ depositDetail.kor_co_nm }}</p>
    <table>
      <thead>
        <tr>
          <th>가입 기간</th>
          <th>금리</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="option in depositDetail.options" :key="option.save_trm">
          <td>{{ option.save_trm }}개월</td>
          <td>{{ option.intr_rate }}%</td>
        </tr>
      </tbody>
    </table>
    <p>특이사항: {{ depositDetail.etc_note }}</p>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useProductStore } from '@/stores/products';

export default {
  setup() {
    const route = useRoute();
    const productStore = useProductStore();
    const depositDetail = ref(null);

    onMounted(() => {
      const id = route.params.id;
      depositDetail.value = productStore.deposits.find(deposit => deposit.id === Number(id));
    });

    return { depositDetail };
  }
};
</script>
