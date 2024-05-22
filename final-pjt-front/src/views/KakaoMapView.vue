<template>
  <div class="container map-container">
    <div class="search-bar">
      <input type="text" v-model="cityInput" placeholder="검색할 지역을 입력하세요." class="form-control">
      <!-- <input type="text" v-model="districtInput" placeholder="구를 입력하세요" class="form-control"> -->
      <select v-model="selectedOption" class="form-select">
        <option value="모든 은행">모든 은행</option>
        <option v-for="bank in uniqueBanks" :key="bank" :value="bank">{{ bank }}</option>
      </select>
      <button @click="search" class="btn btn-primary">검색</button>
    </div>
    <div id="map" class="map"></div>
    <div class="bank-list" v-if="filteredBanks.length">
      <h2>검색된 은행 리스트</h2>
      <ul>
        <li v-for="bank in filteredBanks" :key="bank.id">
          <strong>{{ bank.place_name }}</strong><br>
          {{ bank.road_address_name || bank.address_name }}
        </li>
      </ul>
    </div>
  </div>
  
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import MapComponent from '@/components/MapComponent.vue';

const kakaoMapApiKey = import.meta.env.VITE_KAKAO_MAP_API_KEY;

let map, geocoder;
const cityInput = ref('');
const districtInput = ref('');
const selectedOption = ref('모든 은행');
const banks = ref([]);
const filteredBanks = ref([]);
const uniqueBanks = ref([]);

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

watch(banks, (newBanks) => {
  const bankNames = newBanks.map(bank => bank.place_name.split(' ')[0]);
  uniqueBanks.value = [...new Set(bankNames)];
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
      banks.value = result; // 모든 검색 결과 저장
      filterBanks(); // 필터 적용
    } else {
      console.error('은행 검색 실패:', status);
    }
  };

  places.categorySearch('BK9', callback, {
    location: coords,
    radius: 1000 // 검색 반경 (미터)
  });
};

const filterBanks = () => {
  clearMarkers(); // 기존 마커를 초기화
  filteredBanks.value = banks.value.filter(place => {
    if (selectedOption.value === '모든 은행') {
      return true;
    } else {
      return place.place_name.includes(selectedOption.value);
    }
  });
  filteredBanks.value.forEach(place => {
    addMarker(place);
  });
};

let markers = [];
const addMarker = (place) => {
  const marker = new window.kakao.maps.Marker({
    map: map,
    position: new window.kakao.maps.LatLng(place.y, place.x),
    title: place.place_name
  });
  markers.push(marker);
  
  window.kakao.maps.event.addListener(marker, 'click', () => {
    const infowindow = new window.kakao.maps.InfoWindow({
      content: `<div style="padding:5px;">${place.place_name}</div>`
    });
    infowindow.open(map, marker);
  });
};

const clearMarkers = () => {
  markers.forEach(marker => marker.setMap(null));
  markers = [];
};

watch(selectedOption, () => {
  filterBanks();
});
</script>

<style scoped>
.map-container {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.search-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.form-control, .form-select {
  padding: 10px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  flex: 1;
}

.btn-primary {
  padding: 10px 20px;
  background-color: #002b5c;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: #005c99;
}

#map {
  width: 100%;
  height: 70vh;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.bank-list {
  margin-top: 20px;
}

.bank-list h2 {
  font-size: 24px;
  color: #002b5c;
}

.bank-list ul {
  list-style: none;
  padding: 0;
}

.bank-list li {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.bank-list li strong {
  display: block;
  font-size: 18px;
  color: #002b5c;
}
</style>
