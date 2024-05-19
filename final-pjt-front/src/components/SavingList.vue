<template>
  <table>
    <thead>
      <tr>
        <th>공시 제출월</th>
        <th>금융회사명</th>
        <th>상품명</th>
        <th>6개월</th>
        <th>12개월</th>
        <th>24개월</th>
        <th>36개월</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="saving in savings" :key="saving.id" @click="selectSaving(saving.id)">
        <td>{{ saving.pub_month }}</td>
        <td>{{ saving.kor_co_nm }}</td>
        <td>{{ saving.fin_prdt_nm }}</td>
        <td>{{ getRate(saving, 6) }}</td>
        <td>{{ getRate(saving, 12) }}</td>
        <td>{{ getRate(saving, 24) }}</td>
        <td>{{ getRate(saving, 36) }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    savings: Array
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
