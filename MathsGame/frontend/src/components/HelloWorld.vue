<template>
  <div class="game-container">
    <h1>Pygame Embedded in Django</h1>
    <iframe
      :src="gameUrl"
      width="800"
      height="600"
      frameborder="0"
      allowfullscreen
    ></iframe>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // Assuming the static file for the game is located under static/game/index.html
      gameUrl: 'static/game/index.html',
    };
  },
};
</script>

<style scoped>
.game-container {
  text-align: center;
  padding: 20px;
}

h1 {
  font-size: 2rem;
  margin-bottom: 20px;
}

iframe {
  border: none;
}
</style>
