<template>
  <div>
    <!--component 바깥으로 currentPage를 빼야 됨.-->
    <div v-if="currentPage === 'train'">
      <!-- 추론 요소 페이지 -->
      <LogoComponent />
      <TitleComponent>
        <span class="ccrc">CCRC </span>
        <span class="deep-voice">딥보이스 </span>
        <span class="experience">체험</span>
      </TitleComponent>
      <div v-if="currentPage === 'train'" class="white-box">
        <!-- Inference 컴포넌트의 내용 -->
        <!-- 뒤로 가기 버튼 -->
        <button @click="$emit('changePage', 'l-Model')" class="back-button">
          뒤로 가기
        </button>
        <h2>모델 학습이 완료되었습니다</h2>
        <div class = "grey-box">
            <h3>참여해주셔서 감사합니다</h3>
        </div>
        <div class="button-container">
          <ButtonComponent @click="showModelButton">모델 듣기</ButtonComponent>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ButtonComponent from "../components/ButtonComponent.vue";
import TitleComponent from "../components/TitleComponent.vue";
import LogoComponent from "../components/LogoComponent.vue";

export default {
  name: "TrainComponent",

  components: {
    ButtonComponent,
    TitleComponent,
    LogoComponent,
  },

  data() {
    console.log(this.currentPage);
    return {
      modelButtonVisible: false,
      currentPage: "train", // 현재 화면을 결정하는 데이터
    };
  },

  methods: {
    showModelButton() {
      // 녹음 버튼을 눌렀을 때 할 작업을 여기에 정의
      this.modelButtonVisible = true; // 모델 생성 버튼 표시
    },

    changePage(page) {
      this.currentPage = page;
    },

    back() {
      this.$emit("back"); // 부모 컴포넌트에 'back' 이벤트를 발생시킴
    },
  },
};
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


.grey-box {
  background-color: #e0e0e0; 
  padding: 20px;
  margin: 10px auto;
  width: 80%;
  height: 20%;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  text-align: center;

}

.logo-container {
  display: flex; /* 이미지를 flex item으로 만듬 */
  justify-content: flex-end; /* 오른쪽 정렬 */
}

.button-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-top: 30px; /* 버튼 위에 여백 추가 */
  justify-content: space-around;
}

.next-sentence-button {
  width: 90px;
  height: 45px;
  margin: 0 5px;
  margin-top: 20px;
  margin-bottom: 30px;
  background-color: grey;
  color: #ffffff;
  border: none;
  border-radius: 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.next-sentence-button:hover {
  background-color: rgb(87, 87, 87);
  transform: translateY(-2px);
}

.previous-sentence-button {
  width: 90px;
  height: 45px;
  margin: 0 5px;
  margin-top: 20px;
  margin-bottom: 30px;
  background-color: grey;
  color: #ffffff;
  border: none;
  border-radius: 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.previous-sentence-button:hover {
  background-color: rgb(87, 87, 87);
  transform: translateY(-2px);
}

.ccrc {
  color: rgb(231, 64, 64); /* 파란색으로 통일 */
}

.deep-voice,
.experience {
  color: #007aff; /* 파란색으로 통일 */
}

#app {
  font-family: "나눔스퀘어", sans-serif;
  color: #2c3e50;
}
* {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>s