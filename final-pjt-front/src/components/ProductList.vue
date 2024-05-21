<!-- <template>
  <div class="table-responsive product-list">
    <table class="table table-bordered table-hover">
      <thead class="table-light">
        <tr>
          <th>금융회사명</th>
          <th>상품명</th>
          <th v-for="term in terms" :key="term">{{ term }}개월</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id" @click="selectProduct(product.id)">
          <td>{{ product.kor_co_nm }}</td>
          <td>{{ product.fin_prdt_nm }}</td>
          <td v-for="term in terms" :key="term">{{ getRate(product, term) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    products: Array,
    terms: Array  // Display terms prop
  },
  emits: ['selectProduct'],
  methods: {
    selectProduct(id) {
      this.$emit('selectProduct', id);
    },
    getRate(product, term) {
      if (!product.options) return '-';
      const option = product.options.find(opt => opt.save_trm === term);
      return option ? `${option.intr_rate}%` : '-';
    }
  }
};
</script>

<style scoped>
.product-list {
  margin-top: 20px;
}

.table {
  width: 100%;
  margin-bottom: 1rem;
  color: #212529;
  background: #fff;
  border-radius: 15px;
}

.table th,
.table td {
  padding: 1rem;
  vertical-align: middle;
  border-top: 1px solid #dee2e6;
}

.table-hover tbody tr:hover {
  background-color: rgba(0, 0, 0, 0.075);
  cursor: pointer;
}

.table-bordered {
  border: 1px solid #dee2e6;
}

.table-bordered th,
.table-bordered td {
  border: 1px solid #dee2e6;
}

.table-light {
  background-color: #f8f9fa;
  color: #002b5c;
  font-weight: bold;
}
</style> -->
