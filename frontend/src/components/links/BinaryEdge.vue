<template>
  <div>
    <span class="icon">
      <img
        src="https://www.google.com/s2/favicons?domain=binaryedge.io"
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
export default class BinaryEdge extends Vue {
  @Prop() hashes!: Hashes;

  get queryType(): QueryType {
    if (this.hashes.contentType.includes("text/html")) {
      return "html";
    }
    return "favicon";
  }

  get query(): string {
    if (this.queryType === "html") {
      return `web.body.sha256:${this.hashes.sha256}`;
    }

    return `web.favicon.md5:${this.hashes.md5}`;
  }

  get link(): string {
    const baseUrl = "https://app.binaryedge.io/services/query?";
    const params = {
      query: this.query,
    };
    return baseUrl + qs.stringify(params);
  }
}
</script>
