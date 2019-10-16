<template>
  <section id="app" class="section is-medium">
    <div class="container">
      <h1 class="title">mmhdan</h1>
      <h2 class="subtitle">Calculate MurmurHash3 value for Shodan search</h2>
      <Calculator />
    </div>
  </section>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Calculator from "./components/Calculator.vue";

@Component({
  components: {
    Calculator
  }
})
export default class App extends Vue {}
</script>
