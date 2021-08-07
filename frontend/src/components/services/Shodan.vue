<template>
  <div class="column is-half">
    <div class="box">
      <div class="content is-normal">
        <h4 class="is-size-4">
          <span class="icon">
            <img
              src="https://www.google.com/s2/favicons?domain=shodan.io"
              alt="shodan"
            />
          </span>
          Shodan
        </h4>

        <ul>
          <li v-for="link in aLinks" :key="link.key">
            <a target="_blank" :href="link.link">{{ link.key }}</a>
          </li>

          <li><a target="_blank" :href="htmlLink">HTML</a></li>

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

export default defineComponent({
  name: "Shodan",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
  setup(props) {
    const createLink = (query: string): string => {
      const baseUrl = "https://shodan.io/search?";
      const params = {
        query,
      };
      return baseUrl + qs.stringify(params);
    };

    const htmlLink = computed(() => {
      const query = `http.html_hash:${props.fingerprint.html.mmh3}`;
      return createLink(query);
    });

    const faviconLink = computed(() => {
      if (props.fingerprint.favicon === null) {
        return undefined;
      }

      const query = `http.favicon.hash:${props.fingerprint.favicon.mmh3}`;
      return createLink(query);
    });

    const certificateLink = computed(() => {
      if (props.fingerprint.certificate === null) {
        return undefined;
      }

      const query = `ssl.cert.serial:${props.fingerprint.certificate.serial}`;
      return createLink(query);
    });

    return { htmlLink, faviconLink, certificateLink };
  },
});
</script>
