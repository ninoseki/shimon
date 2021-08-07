<template>
  <div class="column is-half">
    <div class="box">
      <div class="content is-normal">
        <h4 class="is-size-4">
          <span class="icon">
            <img
              src="https://www.google.com/s2/favicons?domain=censys.io"
              alt="shodan"
            />
          </span>
          Censys
        </h4>

        <ul>
          <li><a target="_blank" :href="htmlLink">HTML</a></li>
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
  name: "Censys",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
  setup(props) {
    const createLink = (q: string): string => {
      const baseUrl = "https://search.censys.io/search?";
      const resource = "hosts";
      const params = {
        q,
        resource,
      };
      return baseUrl + qs.stringify(params);
    };

    const htmlLink = computed(() => {
      const q = `services.http.response.body_hash:"sha1:${props.fingerprint.html.sha1}"`;
      return createLink(q);
    });

    const certificateLink = computed(() => {
      if (props.fingerprint.certificate === null) {
        return undefined;
      }

      return createLink(props.fingerprint.certificate.sha256);
    });

    return { htmlLink, certificateLink };
  },
});
</script>
