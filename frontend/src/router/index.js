// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import AboutPage from '../views/AboutPage.vue'
import OverviewPage from '../views/OverviewPage.vue'
import MachineLearning from '../views/MachineLearning.vue'
import FAQPage from '../views/FAQPage.vue'

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
    path: '/FAQ',
    component: FAQPage 
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
