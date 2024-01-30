<template>
  <main id="about-page" class="offset-content">
    <h1 class="clickable-title" style="max-width: 40ch; font-family: 'Times New Roman', Times, serif; font-size: 36px;" @click="redirectToLocalhost">Transformer</h1>
    <p>Transformer是序列转导模型，擅长对非顺序处理的长期依赖关系进行建模。由于自然语言任务受益于多头注意机制，可以更有效地对较长的文本进行建模，并且非顺序计算不再抑制并行化，因此这些属性使得transformer在NLP领域中普遍存在。transformer现在取代lstm作为NLP任务的最先进的模型体系结构。</p>
  </main>
</template>

<script>
export default {
  name: 'TransformerDoc',
  methods: {
    redirectToLocalhost() {
      window.open('http://localhost:5005', '_blank');
    }
  }
};
</script>

<style>
h1.clickable-title {
    max-width: 40ch;
    font-family: 'Times New Roman', Times, serif;
    font-size: 36px;
    cursor: pointer; /* Change cursor to indicate clickability */
    transition: color 0.3s; /* Smooth transition for color change */
}

h1.clickable-title:hover {
    color: blue; /* Change color to blue on hover */
}
.content {
    position: relative;
    z-index: 2; /* Ensure it's above the background */
}

h1 {
    max-width: 40ch;
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
