<template>
  <div>
    <h1>환율 계산기</h1>
    <div v-if="error">{{ error }}</div>
    <div v-else>
      <div>
        <label for="currency">국가:</label>
        <select v-model="selectedCurrency" @change="calculateFromKRW" id="currency">
          <option v-for="rate in exchangeRates" :key="rate.currency" :value="rate.rate">
            {{ rate.currency }}
          </option>
        </select>
      </div>
      <div>
        <label for="krwAmount">원화 입력:</label>
        <input type="number" v-model="krwAmount" @input="calculateFromKRW" id="krwAmount" />
      </div>
      <div>
        <label for="foreignAmount">타국 통화 입력:</label>
        <input type="number" v-model="foreignAmount" @input="calculateFromForeign" id="foreignAmount" />
      </div>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      krwAmount: 0,
      foreignAmount: 0,
      selectedCurrency: null,
      selectedCurrencyName: '',
      exchangeRates: [],
      error: null,
    };
  },
  created() {
    this.fetchExchangeRates();
  },
  methods: {
    async fetchExchangeRates() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/v1/exchange/rate/');
        this.exchangeRates = response.data;
        if (this.exchangeRates.length > 0) {
          this.selectedCurrency = this.exchangeRates[0].rate;
          this.selectedCurrencyName = this.exchangeRates[0].currency;
        }
      } catch (error) {
        this.error = 'Failed to fetch exchange rates.';
      }
    },
    calculateFromKRW() {
      if (this.selectedCurrency && this.krwAmount >= 0) {
        this.foreignAmount = (this.krwAmount / this.selectedCurrency).toFixed(2);
      } else {
        this.foreignAmount = 0;
      }
    },
    calculateFromForeign() {
      if (this.selectedCurrency && this.foreignAmount >= 0) {
        this.krwAmount = (this.foreignAmount * this.selectedCurrency).toFixed(2);
      } else {
        this.krwAmount = 0;
      }
    },
    updateSelectedCurrency(event) {
      const selected = this.exchangeRates.find(rate => rate.rate == event.target.value);
      this.selectedCurrencyName = selected.currency;
      this.calculateFromKRW();
    }
  },
  watch: {
    selectedCurrency() {
      this.calculateFromKRW();
    }
  }
};
</script>

<style scoped>
/* Add styles to match the design */
h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

div {
  margin-bottom: 10px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

select {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

h2 {
  margin-top: 20px;
  font-size: 20px;
}
</style>
