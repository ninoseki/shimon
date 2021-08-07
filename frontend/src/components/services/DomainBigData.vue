<template>
  <div class="column is-half" v-if="link">
    <div class="box">
      <div class="content is-normal">
        <h4 class="is-size-4">
          <span class="icon">
            <img
              src="https://www.google.com/s2/favicons?domain=domainbigdata.com"
              alt="domainbigdata"
            />
          </span>
          DomaingBigData
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
import { computed, defineComponent, PropType } from "vue";

import { Fingerprint } from "@/types";

export default defineComponent({
  name: "DomainBigData",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
  setup(props) {
    const createLink = (query: string): string => {
      return `https://domainbigdata.com/email/${query}`;
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
