<template>
    <h1 style="max-width: 40ch; margin-left: 30%; font-family: 'Times New Roman', Times, serif; font-size: 36px;">
        AI LAB:<span style="font-family: 'KaiTi', '楷体';">数据的时代</span>
    </h1>
    <main id="about-page" class="offset-content">
        <p>数据是推动未来发展的关键动力。在这个数字化日益加速的时代，AI实验室聚焦于利用最先进的技术和理论，解析和利用海量数据，从而为世界带来创新的解决方案,在这个由AI实验室精心打造的网页上，用户将体验到一个充满互动性和视觉震撼的数字世界。页面设计巧妙地将复杂的算法以简洁直观的方式呈现给用户。通过动态图表和实时数据流，用户可以直观地看到算法如何在各种场景中运作，以及它们如何影响数据分析和决策过程。此外，网页还提供了模拟工具，让用户可以实际操作这些算法，亲自体验它们的强大功能。这不仅仅是一个信息展示平台，更是一个互动式学习和探索的空间，让每一位访问者都能深刻理解和感受到数据科学的魅力。</p>
    </main>
</template>

<script>
export default {
    name: 'AboutPage',
    components: {
    }
}
</script>

<style scoped>
.full-page-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('@/assets/background/About.png');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

.full-page-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(255, 255, 255, 0.7); /* White background with 70% opacity */
    z-index: -1;
}

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
