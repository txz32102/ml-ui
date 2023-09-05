<script setup lang="ts">
import { ref } from 'vue'
const greeting = ref('upload file!')
function showPreview(event){
  if(event.target.files.length > 0){
    var src = URL.createObjectURL(event.target.files[0]);
    var preview = document.getElementById("file-ip-1-preview");
    preview.src = src;
    preview.style.display = "block";
  }
}
</script>

<template>
  <p class="greeting">{{ greeting }}</p>
  <form action="/upload" method="post" enctype="multipart/form-data">
  <label for="fileUpload">Select a file:</label>
  <input type="file" id="fileUpload" name="fileUpload">
  <input type="submit" value="Upload">
  </form>

  <label for="file-ip-1">Upload Image</label>
 <input type="file" id="file-ip-1" accept="image/*" onchange="showPreview(event);">
  <div class="center">

  <div class="form-input">

    <div class="preview">
   <img id="file-ip-1-preview">
 </div>

  </div>
</div> 
</template>

<style>
.greeting {
  color: rgb(155, 88, 88);
  font-weight: bold;
}
</style>