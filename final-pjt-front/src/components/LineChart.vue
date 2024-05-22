<template>
  <div>
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import { ref, watch, onMounted } from 'vue';
import Chart from 'chart.js/auto';

export default {
  props: {
    chartData: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    const chart = ref(null);
    const chartCanvas = ref(null);

    const createChart = () => {
      if (chart.value) {
        chart.value.destroy();
      }

      if (chartCanvas.value) {
        const ctx = chartCanvas.value.getContext('2d');
        if (!ctx) {
          console.error('Failed to acquire context from canvas');
          return;
        }

        chart.value = new Chart(ctx, {
          type: 'line',
          data: props.chartData,
          options: {
            responsive: true,
            plugins: {
              legend: {
                position: 'top',
              },
              title: {
                display: true,
                text: 'Interest Rates Comparison'
              }
            },
            scales: {
              y: {
                beginAtZero: true // Ensure Y-axis starts at 0
              }
            }
          }
        });
      }
    };

    onMounted(() => {
      createChart();
    });

    watch(() => props.chartData, () => {
      createChart();
    }, { deep: true });

    return {
      chartCanvas
    };
  }
};
</script>

<style scoped>
canvas {
  max-width: 100%;
}
</style>
