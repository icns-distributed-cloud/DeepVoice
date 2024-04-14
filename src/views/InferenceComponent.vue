<template>
  <div>
    <div v-if="currentPage === 'i-Model'">
      <!-- i-Model 페이지 -->
      <InferenceModel @back="changePage('inference')" @model-selected="handleModelSelected" />
    </div>
    <div v-if="currentPage === 'inference'">
      <!-- 추론 요소 페이지 -->
      <LogoComponent />
      <TitleComponent >
        <span class="ccrc">CCRC </span>
        <span class="deep-voice">딥보이스 </span>
        <span class="experience">체험</span>
      </TitleComponent>
      <div class="white-box">
        <button @click="$emit('changePage', 'home')" class="back-button">뒤로 가기</button>
        <h2>원하는 문장을 입력하세요</h2>
        <div class = "grey-box">
          <!-- 텍스트 입력 창 -->
          <input type="text" v-model="inputText" @keyup.enter="handleInputEnter" placeholder="텍스트를 입력하세요">
          <!-- 성별 선택 라디오 버튼 -->
          <div class="gender-selection">
            <label>
              <input type="radio" v-model="selectedGender" value="male">
              남성
            </label>
            <label>
              <input type="radio" v-model="selectedGender" value="female">
              여성
            </label>
          </div>
        </div>
        <div class="button-container">
          <ButtonComponent @click="showModelSelection">모델 선택</ButtonComponent>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ButtonComponent from "../components/ButtonComponent.vue";
import TitleComponent from "../components/TitleComponent.vue";
import LogoComponent from "../components/LogoComponent.vue";
import InferenceModel from "../views/InferenceModel.vue"; // 새 창으로 사용할 컴포넌트 import

export default {
  name: "InferenceComponent",

  components: {
    ButtonComponent,
    TitleComponent,
    LogoComponent,
    InferenceModel,
  },

  data() {
    return {
      currentPage: "inference", // 현재 화면을 결정하는 데이터
      inputText: "", // 사용자가 입력한 텍스트를 저장할 데이터
      selectedGender: "", // 선택한 성별을 저장하는 변수
      selectedModel: "", // 선택된 모델을 저장할 변수 추가
    };
  },

  methods: {
    showModelSelection() {
      // 모델 선택 버튼 클릭 시 모델 선택 컴포넌트로 화면 전환
      this.changePage('i-Model');
    },

    handleInputEnter(event) {
      // 엔터 키를 누를 때 입력이 완료되고 저장됩니다.
      const newText = event.target.value; // 입력된 텍스트를 newText 변수에 저장
      console.log("입력 완료: ", newText);
      
      // 이전에 입력한 값 위에 새로 입력한 값을 덮어쓰기
      this.inputText = newText;

      // 여기서 입력된 텍스트를 백엔드로 보낼 수 있음
    },

    handleModelSelected(model) {
      this.selectedModel = model; // 선택된 모델을 저장
      console.log("Selected model: ", model);
      // 선택된 모델을 백엔드로 보내는 등의 작업을 수행할 수 있음
    },

    changePage(page) {
      console.log("페이지 전환: ", page); // 페이지 전환 로그
      this.currentPage = page;
    },

    async sendTextInfoToBackend() {
      try {
        const genderValue = this.selectedGender === 'male' ? 0 : 1; // gender를 int로 변환
        const response = await fetch('http://163.180.117.43:8000/text_info', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model_name: this.selectedModel, // 선택한 모델 정보를 함께 전송
            text: this.inputText,
            gender: genderValue,
          }),
        });
        const responseData = await response.json();
        console.log(responseData); // 서버로부터의 응답 확인
      } catch (error) {
        console.error('Error sending text info to backend: ', error);
      }
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

.gender-selection {
  margin-top: 10px;
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

