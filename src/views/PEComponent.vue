<template>
    <div>
      <div v-if="currentPage === 'PE'">
        <!-- 예방 교육 페이지 -->
        <LogoComponent />
        <TitleComponent >
          <span class="ccrc">CCRC </span>
          <span class="deep-voice">딥보이스 </span>
          <span class="experience">체험</span>
        </TitleComponent>
        <div class="white-box">
          <button @click="$emit('changePage', 'inference')" class="back-button">뒤로 가기</button>
          <h2>딥보이스 범죄를 예방하려면</h2>
          <div class = "big-grey-box">
            <h4>- 전화로 자금이체를 요구하면 일단 보이스피싱인지 의심하세요.</h4>
            <h4>- 납치, 협박 전화를 받는 경우 가족의 안전부터 확인하세요.</h4>
            <h4>- 가족 등 사칭 금전 요구 시 먼저 본인인지 확인하세요.</h4>
            <h4>- 출처 불명 파일, 이메일, 문자는 클릭하지 말고 삭제하세요.</h4>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  //import ButtonComponent from "../components/ButtonComponent.vue";
  import TitleComponent from "../components/TitleComponent.vue";
  import LogoComponent from "../components/LogoComponent.vue";
  
  export default {
    name: "PEComponent",
  
    components: {
      //ButtonComponent,
      TitleComponent,
      LogoComponent,
    },
  
    data() {
      return {
        currentPage: "PE", // 현재 화면을 결정하는 데이터
      };
    },
  
    methods: {

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

  .big-grey-box {
    background-color: #e0e0e0; 
    padding: 20px;
    margin: 10px auto;
    width: 70%;
    height: 60%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    text-align: center;
  }

  .big-grey-box h4 {
    text-align: left;
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