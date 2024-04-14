<template>
  <div>
    <LearningModel v-if="currentPage === 'l-Model'" @changePage="changePage"/>
    <div v-if="currentPage === 'learning'">
      <LogoComponent/>
      <TitleComponent>
        <span class="ccrc">CCRC </span>
        <span class="deep-voice">딥보이스 </span>
        <span class="experience">체험</span>
      </TitleComponent>
      <div v-if="currentPage === 'learning'" class="white-box">
        <!-- Learning 컴포넌트의 내용 -->
        <!-- 뒤로 가기 버튼 -->
        <button @click = "$emit('changePage', 'home')" class = "back-button">뒤로 가기</button>
        <h2>음성 학습을 위해 녹음을 시작합니다</h2>
        <div class = "grey-box">
          <h3>음성 학습은 15분 정도 소요됩니다</h3>
        </div>
        <div class="button-container">
          <ButtonComponent @click="showModelButton">학습 시작</ButtonComponent>
        </div>
        <button class = "record-button" v-if="modelButtonVisible" @click="handleModelRecord">문장 녹음</button>
      </div>
    </div>    
  </div>
</template>

<script>
import ButtonComponent from '../components/ButtonComponent.vue';
import TitleComponent from '../components/TitleComponent.vue';
import LogoComponent from '../components/LogoComponent.vue';
import LearningModel from '../views/LearningModel.vue';

export default {
  name: "LearningComponent",

  views: {
    LearningModel,
  },
  
  components: {
    ButtonComponent,
    TitleComponent,
    LogoComponent,
    LearningModel,
  },

  data() {
    console.log("초기 페이지: ", this.currentPage); // 데이터 초기화 시 로그 찍기
    return {
      modelButtonVisible: false,
      currentPage: "learning", // 현재 화면을 결정하는 데이터
    };
  },

  methods: {
    showModelButton() {
      this.modelButtonVisible = true;
    },

    handleModelRecord() {
      if (confirm('20개의 문장 녹음을 시작합니다.')){
        this.modelButtonVisible = false;
        this.changePage('l-Model');
      }
      else {
        this.modelButtonVisible = false;
      }
    },

    changePage(page){
      this.currentPage = page;
    }
  }
}
</script>

<style>
/* 스타일은 App.vue에서 정의한 것과 동일하게 적용하거나 적절히 조정 */
/* App.vue의 기존 스타일 */
/* 컴포넌트별 스타일은 각각의 컴포넌트 파일로 이동 */

.back-button {
  position: absolute;
  top: 20px;
  left: 20px;
  padding: 10px 20px;
  background-color: grey;
  color: white;
  border: none;
  border-radius: 15px;
  cursor: pointer;
}

.back-button:hover {
  background-color: darkgrey;
}

.white-box {
  background-color: #ffffff; /* 박스 색상을 흰색으로 변경 */
  padding: 40px;
  border-radius: 50px; /* 모서리 둥글게 처리 */
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* 그림자를 좀 더 부드럽게 설정 */
  width: 400px; /* 박스의 너비 설정 */
  text-align: center; /* 텍스트 중앙 정렬 */
}

.white-box h2 {
  margin-top: 0px;
}



.logo-container {
  display: flex; /* 이미지를 flex item으로 만듬 */
  justify-content: flex-end; /* 오른쪽 정렬 */
}


.button-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-top: 800px; /* 버튼 위에 여백 추가 */
  justify-content: space-around;
}


.ccrc {
  color: rgb(231, 64, 64); /* 파란색으로 통일 */
}

.deep-voice, .experience {
  color: #007aff; /* 파란색으로 통일 */
}

.record-button {
  width: 100px;
  height: 50px;
  margin-top: 20px;
  margin-bottom: 10px;
  background-color: gray;
  color: #ffffff;
  border: none;
  border-radius: 20px;
  font-size: 16px;
  cursor: pointer;
}

.record-button:hover {
  background-color: darkgrey;
}

#app {
  font-family: '나눔스퀘어', sans-serif;
  color: #2c3e50;
}
* {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>

