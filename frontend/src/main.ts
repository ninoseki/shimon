import "bulma/css/bulma.css"
import "font-awesome-animation/css/font-awesome-animation.min.css"

import { library } from "@fortawesome/fontawesome-svg-core"
import { faCaretDown, faCaretUp, faMoon, faSpinner, faSun } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome"
import { createApp } from "vue"

import App from "@/App.vue"

library.add(faSpinner, faSun, faMoon, faCaretDown, faCaretUp)

createApp(App).component("font-awesome-icon", FontAwesomeIcon).mount("#app")
