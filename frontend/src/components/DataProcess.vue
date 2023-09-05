<script setup lang="ts">
import { ref, onMounted } from 'vue'
const greeting = ref('upload file!')
const count = ref(0)
function increment() {
  count.value++
}
onMounted(() => {
  console.log(`The initial count is ${count.value}.`)
})

function previewImage(event: Event) {
    const fileInput = event.target as HTMLInputElement;
    const file = fileInput.files?.[0];

    if (file) {
      const reader = new FileReader();

      reader.onload = (event) => {
        const imagePreview = document.getElementById('imagePreview');
        if (imagePreview) {
          imagePreview.innerHTML = `<img src="${event?.target?.result}" alt="Preview Image" width="200">`;
        }
      };

      reader.readAsDataURL(file);
    }
  }
</script>

<template>
  <p class="greeting">{{ greeting }}</p>
  <form action="/upload" method="post" enctype="multipart/form-data">
    <label for="fileUpload">Select a file:</label>
    <input type="file" id="fileUpload" name="fileUpload" onchange="previewImage(event)">
    <input type="submit" value="Upload">
  </form>
  <div id="imagePreview"></div>
  <button @click="increment">Count is: {{ count }}</button>
</template>

<style>
.greeting {
  color: rgb(155, 88, 88);
  font-weight: bold;
}
</style>