<template>
  <div>
    <b-field>
      <b-input v-model="url"></b-input>
    </b-field>
    <div class="has-text-centered">
      <b-button type="is-light" @click="calculate">Calculate</b-button>
    </div>

    <div class="links" v-if="hasHashes()">
      <LinkList v-bind:hashes="hashes" />
    </div>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import { Component, Vue } from "vue-property-decorator";

import LinkList from "@/components/links/LinkList.vue";
import { Hashes } from "@/types";

@Component({
  components: {
    LinkList,
  },
})
export default class Calculator extends Vue {
  url: string | undefined = "https://www.google.com/favicon.ico";
  hashes: Hashes | undefined = undefined;

  async calculate(): Promise<void> {
    try {
      const response = await axios.get<Hashes>("/api/hashes/calculate", {
        params: { url: this.url },
      });
      this.hashes = response.data;
      this.$forceUpdate();
    } catch (error) {
      const data = error.response.data;
      if ("error" in data) {
        alert(data.error);
      } else {
        alert(error);
      }
    }
  }

  hasHashes(): boolean {
    return this.hashes !== undefined;
  }
}
</script>

<style scoped>
.links {
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
