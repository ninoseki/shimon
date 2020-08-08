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
import { ErrorData, Hashes } from "@/types";

@Component({
  components: {
    LinkList,
  },
})
export default class Calculator extends Vue {
  url: string | undefined = "https://www.google.com/favicon.ico";
  hashes: Hashes | undefined = undefined;

  async calculate(): Promise<void> {
    const loadingComponent = this.$buefy.loading.open({
      container: this.$el,
    });
    this.hashes = undefined;

    try {
      const response = await axios.get<Hashes>("/api/hashes/calculate", {
        params: { url: this.url },
      });
      this.hashes = response.data;

      loadingComponent.close();
    } catch (error) {
      loadingComponent.close();

      const data = error.response.data as ErrorData;
      alert(data.detail);
    }
    this.$forceUpdate();
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
