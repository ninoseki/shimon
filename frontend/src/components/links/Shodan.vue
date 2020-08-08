<template>
  <div>
    <span class="icon">
      <img
        src="https://www.google.com/s2/favicons?domain=shodan.io"
        alt="shodan"
      />
    </span>
    <a :href="link" target="_blank">{{ query }}</a>
  </div>
</template>

<script lang="ts">
import * as qs from "qs";
import { Component, Prop, Vue } from "vue-property-decorator";

import { Hashes, QueryType } from "@/types";

@Component
export default class Shodan extends Vue {
  @Prop() hashes!: Hashes;

  get queryType(): QueryType {
    if (this.hashes.contentType.includes("text/html")) {
      return "html";
    }
    return "favicon";
  }

  get query(): string {
    if (this.queryType === "html") {
      return `http.html_hash:${this.hashes.mmh3}`;
    }

    return `http.favicon.hash:${this.hashes.mmh3}`;
  }

  get link(): string {
    const baseUrl = "https://shodan.io/search?";
    const params = {
      query: this.query,
    };
    return baseUrl + qs.stringify(params);
  }
}
</script>
