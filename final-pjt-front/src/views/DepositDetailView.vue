<template>
    <div>
      <h1>적금 상세</h1>
      <div v-if="deposit">
        <p>이름: {{ deposit.name }}</p>
        <p>금리: {{ deposit.interest_rate }}%</p>
        <!-- 추가 정보 표시 -->
      </div>
    </div>
  </template>
  
  <script>
  import { useProductStore } from '@/stores/products'
  
  export default {
    data() {
      return {
        deposit: null
      }
    },
    methods: {
      fetchDepositDetail() {
        const productStore = useProductStore()
        const id = this.$route.params.id
        axios.get(`http://127.0.0.1:8000/api/v1/products/depositproducts/${id}/`)
          .then(response => {
            this.deposit = response.data
          })
          .catch(error => {
            console.error(error)
          })
      }
    },
    mounted() {
      this.fetchDepositDetail()
    }
  }
  </script>
  