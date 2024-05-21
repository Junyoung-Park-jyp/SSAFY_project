<template>
  <div>
    <div ref="map" style="width:100%;height:400px;"></div>
  </div>
</template>

<script>
export default {
  name: 'MapComponent',
  mounted() {
    // Kakao 지도 API 로드가 완료되면 실행될 콜백 함수
    if (typeof kakao !== 'undefined') {
      this.initializeMap();
    } 
  },
  methods: {
    initializeMap() {
      const container = this.$refs.map; // 지도를 표시할 div
      const options = {
        center: new kakao.maps.LatLng(37.5665, 126.9780), // 지도의 중심 좌표
        level: 3 // 지도의 확대 레벨
      };

      // 지도 생성
      const map = new kakao.maps.Map(container, options);

      // 마커 생성 및 지도에 표시
      const markerPosition  = new kakao.maps.LatLng(37.5665, 126.9780); 
      const marker = new kakao.maps.Marker({
        position: markerPosition
      });
      marker.setMap(map);
    }
  }
}
</script>

<style scoped>
/* 필요한 스타일 추가 */
</style>
