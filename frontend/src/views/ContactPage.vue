<template>
    <main id="about-page" class="offset-content">
        <p>
            Identification of druggable protein can greatly reduce the cost of discovering new potential drugs. Computational methods have been used in recent years to find druggable protein with different kinds of machine learning methods. Many of these methods are very dependent on the training datasets and do not make good use of the Human Genome Project. With the help of computational power, pretrained models like ESM2 have been applied to embed the protein and feed them to all sorts of deep learning models. PSSM is also applied for the embedding in this study. Our models with different architectures are tested on multiple golden standard datasets including Pharos, DrugBank, and combined datasets generated from UniProt, and have achieved an accuracy of about 95.11% with the fine-tuning of ESM2. This is also the first time for a large language model (LLM) GPT2 to be used for protein-related classification problems. Pretrained models like ESM2 with fine-tuning or GPT2 based transformer lead to a novel binary classification method which may also have potential for other protein-related classification problems.
        </p>
    </main>
</template>

<script>
export default {
    name: 'AboutPage'
}
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
}
</style>