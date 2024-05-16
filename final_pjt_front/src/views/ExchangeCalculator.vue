<template>
    <div>
      <h1>Exchange Calculator</h1>
      <div>
        <label for="currency">Select Currency:</label>
        <select id="currency" v-model="currency">
          <option v-for="currency in currencies" :key="currency" :value="currency">{{ currency }}</option>
        </select>
      </div>
      <div>
        <label for="amount">Amount:</label>
        <input id="amount" v-model="amount" type="number" />
      </div>
      <button @click="convert">Convert</button>
      <p v-if="result">Converted Amount: {{ result }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        currency: 'USD',
        amount: 0,
        result: null,
        currencies: ['USD', 'EUR', 'JPY'],
      };
    },
    methods: {
      async convert() {
        const response = await axios.get(`http://localhost:8000/api/exchange?currency=${this.currency}&amount=${this.amount}`);
        this.result = response.data.converted_amount;
      }
    }
  };
  </script>
  