<template>
    <div>
      <h1>Bank Search</h1>
      <div>
        <label for="location">Location:</label>
        <input id="location" v-model="location" type="text" />
      </div>
      <div>
        <label for="bank">Bank:</label>
        <input id="bank" v-model="bank" type="text" />
      </div>
      <button @click="search">Search</button>
      <div v-if="banks.length">
        <h2>Results:</h2>
        <ul>
          <li v-for="bank in banks" :key="bank.id">{{ bank.name }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        location: '',
        bank: '',
        banks: [],
      };
    },
    methods: {
      async search() {
        const response = await axios.get(`http://localhost:8000/api/banks?location=${this.location}&bank=${this.bank}`);
        this.banks = response.data.banks;
      }
    }
  };
  </script>
  