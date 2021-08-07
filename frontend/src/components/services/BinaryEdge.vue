<template>
  <div class="column is-half">
    <div class="box">
      <div class="content is-normal">
        <h4 class="is-size-4">
          <span class="icon">
            <img
              src="https://www.google.com/s2/favicons?domain=binaryedge.io"
              alt="binaryedge"
            />
          </span>
          BinaryEdge
        </h4>

        <ul>
          <li>
            <a target="_blank" :href="htmlLink">HTML</a>
          </li>
          <li v-if="faviconLink">
            <a target="_blank" :href="faviconLink">Favicon</a>
          </li>
          <li v-if="certificateLink">
            <a target="_blank" :href="certificateLink">Certificate</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import * as qs from "qs";
import { computed, defineComponent, PropType } from "vue";

import { Fingerprint } from "@/types";
import { convertToColonSeparatedText } from "@/utils";

export default defineComponent({
  name: "BinaryEdge",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
  setup(props) {
    const createLink = (query: string): string => {
      const baseUrl = "https://app.binaryedge.io/services/query?";
      const params = {
        query,
      };
      return baseUrl + qs.stringify(params);
    };

    const htmlLink = computed(() => {
      const query = `web.body.sha256:${props.fingerprint.html.sha256}`;
      return createLink(query);
    });

    const faviconLink = computed(() => {
      if (props.fingerprint.favicon === null) {
        return undefined;
      }

      const query = `http.favicon.md5:${props.fingerprint.favicon.md5}`;
      return createLink(query);
    });

    const certificateLink = computed(() => {
      if (props.fingerprint.certificate === null) {
        return undefined;
      }

      const sha1 = convertToColonSeparatedText(
        props.fingerprint.certificate.sha1
      );
      const query = `ssl.cert.sha1_fingerprint:"${sha1}"`;
      return createLink(query);
    });

    return { htmlLink, faviconLink, certificateLink };
  },
});
</script>
