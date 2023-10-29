<template>
  <div class="box content is-normal" v-if="queries.length > 0">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=www.zoomeye.org" alt="zoomeye" />
      </span>
      ZoomEye
    </h4>
    <QueryTags :queries="queries"></QueryTags>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, type PropType } from "vue"

import QueryTags from "@/components/services/QueryTags.vue"
import type { Fingerprint, Query } from "@/types"

export default defineComponent({
  name: "ZoomEyeComponent",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true
    }
  },
  components: {
    QueryTags
  },
  setup(props) {
    const createLink = (query: string): string => {
      const baseUrl = "https://www.zoomeye.org/searchResult?q="
      return baseUrl + encodeURI(query)
    }

    const queries = computed<Query[]>(() => {
      const q: Query[] = []

      if (props.fingerprint.favicon) {
        const query = `iconhash:"${props.fingerprint.favicon.mmh3}"`
        q.push({ key: "Favicon", query: query, link: createLink(query) })
      }

      if (props.fingerprint.certificate) {
        const query = `ssl.cert.fingerprint:"${props.fingerprint.certificate.sha1}"`
        q.push({ key: "Certificate", query: query, link: createLink(query) })
      }

      return q
    })

    return { queries }
  }
})
</script>
