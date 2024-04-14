<template>
  <button @click="$emit('click')" class="custom-button">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'ButtonComponent',
}
</script>

<style scoped>
.custom-button {
  width: 100px;
  height: 50px;
  margin: 0 5px;
  margin-bottom: 0px;
  background-color: #007aff;
  color: #ffffff;
  border: none;
  border-radius: 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}
.custom-button:hover {
  background-color: #005ecb;
  transform: translateY(-2px);
}
</style>
