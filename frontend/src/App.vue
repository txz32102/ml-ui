<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'

import axios from 'axios';
// const res = await axios.get(`https://finalspaceapi.com/api/v0/character/?limit=2`);

const res = await axios.get(`http://127.0.0.1:8000/api/`);
console.log(res)

// Data to send
// const data = {
//   name: 'John Doe',
//   email: 'johndoe@example.com'
// };

// // Send POST request
// axios.post('https://example.com/api/endpoint', data)
//   .then(response => {
//     // Handle response
//     console.log(response.data);
//   })
//   .catch(error => {
//     // Handle error
//     console.error(error);
//   });
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
  <form action="/your-name/" method="post">
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name" value="{{ current_name }}">
    <input type="submit" value="OK">
  </form>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
