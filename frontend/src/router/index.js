// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import AboutPage from '../views/AboutPage.vue'
import PredictPage from '../views/PredictPage.vue'
import ResultPage from '../views/ResultPage.vue'
import ContactPage from '../views/ContactPage.vue'
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
    path: '/Predict',
    component: PredictPage
  },
  {
    path: '/Result',
    component: ResultPage 
  },
  {
    path: '/Contact',
    component: ContactPage 
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
