<script setup lang="ts">
import { ref } from 'vue'
const greeting = ref('upload file!')
</script>

<template>
  <p class="greeting">{{ greeting }}</p>
  <form action="/upload" method="post" enctype="multipart/form-data">
  <label for="fileUpload">Select a file:</label>
  <input type="file" id="fileUpload" name="fileUpload">
  <input type="submit" value="Upload">
</form>
</template>

<style>
.greeting {
  color: rgb(155, 88, 88);
  font-weight: bold;
}
</style>