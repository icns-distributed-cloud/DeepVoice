<template>
    <div>
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
            <div class = "audioPlayer">
              <ul>
                <li v-for="(audio, index) in responseAudioList" :key="index">
                  <h3 @click="play(audio)">{{audio}}</h3>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>  
  export default {
    name: "AudioList",
    props: {
      responseAudioList: {
      type: Array,
      required: true
    }
  },
    components: {
    },
  
    data() {
      return {
        currentPage: "inference", // 현재 화면을 결정하는 데이터

      };
    },
  
    methods: {  
      play(audio){
        if(audio){
          var sound = new Audio(audio);
          sound.play();
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