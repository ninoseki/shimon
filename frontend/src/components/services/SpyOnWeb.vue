<template>
  <div class="column is-half" v-if="link">
    <div class="box">
      <div class="content is-normal">
        <h4 class="is-size-4">
          <span class="icon">
            <img
              src="https://www.google.com/s2/favicons?domain=spyonweb.com"
              alt="spyonweb"
            />
          </span>
          SpyOnWeb
        </h4>

        <ul>
          <li>
            <a target="_blank" :href="link">Google Analytics ID</a>
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
  name: "SpyOnWeb",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
  setup(props) {
    const createLink = (query: string): string => {
      return `https://spyonweb.com/${query}`;
    };

    const link = computed(() => {
      if (props.fingerprint.tracker.googleAnalyticsId === null) {
        return undefined;
      }

      return createLink(props.fingerprint.tracker.googleAnalyticsId);
    });

    return { link };
  },
});
</script>
