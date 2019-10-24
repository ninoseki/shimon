<template>
  <div id="app">
    <section class="section is-medium">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-half">
            <h1 class="title">mmhdan</h1>
            <h2 class="subtitle">Calculate MurmurHash3 value for Shodan search</h2>
            <Calculator />

            <hr />

            <h5 class="title is-5">Note</h5>
            <p class="content">
              It only accepts a
              <code>base URL</code> and
              <code>/favicon.ico</code> as an input.
            </p>

            <h5 class="title is-5">References</h5>
            <ul class="content">
              <li>
                <a
                  href="https://help.shodan.io/mastery/property-hashes"
                  target="_blank"
                >Pivoting with Property Hashes</a>
              </li>
              <li>
                <a
                  href="https://www.sderosiaux.com/articles/2017/08/26/the-murmur3-hash-function--hashtables-bloom-filters-hyperloglog/"
                  target="_blank"
                >The murmur3 hash function: hashtables, bloom filters, hyperloglog</a>
              </li>
              <li>
                <a
                  href="https://www.cnblogs.com/miaodaren/p/9177379.html"
                  target="_blank"
                >Shodan的http.favicon.hash语法详解与使用技巧</a>
              </li>
            </ul>

            <h5 class="title is-5">Source code</h5>
            <ul class="content">
              <li>
                <a href="https://github.com/ninoseki/mmhdan" target="_blank">ninoseki/mmhdan</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  </div>
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

<style scoped>
</style>
