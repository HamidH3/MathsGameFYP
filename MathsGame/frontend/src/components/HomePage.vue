<template>
  <div class="home">
    <h1>Welcome to the Maths Game</h1>
    <p>Start playing to improve your math skills!</p>
    <router-link to="/game" class="btn btn-primary">Start Game</router-link>
  </div>
</template>

<script>
export default {
  name: "HomePage"
};
</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 50px;
}
</style>
