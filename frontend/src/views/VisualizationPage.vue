<template>
    <h1 style="max-width: 40ch; margin-left: 30%; font-family: 'KaiTi', '楷体'; font-size: 36px;">
      可视化展示
    </h1>
  <TransformerDoc />
</template>

<script>
import ml_intro1 from '../assets/background/ml_intro1.svg';
import TransformerDoc from '@/components/article/TransformerDoc.vue';
export default {
  components: {
    TransformerDoc,
  },
  data() {
    return {
      ml_intro1: ml_intro1
    };
  }
  // Your component details
};
</script>

<style scoped>

.content {
  position: relative;
  z-index: 2; /* Ensure it's above the background */
}

h1 {
  max-width: 40ch;
  margin-left: 30%;
  font-family: 'Times New Roman', Times, serif;
  font-size: 36px;
}

.offset-content {
  margin-left: 25%;
  font-family: 'Times New Roman', Times, serif;
  text-align: justify;
}

.offset-content p {
  word-wrap: break-word;
  max-width: 70ch;
  font-size: 24px;
}
</style>
