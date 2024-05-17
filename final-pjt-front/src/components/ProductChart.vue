<template>
    <div>
      <!-- <canvas ref="chart"></canvas> -->
    </div>
  </template>
  
  <script>
  // import { ref, onMounted } from 'vue'
  // import { Chart } from 'chart.js'
  
  // export default {
  //   props: {
  //     savingProducts: {
  //       type: Array,
  //       required: true
  //     },
  //     depositProducts: {
  //       type: Array,
  //       required: true
  //     }
  //   },
  //   setup(props) {
  //     const chart = ref(null)
  
  //     onMounted(() => {
  //       const ctx = chart.value.getContext('2d')
  //       new Chart(ctx, {
  //         type: 'bar',
  //         data: {
  //           labels: props.savingProducts.map(p => p.name).concat(props.depositProducts.map(p => p.name)),
  //           datasets: [{
  //             label: '가입 금리',
  //             data: props.savingProducts.map(p => p.interest_rate).concat(props.depositProducts.map(p => p.interest_rate)),
  //             backgroundColor: 'rgba(75, 192, 192, 0.2)',
  //             borderColor: 'rgba(75, 192, 192, 1)',
  //             borderWidth: 1
  //           }]
  //         },
  //         options: {
  //           scales: {
  //             y: {
  //               beginAtZero: true
  //             }
  //           }
  //         }
  //       })
  //     })
  
  //     return {
  //       chart
  //     }
  //   }
  // }
  </script>
  