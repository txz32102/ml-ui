// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import AboutPage from '../views/AboutPage.vue'
import OverviewPage from '../views/OverviewPage.vue'
import MachineLearning from '../views/MachineLearning.vue'
import DeepLearning from '../views/DeepLearning.vue'
import VisualizationPage from "../views/VisualizationPage.vue"
import KnowledgeGraph from "../views/KnowledgeGraph.vue"
import JupyterNotebook from '../views/JupyterDemo.vue'

const routes = [
  {
    path: '/',  
    component: AboutPage
  },
  {
    path: '/About',
    component: AboutPage
  },
  {
    path: '/Overview',
    component: OverviewPage
  },
  {
    path: '/MachineLearning',
    component: MachineLearning 
  },
  {
    path: '/DeepLearning',
    component: DeepLearning 
  },
  {
    path: '/Visualization',
    component: VisualizationPage 
  },
  {
    path: '/KnowledgeGraph',
    component: KnowledgeGraph 
  },
  {
    path: '/JupyterNotebook',
    component: JupyterNotebook 
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
