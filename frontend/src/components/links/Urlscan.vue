<template>
  <div>
    <span class="icon">
      <img
        src="https://www.google.com/s2/favicons?domain=urlscan.io"
        alt="urlscan.io"
      />
    </span>
    <a :href="link" target="_blank">{{ query }}</a>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

import { Hashes } from "@/types";

@Component
export default class Urlscan extends Vue {
  @Prop() hashes!: Hashes;

  get query(): string {
    return `hash:"${this.hashes.sha256}"`;
  }

  get link(): string {
    const baseUrl = "https://urlscan.io/search/#";
    return baseUrl + encodeURI(this.query);
  }
}
</script>
