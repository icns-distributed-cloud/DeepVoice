<template>
  <div class="logo-container">
    <img src="@/assets/ccrc_logo.png" alt="CCRC 로고" />
  </div>
</template>

<script>
export default {
  name: 'LogoComponent',
}
</script>

<style scoped>
.logo-container {
  position: absolute;
  top: 20px;
  right: 20px;
}

.logo-container img {
  width: 220px;
  height: auto;
}
</style>
