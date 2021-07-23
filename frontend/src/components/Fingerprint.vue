<template>
  <div class="box">
    <div class="content is-normal">
      <div class="mt-4 mb-4">
        <h4 class="is-size-4">HTML</h4>
        <ul>
          <li><strong>URL:</strong> {{ fingerprint.html.url }}</li>
          <li><strong>MMH3:</strong> {{ fingerprint.html.mmh3 }}</li>
          <li><strong>MD5:</strong> {{ fingerprint.html.md5 }}</li>
          <li><strong>SHA1:</strong> {{ fingerprint.html.sha1 }}</li>
          <li><strong>SHA256:</strong> {{ fingerprint.html.sha256 }}</li>
        </ul>
      </div>

      <div class="mt-4 mb-4">
        <h4 class="is-size-4">DNS</h4>
        <ul>
          <li>
            <strong>A:</strong>
            <span v-if="fingerprint.dns.a">
              {{
                " " + fingerprint.dns.a.map((record) => record.host).join(", ")
              }}
            </span>
            <span v-else> N/A</span>
          </li>
          <li>
            <strong>AAAA:</strong>
            <span v-if="fingerprint.dns.aaaa">
              {{
                " " +
                fingerprint.dns.aaaa.map((record) => record.host).join(", ")
              }}
            </span>
            <span v-else> N/A</span>
          </li>
          <li>
            <strong>CNAME:</strong>
            <span v-if="fingerprint.dns.cname">
              {{
                " " +
                fingerprint.dns.cname.map((record) => record.cnmae).join(", ")
              }}
            </span>
            <span v-else> N/A</span>
          </li>
          <li>
            <strong>TXT:</strong>
            <span v-if="fingerprint.dns.txt">
              {{
                " " +
                fingerprint.dns.txt.map((record) => record.text).join(", ")
              }}
            </span>
            <span v-else> N/A</span>
          </li>
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
            <strong>SHA1:</strong> {{ fingerprint.favicon?.sha1 || "N/A" }}
          </li>
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
