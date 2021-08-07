<template>
  <div class="column is-half">
    <div class="box">
      <div class="content is-normal">
        <h4 class="is-size-4">
          <span class="icon">
            <img
              src="https://www.google.com/s2/favicons?domain=urlscan.io"
              alt="shodan"
            />
          </span>
          urlscan.io
        </h4>

        <ul>
          <li><a target="_blank" :href="htmlLink">HTML</a></li>
          <li v-if="faviconLink">
            <a target="_blank" :href="faviconLink">Favicon</a>
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
  name: "Shodan",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
  setup(props) {
    const createLink = (query: string): string => {
      const baseUrl = "https://urlscan.io/search/#";
      return baseUrl + encodeURI(query);
    };

    const htmlLink = computed(() => {
      return createLink(props.fingerprint.html.sha256);
    });

    const faviconLink = computed(() => {
      if (props.fingerprint.favicon === null) {
        return undefined;
      }

      return createLink(props.fingerprint.favicon.sha256);
    });

    return { htmlLink, faviconLink };
  },
});
</script>
