<template>
  <div id="app">
    <Navbar />
    <section class="section is-medium">
      <div class="container">
        <h2 class="subtitle">
          Calculate HTML/favicon hashes for searching on BinaryEdge, Shodan and
          Spyse
        </h2>
        <Calculator />

        <hr />

        <h5 class="title is-5">Note</h5>
        <p class="content">
          It only accepts a
          <code>base URL</code> and <code>/favicon.ico</code> as an input.
        </p>
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
