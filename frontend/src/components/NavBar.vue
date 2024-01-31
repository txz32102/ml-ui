<template>
  <nav class="navbar">
    AI LAB
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
};
</script>

<style scoped>
.navbar {
  background-color: black;
  color: white;
  padding: 10px;
  font-size: 20px;
  text-align: left;
  z-index: 1000; /* 添加这一行 */
  position: relative; /* 添加这一行，因为 z-index 只对定位元素有效 */
  height: 20px;
}
</style>