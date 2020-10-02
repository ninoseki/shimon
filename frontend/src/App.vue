<template>
  <div id="app">
    <Navbar />
    <section class="section is-medium">
      <div class="container">
        <h2 class="subtitle">
          Calculate HTML/favicon hashes for searching on BinaryEdge, Onyphe,
          Shodan and Spyse
        </h2>
        <Calculator />

        <hr />

        <h5 class="title is-5">Note</h5>
        <div class="content">
          It accepts the following as an input.
          <ul>
            <li><code>Base URL</code>(e.g. http://example.com)</li>
            <li><code>/favicon.ico</code></li>
            <li><code>/favicon.png</code></li>
            <li><code>/touch-icon.png</code></li>
          </ul>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import Calculator from "./components/Calculator.vue";
import Navbar from "./components/Navbar.vue";

@Component({
  components: {
    Calculator,
    Navbar,
  },
})
export default class App extends Vue {}
</script>

<style scoped></style>
