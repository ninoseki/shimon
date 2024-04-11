<template>
  <Navbar />
  <section class="section is-medium">
    <div class="container">
      <h2 class="subtitle">URL fingerprinting made easy.</h2>
      <Calculator />
    </div>
  </section>
</template>

<script setup lang="ts">
import Calculator from "@/components/CalculatorItem.vue"
import Navbar from "@/components/NavbarItem.vue"
</script>
