<template>
    <div>
      <input v-model="message" type="text" placeholder="Enter a message">
      <button @click="sendMessage">Send</button>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import axios, { AxiosError } from 'axios';
  
  const setup = () => {
    const message = ref('');
  
    const sendMessage = () => {
      // Create a payload object with the message
      const payload = { message: message.value };
  
      // Make a POST request to the Django server
      axios.post('/your-endpoint/', payload)
        .then(response => {
          console.log('Response:', response.data);
          // Handle the response as needed
        })
        .catch(error: AxiosError => {
          console.error('Error:', error);
          // Handle the error as needed
        });
    };
  
    return {
      message,
      sendMessage,
    };
  };
  </script>
  