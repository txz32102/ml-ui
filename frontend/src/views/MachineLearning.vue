<template>
  <div class="centered-container">
    <div class="content">
      <!-- Include the HTML content from MachineLearningDoc.html -->
      <div v-html="htmlContent"></div>
    </div>
  </div>
</template>

<script>
import MachineLearningDocHTML from '@/assets/doc/MachineLearningDoc.html';

export default {
  data() {
    return {
      htmlContent: MachineLearningDocHTML
    };
  }
};
</script>

<style scoped>
.centered-container {
  display: flex;
  justify-content: center; /* Horizontally center content */
  align-items: center;     /* Vertically center content */
  height: 100vh;           /* Set container height to full viewport height */
}

</style>
