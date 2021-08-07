<template>
  <div class="column is-half">
    <div class="box">
      <div class="content is-normal">
        <h4 class="is-size-4">
          <span class="icon">
            <img
              src="https://www.google.com/s2/favicons?domain=onyphe.io"
              alt="shodan"
            />
          </span>
          Onyphe
        </h4>

        <ul>
          <li>
            <a target="_blank" :href="htmlLink">HTML</a>
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
  name: "Onyphe",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true,
    },
  },
  setup(props) {
    const createLink = (query: string): string => {
      const baseUrl = "https://onyphe.io/search/?";
      const params = {
        query,
      };
      return baseUrl + qs.stringify(params);
    };

    const htmlLink = computed(() => {
      const query = `category:datascan app.http.bodymd5:"${props.fingerprint.html.md5}"`;
      return createLink(query);
    });

    return { htmlLink };
  },
});
</script>
