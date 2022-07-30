<template>
  <div class="column is-half" v-if="hasLinks">
    <div class="box">
      <div class="content is-normal">
        <h4 class="is-size-4">
          <span class="icon">
            <img
              src="https://www.google.com/s2/favicons?domain=www.zoomeye.org"
              alt="zoomeye"
            />
          </span>
          ZoomEye
        </h4>

        <ul>
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
import { computed, defineComponent, PropType } from "vue";

import { Fingerprint } from "@/types";

export default defineComponent({
  name: "ZoomEyeComponent",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
  setup(props) {
    const createLink = (query: string): string => {
      const baseUrl = "https://www.zoomeye.org/searchResult?q=";
      return baseUrl + encodeURI(query);
    };

    const faviconLink = computed(() => {
      if (props.fingerprint.favicon === null) {
        return undefined;
      }

      const query = `iconhash:"${props.fingerprint.favicon.mmh3}"`;
      return createLink(query);
    });

    const certificateLink = computed(() => {
      if (props.fingerprint.certificate === null) {
        return undefined;
      }

      const query = `ssl.cert.fingerprint:"${props.fingerprint.certificate.sha1}"`;
      return createLink(query);
    });

    const hasLinks = computed(() => {
      return (
        certificateLink.value !== undefined || faviconLink.value !== undefined
      );
    });

    return { faviconLink, certificateLink, hasLinks };
  },
});
</script>
