<template>
  <div>
    <span class="icon">
      <img
        src="https://www.google.com/s2/favicons?domain=onyphe.io"
        alt="onyphe"
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
export default class Onyphe extends Vue {
  @Prop() hashes!: Hashes;

  get queryType(): QueryType {
    if (this.hashes.contentType.includes("text/html")) {
      return "html";
    }
    return "favicon";
  }

  get query(): string {
    if (this.queryType === "favicon") {
      return "N/A";
    }

    return `category:datascan app.http.bodymd5:"${this.hashes.md5}"`;
  }

  get link(): string {
    if (this.query === "N/A") {
      return "/";
    }

    const baseUrl = "https://onyphe.io/search/?";
    const params = {
      query: this.query,
    };
    return baseUrl + qs.stringify(params);
  }
}
</script>
