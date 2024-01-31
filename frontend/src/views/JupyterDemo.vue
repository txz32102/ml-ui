<template>
    <h1>
        Are you ok?
    </h1>
    <div>
        <iframe src="http://localhost:8888/tree#notebooks" width="100%" height="600"></iframe>
    </div>
</template>

<script>
export default {
    name: "JupyterDemo",
};
</script>

<style scoped>

.content {
  position: relative;
  z-index: 2; /* Ensure it's above the background */
}

h1 {
  max-width: 40ch;
  margin-left: 30%;
  font-family: 'Times New Roman', Times, serif;
  font-size: 36px;
}

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