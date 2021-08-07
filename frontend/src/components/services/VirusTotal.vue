<template>
  <div class="column is-half" v-if="aLinks.length > 0">
    <div class="box">
      <div class="content is-normal">
        <h4 class="is-size-4">
          <span class="icon">
            <img
              src="https://www.google.com/s2/favicons?domain=virustotal.com"
              alt="vt"
            />
          </span>
          VirusTotal
        </h4>

        <ul>
          <li v-for="link in aLinks" :key="link.key">
            <a target="_blank" :href="link.link">{{ link.key }}</a>
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
  name: "VirusTotal",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
  setup(props) {
    const createLink = (query: string): string => {
      return `https://www.virustotal.com/gui/ip-address/${query}/detail`;
    };

    const aLinks = computed(() => {
      return (props.fingerprint.dns.a || []).map((record) => {
        return { key: record.host, link: createLink(record.host) };
      });
    });

    return { aLinks };
  },
});
</script>
