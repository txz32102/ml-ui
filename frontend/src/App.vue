<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/>
  <ThreeButton @file-selected="handleFileSelected" /> -->
  <SideBar />
  <router-view />
</template>

<script>
import SideBar from './components/SideBar.vue'
export default {
  name: 'App',
  components: {
    SideBar,
},
};
// import HelloWorld from './components/HelloWorld.vue';
// import ThreeButton from './components/ThreeButton.vue';

// export default {
//   name: 'App',
//   components: {
//     ThreeButton,
//     HelloWorld
// },
//   methods: {
//     handleFileSelected(selectedFile) {
//       console.log('Selected file:', selectedFile);
//     },
//   },
// };
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
