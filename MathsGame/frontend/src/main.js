import { createApp } from 'vue'
import App from './App.vue'
import router from './router';

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

//App acts as root component. 
/* using router allows for navigation in App.vue, 
where the navlinks are being called*/
const app = createApp(App); 
app.use(router); 
app.mount('#app'); 
