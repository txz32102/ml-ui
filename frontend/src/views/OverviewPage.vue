<template>
  <div>
    <!-- Your other component HTML -->
    <img :src="overViewSvg"/>
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
</style>