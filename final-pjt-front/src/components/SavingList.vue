<template>
  <div class="table-responsive">
    <table class="table table-bordered table-hover">
      <thead class="table-light">
        <tr>
          <th>공시 제출월</th>
          <th>금융회사명</th>
          <th>상품명</th>
          <th v-for="term in terms" :key="term">{{ term }}개월</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="saving in savings" :key="saving.id" @click="selectSaving(saving.id)">
          <td>{{ saving.pub_month }}</td>
          <td>{{ saving.kor_co_nm }}</td>
          <td>{{ saving.fin_prdt_nm }}</td>
          <td v-for="term in terms" :key="term">{{ getRate(saving, term) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    savings: Array,
    terms: Array  // 추가된 부분: 표시할 기간을 받는 prop
  },
  emits: ['selectSaving'],
  methods: {
    selectSaving(id) {
      this.$emit('selectSaving', id);
    },
    getRate(saving, term) {
      if (!saving.options) return '-';
      const option = saving.options.find(opt => opt.save_trm === term);
      return option ? option.intr_rate : '-';
    }
  }
};
</script>
