<template>
  <div v-if="savingDetail">
    <h1>{{ savingDetail.fin_prdt_nm }}</h1>
    <p>은행: {{ savingDetail.kor_co_nm }}</p>
    <table>
      <thead>
        <tr>
          <th>가입 기간</th>
          <th>금리</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="option in savingDetail.options" :key="option.save_trm">
          <td>{{ option.save_trm }}개월</td>
          <td>{{ option.intr_rate }}%</td>
        </tr>
      </tbody>
    </table>
    <p>특이사항: {{ savingDetail.etc_note }}</p>
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
    const savingDetail = ref(null);

    onMounted(() => {
      const id = route.params.id;
      savingDetail.value = productStore.savings.find(saving => saving.id === Number(id));
    });

    return { savingDetail };
  }
};
</script>
