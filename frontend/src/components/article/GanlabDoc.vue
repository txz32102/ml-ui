<template>
    <main id="about-page" class="offset-content">
      <h1 class="clickable-title" style="max-width: 40ch; font-family: 'Times New Roman', Times, serif; font-size: 36px;" @click="redirectToLocalhost">Transformer</h1>
      <p>许多机器学习系统查看某种复杂的输入(例如，图像)并产生简单的输出(如“猫”这样的标签)。相比之下，生成模型的目标恰恰相反:取一小块输入——也许是几个随机数——然后产生一个复杂的输出，比如一张看起来很逼真的脸的图像。生成对抗网络(GAN)是一种特别有效的生成模型类型，仅在几年前引入，一直是机器学习社区中非常感兴趣的主题。你可能想知道为什么我们需要一个系统来产生真实的图像，或者对任何其他类型的数据进行貌似合理的模拟。除了固有的智力挑战之外，事实证明这是一个非常方便的工具，从艺术到增强模糊图像的应用范围都很广。</p>
    </main>
  </template>
  
  <script>
  export default {
    name: 'GanlabDoc',
    methods: {
      redirectToLocalhost() {
        window.open('http://localhost:8080', '_blank');
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
  