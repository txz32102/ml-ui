<template>
    <main id="about-page" class="offset-content">
      <h1 class="clickable-title" style="max-width: 40ch; font-family: 'KaiTi', '楷体', Times, serif; font-size: 36px;" @click="redirectToLocalhost">卷积神经网络</h1>
      <p>在机器学习中，分类器为数据点分配一个类标签。例如，图像分类器为图像中存在的对象生成一个类标签(例如，bird, plane)。卷积神经网络，简称CNN，是一种分类器，它擅长解决这个问题!CNN是一种神经网络:一种用于识别数据模式的算法。一般来说，神经网络是由一组神经元组成的，这些神经元是分层组织的，每个神经元都有自己的可学习权值和偏差。让我们把CNN分解成它的基本组成部分。</p>
    </main>
  </template>
  
  <script>
  export default {
    name: 'CnnDoc',
    methods: {
      redirectToLocalhost() {
        window.open('http://localhost:3000', '_blank');
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
  