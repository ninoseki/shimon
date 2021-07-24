<template>
  <div class="column is-half" v-if="hasLinks">
    <div class="box">
      <div class="content is-normal">
        <h4 class="is-size-4">
          <span class="icon">
            <img
              src="https://www.google.com/s2/favicons?domain=spyse.com"
              alt="spyse"
            />
          </span>
          Spyse
        </h4>

        <ul>
          <li v-if="faviconLink">
            <a :href="faviconLink">Favicon</a>
          </li>
          <li v-if="certificateLink">
            <a :href="certificateLink">Certificate</a>
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
  name: "Spyse",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
  setup(props) {
    const createLink = (search_params: string): string => {
      const baseUrl = "https://spyse.com/advanced-search/domain?";
      const params = {
        search_params,
      };
      return baseUrl + qs.stringify(params);
    };

    const faviconLink = computed(() => {
      if (props.fingerprint.favicon === null) {
        return undefined;
      }

      const params = [
        {
          domain_info_favicon_hash: {
            value: props.fingerprint.favicon.sha256,
            operator: "eq",
          },
        },
      ];
      return createLink(JSON.stringify(params));
    });

    const certificateLink = computed(() => {
      if (props.fingerprint.certificate === null) {
        return undefined;
      }

      const params = [
        {
          cert_fingerprint_sha256: {
            value: props.fingerprint.certificate.sha256,
            operator: "eq",
          },
        },
      ];
      return createLink(JSON.stringify(params));
    });

    const hasLinks = computed(() => {
      return (
        props.fingerprint.favicon !== null ||
        props.fingerprint.certificate !== null
      );
    });

    return { faviconLink, certificateLink, hasLinks };
  },
});
</script>
