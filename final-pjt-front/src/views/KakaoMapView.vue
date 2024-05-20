<template>
  <div>
    <input type="text" v-model="cityInput" placeholder="시를 입력하세요">
    <input type="text" v-model="districtInput" placeholder="구를 입력하세요">
    <button @click="search">검색</button>
    <div id="map"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const kakaoMapApiKey = import.meta.env.VITE_KAKAO_MAP_API_KEY;

let map, geocoder;
const cityInput = ref('');
const districtInput = ref('');

onMounted(() => {
  // 카카오 맵 API 스크립트를 동적으로 로드
  const script = document.createElement('script');
  script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${kakaoMapApiKey}&libraries=services,clusterer&autoload=false`;
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
  const fullAddress = cityInput.value + ' ' + districtInput.value;
  geocoder.addressSearch(fullAddress, (result, status) => {
    if (status === window.kakao.maps.services.Status.OK) {
      const coords = new window.kakao.maps.LatLng(result[0].y, result[0].x);
      map.setCenter(coords);
      // 근처 은행 검색 및 마커 추가
      searchBanks(coords);
    }
  });
};

const searchBanks = (coords) => {
  const places = new window.kakao.maps.services.Places();
  const request = {
    categoryCode: 'BK9', // 은행 카테고리 코드
    location: coords,
    radius: 1000 // 검색 반경 (미터)
  };
  places.categorySearch(request, (result, status) => {
    if (status === window.kakao.maps.services.Status.OK) {
      result.forEach(place => {
        addMarker(place);
      });
    }
  });
};

const addMarker = (place) => {
  const marker = new window.kakao.maps.Marker({
    map: map,
    position: new window.kakao.maps.LatLng(place.y, place.x),
    title: place.place_name
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

