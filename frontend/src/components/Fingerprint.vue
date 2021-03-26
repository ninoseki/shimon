<template>
  <div class="box">
    <div class="content is-normal">
      <div class="mt-4 mb-4">
        <h4 class="is-size-4">HTML</h4>
        <ul>
          <li><strong>URL:</strong> {{ fingerprint.html.url }}</li>
          <li><strong>MMH3:</strong> {{ fingerprint.html.mmh3 }}</li>
          <li><strong>MD5:</strong> {{ fingerprint.html.md5 }}</li>
          <li><strong>SHA256:</strong> {{ fingerprint.html.sha256 }}</li>
        </ul>
      </div>

      <div class="mt-4 mb-4">
        <h4 class="is-size-4">Favicon</h4>
        <ul>
          <li><strong>URL:</strong> {{ fingerprint.favicon?.url || "N/A" }}</li>
          <li>
            <strong>MMH3:</strong> {{ fingerprint.favicon?.mmh3 || "N/A" }}
          </li>
          <li><strong>MD5:</strong> {{ fingerprint.favicon?.md5 || "N/A" }}</li>
          <li>
            <strong>SHA256:</strong> {{ fingerprint.favicon?.sha256 || "N/A" }}
          </li>
        </ul>
      </div>

      <div class="mt-4 mb-4">
        <h4 class="is-size-4">Certificate</h4>
        <ul>
          <li>
            <strong>SHA1:</strong> {{ fingerprint.certificate?.sha1 || "N/A" }}
          </li>
          <li>
            <strong>SHA256:</strong>
            {{ fingerprint.certificate?.sha256 || "N/A" }}
          </li>
          <li>
            <strong>Serial:</strong>
            {{ fingerprint.certificate?.serial || "N/A" }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

import { Fingerprint } from "@/types";

export default defineComponent({
  name: "Fingerprint",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
});
</script>
