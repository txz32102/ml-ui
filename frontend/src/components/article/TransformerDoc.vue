<template>
  <main id="about-page" class="offset-content">
    <h1 
        style="max-width: 40ch; font-family: 'Times New Roman', Times, serif; font-size: 36px;"
        @click="redirectToLocalhost"
    >
      Transformer
    </h1>
    <p>Transformer是序列转导模型，擅长对非顺序处理的长期依赖关系进行建模。由于自然语言任务受益于多头注意机制，可以更有效地对较长的文本进行建模，并且非顺序计算不再抑制并行化，因此这些属性使得transformer在NLP领域中普遍存在。transformer现在取代lstm作为NLP任务的最先进的模型体系结构。</p>
  </main>
</template>

<script>
export default {
  name: 'TransformerDoc',
  methods: {
    redirectToLocalhost() {
      window.location.href = 'http://localhost:5005';
    }
  }
};
</script>

<style>
/* Your existing styles */
</style>
