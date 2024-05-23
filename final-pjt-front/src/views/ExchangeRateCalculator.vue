<template>
  <div class="container exchange-rate">
    <h1>환율 계산기</h1>
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <div v-else>
      <div class="form-group">
        <label for="currency" class="form-label">국가:</label>
        <select v-model="selectedCurrency" @change="updateSelectedCurrency" id="currency" class="form-control">
          <option v-for="rate in exchangeRates" :key="rate.currency" :value="rate.rate">
            {{ rate.currency }} ({{ rate.country_name_ko }} / {{ rate.country_name_en }})
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="krwAmount" class="form-label">원화 입력:</label>
        <input type="number" v-model="krwAmount" @input="calculateFromKRW" id="krwAmount" class="form-control" />
      </div>
      <div class="form-group">
        <label for="foreignAmount" class="form-label">타국 통화 입력:</label>
        <input type="number" v-model="foreignAmount" @input="calculateFromForeign" id="foreignAmount" class="form-control" />
      </div>
      <div class="result-group">
        <p><strong>환율 계산 결과:</strong></p>
        <p>{{ krwAmount }} KRW = {{ foreignAmount }} {{ selectedCurrencyName }}</p>
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
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

.exchange-rate {
  background: linear-gradient(to bottom right, #ffffff, #e6f7ff);
  padding: 60px 40px;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  margin: 40px auto;
  font-family: 'Montserrat', sans-serif;
  max-width: 800px;
  color: #333;
  transition: transform 0.3s, box-shadow 0.3s;
  animation: fadeIn 0.5s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.exchange-rate:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

h1 {
  color: #005c99;
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 30px;
  text-align: center;
  text-transform: uppercase;
  animation: slideIn 0.5s ease-in-out;
}

@keyframes slideIn {
  from {
    transform: translateX(-20px);
  }
  to {
    transform: translateX(0);
  }
}

.form-group {
  margin-bottom: 30px;
  animation: fadeInUp 2s ease-in-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.form-label {
  display: block;
  font-weight: bold;
  margin-bottom: 10px;
  font-size: 18px;
  color: #005c99;
}

.form-control {
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 10px;
  font-size: 18px;
  margin-bottom: 10px;
  transition: border-color 2s, box-shadow 2s;
}

.form-control:focus {
  border-color: #005c99;
  box-shadow: 0 0 15px rgba(0, 92, 153, 0.5);
}

.result-group {
  background: #e9f5fb;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
  margin-top: 20px;
  font-size: 18px;
  color: #002b5c;
  transition: transform 2s ease, box-shadow 2s ease;
}

.result-group:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.alert {
  padding: 15px;
  margin-bottom: 30px;
  border-radius: 10px;
  color: white;
  text-align: center;
  font-size: 18px;
}

.alert-danger {
  background-color: #d9534f;
  animation: shake 2s ease;
}

@keyframes shake {
  0%, 100% {
    transform: translateX(0);
  }
  20%, 60% {
    transform: translateX(-10px);
  }
  40%, 80% {
    transform: translateX(10px);
  }
}

</style>
