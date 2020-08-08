<template>
  <div>
    <span class="icon">
      <img
        src="https://www.google.com/s2/favicons?domain=spyse.com"
        alt="spyse"
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
export default class Spyse extends Vue {
  @Prop() hashes!: Hashes;

  get queryType(): QueryType {
    if (this.hashes.contentType.includes("text/html")) {
      return "html";
    }
    return "favicon";
  }

  get query(): string {
    if (this.queryType === "html") {
      return "N/A";
    }

    const params = [
      {
        domain_info_favicon_hash: {
          value: this.hashes.sha256,
          operator: "eq",
        },
      },
    ];
    return JSON.stringify(params);
  }

  get link(): string {
    if (this.query === "N/A") {
      return "/";
    }

    const baseUrl = "https://spyse.com/advanced-search/domain?";
    const params = {
      search_params: this.query,
    };
    return baseUrl + qs.stringify(params);
  }
}
</script>
