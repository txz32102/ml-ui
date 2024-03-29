<template>
  <h1 style="max-width: 40ch; margin-left: 30%; font-family: 'KaiTi', '楷体'; font-size: 36px;">
    深度学习解释
  </h1>
<main id="about-page" class="offset-content">
    <p><strong>深度学习的定义</strong></p>
    <p>深度学习是机器学习 (ML) 的一个子集，指人工神经网络（由算法建模而成，能够像人的大脑一样工作）学习大量数据。</p>
    <p><strong>深度学习的工作原理是什么？</strong></p>
    <p>深度学习由神经网络层驱动。神经网络由一系列算法按照人类大脑的工作方式松散建模而成，而使用大量数据进行训练，即对神经网络的神经进行配置。经过训练后，深度学习模型可以处理新数据，能够摄取并实时分析多个来源的数据，无需人为干预。在深度学习中，图形处理单元 (GPU) 可以同时处理多个计算，以优化方式训练深度学习模型。在现实中，深度学习助力众多人工智能 (AI) 技术改善自动化和分析任务。绝大多数人每天都会接触到深度学习，例如在浏览互联网或使用手机时。深度学习可为 YouTube 视频生成摘要；在手机和智能音箱上执行语音识别；针对图片开展人脸识别；驱动无人驾驶汽车。随着数据科学家和研究人员不断运用深度学习框架来处理日益复杂的深度学习项目，深度学习将逐步成为我们日常生活的一部分。</p>
    <p><strong>深度学习与神经网络有何区别？</strong></p>
    <p>简单来说，深度学习就是具有多个神经层的神经网络的另一种说法。为了充分利用观测数据（例如图片或音频），神经网络会跨互联的神经网络节点层传递数据。在每一个节点层上，每一个节点都会对数据进行简单运算，并有选择地将数据传递到其他节点。随着数据不断传递，每一个节点层都会利用比上一层更高级的特性来处理数据，直至输出结果。在输入层与输出层之间，所有的神经网络层均被称为隐藏层。神经网络与深度学习的区别在于，一个基本的神经网络可能拥有一个或两个隐藏层，而一个深度学习网络可能拥有数十个甚至数百个隐藏层。一般来说，层数和节点越多，结果就越准确。不过，层数越多，深度学习模型的参数和对计算的需求就越多。神经网络可通过一组输入层来接收原始数据，而深度学习可以通过神经网络层对信息进行分类。例如，经过鸟类图像训练的神经网络可以识别鸟类图像。更多的层意味着更准确的结果，例如随着层数增加，神经网络能够从区分乌鸦和鸡升级到区分渡鸦和乌鸦。此外，深度学习算法驱动的深度神经网络拥有多个隐藏层（位于输入节点和输出节点之间），可以完成更加复杂的数据分类工作。深度学习算法必须基于大量的数据进行训练，它接收的数据越多，就越准确。例如，只有经过数千张鸟类图像的训练，算法才能准确地对新的鸟类图像进行分类。对于神经网络而言，深度学习模型训练是一项资源密集型工作。在训练中，神经网络摄取数据（即输入），然后隐藏层基于权重（即表示输入数据之间连接强度的参数，将在训练过程中适时调整）对数据进行处理，最后输出预测。其中，权重将基于训练所使用的输入数据进行调整，以此来优化预测。深度学习模型需要耗费大量时间来训练海量数据，因此，高性能计算不可或缺。GPU 针对数据计算进行了专门优化，旨在提高大规模矩阵计算的性能。它尤其适用于并行执行大规模机器学习 (ML) 和深度学习，可帮助机器学习应用高效地对大量结构化或非结构化数据（例如图像、文本和语音）执行大量运算，实现超强性能。</p>
    <p><strong>使用深度学习的 5 大理由</strong></p>
    <p>分析非结构化数据</p>
    <p>深度学习算法可以分析社交媒体帖子、新闻资讯和调查报告，从而探查文本数据，提供有价值的业务和客户洞察。</p>
    <p>数据标记</p>
    <p>深度学习模型的训练离不开标记数据。经过训练，深度学习模型可以自行标记新数据，识别各类数据。</p>
    <p>特征工程</p>
    <p>机器学习算法可显著节约时间 — 无需手动从原始数据中提取特征。</p>
    <p>效率</p>
    <p>经过适当训练，深度学习算法能够以远超人类的速度，持续执行数千项任务。</p>
    <p>训练</p>
    <p>在深度学习中，神经网络适用于多种类型的数据和应用。而通过使用新数据重新训练，深度学习模型可响应新的变化。</p>
    <img :src="ml_intro1"/>
</main>
</template>

<script>
import ml_intro1 from '../assets/background/ml_intro1.svg';
export default {
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
