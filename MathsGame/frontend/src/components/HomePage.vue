<!-- <template>
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
</style> -->

<template>
  <div class="home">
    <h1> Welcome to the Maths Game! </h1>
    <p>🧮 Have fun while learning and improving your math skills! 🚀</p>

    <!-- Form to input username -->
    <div class="username-form">
      <input v-model="newUser.username" type="text" placeholder="Enter Username" />
      <button @click="saveUsername" class="btn-saveusername">Save Username</button>
    </div>

    <router-link to="/game" class="btn">🎮 Start Game</router-link>
  </div>
</template>

<script>
const baseURL = "http://localhost:8000";

export default {
  name: "HomePage",
  data() {

    return {
      users:[],
      newUser:{
        username: "",  
      }
      
    };
  },
  methods:{
  async saveUsername(){
    if (!this.newUser.username || !this.newUser.username.trim()){
      alert("Please enter a valid username!");
      return;
    }
    const response = await fetch(`${baseURL}/game/users/create/`, {
      method:'POST',
      headers:{
        'Content-Type': 'application/json',
      },
      body:JSON.stringify({
        username: this.newUser.username,
      }),
    });
    if (response.ok){
      const newUser = await response.json();
      this.users.push(newUser);

      //reset users data
      this.newUser = {
        username:'',
      };
    }
    
  }
}
};

</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 50px;
  background-color: #B3E5FC;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
}

h1 {
  color: #FF4081; /* Pink */
  font-family: 'Comic Sans MS', cursive, sans-serif;
  font-size: 32px;
}

p {
  color: #51017b; /* Orange */
  font-size: 18px;
  font-weight: bold;
}

.btn {
  display: inline-block;
  background: linear-gradient(135deg, #4CAF50, #8BC34A); /* Green gradient */
  color: white;
  padding: 12px 25px;
  font-size: 20px;
  font-weight: bold;
  border-radius: 30px;
  text-decoration: none;
  transition: transform 0.2s, background 0.3s;
}

.btn:hover {
  background: linear-gradient(135deg, #43A047, #7CB342); /* Darker green */
  transform: scale(1.1);
}
.btn-saveusername {
  display: inline-block;
background: blue;
  color: white;
  padding: 0.2rem 1rem;
  font-size: 0.8rem;
  font-weight: bold;
  border-radius: 8px;
  text-decoration: none;
  transition: transform 0.2s, background 0.3s;
}

.btn-saveusername:hover {
 
  transform: scale(1.1);
}
</style>
