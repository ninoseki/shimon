<template>
  <div id="app">
    <Navbar></Navbar>
    <section class="section is-medium">
      <div class="container">
        <h2 class="subtitle">URL fingerprinting made easy.</h2>
        <Calculator></Calculator>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue"

import Calculator from "@/components/Calculator.vue"
import Navbar from "@/components/Navbar.vue"

export default defineComponent({
  name: "App",
  components: {
    Navbar,
    Calculator
  }
})
</script>
