<template>
  <div class="table-responsive">
    <table class="table table-bordered table-hover">
      <thead class="table-light">
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
        <tr v-for="deposit in deposits" :key="deposit.id" @click="selectDeposit(deposit.id)">
          <td>{{ deposit.pub_month }}</td>
          <td>{{ deposit.kor_co_nm }}</td>
          <td>{{ deposit.fin_prdt_nm }}</td>
          <td>{{ getRate(deposit, 6) }}</td>
          <td>{{ getRate(deposit, 12) }}</td>
          <td>{{ getRate(deposit, 24) }}</td>
          <td>{{ getRate(deposit, 36) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    deposits: Array
  },
  emits: ['selectDeposit'],
  methods: {
    selectDeposit(id) {
      this.$emit('selectDeposit', id);
    },
    getRate(deposit, term) {
      if (!deposit.options) return '-';
      const option = deposit.options.find(opt => opt.save_trm === term);
      return option ? option.intr_rate : '-';
    }
  }
};
</script>
