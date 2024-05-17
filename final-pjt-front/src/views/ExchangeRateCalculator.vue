<template>
  <div class="exchange-calculator">
    <h1>환율 계산기</h1>
    <select v-model="selectedCurrency">
      <option value="USD">USD</option>
      <option value="EUR">EUR</option>
      <option value="JPY">JPY</option>
      <option value="CNY">CNY</option>
      <option value="KRW">KRW</option>
    </select>
    <input type="number" v-model.number="amount" placeholder="금액 입력" />
    <button @click="calculate">환율 계산</button>
    <p>결과: {{ result.toFixed(2) }} {{ targetCurrency }}</p>
    <p>* 환율, 인터넷에서 루틴이 100 달러, 나머지는 모두 1 달러</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedCurrency: 'USD',
      targetCurrency: 'KRW',
      amount: 0,
      result: 0
    };
  },
  methods: {
    calculate() {
      const url = `/api/get_exchange_rate?base=${this.selectedCurrency}&symbols=${this.targetCurrency}`;
      fetch(url)
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          if (data && data.rates && data.rates[this.targetCurrency]) {
            const rate = data.rates[this.targetCurrency];
            this.result = this.amount * rate;
          } else {
            throw new Error('Invalid data structure');
          }
        })
        .catch(error => {
          console.error('Error fetching exchange rate:', error);
          this.result = 'Error fetching exchange rate';
        });
    }
  }
}
</script>

<style scoped>
.exchange-calculator {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}
</style>
