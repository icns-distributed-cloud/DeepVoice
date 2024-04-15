<template>
  <div class="container">
    <div class="purple-gradient"></div> <!--새로운 배경 추가-->
    <div v-if = "currentPage === 'home'">
      <!-- 시작 페이지 컨텐츠 -->
      <LogoComponent/>
      <TitleComponent>
        <span class="ccrc">CCRC </span>
        <span class="deep-voice">딥보이스 </span>
        <span class="experience">체험</span>
      </TitleComponent>
      <div v-if = "currentPage === 'home'" class = "white-box">
        <h2>환영합니다!</h2>
        <div class = "grey-box">
            <h3>여기는 CCRC 딥보이스 체험장입니다</h3>
        </div>
        <div class="button-container">
          <!-- 추론 버튼 -->
          <button @click= "currentPage = 'inference'" class="main-button">체험하기</button>
        </div>
      </div>
    </div>  
    <!-- InferenceComponent 렌더링 -->
    <InferenceComponent v-if = "currentPage === 'inference'" @changePage ="changePage"/>
    
    <!-- PEComponent (Prevention Education 예방 교육) 렌더링 -->
    <PEComponent v-if = "currentPage === 'PE'" @changePage ="changePage"/>

  </div>
</template>

<script>
import LogoComponent from './components/LogoComponent.vue';
import TitleComponent from './components/TitleComponent.vue';
import InferenceComponent from './views/InferenceComponent.vue';
import PEComponent from './views/InferenceComponent.vue';

export default {
  components: {
    LogoComponent,
    TitleComponent,
    InferenceComponent,
    PEComponent,
  },

  data() {
    return {
      currentPage: 'home', // 현재 화면을 결정하는 데이터
    };
  },

  methods: {
    // 페이지 변경 메서드
    changePage(page) {
      this.currentPage = page;
      console.log(this.currentPage);
    }
  }
}
</script>

<style>
.white-box {  
  z-index: 5;
  background-color: #ffffff;
  padding: 50px;
  border-radius: 50px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  width: 800px;
  height: 300px;
  text-align: center;
}

.white-box h2 {
  margin-top: 0px;
  margin-bottom: 20px;
}

.white-box h3 {
  margin-bottom: 30px;
}

.grey-box {
  background-color: #e0e0e0; 
  padding: 20px;
  margin: 10px auto;
  width: 80%;
  height: 20%;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  text-align: center;
}


.container {
  /* 스타일 설정 */
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  /* 파란색 그라데이션 배경 추가 */
  background: linear-gradient(to right top, #DFFFFF, #AABBFF);
  font-family: '나눔스퀘어', sans-serif; /* 전체적으로 사용할 폰트 설정 */
}

.gradient-background {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 2275px;  /* 원래 이미지의 너비 */
  height: 1169px; /* 원래 이미지의 높이 */
  background: linear-gradient(90deg, #B990F8 0%, #9B94F3 100%);
  border: 4.37px dotted; /* 점선 테두리 */
  z-index: 0; /* 가장 아래에 위치 */
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 40px;
}

.main-button {
  width: 120px;
  height: 60px;
  margin: 0 5px;
  margin-bottom: 10px;
  margin-right: 20px;
  margin-left: 20px;
  background-color: #007aff;
  color: #ffffff;
  border: none;
  border-radius: 20px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.main-button:hover {
  background-color: #005ecb;
  transform: translateY(-2px);
}

</style>
