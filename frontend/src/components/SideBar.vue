<template>
  <SidebarMenu :menu="menu" theme="white-theme" :width="'200px'"/>
</template>

<script>
import {SidebarMenu} from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import '@fortawesome/fontawesome-free/css/all.css'
import llt from '@/assets/icons/llt.png';
import ht from '@/assets/icons/ht.png';
import cs from '@/assets/icons/cs.png';
import ls from '@/assets/icons/ls.png';
import wd from '@/assets/icons/wd.png';
import xh from '@/assets/icons/xh-optimize.gif';

const createMenuItem = (href, title, src) => ({
  href,
  title,
  icon: {
    element: 'img',
    attributes: { src },
  },
});

export default {
  name: "SideBar",
  components: {
    SidebarMenu,
  },
  data() {
      return {
        menu: [
          {
            header: 'AI LAB',
            hiddenOnCollapse: true,
          },
          createMenuItem('/About', '简介', cs),
          createMenuItem('/Overview', '功能概述', ht),
          createMenuItem('/MachineLearning', '机器学习解释', ls),
          createMenuItem('/DeepLearning', '深度学习解释', llt),
          createMenuItem('/Visualization', '可视化展示', wd),
          createMenuItem('/KnowledgeGraph', '知识图谱', xh),
          createMenuItem('/JupyterDemo', '跳转到Notebook', xh),
        ],
      }
    },
}
</script>

<style scoped>
.SidebarMenu {
  margin-top: 60px; /* 添加这一行 */
}
</style>