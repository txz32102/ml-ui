<template>
	<div>
		<main id="overview-page" class="offset-content">
        <p>
			We have developed a simple web server that predicts druggable proteins using our classification model. This model generates a 1200-dimensional feature matrix based on PSSM, utilizing the methods proposed in our paper. It also produces 320-dimensional fine-tuned ESM2 embeddings. You can upload a FASTA file, and we will process the prediction for you. However, due to computational power restrictions, it is not advisable to upload proteins with excessively long sequences.		
		</p>
    </main>
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
        <FileSelectButton @fileSelected="handleFileSelected" />
        <UploadAndDownload :file="selectedFile" @uploadComplete="handleUploadComplete" />
    </div>
	</div>
</template>

<script>
import FileSelectButton from '@/components/button/FileSelectButton.vue';
import UploadAndDownload from '@/components/button/UploadAndDownload.vue';

export default {
name: "PredictPage",

components: {
FileSelectButton,
UploadAndDownload,
},

data() {
return {
selectedFile: null,
downloadLink: ''
};
},

methods: {
handleFileSelected(file) {
this.selectedFile = file;
},

handleUploadComplete(link) {
this.downloadLink = link;
}
}
};
</script>

<style scoped>
.offset-content {
    margin-left: 25%;
    font-family: 'Times New Roman', Times, serif;
    text-align: justify;
}

.offset-content p {
    word-wrap: break-word;
    max-width: 70ch;
    font-size: 24px;
}
</style>