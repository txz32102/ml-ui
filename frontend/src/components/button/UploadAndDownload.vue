<template>
  <div>
    <button @click="uploadFile" class="green-button">Upload File</button>
    <button @click="downloadFile" class="green-button">Download File</button>
  </div>
</template>

<script>
export default {
  name: "UploadAndDownload",
  props: {
    file: File
  },
  data() {
    return {
      isDownloadLinkUnavailable: true,
      requestedFileLink: null
    };
  },

  methods: {
    async uploadFile() {
      if (!this.file) {
        alert("No file selected.");
        return;
      }

      const formData = new FormData();
      formData.append('file', this.file);
      const now = new Date();
      const uploadTime = now.getFullYear().toString().padStart(4, '0') + '-' +
                         (now.getMonth() + 1).toString().padStart(2, '0') + '-' +
                         now.getDate().toString().padStart(2, '0') + ' ' +
                         now.getHours().toString().padStart(2, '0') + ':' +
                         now.getMinutes().toString().padStart(2, '0') + ':' +
                         now.getSeconds().toString().padStart(2, '0') + '.' +
                         now.getMilliseconds().toString().padStart(3, '0');
      formData.append('uploadTime', uploadTime);
      const [datePart, timePart] = uploadTime.split(' ');
      const [year, month, day] = datePart.split('-');
      const [hour, minute, secondWithMilliseconds] = timePart.split(':');
      const [second] = secondWithMilliseconds.split('.');
      this.requestedFileLink = `result_${year}-${month}-${day}_${hour}-${minute}-${second}.zip`;      
      console.log(this.requestedFileLink);
      
      try {
        const response = await fetch('http://localhost:8900/upload', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          const result = await response.json();
          alert(result.message); 
          this.isDownloadLinkUnavailable = false; 
        } else {
          alert("Failed to upload file.");
          this.isDownloadLinkUnavailable = true; 
        }
      } catch (error) {
        console.error("Error during file upload:", error);
        alert("Error during file upload.");
        this.isDownloadLinkUnavailable = true;
      }
    },

    async downloadFile() {
    if (this.requestedFileLink) {
      try {
        const response = await fetch(`http://localhost:8900/static/processed/${this.requestedFileLink}`, {
          method: 'HEAD' // Use HEAD request to check if the file exists
        });

        if (response.ok) {
          // If the file exists, proceed with downloading
          window.location.href = `http://localhost:8900/static/processed/${this.requestedFileLink}`;
        } else {
          // If the file does not exist, inform the user
          alert("File is still processing. Please try downloading again later.");
        }
      } catch (error) {
        console.error("Error during file check:", error);
        alert("An error occurred while checking the file. Please try again.");
      }
    } else {
      alert("File not available for download.");
    }
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