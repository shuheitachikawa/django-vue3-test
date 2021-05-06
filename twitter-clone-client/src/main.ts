import { createApp } from "vue";
import App from "./App.vue";
import "./assets/index.css";
import router from "./router/index";
import { store } from "./store/index";
import timestamp from "./plugins/timestamp"

const app = createApp(App);

app.use(router);
app.use(store);

app.use(timestamp)

app.mount("#app");
