<template>
  <div id="app">
    <NavBar />
    <div class="main">
      <SideBar />
      <div class="content">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import SideBar from './components/SideBar.vue'
export default {
  name: 'App',
  components: {
    NavBar,
    SideBar,
  },
};
</script>

<style>
html, body, #app {
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
}

.main {
  display: flex;
  flex-direction: row;
  height: calc(100% - 60px); /* Assuming your NavBar is 60px high */
}

.content {
  flex-grow: 1;
}
</style>