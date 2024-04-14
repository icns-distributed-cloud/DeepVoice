<template>
  <div>
    <!-- 추론 요소 페이지 -->
    <LogoComponent />
    <TitleComponent >
      <span class="ccrc">CCRC </span>
      <span class="deep-voice">딥보이스 </span>
      <span class="experience">체험</span>
    </TitleComponent>
    <div class="white-box">
      <button @click="back" class="back-button">뒤로 가기</button>
      <h2>음성을 선택해주세요</h2>
      <div class="button-container">
        <!-- 모델 리스트를 순회하며 동적으로 버튼을 생성함 -->
        <ButtonComponent v-for="model in modelList" :key="model" @click="selectModel(model)">
          {{ model }}
        </ButtonComponent>
      </div>
      <button class="model-listen-button" v-if="modelButtonVisible" @click="handleModelListen">추론 음성</button>
    </div>
  </div>
</template>

<script>
import ButtonComponent from "../components/ButtonComponent.vue";
import TitleComponent from "../components/TitleComponent.vue";
import LogoComponent from "../components/LogoComponent.vue";

export default {
  name: "InferenceModel",

  components: {
    ButtonComponent,
    TitleComponent,
    LogoComponent,
  },

  data() {
    return {
      modelButtonVisible: false,
      modelList: [], // 모델 리스트를 저장할 배열을 생성
      selectedModel: '', // 선택된 모델을 저장할 변수
    };
  },

  methods: {
    showModelButton() {
      // 모델 생성 버튼을 보이게 하는 메서드
      this.modelButtonVisible = true;
    },

    selectModel(model) {
      this.selectedModel = model;
      this.modelButtonVisible = true; // 모델이 선택되면 버튼을 보이도록 설정
      this.$emit('model-selected', model); // 선택한 모델을 상위 컴포넌트로 전달
    },

    async handleModelListen() {
      try {
        const response = await fetch('http://163.180.117.43:8000/text_info', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model_name: this.selectedModel,
            text: this.inputText,
          })
        });
        
        const responseData = await response.json(); // 서버로부터의 응답을 JSON으로 파싱
        console.log(responseData); // 응답데이터를 콘솔에 출력
      } catch (error) {
        console.error('Error handling model listening: ', error);
      }
    }, 

    async getModels() {
      try {
        const response = await fetch("http://163.180.117.43:8000/models/"); // 백엔드의 get_models 엔드포인트에 GET 요청을 내보냄
        if (!response.ok) {
          throw new Error("Failed to fetch  models");
        }
        const data = await response.json(); // 응답을 JSON 형식으로 파싱
        this.modelList = data.data.models; // 모델 리스트를 Vue 컴포넌트의 데이터에 저장
      } catch (error) {
        console.error("Error fetching models: ", error);
      }
    },

    back() {
      this.$emit("back"); // 부모 컴포넌트에 'back' 이벤트를 발생시킴
    },
  },

  mounted() {
    this.getModels(); // 컴포넌트가 마운트될 때 모델 리스트를 가져옴
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

.white-box h2 {
  margin-top: 0px;
  margin-bottom: 100px;
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

.model-listen-button {
  width: 100px;
  height: 50px;
  margin: 0 5px;
  margin-top: 50px;
  margin-bottom: 30px;
  background-color: grey;
  color: #ffffff;
  border: none;
  border-radius: 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.model-listen-button:hover {
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
</style>
