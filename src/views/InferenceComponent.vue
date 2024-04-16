<template>
  <div>
    <PEComponent v-if="currentPage === 'PE'" @changePage="changePage"/>
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
        <div v-if="loading" class="loading-message">
          <h2>음성 추론 중입니다. 잠시 기다려주세요.</h2>
        </div>
        <div v-if="!loading">
          <h2>원하는 문장을 입력하세요</h2>
        </div> 
        <div class = "grey-box">
          <!-- 텍스트 입력 창 -->
          <div class="input-container">
            <input type="text" v-model="inputText" @keyup.enter="handleInputEnter" placeholder="텍스트를 입력하세요 (글자 수 50자 제한)" maxlength="50" style="width: 70%">
          </div>
          </div>
        <!-- 모델 리스트 -->
        <div class="button-container">
          <div class="model-list-buttons">
            <ButtonComponent v-for="model in modelList" :key="model" @click="selectModel(model)">
              {{ model }}
            </ButtonComponent>
          </div>
        </div>
        <!-- 선택한 모델에 대한 버튼 -->
        <button v-if="selectedModel && !loading && !showAudioBox" class="voice-creation-button" @click="sendTextInfoToBackend">음성 생성</button>
        <button v-if="selectedModel && !loading && showAudioBox" class="PE-button" @click="goToPE">예방 교육</button>
      </div>
      <div class="audio-box" v-if="showAudioBox">
        <h2>생성된 음성을 재생해보세요</h2>
        <audio :src="audioSrc" controls>
        </audio>        
      </div>
    </div>
  </div>
</template>

<script>
import ButtonComponent from "../components/ButtonComponent.vue";
import TitleComponent from "../components/TitleComponent.vue";
import LogoComponent from "../components/LogoComponent.vue";
import PEComponent from "./PEComponent.vue";

export default {
  name: "InferenceComponent",

  components: {
    ButtonComponent,
    TitleComponent,
    LogoComponent,
    PEComponent,
  },

  data() {
    return {
      currentPage: "inference", // 현재 화면을 결정하는 데이터
      inputText: "", // 사용자가 입력한 텍스트를 저장할 데이터
      selectedGender: "", // 선택한 성별을 저장하는 변수
      selectedModel: "", // 선택된 모델을 저장할 변수 추가
      modelList: [], // 모델 리스트 데이터 추가
      modelListVisible: false, // 모델 리스트 보이기 여부
      loading: false, // 로딩 상태를 나타내는 변수 추가

      showAudioBox: false,
      BaseaudioSrc: "http://163.180.117.43:8000/get_audio/?model_name=",
      audioSrc:"",
    };
  },

  methods: {
    goToPE() {
      this.changePage('PE');
    },

    changePage(page){
      this.currentPage = page;
    },

    showModelSelection() {
      this.modelListVisible = true;
      this.fetchModelList(); // 모델 선택 버튼을 누르면 모델 리스트를 불러오는 함수 호출
    },
    
    selectModel(model) {
      // 모델 선택 시 선택된 모델 저장 및 모델 리스트 감추기
      this.selectedModel = model;
      // 선택한 모델에 따라 텍스트 정보를 백엔드로 전송
    },

    handleInputEnter(event) {
      // 엔터 키를 누를 때 입력이 완료되고 저장됩니다.
      const newText = event.target.value; // 입력된 텍스트를 newText 변수에 저장
      console.log("입력 완료: ", newText);
      
      // 이전에 입력한 값 위에 새로 입력한 값을 덮어쓰기
      this.inputText = newText;
    },
    
    // 모델 리스트를 불러와서 Vue.js 데이터에 저장하는 함수
    async fetchModelList() {
      try {
        const response = await fetch('http://163.180.117.43:8000/models/', {
          method: 'GET', // 요청 사용
        });
        const data = await response.json();
        console.log(data.data.models);  // 데이터 확인용 콘솔 출력
        if (data.success === 1) {
          this.modelList = data.data.models; // 모델 리스트 데이터를 Vue.js 데이터에 저장
        } else {
          console.error('Failed to fetch model list: ', data.message);
        }
      } catch (error) {
        console.error('Error fetching model list: ', error);
      }
    },
   
    async sendTextInfoToBackend() {
      try {
        const genderValue = this.selectedGender === 'male' ? "0" : "1"; // gender를 int로 변환
        var data = new FormData(); // 요것이 핵심
        data.append("model_name", this.selectedModel);
        data.append("text", this.inputText);
        data.append("gender", genderValue);
        console.log(data.keys);

        this.showAudioBox = false;
        this.loading = true; // 데이터를 보내는 중이므로 로딩 상태를 true로 변경
        const response = await fetch('http://163.180.117.43:8000/text_info', {
          method: "POST",
          body: data, // 요것이 핵심
        });
        if (!response.ok) {
          throw new Error('Failed to send text info to backend');
        }
        const responseData = await response.json(); // 응답 데이터를 responseData 변수에 저장
        console.log("Response from backend: ", responseData); // 백엔드로부터의 응답 확인
        this.listenVoice(responseData);
      
      } catch (error) {
        console.error('Error sending text info to backend: ', error);
      } finally {
        this.loading = false; // 요청이 완료되면 로딩 상태를 false로 변경
        this.listenVoice();
      }
    },

    listenVoice() {
      this.audioSrc = this.BaseaudioSrc + this.selectedModel;
      this.showAudioBox = true;
    },

  },
  mounted(){
      this.fetchModelList();
  }
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

.grey-box {
  display: flex;
  justify-content: center;
  align-items: center;
}

.input-container {
  width: 100%;
}

.audio-box {
  background-color: #ffffff; /* 박스 색상을 흰색으로 변경 */
  padding: 10px;
  margin: 5px;
  border-radius: 50px; /* 모서리 둥글게 처리 */
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* 그림자를 좀 더 부드럽게 설정 */
  text-align: center; /* 텍스트 중앙 정렬 */
  align-items: center;
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

.voice-creation-button {
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

.voice-creation-button:hover{
  background-color: rgb(87, 87, 87);
  transform: translateY(-2px);
}

.PE-button {
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

.PE-button:hover{
  background-color: rgb(87, 87, 87);
  transform: translateY(-2px);
}

.model-list-header {
  position: relative;
  text-align: center;
}

.model-list-header h4 {
  position: absolute;
  top: -75px;
  left: -50px;;
  display: inline-block;
  white-space: nowrap;
}

.model-listen-button {
  width: 150px;
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

.loading-message {
  margin-top: 20px; 
  font-size: 16px;
  color: #333;
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