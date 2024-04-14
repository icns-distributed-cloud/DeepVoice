<template>
  <div>
    <!--component 바깥으로 currentPage를 빼야 됨.-->
    <TrainComponent v-if="currentPage === 'train'" @changePage="changePage"/>
    <div v-if="currentPage === 'l-Model'">
      <!-- 추론 요소 페이지 -->
      <LogoComponent />
      <TitleComponent>
        <span class="ccrc">CCRC </span>
        <span class="deep-voice">딥보이스 </span>
        <span class="experience">체험</span>
      </TitleComponent>
      <div v-if="currentPage === 'l-Model'" class="white-box">
        <!-- Inference 컴포넌트의 내용 -->
        <!-- 뒤로 가기 버튼 -->
        <button @click="$emit('changePage', 'learning')" class="back-button">
          뒤로 가기
        </button>
        <h2>음성을 선택해주세요</h2>
        <div class = "grey-box">
            <h3>{{ sentences[currentSentenceIndex] }}</h3>
        </div>
        <div class="button-container">
          <ButtonComponent @click="showModelButton">음성 녹음</ButtonComponent>
        </div>
        <button v-if="currentSentenceIndex > 0" class="previous-sentence-button" @click="handlePreviousSentence">이전 문장</button>
        <button v-if="modelButtonVisible" class="next-sentence-button" @click="handleNextSentence">다음 문장</button>
        <button v-if="showTrainingButton" class="train-model-button" @click="trainModel">모델 훈련</button>
      </div>
    </div>
  </div>
</template>

<script>
import ButtonComponent from "../components/ButtonComponent.vue";
import TitleComponent from "../components/TitleComponent.vue";
import LogoComponent from "../components/LogoComponent.vue";
import TrainComponent from "../views/TrainComponent.vue"; // TrainComponent import

export default {
  name: "LearningModel",

  components: {
    ButtonComponent,
    TitleComponent,
    LogoComponent,
    TrainComponent,
  },

  data() {
    console.log(this.currentPage);
    return {
      modelButtonVisible: true,
      showTrainingButton: false, // 훈련 버튼을 표시할지 결정하는 플래그
      currentPage: "l-Model", // 현재 화면을 결정하는 데이터
      currentSentenceIndex: 0,
      sentences: [
        "1. 안녕하세요, 반갑습니다.", // 문장 1
        "2. 클라우드 컨티뉴엄에 오신 것을 환영합니다.",
        "3. 여기는 딥보이스 체험장입니다.",
        "4. 오늘은 날씨가 정말 좋습니다.",
        "5. 맛있는 음식을 먹으면 기분이 좋아집니다.",
        "6. 운동을 하면 건강이 좋아집니다.",
        "7. 새로운 도전을 받아들이는 것은 성장의 기회입니다.",
        "8. 일상의 작은 기쁨들을 잊지 말아야 겠어요.",
        "9. 생각보다 시간이 빨리 가네요.",
        "10. 내일의 계획을 세우는 것이 중요합니다.",
        "11. 책을 읽으면서 새로운 지식을 얻는 것은 즐겁습니다.",
        "12. 꽃이 피면 봄이 온 것 같아 기분이 좋아져요.",
        "13. 왜 그렇게 기분이 좋아보여?",
        "14. 어디로 가는 게 좋을까?",
        "15. 이 음악은 정말 감동적이야!",
        "16. 정말 신기하다!",
        "17. 어디서 이런 좋은 소식을 들었어?",
        "18. 조금만 더 힘을 내!",
        "19. 정말 특별한 순간이야!",
        "20. 문장을 끝까지 읽느라 수고많았어요." // 문장 20
      ]
    };
  },

  methods: {
    showModelButton() {
      // 녹음 버튼을 눌렀을 때 할 작업을 여기에 정의
      this.modelButtonVisible = true; // 모델 생성 버튼 표시
    },

    // 다음 문장으로 넘어가게 해주는 메소드
    handleNextSentence() {
      if (this.currentSentenceIndex < this.sentences.length - 1) { 
        this.currentSentenceIndex += 1;
        this.showTrainingButton = false;
      }
      this.updateVisibility();
    }, 

    // 이전 문장으로 넘어가게 해주는 메소드
    handlePreviousSentence() {
      if (this.currentSentenceIndex > 0) {
        this.currentSentenceIndex -= 1;
      } 
      this.updateVisibility();
    },

    updateVisibility() {
      if (this.currentSentenceIndex === 0) {
        this.modelButtonVisible = false;
      } else if (this.currentSentenceIndex === this.sentences.length - 1) {
        this.modelButtonVisible = false;
        this.showTrainingButton = true; // 마지막 문장에서 훈련 버튼을 표시
      } else {
        this.modelButtonVisible = true;
        this.showTrainingButton = false;
      }
    },

    trainModel() {
      if (confirm("모델을 훈련 중입니다.")) {
        this.changePage('train');
      }
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

.train-model-button {
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

.train-model-button:hover {
  background-color: rgb(87, 87, 87);
  transform: translateY(-2px);
}

#app {
  font-family: "나눔스퀘어", sans-serif;
  color: #2c3e50;
}
* {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>