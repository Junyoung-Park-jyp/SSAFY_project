# 관통 프로젝트(주제: 금융)

## TEAM 북박박

* 팀장: 박준영
* 팀원: 박기현

---

## 팀원 소개

### 박준영

* Frontend(vue) 총괄
  * store에 products, user 기초 함수 정리
  * Axios를 이용한 비동기 요청 처리
  * Component, View 세팅
* User, UserInfo 테이블 분리 및 정보 저장
* 카카오맵 API 이식
* 상품 추천 알고리즘 고안
* ERD 그리기

#### 박기현

* Backend(Django) 총괄
  * App별 url 구축
  * views의 authorization, api method 정리
  * Serializer, Model 구축
* 페이지 디자인
  * 웹 로고 제작
  * AI 기반 앱 이미지 제작
  * 메인 테마 디자인
* 카카오맵 API를 이용한 은행 필터링, 마커 추가
* 환율 계산 API를 이용해 양방향으로 계산 가능한 환율 계산기 구현
* OpenAI API를 이용한 챗봇 구현, 추천 알고리즘 이식

## 기획 단계

### ERD 다이어그램

![2021_04_user_count](./관통프로젝트ERD.drawio.png)

* Accounts 앱
  1. Django Auth에서 제공하는 User정보가 담긴 User 모델
  2. User의 부가적인 정보를 담은, User와 1:1 관계의 UserInfo 모델
  3. UserInfo와 Products app의 예금, 적금 옵션과 연결된 M:N 관계의 2개 모델
   
* Products 앱
  1. 금융감독원 API로 수집한 예금, 적금 모델
  2. 각 예금 적금의 옵션을 담은 1:N관계의 Options 모델 2개
  
* Community 앱
  1. 게시판의 글을 저장하고, 작성자를 User에서 Foreign key로 사용하는 Post 모델
  2. 게시판의 댓글을 저장하고, Post와 1:N인 Comment 모델
  3. 각 Post, Comment와 User간 M:N의 좋아요 모델
  
* Exchange 앱
  * 환율을 API에서 가져와서 저장하는 ExchangeRate 모델

### 상품 추천 알고리즘

* 나이와 주 사용 은행을 회원가입 단계에서 수집

* 이후 나이, 주 은행에 맞추어 추천

* 이외에도 목표 금액과, 월간 저축 가능 금액을 이용해 추가하기로 기획

