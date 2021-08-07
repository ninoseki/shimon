<template>
  <div class="column is-half" v-if="link">
    <div class="box">
      <div class="content is-normal">
        <h4 class="is-size-4">
          <span class="icon">
            <img
              src="https://www.google.com/s2/favicons?domain=domainwat.ch"
              alt="domainwatch"
            />
          </span>
          DomainWatch
        </h4>

        <ul>
          <li>
            <a target="_blank" :href="link">Registrant email</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import emailRegex from "email-regex";
import qs from "qs";
import { computed, defineComponent, PropType } from "vue";

import { Fingerprint } from "@/types";

export default defineComponent({
  name: "DomainWatch",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
  setup(props) {
    const createLink = (query: string): string => {
      const baseUrl = "https://domainwat.ch/search?";
      const params = {
        query: `email:${query}`,
        type: `whois_raw`,
      };
      return baseUrl + qs.stringify(params);
    };

    const link = computed(() => {
      if (props.fingerprint.whois.registrantEmail === null) {
        return undefined;
      }

      if (!emailRegex().test(props.fingerprint.whois.registrantEmail)) {
        return undefined;
      }

      return createLink(props.fingerprint.whois.registrantEmail);
    });

    return { link };
  },
});
</script>
