import "bulma/css/bulma.css";
import "@fortawesome/fontawesome-free/css/all.css";
import "@fortawesome/fontawesome-free/js/all.js";

// Polyfill
import "regenerator-runtime/runtime";

import { createApp } from "vue";

import App from "./App.vue";

createApp(App).mount("#app");
