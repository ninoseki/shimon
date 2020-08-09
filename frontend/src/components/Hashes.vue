<template>
  <div class="box">
    <ul>
      <li><strong>MMH3:</strong> {{ hashes.mmh3 }}</li>
      <li><strong>MD5:</strong> {{ hashes.md5 }}</li>
      <li><strong>SHA256:</strong> {{ hashes.sha256 }}</li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

import { Hashes } from "@/types";

@Component
export default class HashesComponent extends Vue {
  @Prop() hashes!: Hashes;
}
</script>
