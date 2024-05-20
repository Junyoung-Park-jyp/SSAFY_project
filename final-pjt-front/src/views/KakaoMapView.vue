<template>
  <div>
    <select v-model="selectedCity">
      <option v-for="city in cities" :key="city.name" :value="city">
        {{ city.name }}
      </option>
    </select>
    <select v-model="selectedDistrict">
      <option v-for="district in selectedCity.districts" :key="district" :value="district">
        {{ district }}
      </option>
    </select>
    <button @click="search">검색</button>
    <div id="map"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const kakaoMapApiKey = import.meta.env.VITE_KAKAO_MAP_API_KEY;

const cities = ref([
  { name: '서울특별시', districts: ['전체', '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'] },
  { name: '부산광역시', districts: ['전체', '강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구'] },
  { name: '대구광역시', districts: ['전체', '남구', '달서구', '달성군', '동구', '북구', '서구', '수성구'] },
  { name: '인천광역시', districts: ['전체', '강화군', '계양구', '남동구', '동구', '미추홀구', '부평구', '서구', '연수구', '옹진군'] },
  { name: '광주광역시', districts: ['전체', '광산구', '남구', '동구', '북구', '서구'] },
  { name: '대전광역시', districts: ['전체', '대덕구', '동구', '서구', '유성구'] },
  { name: '울산광역시', districts: ['전체', '남구', '동구', '북구', '울주군', '중구'] }
]);

const selectedCity = ref(cities.value[0]);
const selectedDistrict = ref(selectedCity.value.districts[0]);

let map, geocoder;

onMounted(() => {
  // 카카오 맵 API 스크립트를 동적으로 로드
  const script = document.createElement('script');
  script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${kakaoMapApiKey}&libraries=services&autoload=false`;
  script.onload = () => {
    window.kakao.maps.load(() => {
      const container = document.getElementById('map');
      const options = {
        center: new window.kakao.maps.LatLng(37.5665, 126.9780), // 초기 위치 (서울)
        level: 3 // 초기 줌 레벨
      };
      map = new window.kakao.maps.Map(container, options);
      geocoder = new window.kakao.maps.services.Geocoder();
    });
  };
  document.head.appendChild(script);
});

const search = () => {
  const fullAddress = selectedCity.value.name + ' ' + selectedDistrict.value;
  geocoder.addressSearch(fullAddress, (result, status) => {
    if (status === window.kakao.maps.services.Status.OK) {
      const coords = new window.kakao.maps.LatLng(result[0].y, result[0].x);
      map.setCenter(coords);
    }
  });
};
</script>

<style>
#map {
  width: 70%;
  height: 70vh;
  margin: 0 auto;
}
</style>
