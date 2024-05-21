<template>
  <div>
    <input type="text" v-model="cityInput" placeholder="시를 입력하세요">
    <input type="text" v-model="districtInput" placeholder="구를 입력하세요">
    <button @click="search">검색</button>
    <select v-model="selectedOption">
      <option value="모든 은행">모든 은행</option>
      <option value="신한은행">신한은행</option>
      <option value="국민은행">국민은행</option>
    </select>
    <div id="map">
      <MapComponent />
    </div>
  </div>
  
</template>

<script setup>
import { ref, onMounted } from 'vue';
import MapComponent from '@/components/MapComponent.vue';

const kakaoMapApiKey = import.meta.env.VITE_KAKAO_MAP_API_KEY;

let map, geocoder;
const cityInput = ref('');
const districtInput = ref('');
const selectedOption = ref('모든 은행');

onMounted(() => {
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
  const fullAddress = `${cityInput.value} ${districtInput.value}`;
  geocoder.addressSearch(fullAddress, (result, status) => {
    if (status === window.kakao.maps.services.Status.OK) {
      const coords = new window.kakao.maps.LatLng(result[0].y, result[0].x);
      map.setCenter(coords);
      searchBanks(coords);
    } else {
      console.error('주소 검색 실패:', status);
    }
  });
};

const searchBanks = (coords) => {
  const places = new window.kakao.maps.services.Places();
  const callback = (result, status) => {
    if (status === window.kakao.maps.services.Status.OK) {
      const filteredResults = result.filter(place => {
        if (selectedOption.value === '모든 은행') {
          return true;
        } else {
          return place.place_name.includes(selectedOption.value);
        }
      });
      filteredResults.forEach(place => {
        addMarker(place);
      });
    } else {
      console.error('은행 검색 실패:', status);
    }
  };

  places.categorySearch('BK9', callback, {
    location: coords,
    radius: 1000 // 검색 반경 (미터)
  });
};

const addMarker = (place) => {
  const marker = new window.kakao.maps.Marker({
    map: map,
    position: new window.kakao.maps.LatLng(place.y, place.x),
    title: place.place_name
  });

  window.kakao.maps.event.addListener(marker, 'click', () => {
    const infowindow = new window.kakao.maps.InfoWindow({
      content: `<div style="padding:5px;">${place.place_name}</div>`
    });
    infowindow.open(map, marker);
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

