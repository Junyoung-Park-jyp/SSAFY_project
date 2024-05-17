<template>
    <div>
      <h1>예금 상세</h1>
      <div v-if="saving">
        <p>이름: {{ saving.name }}</p>
        <p>금리: {{ saving.interest_rate }}%</p>
        <!-- 추가 정보 표시 -->
      </div>
    </div>
  </template>
  
  <script>
  import { useProductStore } from '@/stores/products'
  
  export default {
    data() {
      return {
        saving: null
      }
    },
    methods: {
      fetchSavingDetail() {
        const productStore = useProductStore()
        const id = this.$route.params.id
        axios.get(`http://127.0.0.1:8000/api/v1/products/savingproducts/${id}/`)
          .then(response => {
            this.saving = response.data
          })
          .catch(error => {
            console.error(error)
          })
      }
    },
    mounted() {
      this.fetchSavingDetail()
    }
  }
  </script>
  