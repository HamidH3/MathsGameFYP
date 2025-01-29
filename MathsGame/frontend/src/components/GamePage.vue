<!-- <template>
    <div id="game-page">
      <h1>Pygame Embedded in Vue</h1>
      <iframe
        :src="gameIframeSrc"
        width="800"
        height="600"
        frameborder="0"
      ></iframe>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        gameIframeSrc: "/static/game/index.html", // Adjust the path as needed
      };
    },
  };
  </script>
  
  <style scoped>
  #game-page {
    text-align: center;
    margin-top: 20px;
  }
  iframe {
    border: none;
  }
  </style>
   -->

   <template>
    <div class="game-container">
      <iframe
        src="http://127.0.0.1:8000/static/game/game.html"
        class="game-frame"
        frameborder="0"
        allowfullscreen
      ></iframe>
      
    </div>
  </template>
  
  <style scoped>
  .game-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .game-frame {
    width: 80vw;
    height: 80vh;
    border: none;
  }
  </style>
  