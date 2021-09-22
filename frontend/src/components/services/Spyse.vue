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
            <a target="_blank" :href="faviconLink">Favicon</a>
          </li>
          <li v-if="certificateLink">
            <a target="_blank" :href="certificateLink">Certificate</a>
          </li>
          <li v-for="link in aLinks" :key="link.key">
            <a target="_blank" :href="link.link">{{ link.key }}</a>
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
      const baseUrl = "https://spyse.com/search?target=domain&";
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
          http_extract_favicon_sha256: {
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
          certificate_sha256: {
            value: props.fingerprint.certificate.sha256,
            operator: "eq",
          },
        },
      ];
      return createLink(JSON.stringify(params));
    });

    const aLinks = computed(() => {
      if (props.fingerprint.dns.a === null) {
        return undefined;
      }

      return (props.fingerprint.dns.a || []).map((record) => {
        const params = [
          {
            dns_a: {
              value: record.host,
              operator: "eq",
            },
          },
        ];
        return {
          key: record.host,
          link: createLink(JSON.stringify(params)),
        };
      });
    });

    const hasLinks = computed(() => {
      return (
        props.fingerprint.favicon !== null ||
        props.fingerprint.certificate !== null ||
        props.fingerprint.dns.a ||
        null
      );
    });

    return { faviconLink, certificateLink, hasLinks, aLinks };
  },
});
</script>
