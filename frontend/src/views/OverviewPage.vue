<template>
  <div>
    <!-- Your other component HTML -->
    <img :src="overViewSvg" alt="Overview Background"/>
    <!-- More of your component HTML -->
  </div>
</template>

<script>
import OverViewSvg from '../assets/background/OverView.svg';

export default {
  data() {
    return {
      overViewSvg: OverViewSvg
    };
  }
  // Your component details
};
</script>

<style>
.full-screen {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}

.full-screen-img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover; /* or 'contain' depending on your need */
  top: 0;
  left: 0;
}
</style>