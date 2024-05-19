<template>
  <div>
    <div>
      <label for="location">Location: </label>
      <input type="text" v-model="location" placeholder="Enter latitude,longitude (e.g., 37.5665,126.9780)" />
    </div>
    <div>
      <label for="bank_name">Bank Name: </label>
      <input type="text" v-model="bankName" placeholder="Enter bank name" />
    </div>
    <div>
      <button @click="searchBanks">Search</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BankSearchForm',
  data() {
    return {
      location: '',
      bankName: ''
    };
  },
  methods: {
    searchBanks() {
      this.$emit('search', { location: this.location, bankName: this.bankName });
    }
  }
};
</script>

<style scoped>
/* Add component-specific styles here */
</style>
