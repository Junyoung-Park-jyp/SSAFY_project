import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useProductStore = defineStore('product', () => {
    const router = useRouter()
    const deposits = ref([])
    const savings = ref([])

    

    return { deposits, savings, }
}, { persist: true });