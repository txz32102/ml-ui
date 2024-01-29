<template>
  <div>
    <button @click="selectFile" class="green-button">Select FASTA File</button>
    <input type="file" ref="fileInput" @change="handleFileChange" style="display: none" />
    <div v-if="fileName" class="file-name">{{ fileName }}</div>
  </div>
</template>

<script>
export default {
  name: "FileSelectButton",

  data() {
    return {
      fileName: null,
    };
  },

  methods: {
    selectFile() {
      this.$refs.fileInput.click();
    },

    handleFileChange(event) {
      const file = event.target.files[0];
      
      if (!file) {
        return;
      }

      this.fileName = file.name; // Store the file name

      if (!this.isValidFastaFile(file)) {
        alert("Please select a valid FASTA file that is less than 3KB.");
        return;
      }

      this.$emit('fileSelected', file);
    },

    isValidFastaFile(file) {
      const maxSize = 3 * 1024; // 3KB
      return file.size <= maxSize;
    }
  }
};
</script>

<style scoped>
.green-button {
  background-color: green;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 8px;
}

/* Add any additional button styling here */
</style>
